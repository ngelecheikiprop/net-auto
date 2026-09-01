"""
xpath with juniper config
"""
from jnpr.junos import Device
with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
  print(dev.facts["hostname"])
