#Fade Khalifah Rosyad
#Python script build for send post and receive get for Genesis IVA

#Pada import digunakan 2 request dimana 1 requests dari python dan satu lagi request dari Flask
#Hal ini terjadi dikarenakan terdapat perbedaan cara penggunaan yang menyebabkan dibutuhkan requests pada function dan request pada route
import requests, json
from flask import Flask, render_template, request, json
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%d-%m-%Y %H:%M:%S"))

KVStoreEndpoint = 'http://127.0.0.1:5000/api/v1/kvstore' #Endpoint URL untuk Genesis IVA bagian KVStore
ServicesEndpoint = 'http://127.0.0.1:5000/api/v1/services' #Endpoint URL untuk Genesis IVA bagian Services
headers = {'Content-type': 'application/json'} # Header yang dapat diterima oleh Genesis IVA

#Function untuk menerima data dari Genesis IVA dengan method GET (KeyValue)
def gettingdata():
    terima = requests.get(KVStoreEndpoint, headers=headers)
    return terima

#Function untuk mengirimkan data ke Genesis IVA dengan method POST (KeyValue)
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
    #iterasi untuk mengirimkan banyak data key dan value secara bersamaan
            i = 0
            while i < 100: #Pembatasan pengiriman hanya untuk 100 key dan value
                key = request.form.get('key'+ str(i))
                value = request.form['value'+ str(i)]
                kirimin = postingdata(key, value)
                i += 1
            timestamp = get_timestamp()
            return render_template('home2.html', key=key, value=value, timestamp=timestamp) #masih terdapat masalah dalam penampilan ke table, akan dicoba untuk melakukan GET ke table

    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug = True, port= 2000)
