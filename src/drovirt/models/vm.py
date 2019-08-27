
import logging
from sqlalchemy.sql import func

from drovirt.models.base import db, SerializerMixin
from drovirt.models.hypervisor import Cluster, Datacenter, Hypervisor
from drovirt.models.hypervisormanager import HypervisorManager

logger = logging.getLogger(__name__)


class Vm(SerializerMixin, db.Model):
    __tablename__ = "vm"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')

    vm_type = db.Column(db.String(64), nullable=True, default=None)
    status = db.Column(db.String(64), nullable=True, default=None)
    cpus = db.Column(db.Integer, nullable=True, default=None)
    memory = db.Column(db.BigInteger, nullable=True, default=None)

    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())

    uuid = db.Column(db.String(256), nullable=False, default='')
    last_replication = db.Column(db.DateTime, nullable=True)

    datacenter_id = db.Column(db.Integer, db.ForeignKey('datacenter.id'), nullable=True)
    cluster_id = db.Column(db.Integer, db.ForeignKey('cluster.id'), nullable=True)
    hypervisor_id = db.Column(db.Integer, db.ForeignKey('hypervisor.id'), nullable=True)
    hypervisor_manager_id = db.Column(db.Integer, db.ForeignKey('hypervisor_manager.id'), nullable=False)

    datacenter = db.relationship("Datacenter", backref=db.backref("vms", lazy=True))
    cluster = db.relationship("Cluster", backref=db.backref("vms", lazy=True))
    hypervisor = db.relationship("Hypervisor", backref=db.backref("vms", lazy=True))
    hypervisor_manager = db.relationship("HypervisorManager", backref=db.backref("vms", lazy=True))
