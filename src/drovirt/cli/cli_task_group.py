#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import tasks


@click.group(help="Manage task groups")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show task groups")
@click.option("--id", default=None, help="Show details about a specific task group ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    task_group_info = tasks.get_task_group(id)
    cliutil.display_output(task_group_info, details)


@dvcli.command(help="Create a new task group")
@click.option("--name", required=True, help="Name of a new task group")
@cliutil.pass_context
def create(ctx, **kwargs):
    new_task_group = tasks.create_task_group(kwargs)
    cliutil.display_output(new_task_group)
