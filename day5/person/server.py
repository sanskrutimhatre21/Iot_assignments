from flask import Flask, jsonify, request
from dbutils.execute import execute_query, execute_select_query
srv = Flask(__name__)


@srv.route('/', methods = ['GET'])
def homepage():
    return "Welcome to Person's Management"

@srv.route('/persons', methods = ['GET'])
def get_persons():
    query = "select * from persons;"
    return jsonify(execute_select_query(query=query))
    
@srv.route('/add', methods = ['POST'])
def add_person():
    uid = request.form.get('uid')
    name = request.form.get('name')
    age = request.form.get('age')
    address = request.form.get('address')
    mobile = request.form.get('mobile')
    
    query = f"insert into persons values({uid}, '{name}', {age}, '{address}', '{mobile}');"
     
    execute_query(query=query)

    return "Person is added successfully!!"

@srv.route('/del', methods = ['DELETE'])
def del_person():
    uid = request.form.get('uid')
    query = f"delete from persons where uid = {uid};"
    
    execute_query(query=query)
    return "Person is deleted successfully!!"

@srv.route('/modify', methods = ['POST'])
def modify_person():
    choice = request.form.get('choice')
    nvalue = request.form.get('nvalue')
    uid = request.form.get('uid')
    if choice == 'address':
        query = f"update persons SET address='{nvalue}' where uid = {uid};"
    elif choice == 'mobile':
        query = f"update persons SET mobile='{nvalue}' where uid = {uid};"

    execute_query(query)
    return "Person is updated successfully!!"    

if __name__ == '__main__':
    srv.run(host='0.0.0.0', port=4000, debug=True)
