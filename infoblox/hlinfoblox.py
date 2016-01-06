# -*- coding: utf-8 -*-
#
# Copyright stuff
#
# License stuff
#

from .infoblox import Infoblox

# import more stuff


class HighLevelInfobloxActions(object):

    """ Implements the following high level infoblox actions
    convert_lease_to_fixed_address
    """

    def __init__(self,
                 iba_ipaddr,
                 iba_user,
                 iba_password,
                 iba_wapi_version,
                 iba_dns_view,
                 iba_network_view,
                 iba_verify_ssl=False):
        """ Class initialization method
        :param iba_ipaddr: IBA IP address of management interface
        :param iba_user: IBA user name
        :param iba_password: IBA user password
        :param iba_wapi_version: IBA WAPI version (example: 1.0)
        :param iba_dns_view: IBA default view
        :param iba_network_view: IBA default network view
        :param iba_verify_ssl: IBA SSL certificate validation (example: False)
        """
        self.iba_host = iba_ipaddr
        self.iba_user = iba_user
        self.iba_password = iba_password
        self.iba_wapi_version = iba_wapi_version
        self.iba_dns_view = iba_dns_view
        self.iba_network_view = iba_network_view
        self.iba_verify_ssl = iba_verify_ssl

        self.api = Infoblox(iba_ipaddr, iba_user, iba_password,
                            iba_wapi_version, iba_dns_view, iba_network_view,
                            iba_verify_ssl)

    def convert_lease_to_fixed_address(self, address):
        """ Convert a DHCP-assigned leased address to a fixed address.
        :param address: IP Address to be converted
        """

        # Get our current lease information

        # Get the A record for ipaddress

        # Get the PTR record for ipaddress

        # Get other records for ipaddress?

        # Delete the records we have found

        # Create the Host (where can we find fqdn?)
        # self.api.create_host_record(address, fqdn)


