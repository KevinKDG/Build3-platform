import pycom
from network import WLAN
import machine
import time

def wificonnect(ssid, passwrd):
    pycom.heartbeat(False)
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid, auth=(WLAN.WPA2, passwrd))

    while not wlan.isconnected():
        time.sleep(5)
        pycom.rgbled(0xFF0000)          # rgb Red
        print("no connection")
        machine.idle()

    print("WiFi connected succesfully")
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)              # rgb Green
