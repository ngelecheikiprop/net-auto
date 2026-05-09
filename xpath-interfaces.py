from jnpr.junos import Device

dev = Device(host="10.10.10.1", user=admin, password="mypass")

dev.open()

interfaces = dev.rpc.get_interface_information()

names = interfaces.xpath("//physical-interface/name")

for nam in nmaes:
  print(name.text)

dev.close()
