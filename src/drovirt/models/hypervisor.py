
import logging
import datetime
from sqlalchemy import Column, Integer, String, DateTime

from drovirt.models.base import Base

logger = logging.getLogger(__name__)


class Hypervisor(Base):
    __tablename__ = "hypervisor"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)

    
class Datacenter(Base):
    __tablename__ = "datacenter"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)


class Cluster(Base):
    __tablename__ = "hypervisor"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)
