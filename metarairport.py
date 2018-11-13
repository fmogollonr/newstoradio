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
        #self.gs = goslate.Goslate()

    def validAirport(self,airport):
        if airport in aeropuertos.aeropuertos:
            return True
        return False

    def getMetar(self,ICAO):
        response=requests.get('https://api.checkwx.com/metar/'+ICAO,headers=self.headers)
        return response
    
    def preparseMetar(self,metarResponse):
        obs = Metar.Metar(metarResponse)
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        self.metar=obs

        self.code = obs.code              # original METAR code
        self.type = 'METAR'                # METAR (routine) or SPECI (special)
        #self.correction = obs.correction             # COR (corrected - WMO spec)
        self.mod = "AUTO"                  # AUTO (automatic) or COR (corrected - US spec)
        self.station_id = obs.station_id             # 4-character ICAO station code
        self.time = obs.time                 # observation time [datetime]
        self.cycle = obs.cycle                  # observation cycle (0-23) [int]
        self.wind_dir = obs.wind_dir               # wind direction [direction]
        self.wind_speed = obs.wind_speed             # wind speed [speed]
        self.wind_gust = obs.wind_gust               # wind gust speed [speed]
        self.wind_dir_from = obs.wind_dir_from          # beginning of range for win dir [direction]
        self.wind_dir_to = obs.wind_dir_to            # end of range for wind dir [direction]
        self.vis = obs.vis                    # visibility [distance]
        self.vis_dir = obs.vis_dir                # visibility direction [direction]
        self.max_vis = obs.max_vis                # visibility [distance]
        self.max_vis_dir = obs.max_vis_dir            # visibility direction [direction]
        self.temp = obs.temp                   # temperature (C) [temperature]
        self.dewpt = obs.dewpt                  # dew point (C) [temperature]
        self.press = obs.press                  # barometric pressure [pressure]
        self.runway = obs.runway                   # runway visibility (list of tuples)
        self.weather = obs.weather                  # present weather (list of tuples)
        self.recent = obs.recent                   # recent weather (list of tuples)
        self.sky = obs.sky                      # sky conditions (list of tuples)
        self.windshear = obs.windshear               # runways w/ wind shear (list of strings)
        self.wind_speed_peak = obs.wind_speed_peak        # peak wind speed in last hour
        self.wind_dir_peak = obs.wind_dir_peak          # direction of peak wind speed in last hour
        self.peak_wind_time = obs.peak_wind_time         # time of peak wind observation [datetime]
        self.wind_shift_time = obs.wind_shift_time        # time of wind shift [datetime]
        self.max_temp_6hr = obs.max_temp_6hr           # max temp in last 6 hours
        self.min_temp_6hr = obs.min_temp_6hr           # min temp in last 6 hours
        self.max_temp_24hr = obs.max_temp_24hr          # max temp in last 24 hours
        self.min_temp_24hr = obs.min_temp_24hr          # min temp in last 24 hours
        self.press_sea_level = obs.press_sea_level        # sea-level pressure
        self.precip_1hr = obs.precip_1hr             # precipitation over the last hour
        self.precip_3hr = obs.precip_3hr             # precipitation over the last 3 hours
        self.precip_6hr = obs.precip_6hr             # precipitation over the last 6 hours
        self.precip_6hr = obs.precip_6hr            # precipitation over the last 24 hours
        #self.snowdepth = obs.snowdepth              # snow depth (distance)
        self._trend = False                # trend groups present (bool)
        self._trend_groups = obs._trend_groups            # trend forecast groups
        self._trend_groups = obs._trend_groups                 # remarks (list of strings)
        self._unparsed_groups = obs._unparsed_groups
        self._unparsed_remarks = obs._unparsed_remarks

        #print(obs.dewpt)

        pprint(vars(obs))

    def parseMetar(self,currentMetar):
        self.preparseMetar(currentMetar)
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

