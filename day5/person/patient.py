from flask import Flask, jsonify,request
from dbutils.execute import execute_query, execute_select_query
import paho.mqtt.client as mqtt


srv = Flask(__name__)

mqttc = mqtt.Client("Publisher")

@srv.route('/', methods = ['GET'])
def homepage():
    mqttc.connect("localhost");
    mqttc.publish("patient/status", "GET : Fit")
    mqttc.disconnect()
    return "Welcome to Patient's Record File"

@srv.route('/add', methods = ['POST'])
def add_patient():
    name = request.form.get('name')
    age = request.form.get('age')
    bloodgroup = request.form.get('bloodgroup')
    weight = request.form.get('weight')

    query = f"insert into patients values('{name}', {age}, '{bloodgroup}', {weight});"
    
    execute_query(query=query)
    
    return "Patient added successfully!!"

@srv.route('/all', methods = ['GET'])
def get_all():

    query = f"select * from patients;"
     
    return execute_select_query(query=query)


@srv.route('/del', methods = ['DELETE'])
def del_patient():
    name = request.form.get('name')

    query = f"delete from patients where name = '{name}';"

    execute_query(query=query)
    return "Patient's record deleted successfully!!"
    
@srv.route('/update', methods = ['PUT'])
def update_patient():
    choice = request.form.get('choice')
    nvalue = request.form.get('nvalue')
    name = request.form.get('name')
    if choice == 'weight':
        query = f"update patients SET weight='{nvalue}' where name = '{name}';"
    elif choice == 'age':
        query = f"update patients SET age='{nvalue}' where name = '{name}';"

        execute_query(query)
        
        return "Patient's record is updated successfully!!"

if __name__ == '__main__':
    srv.run(host='0.0.0.0', port=4000, debug=True)