# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:15:05 2019

@author: Javi P
"""


import datetime
import time
import random
import requests

contador = 0

url = "http://iot-agent:7896/iot/d?i="

status = "ok"
powerState = "on"

while (contador < 60):
    
    ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
	
    powerConsumption1 = random.uniform(5, 300)
    luminousFlux1 = random.uniform(500, 3000)
    devicename1 ="onda_energia_ener001"

    endpoint1 = "http://iot-agent:7896/iot/d?i="+devicename1+"&k=4jggokgpepnvsb2uv4s40d5917"
    payload1 = "st|"+str(status)+"|poSt|"+str(powerState)+"|power|"+str(powerConsumption1)+"|lum|"+str(luminousFlux1)+"|date|"+str(ahora)
    
    powerConsumption2 = random.uniform(5, 300)
    luminousFlux2 = random.uniform(500, 3000)
    devicename2 ="onda_energia_ener002"

    endpoint2 = "http://iot-agent:7896/iot/d?i="+devicename2+"&k=4jggokgpepnvsb2uv4s40d5917"
    payload2 = "st|"+str(status)+"|poSt|"+str(powerState)+"|power|"+str(powerConsumption2)+"|lum|"+str(luminousFlux2)+"|date|"+str(ahora)

    powerConsumption3 = random.uniform(5, 300)
    luminousFlux3 = random.uniform(500, 3000)
    devicename3 ="onda_energia_ener003"

    endpoint3 = "http://iot-agent:7896/iot/d?i="+devicename3+"&k=4jggokgpepnvsb2uv4s40d5917"
    payload3 = "st|"+str(status)+"|poSt|"+str(powerState)+"|power|"+str(powerConsumption3)+"|lum|"+str(luminousFlux3)+"|date|"+str(ahora)

    header = {"ContentType":"text/plain"} 
    r1 = requests.post(url= endpoint1,headers=header, data=payload1)
    time.sleep(2)
    r2 = requests.post(url= endpoint2,headers=header, data=payload2)
    time.sleep(2)
    r3 = requests.post(url= endpoint3,headers=header, data=payload3)
    time.sleep(56)
    
    contador+=1 
