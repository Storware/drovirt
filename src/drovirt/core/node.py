
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.node import Node


def get_node(node_id=None):
    query = Node.query
    if node_id:
        query = query.filter_by(id=node_id)
    node_list = query.all()
    return node_list


def create_node(attributes):
    try:
        node = Node(**attributes)
        db.session.add(node)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return node


def delete_node(node_id):
    node = get_node(node_id=node_id)[0]
    try:
        db.session.delete(node)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return True


def update_node(attributes):
    allowed_fields = ['name', 'state', 'watchdog']
    allowed_kwargs = {field: val for field, val in attributes.items() if field in allowed_fields}
    try:
        node = Node.query.filter_by(id=attributes['node_id']).one()
        for key, value in allowed_kwargs.items():
            setattr(node, key, value)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return node
