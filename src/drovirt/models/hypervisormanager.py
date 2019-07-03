
import logging
from sqlalchemy.sql import func
from drovirt.models.base import db, SerializerMixin
from drovirt.core.errors import UnsupportedHypervisorManagerAction
import drovirt.core.vm as core_vm
import drovirt.connectors.ovirt as ovirt


logger = logging.getLogger(__name__)


class HypervisorManager(SerializerMixin, db.Model):
    __tablename__ = "hypervisor_manager"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime)

    api_url = db.Column(db.String(256), nullable=False, default='')
    manager_type = db.Column(db.String(64), nullable=False, default='')

    allow_insecure = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(256), nullable=False, default='')
    password = db.Column(db.String(256), nullable=False, default='')

    def load_vms(self):
        if self.manager_type == 'ovirt':
            connection = ovirt.connection.get_connection(self.api_url, self.username, self.password, True)
            hvm_vms = ovirt.system.get_vms(connection)
            connection.close()
            logger.info("Loaded %s vms" % len(hvm_vms))
            core_vm.update_vms(hvm_vms, hvm_id=self.id)
            logger.info("Updating VMs finished ...")
            return len(hvm_vms)

        raise UnsupportedHypervisorManagerAction(self.manager_type, "loading vms")
