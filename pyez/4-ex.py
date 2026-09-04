"""write descipritions to interface
"""
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree

config_update = """
interfaces {
    ge-0/0/2 {
        description CHNAGED_FROM_CONFIGURED_USING_NETCONF;
        unit 0 {
            family inet {
                address 10.10.13.1/30;
            }
        }                                   
    }
}

"""
with Device(host="10.100.100.2", user="lab", password="lab123") as dev:
    cu = Config(dev)
    # print(help(cu))
    cu.load(config_update)
    print(cu.diff())
    cu.commit_check()
    cu.commit()