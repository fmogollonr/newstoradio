import requests


class metar:
    def __init__(self):
        key=""
        file = open('config.cfg', 'r') 
        for line in file: 
            if 'checkwxkey' in line:
                aux= line.split(":")
                key=aux[1]
            
        self.headers={ 'X-API-Key': key }


    def getMetar(self,ICAO):
        response=requests.get('https://api.checkwx.com/metar/'+ICAO,headers=self.headers)
        return response

