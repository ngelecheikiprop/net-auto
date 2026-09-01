from jnpr.junos import Device
from lxml import etree
with Device(host="10.100.100.2", user="lab",password="lab123") as dev:
  my_config = dev.rpc.get_config()
  print(etree.tostring(my_config.xpath("./system/host-name")[0]).decode())
