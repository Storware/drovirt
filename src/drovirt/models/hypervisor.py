
import logging
from sqlalchemy.sql import func
from drovirt.models.base import db, SerializerMixin

logger = logging.getLogger(__name__)


class Hypervisor(SerializerMixin, db.Model):
    __tablename__ = "hypervisor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())

    
class Datacenter(SerializerMixin, db.Model):
    __tablename__ = "datacenter"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())


class Cluster(SerializerMixin, db.Model):
    __tablename__ = "cluster"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True, default='')
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())
