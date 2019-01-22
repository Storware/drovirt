
import logging
import datetime

from drovirt.models.base import db

logger = logging.getLogger(__name__)


class Node(db.Model):
    __tablename__ = "node"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime)

    ip_addr = db.Column(db.String(64), nullable=False, default='')
    state = db.Column(db.String(16), nullable=False, default='')
    watchdog = db.Column(db.DateTime)

