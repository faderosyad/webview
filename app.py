#Fade Khalifah Rosyad
#Python script build for send post and receive get for Genesis IVA

#Pada import digunakan 2 request dimana 1 requests dari python dan satu lagi request dari Flask
#Hal ini terjadi dikarenakan terdapat perbedaan cara penggunaan yang menyebabkan dibutuhkan requests pada function dan request pada route
import requests, json
from flask import Flask, render_template, request, json
from flask.views import View
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

KVStoreEndpoint = 'http://127.0.0.1:5000/api/v1/kvstore' #Endpoint URL untuk Genesis IVA bagian KVStore
ServicesEndpoint = 'http://127.0.0.1:5000/api/v1/services' #Endpoint URL untuk Genesis IVA bagian Services
headers = {'Content-type': 'application/json'} # Header yang dapat diterima oleh Genesis IVA

#Function untuk menerima data dari Genesis IVA dengan method GET
def gettingdata():
    terima = requests.get(KVStoreEndpoint, headers=headers)
    return terima

#Function untuk mengirimkan data ke Genesis IVA dengan method POST
def postingdata(key, value):
    data = {'key': key, 'value': value}
    kirim = requests.post(KVStoreEndpoint, data=json.dumps(data), headers=headers)
    return kirim

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
    #Disini perlu diiterasikan untuk membentuk pengiriman data secara iterasi dalam sekali operasi
        key = request.form.get('key')
        value = request.form['value']
        kirimin = postingdata(key, value)
        timestamp = get_timestamp()
        return render_template('home2.html', key=key, value=value, timestamp=timestamp)

    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug = True, port= 2000)
