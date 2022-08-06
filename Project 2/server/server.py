from flask import Flask, jsonify
import os
import requests
import socket

app = Flask(__name__)

port = os.getenv('serverport', '8080')

@app.route("/")
def return_information():
    hostname = socket.gethostname()
    url = 'http://api.weatherstack.com/current?access_key=c01b87aa277ab75433b387842e114c59&query=Tehran'
    res = requests.get(url)
    res = res.json()['current']

    data = dict()
    data['hostname'] = hostname
    data['weather_descriptions'] = res['weather_descriptions'][0]
    data['temperature'] = res['temperature']
    data['wind_speed'] = res['wind_speed']
    data['humidity'] = res['humidity']
    data['feelslike'] = res['feelslike']
    
    print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
