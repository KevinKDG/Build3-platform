#!/usr/bin/python3
import mysql.connector
import time
import paho.mqtt.client as mqtt
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123",
  database="php"
)

print(mydb)
mycursor = mydb.cursor()


#send requests
def send_query_rpi(plate, stationid):
  sql = "UPDATE anpr SET plate = %s WHERE stationid = %s"
  val = (plate, stationid)
  mycursor.execute(sql, val)
  mydb.commit()

def send_query_fipy(plate, co2):
  sql = "update autos SET verbruik = %s WHERE plate = %s"
  val = (co2, plate)
  mycursor.execute(sql, val)
  mydb.commit()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("fipy/co2")
  client.subscribe("rpi/plate")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  data = json.loads(msg.payload)
  print(data)
  if(msg.topic == "fipy/co2"):
    print(data["co2"])
    print(data["plate"])
    send_query_fipy(data["plate"], data["co2"])
  elif(msg.topic == "fipy/co2"):
    print(data["plate"])
    print(data["id"])
    send_query_fipy(data["plate"], data["stationid"])
  #print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="anpr",password="TFJ")

client.connect("localhost", 1883, 60)
