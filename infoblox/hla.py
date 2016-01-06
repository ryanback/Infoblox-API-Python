# -*- coding: utf-8 -*-
import click
from .hlinfoblox import HighLevelInfobloxActions

# hla == High Level Abstractions or, if you like, High Level Actions


@click.group()
@click.option('--ipaddr', envvar='IB_IPADDR',
              help='IP address of the infoblox API')
@click.option('--user', envvar='IB_USER',
              help='Infoblox API username')
@click.option('--password', envvar='IB_PASSWORD',
              help='Infoblox API password')
@click.option('--wapi-version', envvar='IB_WAPI_VERSION', default='1.6',
              help='Infoblox API version')
@click.option('--dns-view', envvar='IB_DNS_VIEW', default='default',
              help='Default DNS view')
@click.option('--network-view', envvar='IB_NETWORK_VIEW', default='default',
              help='Default network view')
@click.option('--verify-ssl/--no-verify-ssl', envvar='IB_VERIFY_SSL',
              default=False, help='Enable SSL verification')
@click.pass_context
def cli(ctx, ipaddr, user, password, wapi_version, dns_view, network_view,
        verify_ssl):
    '''Hlinfobloxs is a CLI for High-Level Infoblox commands.'''
    ctx.obj = HighLevelInfobloxActions(ipaddr, user, password, wapi_version,
                                       dns_view, network_view, verify_ssl)


@cli.command('lease2fixed')
@click.pass_obj
def convert_lease_to_fixed_address(api):
    '''Convert a DHCP lease to a fixed address.
       Must be executed on the node for which we want to convert.
    '''
    api.convert_lease_to_fixed_address()
