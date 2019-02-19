from flask import Flask, render_template, request, json
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

app = Flask(__name__)

@app.route('/buatcoba', methods = ['POST', 'GET'])
def keyvalue():
      url = 'http://127.0.0.1:5000/api/v1/kvs'
      headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
      data = {"key": "kipas", "value": value}
      r = request.post(url, data=json.dumps(data), headers=headers)

      return print(r.text)

if __name__ == '__main__':
    app.run(debug = True, port= 3000)