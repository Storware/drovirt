#!/bin/bash

function check_install()
{
    yum list installed $1 >/dev/null 2>&1
    if [[ $? != 0 ]]; then
	echo "Installing $1"
	yum -y install $1
    else
	echo "$1 already installed"
    fi
}

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run with root privileges"
	exit 1
fi

echo "Checking web server installation"
check_install nginx
check_install uwsgi
check_install postgresql-server

echo "Stopping web server..."
systemctl stop uwsgi
systemctl stop nginx
systemctl stop postgresql-server

APP_NAME="drovirt"
SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
STAGING=${SCRIPT_DIR}/workspace/staging
INSTALL_DIR=/opt/${APP_NAME}
SYS_USER=${APP_NAME}
SYS_GROUP=${APP_NAME}

# Create user and group if they do not already exist
getent group ${SYS_GROUP} >/dev/null || groupadd -r ${SYS_GROUP}
getent passwd ${SYS_USER} >/dev/null || useradd -r -m -g ${SYS_GROUP} ${SYS_USER}

if [[ ! -d ${INSTALL_DIR} ]]; then
    mkdir -p ${INSTALL_DIR}
else
    ls ${INSTALL_DIR} | grep -v log | while read file; do
	rm -rf ${INSTALL_DIR}/${file}
    done
fi

mkdir -p ${INSTALL_DIR}/run
mkdir -p ${INSTALL_DIR}/log
cp -ar ${STAGING}/* ${INSTALL_DIR}/

chown -R ${SYS_USER}:${SYS_GROUP} ${INSTALL_DIR}
chmod -R 0755 ${INSTALL_DIR}

find ${INSTALL_DIR} -type f -exec chmod 0644 {} \;


if [[ ! -d /var/lib/pgsql/data ]]; then
    echo "Setting up database"
    postgresql-setup initdb
    #sed -e '/local/ s/^#*/#/' -i /var/lib/pgsql/data/pg_hba.conf
    echo -e "local\tdrovirt\t\tdrovirt\t\t\t\ttrust" >> /var/lib/pgsql/data/pg_hba.conf
    systemctl start postgresql
    sudo -Hiu postgres createuser --no-password drovirt
    sudo -Hiu postgres createdb --no-password --owner drovirt drovirt
else
    echo "Database already present."
    systemctl start postgresql
fi    


echo "Starting web server..."

# Pass-through firewall
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --reload

# Deploy nginx config files and start/reload the service
if [[ ! -d /etc/nginx ]]; then
	mkdir -p /etc/nginx
else
    rm -rf /etc/nginx/*
fi

cp -ar ${INSTALL_DIR}/config/nginx/* /etc/nginx/
chown -R root:root /etc/nginx/*
chown -R ${SYS_USER}:${SYS_GROUP} /var/lib/nginx
chmod -R 0755 /etc/nginx/*
find /etc/nginx -type f -exec chmod 0644 {} \;
echo "Starting nginx"
systemctl start nginx

# Deploy uwsgi config files and start the service
# No need to reload the service if it's already running because
# it will reload itself when the config files are touched

if [[ ! -d /etc/uwsgi.d ]]; then
	mkdir -p /etc/uwsgi.d
fi
cp -f ${INSTALL_DIR}/config/uwsgi/uwsgi.ini /etc/uwsgi.ini
cp -f ${INSTALL_DIR}/config/uwsgi/uwsgi.d/* /etc/uwsgi.d/
chown root:root /etc/uwsgi.ini
chmod 644 /etc/uwsgi.ini
chown -R root:root /etc/uwsgi.d
chmod -R 0755 /etc/uwsgi.d
find /etc/uwsgi.d -type f -exec chmod 0644 {} \;

echo "Starting uwsgi"
systemctl start uwsgi

echo
echo "$APP_NAME installed."
echo
