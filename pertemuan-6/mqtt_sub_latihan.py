import json
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from datetime import datetime

client_mongo = MongoClient("mongodb://localhost:27017/")
db = client_mongo["latihan6"]
collection = db["produksi_mqtt"]

def on_connect(client, userdata, flags, rc):
    print("Connected:", rc)
    client.subscribe("pabrik/produksi")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    # tambah timestamp
    data["timestamp"] = datetime.now()

    # hitung reject rate
    reject_rate = (data["reject"] / data["jumlah"]) * 100

    if reject_rate > 5:
        print("⚠️ WARNING: Reject tinggi!")
        data["peringatan"] = True
    else:
        data["peringatan"] = False

    collection.insert_one(data)
    print("[SUB]", data)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com", 1883, 60)
mqtt_client.loop_forever()