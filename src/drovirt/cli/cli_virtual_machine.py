#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import vm


@click.group(help="Manage virutal machines")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show virtual machines")
@click.option("--id", default=None, help="Show details about a specific virtual machine ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    vm_info = vm.get_vm(id)
    cliutil.display_output(vm_info, details)


@dvcli.command(help="Create a new vritual machine")
@click.option("--name", required=True, help="")
@click.option("--vm_type", help="")
@click.option("--status", help="")
@click.option("--cpus", help="")
@click.option("--uuid", required=True, help="")
@click.option("--datacenter_id", help="")
@click.option("--cluster_id", help="")
@click.option("--hypervisor_id", help="")
@click.option("--hypervisor_manager_id", required=True, help="")
@cliutil.pass_context
def create(ctx, **kwargs):
    vm_info = vm.create_vm(kwargs)
    cliutil.display_output(vm_info)


@dvcli.command(help="Delete a virtual machine")
@click.option("--id", default=None, help="ID of a virtual machine to delete")
@cliutil.pass_context
def delete(ctx, id):
    vm.delete_vm(id)
