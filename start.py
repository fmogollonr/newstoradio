# -*- coding: utf-8 -*-
import tts
import Aemet
import time
import threading

from flask import Flask, jsonify, request

app = Flask(__name__) #create the Flask app


def say(text):
    speech=tts.tts()
    speech.say(text)


@app.route('/speak')
def speak():
    if 'text' in request.args:
        say("Hola "+request.args['text'])
        return 'Say '+request.args['text']
    else:
  	    return 'Dont say anything'

@app.route('/weather')
def query_weather():
    if 'city' in request.args:
        tiempo = Aemet.Localidad('28079', time.strftime("%d/%m/%Y"))
        tiempo_texto="El tiempo para "+tiempo.get_localidad()+": temperatura máxima: "+tiempo.get_temperatura_maxima()
        #say("El tiempo para Madrid: temperatura máxima: 16 grados")
        return 'Get weather for '+request.args['city']
    else:
        return 'De que me hablas'



if __name__ == '__main__':
    app.run(debug=False, port=5000) #run app in debug mode on port 5000