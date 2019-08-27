
import datetime
import logging
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.tasks import Task, TaskGroup, TaskStatus
from drovirt.models.node import Node

logger = logging.getLogger(__name__)


def get_task(task_id=None):
    query = Task.query
    if task_id:
        query = query.filter_by(id=task_id)
    task_list = query.all()
    return task_list


def get_task_for_node(node_id):
    """ Get a new task or previously assigned task for node """

    # get ACTIVE task that was previously assigned to this node
    query = Task.query.filter_by(node_id=node_id).filter_by(status=TaskStatus.ACTIVE)
    task = query.first()
    if task:
        return task

    node = Node.query.filter_by(id=node_id).one()

    return _assign_task(node)


def _assign_task(node):
    """ Assign new task for node, there should be one active task per TaskGroup, per Node """

    query = Task.query.filter(Task.status == TaskStatus.QUEUED)
    query = query.filter(~Task.task_group.has(TaskGroup.tasks.any(Task.status == TaskStatus.ACTIVE)))
    query = query.order_by(Task.task_group_id, Task.order)
    task = query.first()

    if not task:
        return None

    task.status = TaskStatus.ACTIVE
    task.node = node
    task.started = datetime.datetime.now()

    db.session.commit()
    return task


def create_task(attributes):
    try:
        task = Task(**attributes)
        db.session.add(task)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return task


def update_task(attributes):
    allowed_fields = ['name', 'node_id', 'status', 'message']
    allowed_kwargs = {field: val for field, val in attributes.items() if field in allowed_fields}
    try:
        task = Task.query.filter_by(id=attributes['task_id']).one()
        for key, value in allowed_kwargs.items():
            setattr(task, key, value)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return task


def get_task_group(task_group_id=None):
    query = TaskGroup.query
    if task_group_id:
        query = query.filter_by(id=task_group_id)
    task_group_list = query.all()
    return task_group_list


def create_task_group(attributes):
    try:
        task_group = TaskGroup(**attributes)
        db.session.add(task_group)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return task_group


def complete_task(task_id, status, message):
    allowed_status = [TaskStatus.COMPLETED, TaskStatus.FAILED]
    print("Task %s completed with status" % status)
    if status not in [status.value for status in allowed_status]:
        raise Exception("Illegal task status %s" % status)
    try:
        task = Task.query.filter_by(id=task_id).one()
        print(message)
        task.message = message[:4095]
        task.status = status
        task.finished = datetime.datetime.now()
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    logger.info("Task %s completed" % task)
    return task
