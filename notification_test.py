from ncclient import manager

HOST="192.168.100.2"
USER="lab"
PASS="lab123"

with manager.connect(
    host=HOST,
    port=830,
    username=USER,
    password=PASS,
    ) as m:
    m.create_subscription()
    print("created")
    while True:
        notification = m.take_notification()
        print("recieved")
        if notification:
            print(notification.notification_xml)