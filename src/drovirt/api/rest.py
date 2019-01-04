#!/usr/bin/python3

import logging
from flask import Flask
from flask import jsonify
from flask import request

logger = logging.getLogger(__name__)
logger.info("Started API process")
app = Flask(__name__)


# TASKGROUP

@app.route("/task_group", methods=["GET"])
def api_task_group_get_all():
    task_groups = []
    output = {}
    output['total'] = len(task_groups)
    output['task_groups'] = []
    for task_group in task_groups:
        output['task_groups'].append(task_group.to_dict())
    return jsonify(output)


@app.route("/task_group/<task_group_id>", methods=["GET"])
def api_task_group_get_one(task_group_id):
    task_group = {}
    return jsonify(task_group.to_dict())


@app.route("/task_group", methods=["POST"])
def api_task_group_create():
    req = request.get_json()
    req = req if req is not None else {}
    task_group = {}
    return jsonify(task_group.to_dict())

# TASK

@app.route("/task", methods=["GET"])
def api_task_get_all():
    tasks = []
    output = {}
    output['total'] = len(tasks)
    output['tasks'] = []
    for task in tasks:
        output['tasks'].append(task.to_dict())
    return jsonify(output)


@app.route("/task/<task_id>", methods=["GET"])
def api_task_get_one(task_id):
    task = {}
    return jsonify(task.to_dict())


@app.route("/task", methods=["POST"])
def api_task_create():
    req = request.get_json()
    req = req if req is not None else {}
    task = {}
    return jsonify(task.to_dict())


@app.route("/task", methods=["PUT"])
def api_task_update():
    req = request.get_json()
    req = req if req is not None else {}
    task = {}
    return jsonify(task.to_dict())


# NODE

@app.route("/node", methods=["GET"])
def api_node_get_all():
    nodes = []
    output = {}
    output['total'] = len(nodes)
    output['nodes'] = []
    for node in nodes:
        output['nodes'].append(node.to_dict())
    return jsonify(output)


@app.route("/node/<node_id>", methods=["GET"])
def api_node_get_one(node_id):
    node = {}
    return jsonify(node.to_dict())


@app.route("/node", methods=["POST"])
def api_node_create():
    req = request.get_json()
    req = req if req is not None else {}
    node = {}
    return jsonify(node.to_dict())


@app.route("/node/<node_id>", methods=["DELETE"])
def api_node_delete_one(node_id):
    # delete a node 
    return jsonify({})


# DATACENTER

@app.route("/datacenter", methods=["GET"])
def api_datacenter_get_all():
    datacenters = []
    output = {}
    output['total'] = len(datacenters)
    output['datacenters'] = []
    for datacenter in datacenters:
        output['datacenters'].append(datacenter.to_dict())
    return jsonify(output)


@app.route("/datacenter/<datacenter_id>", methods=["GET"])
def api_datacenter_get_one(datacenter_id):
    datacenter = {}
    return jsonify(datacenter.to_dict())


@app.route("/datacenter", methods=["POST"])
def api_datacenter_create():
    req = request.get_json()
    req = req if req is not None else {}
    datacenter = {}
    return jsonify(datacenter.to_dict())


@app.route("/datacenter/<datacenter_id>", methods=["DELETE"])
def api_datacenter_delete_one(datacenter_id):
    # delete a datacenter 
    return jsonify({})


# CLUSTER

@app.route("/cluster", methods=["GET"])
def api_cluster_get_all():
    clusters = []
    output = {}
    output['total'] = len(clusters)
    output['clusters'] = []
    for cluster in clusters:
        output['clusters'].append(cluster.to_dict())
    return jsonify(output)


@app.route("/cluster/<cluster_id>", methods=["GET"])
def api_cluster_get_one(cluster_id):
    cluster = {}
    return jsonify(cluster.to_dict())


@app.route("/cluster", methods=["POST"])
def api_cluster_create():
    req = request.get_json()
    req = req if req is not None else {}
    cluster = {}
    return jsonify(cluster.to_dict())


@app.route("/cluster/<cluster_id>", methods=["DELETE"])
def api_cluster_delete_one(cluster_id):
    # delete a cluster 
    return jsonify({})


# HYPERVISOR

@app.route("/hypervisor", methods=["GET"])
def api_hypervisor_get_all():
    hypervisors = []
    output = {}
    output['total'] = len(hypervisors)
    output['hypervisors'] = []
    for hypervisor in hypervisors:
        output['hypervisors'].append(hypervisor.to_dict())
    return jsonify(output)


@app.route("/hypervisor/<hypervisor_id>", methods=["GET"])
def api_hypervisor_get_one(hypervisor_id):
    hypervisor = {}
    return jsonify(hypervisor.to_dict())


@app.route("/hypervisor", methods=["POST"])
def api_hypervisor_create():
    req = request.get_json()
    req = req if req is not None else {}
    hypervisor = {}
    return jsonify(hypervisor.to_dict())


@app.route("/hypervisor/<hypervisor_id>", methods=["DELETE"])
def api_hypervisor_delete_one(hypervisor_id):
    # delete a hypervisor 
    return jsonify({})


# HYPERVISOR MANAGER

@app.route("/hypervisor_manager", methods=["GET"])
def api_hypervisor_manager_get_all():
    hypervisor_managers = []
    output = {}
    output['total'] = len(hypervisor_managers)
    output['hypervisor_managers'] = []
    for hypervisor_manager in hypervisor_managers:
        output['hypervisor_managers'].append(hypervisor_manager.to_dict())
    return jsonify(output)


@app.route("/hypervisor_manager/<hypervisor_manager_id>", methods=["GET"])
def api_hypervisor_manager_get_one(hypervisor_manager_id):
    hypervisor_manager = {}
    return jsonify(hypervisor_manager.to_dict())


@app.route("/hypervisor_manager", methods=["POST"])
def api_hypervisor_manager_create():
    req = request.get_json()
    req = req if req is not None else {}
    hypervisor_manager = {}
    return jsonify(hypervisor_manager.to_dict())


@app.route("/hypervisor_manager/<hypervisor_manager_id>", methods=["DELETE"])
def api_hypervisor_manager_delete_one(hypervisor_manager_id):
    # delete a hypervisor manager
    return jsonify({})


# VM

@app.route("/vm", methods=["GET"])
def api_vm_get_all():
    vms = []
    output = {}
    output['total'] = len(vms)
    output['vms'] = []
    for vm in vms:
        output['vms'].append(vm.to_dict())
    return jsonify(output)


@app.route("/vm/<vm_id>", methods=["GET"])
def api_vm_get_one(vm_id):
    vm = {}
    return jsonify(vm.to_dict())


@app.route("/vm", methods=["POST"])
def api_vm_create():
    req = request.get_json()
    req = req if req is not None else {}
    vm = {}
    return jsonify(vm.to_dict())


@app.route("/vm/<vm_id>", methods=["DELETE"])
def api_vm_delete_one(vm_id):
    # delete a vm 
    return jsonify({})


