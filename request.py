# -*- coding: utf-8 -*-
import requests
import Aemet
import time
import threading

def getWeather():

    threading.Timer(10, getWeather).start()
    tiempo = Aemet.Localidad('28079', time.strftime("%d/%m/%Y"))
    tiempo_texto="El tiempo para "+tiempo.get_localidad()+": temperatura maxima: "+tiempo.get_temperatura_maxima()
    r = requests.get("http://localhost:5000/speak?text="+tiempo_texto)

getWeather()