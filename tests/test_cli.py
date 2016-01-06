import click
from click.testing import CliRunner
from infoblox import cli

def test_create_cname():
    runner = CliRunner()
    result = runner.invoke(cli.create_cname, ['', ''])
    assert 'adding cname' in result.output

def test__delete_cname():
    runner = CliRunner()
    result = runner.invoke(cli.delete_cname, [''])
    assert 'deleting cname' in result.output

def test__update_cname():
    runner = CliRunner()
    result = runner.invoke(cli.update_cname, ['', ''])
    assert 'updating cname' in result.output

def test_create_host_record():
    runner = CliRunner()
    result = runner.invoke(cli.create_host_record, ['', ''])
    assert 'creating host' in result.output

def test_delete_host_record():
    runner = CliRunner()
    result = runner.invoke(cli.delete_host_record, [''])
    assert 'deleting host' in result.output

def test_add_host_alias():
    runner = CliRunner()
    result = runner.invoke(cli.add_host_alias, ['', ''])
    assert 'adding alias' in result.output

def test_delete_host_alias():
    runner = CliRunner()
    result = runner.invoke(cli.delete_host_alias, ['', ''])
    assert 'deleting alias' in result.output

def test_delete_host_alias():
    runner = CliRunner()
    result = runner.invoke(cli.delete_host_alias, ['', ''])
    assert 'deleting alias' in result.output

def test_get_host_by_extattrs():
    runner = CliRunner()
    result = runner.invoke(cli.get_host_by_extattrs, [''])
    assert 'getting host by extensible' in result.output

def test_get_host_by_regexp():
    runner = CliRunner()
    result = runner.invoke(cli.get_host_by_regexp, [''])
    assert 'getting host by fqdn regexp' in result.output

def test_get_host():
    runner = CliRunner()
    result = runner.invoke(cli.get_host, [''])
    assert 'get host record' in result.output

def test_get_host_by_ip():
    runner = CliRunner()
    result = runner.invoke(cli.get_host_by_ip, [''])
    assert 'getting host record by ip' in result.output

def test_get_host_extattrs():
    runner = CliRunner()
    result = runner.invoke(cli.get_host_extattrs, [''])
    print (result.output)
    assert 'getting host extensible' in result.output

def test_create_network():
    runner = CliRunner()
    result = runner.invoke(cli.create_network, [''])
    assert 'creating network' in result.output

def test_delete_network():
    runner = CliRunner()
    result = runner.invoke(cli.delete_network, [''])
    assert 'deleting network' in result.output

def test_next_avaiable_network():
    runner = CliRunner()
    result = runner.invoke(cli.next_available_network, ['', ''])
    assert 'getting next available network' in result.output

def test_get_networkobject():
    runner = CliRunner()
    result = runner.invoke(cli.get_networkobject, [''])
    assert 'getting networkobject' in result.output

def test_get_network_by_ip():
    runner = CliRunner()
    result = runner.invoke(cli.get_network_by_ip, [''])
    assert 'getting network by ip' in result.output

def test_get_network_by_extattrs():
    runner = CliRunner()
    result = runner.invoke(cli.get_network_by_extattrs, [''])
    assert 'getting network by extensible' in result.output

def test_get_network_extattrs():
    runner = CliRunner()
    result = runner.invoke(cli.get_network_extattrs, [''])
    assert 'getting network extensible' in result.output

def test_update_network_extattrs():
    runner = CliRunner()
    result = runner.invoke(cli.update_network_extattrs, ['', ''])
    assert 'updating network extensible' in result.output

def test_delete_network_extattrs():
    runner = CliRunner()
    result = runner.invoke(cli.delete_network_extattrs, ['', ''])
    assert 'deleting network extensible' in result.output

def test_create_networkcontainer():
    runner = CliRunner()
    result = runner.invoke(cli.create_networkcontainer, [''])
    assert 'creating network container' in result.output

def test_delete_networkcontainer():
    runner = CliRunner()
    result = runner.invoke(cli.delete_networkcontainer, [''])
    assert 'deleting network container' in result.output

def test_create_txt_record():
    runner = CliRunner()
    result = runner.invoke(cli.create_txt_record, ['', ''])
    assert 'creating text record' in result.output

def test_delete_txt_record():
    runner = CliRunner()
    result = runner.invoke(cli.delete_txt_record, [''])
    assert 'deleting text record' in result.output

def test_get_txt_by_regexp():
    runner = CliRunner()
    result = runner.invoke(cli.get_txt_by_regexp, [''])
    assert 'getting text record by regexp' in result.output

def test_create_dhcp_range():
    runner = CliRunner()
    result = runner.invoke(cli.create_dhcp_range, ['', ''])
    assert 'creating DHCP IP range' in result.output

def test_delete_dhcp_range():
    runner = CliRunner()
    result = runner.invoke(cli.delete_dhcp_range, ['', ''])
    assert 'deleting DHCP IP range' in result.output

def test_get_next_available_ip():
    runner = CliRunner()
    result = runner.invoke(cli.get_next_available_ip, [''])
    assert 'getting next available ip' in result.output

def test_get_ip_by_host():
    runner = CliRunner()
    result = runner.invoke(cli.get_ip_by_host, [''])
    assert 'getting ip for host' in result.output

if __name__ == '__main__':
    test__delete_cname()
    test_create_cname()
    test__update_cname()
    test_create_host_record()
    test_delete_host_record()
    test_add_host_alias()
    test_delete_host_alias
    test_get_host_by_extattrs()
    test_get_host_by_regexp()
    test_get_host()
    test_get_host_by_ip()
    test_get_host_extattrs()
    test_create_network()
    test_delete_network()
    test_get_next_available_network()
    test_get_networkobject()
    test_get_network_by_ip()
    test_get_network_by_extattrs()
    test_get_network_extrattrs()
    test_update_network_extattrs()
    test_delete_network_extattrs()
    test_create_networkcontainer()
    test_delete_networkcontainer()
    test_create_txt_record()
    test_delete_txt_record()
    test_get_txt_by_regexp()
    test_create_dhcp_range()
    test_delete_dhcp_range()
    test_get_next_available_ip()
    test_get_ip_by_host()