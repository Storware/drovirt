
import logging
import datetime

from drovirt.models.base import db

logger = logging.getLogger(__name__)


class Vm(db.Model):
    __tablename__ = "vm"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime)

    uuid = db.Column(db.String(256), nullable=False, default='')
    last_replication = db.Column(db.DateTime)
    datacenter = db.relationship("Datacenter", back_populates="vms")
    cluster = db.relationship("Cluster", back_populates="vms")
    hypervisor = db.relationship("Hypervisor", back_populates="vms")
    hypervisor_manager = db.relationship("HypervisorManager", back_populates="vms")
