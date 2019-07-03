
from sqlalchemy.exc import IntegrityError

from drovirt.models.base import db
from drovirt.models.hypervisor import Hypervisor, Cluster, Datacenter


def get_hypervisor(hypervisor_id=None):
    query = Hypervisor.query
    if hypervisor_id:
        query = query.filter_by(id=hypervisor_id)
    hypervisor_list = query.all()
    return hypervisor_list


def create_hypervisor(attributes):
    try:
        hypervisor = Hypervisor(**attributes)
        db.session.add(hypervisor)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return hypervisor


def delete_hypervisor(hypervisor_id):
    hypervisor = get_hypervisor(hypervisor_id=hypervisor_id)
    try:
        db.session.delete(hypervisor)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return True


def get_cluster(cluster_id=None):
    query = Cluster.query
    if cluster_id:
        query = query.filter_by(id=cluster_id)
    cluster_list = query.all()
    return cluster_list


def create_cluster(attributes):
    try:
        cluster = Cluster(**attributes)
        db.session.add(cluster)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return cluster


def delete_cluster(cluster_id):
    cluster = get_cluster(cluster_id=cluster_id)
    try:
        db.session.delete(cluster)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return True


def get_datacenter(datacenter_id=None):
    query = Datacenter.query
    if datacenter_id:
        query = query.filter_by(id=datacenter_id)
    datacenter_list = query.all()
    return datacenter_list


def create_datacenter(attributes):
    try:
        datacenter = Datacenter(**attributes)
        db.session.add(datacenter)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return datacenter


def delete_datacenter(datacenter_id):
    datacenter = get_datacenter(datacenter_id=datacenter_id)
    try:
        db.session.delete(datacenter)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return True
