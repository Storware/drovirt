#!/usr/bin/env python3

import sys
sys.path.append("/opt/drovirt/lib")

import click
import logging
import sys
import os
import traceback

import drovirt.cli.util as cliutil
# import drovirt.core

class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(os.path.dirname(__file__)):
            if filename.endswith('.pyc') and filename.startswith('cli_'):
                rv.append(filename[4:-4])
        rv.sort()
        return rv
        # return ['task']

    def get_command(self, ctx, cmd_name):
        mod = None
        try:
            mod = __import__(f"drovirt.cli.cli_{cmd_name}", fromlist=["dvcli"])
        except ImportError:
            raise
        return mod.dvcli


@click.command(cls=CLI)
@cliutil.pass_context
def dvcli(ctx, **kwargs):
    pass


if __name__ == '__main__':
    try:
        dvcli()
    except Exception as e:
        click.echo(f'ERROR: {e.__class__.__name__} : {str(e)}', err=True)
        click.echo((traceback.format_exc()))
        sys.exit(1)
