#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import hypervisormanager


@click.group(help="Manage hypervisor managers")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show hypervisor managers")
@click.option("--id", default=None, help="Show details about a specific hypervisor manager ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    hv_manager_info = hypervisormanager.get_hypervisor_manager(id)
    cliutil.display_output(hv_manager_info, details)


@dvcli.command(help="Create a hypervisor manager")
@click.option("--name", required=True, help="Name of a new hypervisor manager")
@click.option("--api_url", required=True, help="URL to api of the hypervisor manager")
@click.option("--manager_type", required=True, help="Type of the hypervisor manager")
@click.option("--allow_insecure", is_flag=True, help="Allow insecure connection to the hypervisor manager")
@click.option("--username", help="Specify username for the hypervisor manager")
@click.option("--password", help="Specify password for the hypervisor manager")
@cliutil.pass_context
def create(ctx, **kwargs):
    hv_manager_info = hypervisormanager.create_hypervisor_manager(kwargs)
    cliutil.display_output(hv_manager_info)


@dvcli.command(help="Update a hypervisor manager")
@click.option("--hypervisor_manager_id", required=True, help="ID of the hypervisor manager to be updated")
@click.option("--name", help="New name of the hypervisor manager")
@click.option("--api_url", help="New api url of the hypervisor manager")
@click.option("--manage_type", help="New manage type of the hypervisor manager")
@cliutil.pass_context
def update(ctx, **kwargs):
    kwargs = {field: val for field, val in kwargs.items() if val}
    hv_manager_info = hypervisormanager.update_hypervisor_manager(kwargs)
    cliutil.display_output(hv_manager_info)


@dvcli.command(help="Delete a hypervisor manager")
@click.option("--id", default=None, help="ID of a hypervisor manager to delete")
@cliutil.pass_context
def delete(ctx, id):
    hypervisormanager.delete_hypervisor_manager(id)
