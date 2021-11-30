# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:15:05 2019

@author: Javi P
"""


import datetime
import time
import random
import requests

    
ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
#d1 = datetime.timedelta(seconds=-300) #Añadir Ultima hora de riego
#d2 = datetime.timedelta(seconds=+300) #Añadir proxima hora de riego

relativeHumidity1 = random.random()
soilTemperature1 = random.uniform(0, 30)
flowWater1 = random.uniform(20, 40)
devicename1 ="onda_riego_riego001"

url = "http://iot-agent:7896/iot/d?i="

endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5918"
payload1 = "sTemp|"+str("{0:.2f}".format(soilTemperature1))+"|rHum|"+str("{0:.2f}".format(relativeHumidity1))+"|fWat|"+str("{0:.2f}".format(flowWater1))+"|date|"+str(ahora)

relativeHumidity2 = random.random()
soilTemperature2 = random.uniform(0, 30)
flowWater2 = random.uniform(20, 40)
devicename2 ="onda_riego_riego002"

endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5918"
payload2 = "sTemp|"+str("{0:.2f}".format(soilTemperature2))+"|rHum|"+str("{0:.2f}".format(relativeHumidity2))+"|fWat|"+str("{0:.2f}".format(flowWater2))+"|date|"+str(ahora)

relativeHumidity3 = random.random()
soilTemperature3 = random.uniform(0, 30)
flowWater3 = random.uniform(20, 40)
devicename3 ="onda_riego_riego003"

endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5918"
payload3 = "sTemp|"+str("{0:.2f}".format(soilTemperature3))+"|rHum|"+str("{0:.2f}".format(relativeHumidity3))+"|fWat|"+str("{0:.2f}".format(flowWater3))+"|date|"+str(ahora)

header = {"ContentType":"text/plain"} 
r1 = requests.post(url= endpoint1,headers=header, data=payload1)
time.sleep(2)
r2 = requests.post(url= endpoint2,headers=header, data=payload2)
time.sleep(2)
r3 = requests.post(url= endpoint3,headers=header, data=payload3)
time.sleep(2)

