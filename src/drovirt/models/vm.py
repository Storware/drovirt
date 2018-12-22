
import logging
import datetime
from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, DateTime

from drovirt.models.base import Base

logger = logging.getLogger(__name__)


class Vm(Base):
    __tablename__ = "vm"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)

    uuid = Column(String(256), nullable=False, default='')
    last_replication = Column(DateTime)
    datacenter = orm.relationship("Datacenter", back_populates="vms")
    cluster = orm.relationship("Cluster", back_populates="vms")
    hypervisor = orm.relationship("Hypervisor", back_populates="vms")
    hypervisor_manager = orm.relationship("HypervisorManager", back_populates="vms")
