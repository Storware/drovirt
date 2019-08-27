#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import tasks


# logger = logging.getLogger(__name__)


@click.group(help="Manage tasks")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show tasks")
@click.option("--id", default=None, help="Show details about a specific task ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    task_info = tasks.get_task(id)
    cliutil.display_output(task_info, details)


@dvcli.command(help="Create a new task")
@click.option("--name", required=True, help="Name of a task to be created")
@click.option("--node_id", help="ID of a node the task will be assigned to")
@click.option("--task_group_id", required=True, help="ID of a task group the task will be assigned to")
@click.option("--task_type", required=True)
@click.option("--status", help="Status of the task")
@click.option("--order")
@click.option("--message", help="Message to be attached to the task")
@cliutil.pass_context
def create(ctx, **kwargs):
    new_task = tasks.create_task(kwargs)
    cliutil.display_output(new_task)


@dvcli.command(help="Update a task")
@click.option("--task_id", required=True, help="ID od the task to be updated")
@click.option("--name", help="New name of the task")
@click.option("--node_id", help="New ID of a node the task will be assigned to")
@click.option("--status", help="New status of the task")
@click.option("--message", help="New message to be attached to the task")
@cliutil.pass_context
def update(ctx, **kwargs):
    kwargs = {field: val for field, val in kwargs.items() if val}
    task_info = tasks.update_task(kwargs)
    cliutil.display_output(task_info)


@dvcli.command(help="Set task status")
@click.option("--task_id", required=True, help="ID of the task to be completed")
@click.option("--status", required=True, help="Status of the task. COMPLETED or FAILED")
@click.option("--message", required=True, help="Message to be attached to the task")
@cliutil.pass_context
def complete(ctx, **kwargs):
    task_info = tasks.complete_task(**kwargs)
    cliutil.display_output(task_info)
