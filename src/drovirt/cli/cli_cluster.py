#!/usr/bin/env python3

import click

import drovirt.cli.util as cliutil
from drovirt.core import hypervisor


@click.group(help="Manage clusters")
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


@dvcli.command(help="Show clusters")
@click.option("--id", default=None, help="Show details about a specific cluster ID")
@cliutil.pass_context
def show(ctx, id):
    details = True if id else False
    cluster_info = hypervisor.get_cluster(id)
    cliutil.display_output(cluster_info, details=details)


@dvcli.command(help="Create a new cluster")
@click.option("--name", required=True, help="Name of a new cluster")
@cliutil.pass_context
def create(ctx, **kwargs):
    cluster_info = hypervisor.create_cluster(kwargs)
    cliutil.display_output(cluster_info)


@dvcli.command(help="Delete a clusters")
@click.option("--id", default=None, help="ID of a cluster to delete")
@cliutil.pass_context
def delete(ctx, id):
    hypervisor.delete_cluster(id)
