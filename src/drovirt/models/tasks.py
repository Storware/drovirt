
import logging
import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import orm

from drovirt.models.base import Base

logger = logging.getLogger(__name__)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    started = Column(DateTime)
    finished = Column(DateTime)

    node = orm.relationship("Node", back_populates="nodes")
    task_group = orm.relationship("TaskGroup", back_populates="tasks")
    task_type = Column(String(16), nullable=False, default='')
    status = Column(String(16), nullable=False, default='')
    order = Column(Integer, default=1)
    message = Column(String(4096), nullable=True, default='')


class TaskGroup(Base):
    __tablename__ = "task_group"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)


