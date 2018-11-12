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
port=80

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

@app.route('/index.html', methods=['GET'])
def getindex():  # pragma: no cover
    content = get_file('index.html')
    return Response(content, mimetype="text/html")
    
@app.route('/speak')
def genmessage():
    if 'text' in request.args:
        say(request.args['text'])
        return 'Say '+request.args['text']
    else:
  	    return 'Dont say anything'

@app.route('/genmessage')
def speak():
    #return "OK",200
    if 'text' in request.args:
        #return "Text is"+request.args['text'],200
        say(request.args['text'])
        #return 'Say '+request.args['text']
    if 'city' in request.args:
        #return "City is"+request.args['city'],200
        aemettiempoinstance=aemettiempo.amettiempo()
        tiempo=aemettiempoinstance.getTiempo(request.args['city'],time.strftime("%d/%m/%Y"))
        r = requests.get("/speak?text="+tiempo)
        #return tiempo,200
    if 'airport' in request.args:
        #return "Airport is "+['airport'],200
        metarinstance=metarairport.metar()
        results=metarinstance.getMetar(request.args['airport'])
        prediccion=json.loads(results.text)
        metarpredicts =prediccion['data']
        for predict in metarpredicts:
                resumen_meteorologico=metarinstance.parseMetar(predict)
                r = requests.get("/speak?text="+resumen_meteorologico)
                #return 'METAR results: '+resumen_meteorologico,200

    else:
  	    return 'Dont say anything',200
    
    return 'catacrack',200

@app.route('/weather')
def query_weather():
        #http://www.aemet.es/xml/municipios/localidad_20069.xml
    if 'city' in request.args:
        aemettiempoinstance=aemettiempo.amettiempo()
        tiempo=aemettiempoinstance.getTiempo(request.args['city'],time.strftime("%d/%m/%Y"))
        #tiempo = aemet.Localidad(request.args['city'], time.strftime("%d/%m/%Y"))
        #print(tiempo.get_localidad())
        #tiempo_texto="El tiempo para "+tiempo.get_localidad().decode("utf-8")+": temperatura maxima: "+str(tiempo.get_temperatura_maxima())
        #r = requests.get("http://localhost:5000/speak?text="+tiempo_texto)
        #tiempo = Aemet.Localidad('28079', time.strftime("%d/%m/%Y"))
        #tiempo_texto="El tiempo para "+tiempo.get_localidad()+": temperatura máxima: "+tiempo.get_temperatura_maxima()
        #say("El tiempo para Madrid: temperatura máxima: 16 grados")
        #return 'Predicción meteorológica para '+request.args['city']+': '+tiempo_texto,200
        r = requests.get("/speak?text="+tiempo)
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
                r = requests.get("/speak?text="+resumen_meteorologico)
                return 'METAR results: '+resumen_meteorologico,200



if __name__ == '__main__':
    app.run(debug=False, port=5000) #run app in debug mode on port 5000