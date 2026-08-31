#!/usr/bin/env python3
#from jnpr.junos import Device
#from sys import argv
#print(argv)

from lxml import etree

xml = """
<root>
<interface>
    <name>ge-0/0/0</name>
    <status>up</status>
</interface>
<interface>
<name>ge-0/0/1</name>
</interface>
</root>
"""

root = etree.fromstring(xml)
#print(type(root))
result = root.xpath("/root")[0]
print(len(result))
print(type(result))
print(result.text)
"""
for node in result:
    new_node = node.xpath("..")
    for x in new_node:
        print(etree.tostring(x, pretty_print=True).decode())
"""
print(etree.tostring(result, pretty_print=True).decode())
#print(result)
