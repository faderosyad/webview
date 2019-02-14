from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

@app.route('/form_example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST': 
      key = request.form.get('key')
      value = request.form['value']
      timestamp = get_timestamp()

      return '''<table style="width:50%" border = 1>
                <tr>
                  <th>Key</th>
                  <th>Value</th>
                  <th>Timestamp</th>
                </tr>
                <tr>
                  <td align="center">{}</td>
                  <td>{}</td>
                  <td>{}</td>
                </tr>
                </table>'''.format(key, value, timestamp)

        #return print(response.status_code)

    return '''<form method="POST">
            Key:<br> <input type="text" name="key"><br><br>
            Value:<br> <input type="text" name="value"><br><br>
            <input type="submit" value="Submit"><br>
            </form>'''

if __name__ == '__main__':
    app.run(debug = True, port = 8000)