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
wifi.wificonnect('ssid', 'pwd') # ssid , password
# nb.nbconnect()

#  ========== values
randomval = os.urandom(1)[0]s # 0 - 255
plate = "1abc123"

pack = {"plate": plate, "value": randomval} #Json format
jsonObj = json.dumps(pack)
data = jsonObj
# ========== MQTT

client = MQTTClient("fipy", "192.168.1.2", port=1883)
client.connect()
print("client connected")

while True:
    client.publish(topic="fipy/data",msg=data)
    print("Value has been sent!")
    print(data)
    time.sleep(10)
