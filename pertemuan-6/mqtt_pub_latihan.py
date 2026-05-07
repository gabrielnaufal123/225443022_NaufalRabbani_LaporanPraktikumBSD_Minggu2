import json, time, random
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "pabrik/produksi"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

while True:
    data = {
        "batch": f"B{random.randint(1,100)}",
        "mesin": f"CNC-{random.randint(1,5)}",
        "jumlah": random.randint(100, 500),
        "reject": random.randint(0, 50)
    }

    client.publish(TOPIC, json.dumps(data))
    print("[PUB]", data)
    time.sleep(3)