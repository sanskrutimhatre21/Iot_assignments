from flask import Flask, jsonify, request
from person.retrieve import get_persons
from person.create import insert_person
from person.delete import delete_person
from person.update import update_person
from response import create_response

srv = Flask(__name__)

@srv.route('/', methods = ['GET'])
def homepage():
    return ("Welcome to Person's Management") 

@srv.route('/persons', methods = ['GET','POST','DELETE','PUT'])
def get_persons():
    if request.method == 'GET':
        return create_response(get_persons())
    elif request.method == 'POST':
        uid = request.get_json().get('uid')
        name = request.get_json().get('name')
        age = request.get_json().get('age')
        address = request.get_json().get('address')
        mobile = request.get_json().get('mobile')
        insert_person(uid, name, age, address, mobile)
    elif request.method == 'DELETE':
        uid = request.get_json().get('uid')
        delete_person(uid)
        return ("Person deleted successfully!!")
    elif request.method == 'PUT':
        uid = request.get_json().get('uid')
        choice = request.get_json().get('choice')
        nvalue = request.get_json().get('nvalue')
        update_person(choice, nvalue, uid)
    
    return create_response("Executed successfully")

if __name__ == '__main__':
    srv.run(host='0.0.0.0', port=4000, debug=True)