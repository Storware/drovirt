
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.vm import Vm


def get_vm(vm_id=None):
    query = Vm.query
    if vm_id:
        query = query.filter_by(id=vm_id)
    vm_list = query.all()
    return vm_list


def create_vm(**kwargs):
    try:
        vm = Vm(**kwargs)
        db.session.add(vm)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return vm


def delete_vm(vm_id):
    vm = get_vm(vm_id=vm_id)
    try:
        db.session.delete(vm)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return True
