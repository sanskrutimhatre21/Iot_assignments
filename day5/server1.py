from flask import Flask, request, jsonify
from dbutils.execute import execute_query, execute_select_query
import paho.mqtt.client as mqtt


srv = Flask(__name__)

mqttc = mqtt.Client("Publisher")

@srv.route('/', methods = ['GET'])
def homepage():
    mqttc.connect("localhost")
    mqttc.publish("health/status", "GET : success")
    mqttc.disconnect()
    return "Welcome to Fitness Tracker"

@srv.route('/add', methods = ['POST'])
def add_info():
    name = request.get_json().get('name')
    age = request.get_json().get('age')
    city = request.get_json().get('city')
    steps = request.get_json().get('steps')
    pulse = request.get_json().get('pulse')
    oxygen = request.get_json().get('oxygen')
    temperature = request.get_json().get('temperature')

    query = f"insert into health (name, age, city, steps, pulse, oxygen, temp) values('{name}', {age}, '{city}', {steps}, {pulse}, {oxygen}, {temperature});"
     
    execute_query(query=query)

    mqttc.connect("localhost");
    mqttc.publish("health/status", "GET : success")
    mqttc.disconnect()

    return "Health parameters are successfully added"
   

@srv.route('/all', methods = ['GET'])
def get_all():
    query = f"select * from health;"
    
    mqttc.connect("localhost");
    mqttc.publish("health/status", "GET : success")
    mqttc.disconnect()
    
    return jsonify(execute_select_query(query=query))

@srv.route('/info', methods = ['GET'])
def get_info():
    name = request.get_json().get('name')

    query = f"select * from health where name ='{name}';"

    mqttc.connect("localhost");
    mqttc.publish("health/status", "GET : success")
    mqttc.disconnect()
    return jsonify(execute_select_query(query))

@srv.route('/update', methods = ['PUT'])
def update_city():
    name = request.form.get('name')
    city = request.form.get('city')

    query = f"update health SET city = '{city}' where name = '{name}';"

    mqttc.connect("localhost");
    mqttc.publish("health/status", "GET : success")
    mqttc.disconnect()

    execute_query(query)
    
    return f"city of {name} is updated as {city}"

@srv.route('/steps', methods = ['GET'])
def get_steps():
    query = f"select * from health order by steps DESC limit 1;"

    mqttc.connect("localhost");
    mqttc.publish("health/status", "GET : success")
    mqttc.disconnect()
    return jsonify(execute_select_query(query))

if __name__ == '__main__':
    srv.run(host='0.0.0.0', port=3000, debug=True)
