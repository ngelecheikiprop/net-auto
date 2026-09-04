"""get all interfaces"""
from jnpr.junos import Device
from lxml import etree
with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
    interfaces = dev.rpc.get_interface_information()
    names = interfaces.xpath("./physical-interface[normalize-space(name)='ge-0/0/0']")
    print("names:",len(names))
    for name in names:
        print(etree.tostring(name, pretty_print=True).decode())