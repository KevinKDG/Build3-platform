from network import LTE
import time
import socket
import uos
import urequests
import nb
import wifi
import json
from mqtt import MQTTClient

# ========== Wifi or NB
wifi.wificonnect('ssid', 'wachtwoord') # ssid , password


#  ========== values
randomval = os.urandom(1)[0] # 0 - 255
plate = "1abc123"

# ========== MQTT

while True:
    print("connect client")
    client = MQTTClient("fipy", "192.168.1.2", port=1883)
    client.connect()
    pack = {"plate": plate, "value": randomval} #Json format
    jsonObj = json.dumps(jsonvalues)
    data = jsonObj

    client.publish(topic="fipy/data",msg=data)
    print("Value has been sent!")
    print(data)
    time.sleep(10)

lte.deinit()
