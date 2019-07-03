
import logging
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.vm import Vm

logger = logging.getLogger(__name__)


def get_vm(vm_id=None, uuid=None):
    query = Vm.query
    if vm_id:
        query = query.filter_by(id=vm_id)
    elif uuid:
        query = query.filter_by(uuid=uuid)
    vm_list = query.all()
    return vm_list


def create_vm(attributes):
    try:
        vm = Vm(**attributes)
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


def update_vms(hvm_vms, hvm_id):
    """ Creates or updates vms from a list of hypervisor manager's vms """
    for hvm_vm in hvm_vms:
        logger.info("VM detected %s" % hvm_vm.id)
        vm = get_vm(uuid=hvm_vm.id)
        if not vm:
            create_vm(dict(uuid=hvm_vm.id,
                      name=hvm_vm.name,
                      vm_type=str(hvm_vm.type),
                      status=str(hvm_vm.status),
                      memory=hvm_vm.memory,
                      cpus=hvm_vm.cpu.topology.cores,
                      hypervisor_manager_id=hvm_id)
            )
            continue

        vm.uuid = hvm_vm.id,
        vm.name = hvm_vm.name,
        vm.vm_type = str(hvm_vm.type),
        vm.status = str(hvm_vm.status),
        vm.memory = hvm_vm.memory,
        vm.cpus = hvm_vm.cpu.topology.cores

