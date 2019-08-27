#!/usr/bin/python3

import logging
from flask import jsonify
from flask import request
from flask import abort

from drovirt.api.app import app
from drovirt.core.vm import get_vm, create_vm, delete_vm
from drovirt.core.tasks import get_task, create_task, update_task, get_task_group, create_task_group
from drovirt.core.tasks import get_task_for_node, complete_task
from drovirt.core.node import get_node, create_node, update_node, delete_node
from drovirt.core.hypervisor import get_cluster, create_cluster, delete_cluster
from drovirt.core.hypervisor import get_datacenter, create_datacenter, delete_datacenter
from drovirt.core.hypervisor import get_hypervisor, create_hypervisor, delete_hypervisor
from drovirt.core.hypervisormanager import get_hypervisor_manager, create_hypervisor_manager
from drovirt.core.hypervisormanager import delete_hypervisor_manager, load_hypervisor_manager_vms

logger = logging.getLogger(__name__)
logger.info("Started API process")


# TASKGROUP

@app.route("/task_group", methods=["GET"])
def api_task_group_get_all():
    task_groups = get_task_group()
    output = {}
    output['total'] = len(task_groups)
    output['task_groups'] = []
    for task_group in task_groups:
        output['task_groups'].append(task_group.to_dict())
    return jsonify(output)


@app.route("/task_group/<task_group_id>", methods=["GET"])
def api_task_group_get_one(task_group_id):
    task_groups = get_task_group(task_group_id)
    if not task_groups:
        abort(404)
    return jsonify(task_groups[0].to_dict())


@app.route("/task_group", methods=["POST"])
def api_task_group_create():
    req = request.get_json()
    req = req if req is not None else {}
    task_group = create_task_group(req)
    return jsonify(task_group.to_dict())

# TASK

@app.route("/task", methods=["GET"])
def api_task_get_all():
    tasks = get_task()
    output = {}
    output['total'] = len(tasks)
    output['tasks'] = []
    for task in tasks:
        output['tasks'].append(task.to_dict())
    return jsonify(output)


@app.route("/task/<task_id>", methods=["GET"])
def api_task_get_one(task_id):
    tasks = get_task(task_id)
    if not tasks:
        abort(404)
    return jsonify(tasks[0].to_dict())


@app.route("/task", methods=["POST"])
def api_task_create():
    req = request.get_json()
    req = req if req is not None else {}
    task = create_task(req)
    return jsonify(task.to_dict())


@app.route("/task", methods=["PUT"])
def api_task_update():
    req = request.get_json()
    req = req if req is not None else {}
    task = update_task(req)
    return jsonify(task.to_dict())


@app.route("/task/<task_id>/complete", methods=["PATCH"])
def api_task_complete(task_id):
    req = request.get_json()
    req = req if req is not None else {}
    status = req['status']
    message = req['message']
    task = complete_task(task_id, status, message)
    return jsonify(task.to_dict())


# NODE

@app.route("/node", methods=["GET"])
def api_node_get_all():
    nodes = get_node()
    output = {}
    output['total'] = len(nodes)
    output['nodes'] = []
    for node in nodes:
        output['nodes'].append(node.to_dict())
    return jsonify(output)


@app.route("/node/<node_id>", methods=["GET"])
def api_node_get_one(node_id):
    nodes = get_node(node_id)
    if not nodes:
        abort(404)
    return jsonify(nodes[0].to_dict())


@app.route("/node/<node_id>/get_task", methods=["GET"])
def api_task_get_for_node(node_id):
    task = get_task_for_node(node_id)
    if not task:
        return jsonify({})
    return jsonify(task.to_dict())


@app.route("/node", methods=["POST"])
def api_node_create():
    req = request.get_json()
    req = req if req is not None else {}
    node = create_node(req)
    return jsonify(node.to_dict())


@app.route("/node/<node_id>", methods=["DELETE"])
def api_node_delete_one(node_id):
    delete_node(node_id)
    return jsonify({})


@app.route("/node", methods=["PUT"])
def api_node_update():
    req = request.get_json()
    req = req if req is not None else {}
    node = update_node(req)
    return jsonify(node.to_dict())


# DATACENTER

@app.route("/datacenter", methods=["GET"])
def api_datacenter_get_all():
    datacenters = get_datacenter()
    output = {}
    output['total'] = len(datacenters)
    output['datacenters'] = []
    for datacenter in datacenters:
        output['datacenters'].append(datacenter.to_dict())
    return jsonify(output)


@app.route("/datacenter/<datacenter_id>", methods=["GET"])
def api_datacenter_get_one(datacenter_id):
    datacenters = get_datacenter(datacenter_id)
    if not datacenters:
        abort(404)
    return jsonify(datacenters[0].to_dict())


@app.route("/datacenter", methods=["POST"])
def api_datacenter_create():
    req = request.get_json()
    req = req if req is not None else {}
    datacenter = create_datacenter(req)
    return jsonify(datacenter.to_dict())


@app.route("/datacenter/<datacenter_id>", methods=["DELETE"])
def api_datacenter_delete_one(datacenter_id):
    delete_datacenter(datacenter_id)
    return jsonify({})


# CLUSTER

@app.route("/cluster", methods=["GET"])
def api_cluster_get_all():
    clusters = get_cluster()
    output = {}
    output['total'] = len(clusters)
    output['clusters'] = []
    for cluster in clusters:
        output['clusters'].append(cluster.to_dict())
    return jsonify(output)


@app.route("/cluster/<cluster_id>", methods=["GET"])
def api_cluster_get_one(cluster_id):
    clusters = get_cluster(cluster_id)
    if not clusters:
        abort(404)
    return jsonify(clusters[0].to_dict())


@app.route("/cluster", methods=["POST"])
def api_cluster_create():
    req = request.get_json()
    req = req if req is not None else {}
    cluster = create_cluster(req)
    return jsonify(cluster.to_dict())


@app.route("/cluster/<cluster_id>", methods=["DELETE"])
def api_cluster_delete_one(cluster_id):
    delete_cluster(cluster_id)
    return jsonify({})


# HYPERVISOR

@app.route("/hypervisor", methods=["GET"])
def api_hypervisor_get_all():
    hypervisors = get_hypervisor()
    output = {}
    output['total'] = len(hypervisors)
    output['hypervisors'] = []
    for hypervisor in hypervisors:
        output['hypervisors'].append(hypervisor.to_dict())
    return jsonify(output)


@app.route("/hypervisor/<hypervisor_id>", methods=["GET"])
def api_hypervisor_get_one(hypervisor_id):
    hypervisors = get_hypervisor(hypervisor_id)
    if not hypervisors:
        abort(404)
    return jsonify(hypervisors[0].to_dict())


@app.route("/hypervisor", methods=["POST"])
def api_hypervisor_create():
    req = request.get_json()
    req = req if req is not None else {}
    hypervisor = create_hypervisor(req)
    return jsonify(hypervisor.to_dict())


@app.route("/hypervisor/<hypervisor_id>", methods=["DELETE"])
def api_hypervisor_delete_one(hypervisor_id):
    delete_hypervisor(hypervisor_id)
    return jsonify({})


# HYPERVISOR MANAGER

@app.route("/hypervisor_manager", methods=["GET"])
def api_hypervisor_manager_get_all():
    hypervisor_managers = get_hypervisor_manager()
    output = {}
    output['total'] = len(hypervisor_managers)
    output['hypervisor_managers'] = []
    for hypervisor_manager in hypervisor_managers:
        output['hypervisor_managers'].append(hypervisor_manager.to_dict())
    return jsonify(output)


@app.route("/hypervisor_manager/<hypervisor_manager_id>", methods=["GET"])
def api_hypervisor_manager_get_one(hypervisor_manager_id):
    hypervisor_managers = get_hypervisor_manager(hypervisor_manager_id)
    if not hypervisor_managers:
        abort(404)
    return jsonify(hypervisor_managers[0].to_dict())


@app.route("/hypervisor_manager", methods=["POST"])
def api_hypervisor_manager_create():
    req = request.get_json()
    req = req if req is not None else {}
    hypervisor_manager = create_hypervisor_manager(req)
    return jsonify(hypervisor_manager.to_dict())


@app.route("/hypervisor_manager/<hypervisor_manager_id>/load_vms", methods=["POST"])
def api_hypervisor_manager_load_vms(hypervisor_manager_id):
    hypervisor_managers = get_hypervisor_manager(hypervisor_manager_id)
    if not hypervisor_managers:
        abort(404)
    load_hypervisor_manager_vms(hypervisor_managers[0].id)
    req = request.get_json()
    req = req if req is not None else {}
    hypervisor_manager = create_hypervisor_manager(req)

    return jsonify(hypervisor_manager.to_dict())


@app.route("/hypervisor_manager/<hypervisor_manager_id>", methods=["DELETE"])
def api_hypervisor_manager_delete_one(hypervisor_manager_id):
    delete_hypervisor_manager(hypervisor_manager_id)
    return jsonify({})


# VM

@app.route("/vm", methods=["GET"])
def api_vm_get_all():
    vms = get_vm()
    output = {}
    output['total'] = len(vms)
    output['vms'] = []
    for vm in vms:
        output['vms'].append(vm.to_dict())
    return jsonify(output)


@app.route("/vm/<vm_id>", methods=["GET"])
def api_vm_get_one(vm_id):
    vms = get_vm(vm_id)
    if not vms:
        abort(404)
    return jsonify(vms[0].to_dict())


@app.route("/vm", methods=["POST"])
def api_vm_create():
    req = request.get_json()
    req = req if req is not None else {}
    vm = create_vm(req)
    return jsonify(vm.to_dict())


@app.route("/vm/<vm_id>", methods=["DELETE"])
def api_vm_delete_one(vm_id):
    delete_vm(vm_id)
    return jsonify({})


