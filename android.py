# -*- coding: utf-8 -*-
import androidhelper

import aemet
import time
import threading
import metarairport
import aemettiempo
import json



droid = androidhelper.Android()
metarinstance=metarairport.metar()
results=metarinstance.getMetar("LESO")
prediccion=json.loads(results.text)
metarpredicts =prediccion['data']
for predict in metarpredicts:
    resumen_meteorologico=metarinstance.parseMetar(predict)
    droid.ttsSpeak(resumen_meteorologico)
aemettiempoinstance=aemettiempo.amettiempo()
tiempo=aemettiempoinstance.getTiempo('20069',time.strftime("%d/%m/%Y"))
droid.ttsSpeak(tiempo)
   


message = droid.dialogGetInput('TTS', '¿Qué quieres decir?').result
droid.ttsSpeak(message)



