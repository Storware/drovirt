
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.tasks import Task, TaskGroup


def get_task(task_id=None):
    query = Task.query
    if task_id:
        query = query.filter_by(id=task_id)
    task_list = query.all()
    return task_list


def create_task(**kwargs):
    try:
        task = Task(**kwargs)
        db.session.add(task)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return task


def update_task(**kwargs):
    allowed_fields = ['name', 'node', 'status', 'message']
    allowed_kwargs = {field: val for field, val in kwargs if field in allowed_fields}
    try:
        task = Task.query.filter_by(id=kwargs['task_id']).one()
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


def create_task_group(**kwargs):
    try:
        task_group = TaskGroup(**kwargs)
        db.session.add(task_group)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return task_group
