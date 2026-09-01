from jnpr.junos import Device 
from jnpr.junos.utils.config import Config

with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
  with Config(dev) as cu:
    cu.load("set system host-name router1", format="set")
    cu.commit()
    print("hostname updated")
