import paho.mqtt.client as mqtt

mqttc = mqtt.Client("Publisher")

def on_publish(client, userdata, mid):
    print("Message is published successfully")

mqttc.on_publish = on_publish

mqttc.connect(host="localhost")

mqttc.publish("sensor/temperature", "40")

mqttc.disconnect()