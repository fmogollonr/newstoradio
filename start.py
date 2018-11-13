# -*- coding: utf-8 -*-
import tts
import aemettiempo
import threading
import metarairport
import requests
import json
import time
import os

from flask import Flask, jsonify, request,Response

app = Flask(__name__) #create the Flask app

# Get file
def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join("", filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

# serve static html file

def say(text):
    speech=tts.tts()
    speech.say(text)
@app.route('/', methods=['GET'])
def getindex2():  # pragma: no cover
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

@app.route('/index.html', methods=['GET'])
def getindex():  # pragma: no cover
    content = get_file('index.html')
    return Response(content, mimetype="text/html")
    
@app.route('/speak')
def speak():
    if 'text' in request.args:
        say(request.args['text'])
        return 'Say '+request.args['text']
    else:
  	    return 'Dont say anything'

@app.route('/genmessage')
def genmessage():
    if 'text' in request.args:
        if request.args['text'] is not "":
            say(request.args['text'])
    else:
        return 'basura',200
    if 'city' in request.args:
        if request.args['city'] is not "":
            print("city is ",request.args['city'])
            aemettiempoinstance=aemettiempo.amettiempo()
            if aemettiempoinstance.validCity(request.args['city']):
                tiempo=aemettiempoinstance.getTiempo(request.args['city'],time.strftime("%d/%m/%Y"))
                say(tiempo)
    else:
        return 'basura',200
    if 'airport' in request.args:
        if request.args['airport'] is not "":
            metarinstance=metarairport.metar()
            if metarinstance.validAirport(request.args['airport']):
                results=metarinstance.getMetar(request.args['airport'])
                prediccion=json.loads(results.text)
                metarpredicts =prediccion['data']
                for predict in metarpredicts:
                    resumen_meteorologico=metarinstance.parseMetar(predict)
                    say(resumen_meteorologico)
    else:
  	    return 'Dont say anything',200
    
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

@app.route('/weather')
def query_weather():
    if 'city' in request.args:
        aemettiempoinstance=aemettiempo.amettiempo()
        tiempo=aemettiempoinstance.getTiempo(request.args['city'],time.strftime("%d/%m/%Y"))
        say(tiempo)
        return tiempo,200
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
                say(resumen_meteorologico)
                return 'METAR results: '+resumen_meteorologico,200



if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=False, port=5000) #run app in debug mode on port 5000