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

    def convert_lease_to_fixed_address(self, address, confirm=False):
        """Convert a DHCP-assigned leased address to a fixed address.
        :param address: IP Address to be converted
        """

        # Get our host information
        ipv4address_record = self.api.get_host_by_ip(address,
                                                     fields=[
                                                       'mac_address',
                                                       'objects'])
        host_objects = ipv4address_record['objects']

        lease_ref = None
        a_record_ref = None
        ptr_record_ref = None
        for ref in host_objects:
            if ref.startswith('lease/'):
                lease_ref = ref
            elif ref.startswith('record:a/'):
                a_record_ref = ref
            elif ref.startswith('record:ptr/'):
                ptr_record_ref = ref

        if lease_ref is None:
            raise("Cannot locate lease record for [%s]" % (address))

        print("Lease Reference [%s]" % (lease_ref))
        lease_record = self.api.util.get(lease_ref)
        print("Lease Record [%s]" % (lease_record))

        if a_record_ref is not None:
            print("A Record Reference [%s]" % (a_record_ref))
            a_record = self.api.util.get(a_record_ref)
            print("A Record [%s]" % (a_record))

        if ptr_record_ref is not None:
            print("PTR Record Reference [%s]" % (ptr_record_ref))
            ptr_record = self.api.util.get(ptr_record_ref)
            print("PTR Record [%s]" % (ptr_record))

        # A word to those who, like myself, don't understand how
        # Infoblox wires things together...
        # You will not be able to fetch a record:host for a host
        # that is assigned an address via DHCP.

        # Get other records for ipaddress?

        # Delete the records we have found

        # Create the Host (where can we find fqdn?)
        # self.api.create_ipv4address_record(address, fqdn)
