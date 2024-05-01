from flask import  jsonify

def create_response(msg, error=True):
    d = dict()
    if error != True:
        d = {
            "statusCode":'?',
            "statusMsg":'?',
            "msg":msg
        }
    else:
        d = {
            "statusCode":200,
            "stutusMsg":"OK",
            "msg":msg
        }

    return jsonify(d)