from jnpr.junos import Device
from lxml import etree
with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
    interfaces = dev.rpc.get_interface_information()
    print(interfaces)
    with open  ("./0-example_output.xml", "w") as f: 
        f.write(etree.tostring(interfaces).decode())
    # print(etree.tostring(interfaces))