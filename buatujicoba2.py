from flask import Flask, render_template, request, json
from datetime import datetime

app = Flask(__name__)

def keyvalue(key, value):
    url = 'http://127.0.0.1:5000/api/v1/kvs'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {"key": key, "value": value}
    r = request.post(url, data=json.dumps(data), headers=headers)
    return

def cobaaja():
    key = "fade"
    value = "rosyad"
    keyvalue(key, value)
    return ("success")

if __name__ == '__main__':
    app.run(debug = True, port= 1500)
