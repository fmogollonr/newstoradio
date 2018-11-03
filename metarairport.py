# -*- coding: utf-8 -*-
import requests
import json
import goslate
from metar import Metar


class metar:
    def __init__(self):
        key=""
        file = open('config.cfg', 'r') 
        for line in file: 
            if 'checkwxkey' in line:
                aux= line.split(":")
                key=aux[1]
            
        self.headers={ 'X-API-Key': key }
        #self.gs = goslate.Goslate()


    def getMetar(self,ICAO):
        response=requests.get('https://api.checkwx.com/metar/'+ICAO,headers=self.headers)
        return response

    def parseMetar(self,currentMetar):
        print currentMetar
        obs = Metar.Metar(currentMetar)
        response=requests.get('https://api.checkwx.com/station/'+str(obs.station_id),headers=self.headers)
        respuestajson=json.loads(response.text)
        aeroportName=""
        for respuesta in respuestajson['data']:
            aeroportName=respuesta['name']
        text="Meteorological information at "+str(obs.time)+" from "+str(aeroportName)+ " airport"
        text=text+" visibility "+str(obs.vis)+" wind speed "+str(obs.wind_speed)+" from "+str(obs.wind_dir_from)
        text=text+" to "+str(obs.wind_dir_to)
        text=text+" , temperature "+str(obs.temp) 
        #newtext=self.gs.translate(text,"es")
        return text

