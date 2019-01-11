#!/bin/bash

set -x
set -e

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"

WORKSPACE=${SCRIPT_DIR}/workspace
STAGING=${WORKSPACE}/staging
APP_NAME="drovirt"

if [[ -d ${WORKSPACE} ]]; then
	rm -rf ${WORKSPACE}/${APP_NAME}
else
	mkdir -p ${WORKSPACE}
fi

cp -ar ${SCRIPT_DIR}/src/${APP_NAME} ${WORKSPACE}/${APP_NAME}

# compilied files with future dates confuse interpreter and programmer
find ${WORKSPACE}/ -name "*.pyc" -delete
find ${WORKSPACE}/ -name "__pycache__" -delete
find ${WORKSPACE}/ -name ".#*" -delete
python3 -m compileall -b ${WORKSPACE}/${APP_NAME}
find ${WORKSPACE}/${APP_NAME} -name "*.py" -delete

if [[ ! -d ${WORKSPACE}/lib ]]; then
    mkdir -p ${WORKSPACE}/lib
    pip install --target=${WORKSPACE}/lib/ -r requirements.txt
    ls -lah ${WORKSPACE}/lib/
fi

if [[ -d ${STAGING} ]]; then
    rm -rf ${STAGING}/
fi
mkdir -p ${STAGING}

cp -r ${WORKSPACE}/lib ${STAGING}/lib
cp -r ${WORKSPACE}/${APP_NAME} ${STAGING}/lib/${APP_NAME}

if [[ -d ${STAGING}/config ]]; then
    cp -rf -t ${STAGING}/config ${SCRIPT_DIR}/config/*
else
    mkdir -p ${STAGING}/config/
    cp -rf -t ${STAGING}/config ${SCRIPT_DIR}/config/*
fi

set +x
set +e

echo
echo "Build completed."
echo
