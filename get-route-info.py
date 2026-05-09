from jnpr.junos import Device
from lxml import etree

dev = Device("172.25.11.1", user="lab", password="lab123")
dev.open()

routes  = dev.rpc.get_route_information(destintion="10.0.0.0/24", exact=True)

o#print(etree.tostring(routes, pretty_print=True).decode())
"""
<route-information>
  <route-table>
    <table-name>inet.0</table-name>
    <destination-count>9</destination-count>
    <total-route-count>9</total-route-count>
    <active-route-count>9</active-route-count>
    <holddown-route-count>0</holddown-route-count>
    <hidden-route-count>0</hidden-route-count>
    <rt style="brief">
      <rt-destination>10.0.0.0/24</rt-destination>
      <rt-entry>
        <active-tag>*</active-tag>
        <current-active/>
        <last-active/>
        <protocol-name>Direct</protocol-name>
        <preference>0</preference>
        <age seconds="3324">00:55:24</age>
        <nh>
          <selected-next-hop/>
          <via>ge-0/0/0.0</via>
        </nh>
      </rt-entry>
    </rt>
  </route-table>
</route-information>

"""
#now improve to use xpath 
for route in routes.path(".//rt"):
  print(route)
  dest = route.findtext("rt-destination")
  proto = route.findtext(".//protocol-name")
  print(f"{dest} via {proto}")

dev.close()
