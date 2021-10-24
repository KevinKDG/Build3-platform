from network import LTE
import time
import socket
import uos
import urequests

def nbconnect():
    print("starting NB-IOT connection")

    # NB-IOT CONNECTION
    lte = LTE()

    lte.attach()

    print("attaching..",end='')

    while not lte.isattached():
        time.sleep(0.25)    # sleep 0.25 sec

        print('.',end='')
    print("attached!")
    lte.connect()
    print("connecting [##",end='')
    while not lte.isconnected():
        time.sleep(0.25)
        print('#',end='')
    print("] connected!")


    lte.deinit()
