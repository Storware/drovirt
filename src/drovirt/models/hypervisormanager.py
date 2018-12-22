
import logging
import datetime
from sqlalchemy import Column, Integer, String, DateTime

from drovirt.models.base import Base

logger = logging.getLogger(__name__)


class HypervisorManager(Base):
    __tablename__ = "vm"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)

    api_url = Column(String(256), nullable=False, default='')
    manager_type = Column(String(64), nullable=False, default='')

