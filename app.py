from flask import Flask, render_template, request, json
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

app = Flask(__name__)

@app.route('/ivaconfig', methods = ['POST', 'GET'])
def ivaconfig():
    if request.method == 'POST': 
      service = request.form.get('service')
      timestamp = get_timestamp()
      return render_template('home.html', service = service, timestamp = timestamp)

    return render_template('home.html')

@app.route('/keyvalue', methods = ['POST', 'GET'])
def keyvalue():
    if request.method == 'POST': 
      key = request.form.get('key')
      value = request.form['value']
      timestamp = get_timestamp()

      url = 'http://127.0.0.1:5000/api/v1/kvs'
      headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
      data = {"key": key,"value": value}
      r = request.post(url, data=json.dumps(data), headers=headers)

      return r

    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug = True, port= 2000)