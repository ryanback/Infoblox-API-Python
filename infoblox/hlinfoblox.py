# -*- coding: utf-8 -*-
#
# Copyright stuff
#
# License stuff
#

from .infoblox import Infoblox, InfobloxGeneralException

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

    def convert_lease_to_fixed_address(self, address, fqdn=None,
                                       confirm=False):
        """Convert a DHCP-assigned leased address to a fixed address.
        :param address: IP Address to be converted
        :param fqdn: Fully qualified domain name for host if we cannot determine it from the lease information.
        :param confirm: Confirm that you really want to do this.
        """

        # Get our host information
        fields = [
            'dhcp_client_identifier',
            'mac_address',
            'names',
            'objects']
        ipv4address_record = self.api.get_host_by_ip(address, fields=fields)
        print("IPV4 Address Record [%s]" % (ipv4address_record))
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
            raise(InfobloxGeneralException(
                "Cannot locate lease record for [%s]" % (address)))

        print("Lease Reference [%s]" % (lease_ref))
        lease_record = self.api.util.get(lease_ref,
                                         fields=['client_hostname'])
        print("Lease Record [%s]" % (lease_record))

        a_record = None
        if a_record_ref is not None:
            print("A Record Reference [%s]" % (a_record_ref))
            a_record = self.api.util.get(a_record_ref)
            print("A Record [%s]" % (a_record))

        ptr_record = None
        if ptr_record_ref is not None:
            print("PTR Record Reference [%s]" % (ptr_record_ref))
            ptr_record = self.api.util.get(ptr_record_ref)
            print("PTR Record [%s]" % (ptr_record))

        # Try to find a record:host for the host we found.
        names = ipv4address_record['names']
        if names is None and fqdn is None:
            raise(InfobloxGeneralException(
                "Cannot determine fqdn for [%s]" % (address)))

        mac = ipv4address_record['mac_address']
        print("mac [%s]" % (mac))
        if mac is None or mac is '':
            raise(InfobloxGeneralException(
                "Cannot determine mac for [%s]" % (address)))

        if names:
            # If we found names associated with the address then
            # we can use those names to find record:host objects
            # and convert them to fixed.
            for name in names:
                print("Host Name [%s]" % (name))
                host_record = self.api.get_host(name, notFoundFail=False)
                if host_record is not None:
                    print("HOST Record [%s]" % (host_record))
                    print("Converting lease to fixedaddress")
                    for host_host_ipv4addr in host_record['ipv4addrs']:
                        fields = {
                            'configure_for_dhcp': True,
                            'mac': mac
                        }
                        self.api.update_record(host_record,
                                               fields=fields,
                                               confirm=confirm)
        else:
            # If we did not find names associated with the address then
            # we will have to create a new record:host for the ipaddress.
            if fqdn is None and 'dhcp_client_identifier' in ipv4address_record:
                fqdn = ipv4address_record['dhcp_client_identifier']
            if fqdn is None and 'client_hostname' in lease_record:
                fqdn = lease_record['client_hostname']
            if fqdn is None:
                raise(InfobloxGeneralException(
                    "Cannot determine fqdn for new HOST Record for [%s]" %
                    (address)))
            host_data = {'name': fqdn,
                         'ipv4addrs': [{'ipv4addr': address,
                                        'configure_for_dhcp': True,
                                        'mac': mac
                                        }]}
            print("host_data [%s]" % (host_data))
            self.api.create_host_record()
