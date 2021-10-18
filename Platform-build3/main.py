from network import LTE
import time
import socket
import uos


randomval = os.urandom(1)[0]


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

print(randomval)
# -> stuur de random value door naar het platform -> -> ->
time.sleep(10)

lte.deinit()
