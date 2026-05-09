from jnpr.junos import Device
from lxml import etree

dev = Device("172.25.11.1", user="lab", password="lab123")
dev.open()

routes  = dev.rpc.get_route_information(destintion="10.0.0.0/24", exact=True)

print(etree.tostring(routes, pretty_print=True).decode())

dev.close()
