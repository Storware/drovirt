
import logging
from sqlalchemy.sql import func

from drovirt.models.base import db, SerializerMixin

logger = logging.getLogger(__name__)


class Node(SerializerMixin, db.Model):
    __tablename__ = "node"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())

    ip_addr = db.Column(db.String(64), nullable=False, default='')
    state = db.Column(db.String(16), nullable=False, default='')
    watchdog = db.Column(db.DateTime)
