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
      keyjson = request.get_json(key)
      valuejson = request.get_json(value)

      response=app.response_class(
        response = json.dumps(keyjson, valuejson),
        status=200,
        mimetype='application/json'
      )
      return response

    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug = True, port= 2000)