#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import hypervisor


@click.group(help="Manage data centers")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show data centers")
@click.option("--id", default=None, help="Show details about a specific data center ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    datacenter_info = hypervisor.get_datacenter(id)
    cliutil.display_output(datacenter_info, details=details)


@dvcli.command(help="Create a new data center")
@click.option("--name", required=True, help="Name of a new data center")
@cliutil.pass_context
def create(ctx, **kwargs):
    datacenter_info = hypervisor.create_datacenter(kwargs)
    cliutil.display_output(datacenter_info)


@dvcli.command(help="Delete a data center")
@click.option("--id", default=None, help="ID of a data center to delete")
@cliutil.pass_context
def delete(ctx, id):
    hypervisor.delete_datacenter(id)
