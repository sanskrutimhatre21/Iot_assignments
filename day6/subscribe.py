import paho.mqtt.client as MQTTClient

mqttc = MQTTClient.Client("Subscriber")

def on_connect(client, userdata, flags, reason_code):
    if reason_code != 0:
        print(f"Connection is failed {reason_code}")
    else:
        mqttc.subscribe("sensor/ldr")

def on_message(client, userdata, message):
    print(f"Received msg : {message.payload}")

mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("localhost")

mqttc.loop_forever()