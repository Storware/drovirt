
import logging
from sqlalchemy.sql import func
from drovirt.models.base import db, SerializerMixin

logger = logging.getLogger(__name__)


class HypervisorManager(SerializerMixin, db.Model):
    __tablename__ = "hypervisor_manager"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime)

    api_url = db.Column(db.String(256), nullable=False, default='')
    manager_type = db.Column(db.String(64), nullable=False, default='')
