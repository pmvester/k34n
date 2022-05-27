# -*- coding: utf-8 -*-

import json
import paho.mqtt.client as mqtt
import time
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "k34db"
org = "k34"
token = "FYsVKuzgNIBE0AZ435pwuROpkQKnmvcVyYdDSiMxMLt3FwnNi1WXmZLAVSkaLXWXhVvvvIAOj9rP8Ympzr0G8g=="
# Store the URL of your InfluxDB instance
url="http://localhost:8086"

iclient = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = iclient.write_api(write_options=SYNCHRONOUS)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("k34/#")
    client.subscribe("sensors/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
    print(str(msg.payload))
    try:
      pl = json.loads(msg.payload)
      if msg.topic == "k34/bme280":
        json_body = [
          {
            "measurement": "technical",
            "time": pl["time"] * 1000000,
            "fields": {
              "pressure": pl["pressure"],
              "humidity": pl["humidity"],
              "temperature": pl["temperature"]
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "k34/heat/water":
        json_body = [
          {
            "measurement": "heatWater",
            "time": pl["timestamp"] * 1000000,
            "fields": {
              "feedTemperature": pl["temperature"]["feed"],
              "returnTemperature": pl["temperature"]["return"]
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/actual_consumption":
        json_body = [
          {
            "measurement": "power",
            "time": int(time.time() * 1000000000),
            "fields": {
              "power": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/consumption":
        json_body = [
          {
            "measurement": "energy",
            "time": int(time.time() * 1000000000),
            "fields": {
              "energy": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/l1_voltage":
        json_body = [
          {
            "measurement": "p1meter",
            "time": int(time.time() * 1000000000),
            "fields": {
              "l1_voltage": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/l2_voltage":
        json_body = [
          {
            "measurement": "p1meter",
            "time": int(time.time() * 1000000000),
            "fields": {
              "l2_voltage": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/l3_voltage":
        json_body = [
          {
            "measurement": "p1meter",
            "time": int(time.time() * 1000000000),
            "fields": {
              "l3_voltage": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/l1_instant_power_current":
        json_body = [
          {
            "measurement": "p1meter",
            "time": int(time.time() * 1000000000),
            "fields": {
              "l1_current": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/l2_instant_power_current":
        json_body = [
          {
            "measurement": "p1meter",
            "time": int(time.time() * 1000000000),
            "fields": {
              "l2_current": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "sensors/power/p1meter/l3_instant_power_current":
        json_body = [
          {
            "measurement": "p1meter",
            "time": int(time.time() * 1000000000),
            "fields": {
              "l3_current": int(pl)
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "k34/temparkiv":
        json_body = [
          {
            "measurement": "archive",
            "time": int(time.time() * 1000000000),
            "fields": {
              "temperature": pl["temperature"]
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "k34/tempout":
        json_body = [
          {
            "measurement": "outdoor",
            "time": int(time.time() * 1000000000),
            "fields": {
              "temperature": pl["temperature"]
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "k34/tempgarage":
        json_body = [
          {
            "measurement": "garage",
            "time": int(time.time() * 1000000000),
            "fields": {
              "temperature": pl["temperature"]
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      elif msg.topic == "k34/matsal":
        json_body = [
          {
            "measurement": "dining",
            "time": int(time.time() * 1000000000),
            "fields": {
              "humidity": pl["humidity"],
              "temperature": pl["temperature"]
            }
          }
        ]
        write_api.write(bucket, org, json_body)
      else:
        pass
    except:
      print("something went wrong, probably unintelligible payload")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()

