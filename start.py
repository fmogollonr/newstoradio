# -*- coding: utf-8 -*-
import tts
import aemet
import time
import threading
import metarairport
import requests
import json

from flask import Flask, jsonify, request

app = Flask(__name__) #create the Flask app


def say(text):
    speech=tts.tts()
    speech.say(text)


@app.route('/speak')
def speak():
    if 'text' in request.args:
        say(request.args['text'])
        return 'Say '+request.args['text']
    else:
  	    return 'Dont say anything'

@app.route('/weather')
def query_weather():
    if 'city' in request.args:
        tiempo = aemet.Localidad(request.args['city'], time.strftime("%d/%m/%Y"))
        tiempo_texto="El tiempo para "+tiempo.get_localidad()+": temperatura maxima: "+tiempo.get_temperatura_maxima()
        r = requests.get("http://localhost:5000/speak?text="+tiempo_texto)
        #tiempo = Aemet.Localidad('28079', time.strftime("%d/%m/%Y"))
        #tiempo_texto="El tiempo para "+tiempo.get_localidad()+": temperatura máxima: "+tiempo.get_temperatura_maxima()
        #say("El tiempo para Madrid: temperatura máxima: 16 grados")
        return 'Get weather for '+request.args['city']
    else:
        return 'De que me hablas'

@app.route('/airportweather')
def query_airport_weather():
    if 'airport' in request.args:
        metarinstance=metarairport.metar()
        results=metarinstance.getMetar(request.args['airport'])
        prediccion=json.loads(results.text)
        metarpredicts =prediccion['data']
        for predict in metarpredicts:
                resumen_meteorologico=metarinstance.parseMetar(predict)
                #r = requests.get("http://localhost:5000/speak?text="+resumen_meteorologico)
                return 'METAR results: '+resumen_meteorologico,200



if __name__ == '__main__':
    app.run(debug=False, port=5000) #run app in debug mode on port 5000