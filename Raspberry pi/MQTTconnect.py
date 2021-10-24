#!/usr/bin/env python3
import mysql.connector
import paho.mqtt.client as mqtt  # import the client1
import time
import json


mydb = mysql.connector.connect(
    host="localhost",  
    user="name",
    password="pwd",
    database="DB1"
)
print(mydb)
mycursor = mydb.cursor()

def send_fipy_data(plate,value):
    sql = "UPDATE platform SET plate = %s WHERE data = %s"
    val = (plate, value)
    mycursor.execute(sql, val)
    mydb.commit()


def on_message(client, userdata, message):
    global mycursor, sql, val
    mycursor = mydb.cursor()
    jsonvals = json.load(message.payload)
    print(data["plate"])
    print(data["value"])
    send_fipy_data(data["plate"],["value"])

broker_address = "localhost"  #rpi
client = mqtt.Client("")
client.on_message = on_message
client.connect(broker_address)
client.subscribe("fipy/data")
client.loop_forever()


