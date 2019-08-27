#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import hypervisor


@click.group(help="Manage hypervisors")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show hypervisors")
@click.option("--id", default=None, help="Show details about a specific hypervisor ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    hypervisor_info = hypervisor.get_hypervisor(id)
    cliutil.display_output(hypervisor_info, details=details)


@dvcli.command(help="Create a hypervisor")
@click.option("--name", required=True, help="Name of a new hypervisor")
@cliutil.pass_context
def create(ctx, **kwargs):
    hypervisor_info = hypervisor.create_hypervisor(kwargs)
    cliutil.display_output(hypervisor_info)


@dvcli.command(help="Delete a hypervisor")
@click.option("--id", default=None, help="ID of a hypervisor to delete")
@cliutil.pass_context
def delete(ctx, id):
    hypervisor.delete_hypervisor(id)
