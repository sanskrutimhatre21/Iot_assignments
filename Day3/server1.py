# import Flask class from flask module
from flask import Flask

# create a flask server
server = Flask(__name__)         # ==> "__main__"


@server.route('/')  # decorator - it is used to bind function and url (REST API)
def root():
    return "This is my First Flask server"


# run flask server
server.run()

#  http://127.0.0.1:5000 
#   http - protocol 
#   127.0.0.1 - server ip 
#   localhost - domain name 
#   5000 - port 