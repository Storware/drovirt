
import logging
import datetime
from sqlalchemy import Column, Integer, String, DateTime

from drovirt.models.base import Base

logger = logging.getLogger(__name__)


class Node(Base):
    __tablename__ = "node"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, default='')
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = Column(DateTime)

    ip_addr = Column(String(64), nullable=False, default='')
    state = Column(String(16), nullable=False, default='')
    watchdog = Column(DateTime)

