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

while (contador < 60):
    
    ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    entradas_1 = random.randint(50, 200) 
    salidas_1 = random.randint(20, 100)
    
    entradas_2 = random.randint(50, 200) 
    salidas_2 = random.randint(20, 100) 
    
    entradas_3 = random.randint(50, 200) 
    salidas_3 = random.randint(20, 100)
    
    devicename1 ="onda_instalaciones_dep001"  
    devicename2 ="onda_instalaciones_dep002"
    devicename3 ="onda_instalaciones_dep003"
    
    endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5919"
    payload1 = "|in|"+str(entradas_1)+"|out|"+str(salidas_1)+"|date|"+str(ahora)  
    
    endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5919"
    payload2 = "|in|"+str(entradas_2)+"|out|"+str(salidas_2)+"|date|"+str(ahora)
    
    endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5919"
    payload3 = "|in|"+str(entradas_3)+"|out|"+str(salidas_3)+"|date|"+str(ahora)
    
    header = {"ContentType":"text/plain"} 
    

    r1 = requests.post(url= endpoint1,headers=header, data=payload1)
    r2 = requests.post(url= endpoint2,headers=header, data=payload2)
    r3 = requests.post(url= endpoint3,headers=header, data=payload3)
    
    time.sleep(30)
    
    contador+=1 
