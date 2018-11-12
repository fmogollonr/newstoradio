#!/bin/bash

for i in {00001..90000}
do
if [[ `wget -S --spider "http://www.aemet.es/xml/municipios/localidad_"$i".xml"  2>&1 | grep 'HTTP/1.1 200 OK'` ]]; then echo $i; fi
done
