"""get all the descriptions of all interfaces
check the output
"""
from jnpr.junos import Device
from lxml import etree
with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
    interfaces = dev.rpc.get_interface_information(descriptions=True)
    interfaces = interfaces.xpath("./physical-interface/description")
    # etree.ElementTree(interfaces).write(
    #     "3-ex_output_1.xml",
    #     pretty_print=True,
    #     encoding="utf-8",
    #     xml_declaration=True
    # )
    for interface in interfaces:
        print(interface.text)
        # etree.ElementTree(interface).write(
        #     "3-ex_output_1.xml",
        #     pretty_print=True,
        #     encoding="utf-8",
        #     xml_declaration=True
        # )
        # break
    # names = interfaces.xpath("./physical-interface/")
    # print("names:",len(names))
    # for name in names:
    #     print(etree.tostring(name, pretty_print=True).decode())