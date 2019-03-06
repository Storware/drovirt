
import enum
import logging
from sqlalchemy.sql import func

from drovirt.models.base import db, SerializerMixin
from drovirt.models.node import Node

logger = logging.getLogger(__name__)


class TaskStatus(enum.Enum):
    QUEUED = "QUEUED"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Task(SerializerMixin, db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())
    started = db.Column(db.DateTime)
    finished = db.Column(db.DateTime)

    node_id = db.Column(db.Integer, db.ForeignKey('node.id'), nullable=True)
    node = db.relationship("Node", backref=db.backref("tasks", lazy=True), uselist=False)

    task_group_id = db.Column(db.Integer, db.ForeignKey('task_group.id'), nullable=False)
    task_group = db.relationship("TaskGroup", backref=db.backref("tasks", lazy=True))

    task_type = db.Column(db.String(16), nullable=False, default='')
    status = db.Column(db.Enum(TaskStatus), nullable=False, default=TaskStatus.QUEUED)
    order = db.Column(db.Integer, default=1)
    message = db.Column(db.String(4096), nullable=True, default='')


class TaskGroup(SerializerMixin, db.Model):
    __tablename__ = "task_group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())
    #tasks = db.relationship("Task", backref=db.backref("task_group", lazy=True))
