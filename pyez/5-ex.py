
"""write descipritions to interface
"""
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree

command = "set interfaces ge-0/0/3 description CHANGED_AGAIN_CONFIGURED_USING_REST_API"


with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
    cu = Config(dev)
    # print(help(cu))
    cu.load(command)
    cu.pdiff()
