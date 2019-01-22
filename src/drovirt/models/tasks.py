
import logging
import datetime

from drovirt.models.base import db
from drovirt.models.node import Node

logger = logging.getLogger(__name__)


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    started = db.Column(db.DateTime)
    finished = db.Column(db.DateTime)

    node_id = db.Column(db.Integer, db.ForeignKey('node.id'), nullable=False)
    node = db.relationship("Node", backref=db.backref("tasks", lazy=True), uselist=False)

    task_group_id = db.Column(db.Integer, db.ForeignKey('task_group.id'), nullable=False)
    task_group = db.relationship("TaskGroup", backref=db.backref("tasks", lazy=True))

    task_type = db.Column(db.String(16), nullable=False, default='')
    status = db.Column(db.String(16), nullable=False, default='')
    order = db.Column(db.Integer, default=1)
    message = db.Column(db.String(4096), nullable=True, default='')


class TaskGroup(db.Model):
    __tablename__ = "task_group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime)


