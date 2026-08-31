from ncclient import manager

HOST="192.168.100.2"
USER="lab"
PASS="lab123"

# filter = """
# <filter type="subtree">
#   <interface-information xmlns="http://xml.juniper.net/junos/24.2R1/junos-interface">
#   </interface-information>
# </filter>
# # """

with manager.connect(
    host=HOST,
    port=830,
    username=USER,
    password=PASS,
    device_params={"name": "junos"}
    ) as m:
    m.create_subscription()
    print("created")
    while True:
        notification = m.take_notification()
        print("recieved")
        if notification:
            print(notification.notification_xml)
        else:
            print("no notification yet")