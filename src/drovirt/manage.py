#!/usr/bin/env python3

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from drovirt.api.rest import app
from drovirt.models.base import db

# import models so that flask-migrate detects them
from drovirt.models.vm import *
from drovirt.models.hypervisor import *
from drovirt.models.tasks import *
from drovirt.models.hypervisormanager import *
from drovirt.models.node import *


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
