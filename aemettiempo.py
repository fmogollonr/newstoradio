# -*- coding: utf-8 -*-
import aemet
import time


class amettiempo ():
    def __init__(self):
        self.weather=aemet



    def getTiempo (self,localidad,time):
        tiempo = self.weather.Localidad(localidad, time)
        tmax=tiempo.get_temperatura_maxima()
        tmin=tiempo.get_temperatura_minima()
        city=str(tiempo.get_localidad().decode('utf-8'))
        prediccion="La predicción del tiempo para "+city
        precips=tiempo.get_precipitacion()

        for precip in precips:
            if '00-06' in precip and precip[1]:
                prediccion=prediccion+" probabilidad de precipitaciones de 0 a 6 horas de un "+precip[1]+ " por ciento"
            elif '12-18' in precip and precip[1]:
                prediccion=prediccion+" probabilidad de precipitaciones de 12 a 18 horas de un "+precip[1]+ " por ciento"
            elif '06-12' in precip and precip[1]:
                prediccion=prediccion+" probabilidad de precipitaciones de 6 a 12 horas de un "+precip[1]+ " por ciento"
            elif '18-24' in precip and precip[1]:
                prediccion=prediccion+" probabilidad de precipitaciones de 18 a 24 horas de un "+precip[1]+ " por ciento"

        cotas=tiempo.get_cota_nieve()
        for cota in cotas:
            if '00-24' in cota and cota[1]:
                prediccion=prediccion+" ,cota de nive de "+cota[1]+" metros"
        cielos=tiempo.get_estado_cielo()
        for cielo in cielos:
            if '00-06' in cielo and cielo[1]:
                prediccion=prediccion+" con cielo "+cielo[1]+" de 0 a 6 horas"
            elif '12-18' in cielo and cielo[1]:
                prediccion=prediccion+" con cielo "+cielo[1]+" de 12 a 18 horas"
            elif '06-12' in cielo and cielo[1]:
                prediccion=prediccion+" con cielo "+cielo[1]+" de 6 a 12 horas"
            elif '18-24' in cielo and cielo[1]:
                prediccion=prediccion+" con cielo "+cielo[1]+" de 18 a 24 horas"
        vientos=tiempo.get_viento()
        for viento in vientos:
            if '00-06' in viento and viento[1]:
                prediccion=prediccion+" con viento de "+viento[2]+" kilómetros por hora de "+viento[1].replace('S','sur').replace('N','norte').replace('O','oeste').replace('E','este').replace('NO','noroeste').replace('NE','noreste').replace('SO','suroeste').replace('SE','sureste')+" de 0 a 6 horas"
            elif '06-12' in viento and viento[1]:
                prediccion=prediccion+" con viento de "+viento[2]+" kilómetros por hora de "+viento[1].replace('S','sur').replace('N','norte').replace('O','oeste').replace('E','este').replace('NO','noroeste').replace('NE','noreste').replace('SO','suroeste').replace('SE','sureste')+" de 6 a 12 horas"
            elif '12-18' in viento and viento[1]:
                prediccion=prediccion+" con viento de "+viento[2]+" kilómetros por hora de "+viento[1].replace('S','sur').replace('N','norte').replace('O','oeste').replace('E','este').replace('NO','noroeste').replace('NE','noreste').replace('SO','suroeste').replace('SE','sureste')+" de 12 a 18 horas"
            elif '18-24' in viento and viento[1]:
                prediccion=prediccion+" con viento de "+viento[2]+" kilómetros por hora de "+viento[1].replace('S','sur').replace('N','norte').replace('O','oeste').replace('E','este').replace('NO','noroeste').replace('NE','noreste').replace('SO','suroeste').replace('SE','sureste')+" de 18 a 24 horas"
        rachas=tiempo.get_racha()
        for racha in rachas:
            if '00-06' in racha and racha[1]:
                prediccion=prediccion+" con una racha máxima "+racha[1]+" kilómetros por hora de 0 a 6 horas"
            elif '12-18' in racha and racha[1]:
                prediccion=prediccion+" con una racha máxima  "+racha[1]+" kilómetros por hora de 12 a 18 horas"
            elif '06-12' in racha and racha[1]:
                prediccion=prediccion+" con una racha máxima  "+racha[1]+" kilómetros por hora de 6 a 12 horas"
            elif '18-24' in racha and racha[1]:
                prediccion=prediccion+" con una racha máxima  "+racha[1]+" kilómetros por hora de 18 a 24 horas"
        temperaturas=tiempo.get_temperatura_horas()
        for temperatura in temperaturas:
            if '06' in temperatura and temperatura[1]:
                prediccion=prediccion+" con una temperatura de "+temperatura[1]+" grados a las 6 de la mañana"
            elif '12' in temperatura and temperatura[1]:
                prediccion=prediccion+" con una temperatura de  "+temperatura[1]+" grados a las 12 de la mañana"
            elif '18' in temperatura and temperatura[1]:
                prediccion=prediccion+" con una temperatura de  "+temperatura[1]+" grados a las 6 de la tarde"
            elif '24' in temperatura and temperatura[1]:
                prediccion=prediccion+" con una temperatura de  "+temperatura[1]+" grados a las 12 de la noche"
        
        sens_term_max=str(tiempo.get_sensacion_termica_maxima())
        sens_term_min=str(tiempo.get_sensacion_termica_minima())
        prediccion=prediccion+" la sensación térmica será entre "+sens_term_min+" y "+sens_term_max+" grados"

        

        hum_min=str(tiempo.get_humedad_minima())        
        hum_max=str(tiempo.get_humedad_maxima())
        prediccion=prediccion+" la humedad relativa oscilará entre el "+hum_min+" y el "+hum_max+" por ciento"
        
        uv_max=str(tiempo.get_uv_max())
        prediccion=prediccion+" el índice ultravioleta máximo es de "+uv_max
        return prediccion
        
        prediccion=prediccion+" temperatura máxima "+tmax+" y temperatura mínima "+tmin
        prediccion=prediccion+" con una sensación térmica de "+sens_term

        return prediccion