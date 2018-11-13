# -*- coding: utf-8 -*-
import requests
import json
from metar import Metar
import locale
from pprint import pprint
import aeropuertos


class metar ():
    def __init__(self):
        key=""
        file = open('config.cfg', 'r') 
        for line in file: 
            if 'checkwxkey' in line:
                aux= line.split(":")
                key=aux[1]
            
        self.headers={ 'X-API-Key': key }

    def validAirport(self,airport):
        if airport in aeropuertos.aeropuertos:
            return True
        return False

    def getMetar(self,ICAO):
        response=requests.get('https://api.checkwx.com/metar/'+ICAO,headers=self.headers)
        return response
    
    def parseMetar(self,currentMetar):
        obs = Metar.Metar(currentMetar)
        self.metar=obs
        response=requests.get('https://api.checkwx.com/station/'+str(obs.station_id),headers=self.headers)
        respuestajson=json.loads(response.text)
        aeroportName=""
        for respuesta in respuestajson['data']:
            aeroportName=respuesta['name']

        visibilidad=str(obs.vis).replace('greater than','más de')
        print(visibilidad)
        text="Información meteorológica el día "+str(obs.time)+" desde el aeropuerto de "+str(aeroportName)
        text=text+" visibilidad de "+visibilidad+", velocidad del viento de "+str(obs.wind_speed).replace('knots','nudos')+" desde "+str(obs.wind_dir_from)
        text=text+" a "+str(obs.wind_dir_to)
        text=text+" , con una temperatura de "+str(obs.temp)+" y mínima de "+str(obs.dewpt)+' y una presión atmosférica de '+str(obs.press).replace('mb','milibares')
        newtext=text.replace('meters','metros').replace('degrees','grados')
        return newtext

