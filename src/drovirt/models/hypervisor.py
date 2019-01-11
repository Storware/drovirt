
import logging
import datetime
from drovirt.models.base import db

logger = logging.getLogger(__name__)


class Hypervisor(db.Model):
    __tablename__ = "hypervisor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime)

    
class Datacenter(db.Model):
    __tablename__ = "datacenter"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime)


class Cluster(db.Model):
    __tablename__ = "cluster"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime)
