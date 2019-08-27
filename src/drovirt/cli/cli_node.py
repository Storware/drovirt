#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import node


@click.group(help="Manage nodes")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show nodes")
@click.option("--id", default=None, help="Show details about a specific node ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    node_info = node.get_node(id)
    cliutil.display_output(node_info, details)


@dvcli.command(help="Create a new node group")
@click.option("--name", required=True, help="Name of the new node")
@click.option("--ip_addr", required=True, help="IP address of the new node")
@click.option("--state", required=True, help="State of the new node")
@cliutil.pass_context
def create(ctx, **kwargs):
    new_node_info = node.create_node(kwargs)
    cliutil.display_output(new_node_info)


@dvcli.command(help="Delete a node group")
@click.option("--id", required=True, help="ID of a node to delete")
@cliutil.pass_context
def delete(ctx, id):
    node.delete_node(id)


@dvcli.command(help="Update a node group")
@click.option("--node_id", required=True, help="ID of the node to update")
@click.option("--name", help="New name of the node")
@click.option("--state", help="New state of the node")
@click.option("--watchdog", help="New watchdog value for the node")
@cliutil.pass_context
def update(ctx, **kwargs):
    kwargs = {field: val for field, val in kwargs.items() if val}
    node_info = node.update_node(kwargs)
    cliutil.display_output(node_info)
