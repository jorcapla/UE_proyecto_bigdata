# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:15:05 2019

@author: fer.bori
"""


import datetime
import time
from random import randint
import requests

ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

plazasOcupadas1 = randint(60, 400) 
plazasOcupadas2 = randint(60, 400) 
plazasOcupadas3 = randint(60, 400) 

devicename1 ="onda_parking_park001"  
devicename2 ="onda_parking_park002"
devicename3 ="onda_parking_park003"

url = "http://iot-agent:7896/iot/d?i="
endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5912"
payload1 = "a|"+str(plazasOcupadas1)+"|date|"+str(ahora)
    
endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5912"
payload2 = "a|"+str(plazasOcupadas2)+"|date|"+str(ahora)
    
endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5912"
payload3 = "a|"+str(plazasOcupadas3)+"|date|"+str(ahora)
    


header = {"ContentType":"text/plain"} 


r1 = requests.post(url= endpoint1,headers=header, data=payload1)
time.sleep(2)
r2 = requests.post(url= endpoint2,headers=header, data=payload2)
time.sleep(2)
r3 = requests.post(url= endpoint3,headers=header, data=payload3)
time.sleep(2)


