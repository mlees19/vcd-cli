# vCloud Air CLI 0.1
#
# Copyright (c) 2014 VMware, Inc. All Rights Reserved.
#
# This product is licensed to you under the
# Apache License, Version 2.0 (the "License").
# You may not use this product except in compliance with the License.
#
# This product may include a number of subcomponents with
# separate copyright notices and license terms. Your use of the source
# code for the these subcomponents is subject to the terms and
# conditions of the subcomponent's license, as noted in the LICENSE file.
#


import click
from vca_cli import cli, utils


@cli.command()
@click.pass_obj
def vdc(cmd_proc):
    """Operations with Virtual Data Centers (vdc)"""
    utils.print_message('vdc', cmd_proc)


# TODO: user power-on instead of power.on, etc
@cli.command()
@click.pass_obj
def vapp(cmd_proc):
    """Operations with vApps"""
    utils.print_message('vapp', cmd_proc)