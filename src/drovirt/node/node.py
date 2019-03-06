
import sys
import time
import requests
import logging
import logging.handlers

import drovirt.node.tasks
from drovirt.models.tasks import TaskStatus

NO_TASK_TIMEOUT = 15

log = logging.getLogger(__name__)


def configure_node(node_id, srv_addr):
    logging.info("Configuring node %s" % node_id)


def get_task(node_id, srv_addr):
    resp = requests.get('http://%s/node/%s/get_task' % (srv_addr, node_id))
    if resp.status_code != 200:
        log.warning("Getting task failed, HTTP %s" % resp.status_code)
        return None
    task = resp.json()
    return task


def complete_task(task, srv_addr, status, message):
    complete_url = 'http://%s/task/%s/complete' % (srv_addr, task['id'])
    payload = {'status': status.value, 'message': str(message)}
    resp = requests.patch(complete_url, json=payload)
    if resp.status_code != 200:
        log.warning("Completing task failed, HTTP %s" % resp.status_code)
    task = resp.json()
    return task


def main_process(node_id, srv_addr):
    configure_node(node_id, srv_addr)
    while True:
        task = get_task(node_id, srv_addr)
        if task:
            log.info("Received task %s" )
            try:
                result = process_task(task)
            except Exception as e:
                log.error("Failed processing task %s" % task['id'])
                log.error("Exception raised in task:\n%s" % str(e))
                complete_task(task, srv_addr, TaskStatus.FAILED, str(e))
            else:
                complete_task(task, srv_addr, TaskStatus.COMPLETED, result)
        else:
            log.info("No task received, waiting...")
            time.sleep(NO_TASK_TIMEOUT)


def process_task(task):
    try:
        task_class = getattr(drovirt.node.tasks, task['task_type'])
    except AttributeError:
        msg = "Unsupported task type %s" % task['task_type']
        log.error(msg)
        raise Exception(msg)
    task_obj = task_class(task)
    task_obj.run()
    return task_obj.result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <node_id> <server_ip_address>")
        sys.exit(1)

    node_id = sys.argv[1]
    srv_addr = sys.argv[2]

    log_path = "/opt/drovirt/log/node_%s.log" % node_id
    handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=5242880, backupCount=9)
    handler.setFormatter(logging.Formatter('[%(asctime)s] pid-%(process)d %(message)s'))
    log.addHandler(handler)

    main_process(node_id, srv_addr)
