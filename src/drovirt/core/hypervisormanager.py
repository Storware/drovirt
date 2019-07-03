
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.hypervisormanager import HypervisorManager


def get_hypervisor_manager(hypervisor_manager_id=None):
    query = HypervisorManager.query
    if hypervisor_manager_id:
        query = query.filter_by(id=hypervisor_manager_id)
    hypervisor_manager_list = query.all()
    return hypervisor_manager_list


def load_hypervisor_manager_vms(hypervisor_manager_id=None):
    query = HypervisorManager.query
    if hypervisor_manager_id:
        query = query.filter_by(id=hypervisor_manager_id)
    hypervisor_manager_list = query.all()
    for hvm in hypervisor_manager_list:
        hvm.load_vms()
    return hypervisor_manager_list


def create_hypervisor_manager(attributes):
    try:
        hypervisor_manager = HypervisorManager(**attributes)
        db.session.add(hypervisor_manager)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return hypervisor_manager


def delete_hypervisor_manager(hypervisor_manager_id):
    hypervisor_manager = get_hypervisor_manager(hypervisor_manager_id=hypervisor_manager_id)
    try:
        db.session.delete(hypervisor_manager)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return True


def update_hypervisor_manager(**kwargs):
    allowed_fields = ['name', 'api_url', 'manager_type']
    allowed_kwargs = {field: val for field, val in kwargs if field in allowed_fields}
    try:
        hypervisor_manager = HypervisorManager.query.filter_by(id=kwargs['hypervisor_manager_id']).one()
        for key, value in allowed_kwargs.items():
            setattr(hypervisor_manager, key, value)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return hypervisor_manager
