#import function
import json
from flask import Flask, request, url_for, jsonify, render_template, make_response
from pprint import pprint

#create Flask for developing webapplication and integrate postman.com
app = Flask(__name__)

#open and read json file
readjson = json.load(open('weather.json'))
read = readjson
#pprint(read)

#GET and show information
@app.route('/')
def get():
    response = make_response(jsonify(read), 200)
    return response

#GET and show details of information
@app.route('/<readid>')
def get_detail(readid):
    if readid in read:
        response = make_response(jsonify(read[readid]), 200)
        return response
    return "Weather is not found"

#POST informaion by postman.com
app.route('/<readid>', method=['POST'])
def post(readid):
    req = request.get_json()
    if readid in read:
        response = make_response(jsonify({"ERROR": "information already exists"}), 400)
        return response
    read.update({readid:req})
    response = make_response(jsonify({"massage": " New information inserted"}), 201)
    return response

#PUT and UPDATE informaion by postman.com
app.route('/<readid>', method=['PUT'])
def put(readid):
    req = request.get_json()
    if readid in read:
        read[readid] = req
        response = make_response(jsonify({"READ": "information update"}), 400)
        return response
    read.update({readid:req})
    responce = make_response(jsonify({"massage": "new information inserted"}), 201)
    return responce

#DELETE informaion by postman.com
app.route('/<readid>', method=['DELETE'])
def delete(readid):
    req = request.get_json()
    if readid in read:
        del read[readid]
        response = make_response(jsonify({"READ": "information deleted"}), 204)
        return response
    response = make_response(jsonify({"ERROR": "information already exists"}), 404)
    return response

if __name__ =="__main__":
    app.run(debug=True)











