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

temp_1 = random.uniform(0, 45) 
tempSuelo_1 = random.uniform(0, 60)
rHume_1 = random.random()
humeSuelo_1 = random.random() 

temp_2 = random.uniform(0, 45) 
tempSuelo_2 = random.uniform(0, 60)
rHume_2 = random.random()
humeSuelo_2 = random.random() 

temp_3 = random.uniform(0, 45) 
tempSuelo_3 = random.uniform(0, 60)
rHume_3 = random.random()
humeSuelo_3 = random.random() 

devicename1 ="onda_incendios_inc001"  
devicename2 ="onda_incendios_inc002"
devicename3 ="onda_incendios_inc003"

url = "http://iot-agent:7896/iot/d?i="
endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5914"
payload1 = "temp|"+str("{0:.2f}".format(temp_1))+"|tempSuelo|"+str("{0:.2f}".format(tempSuelo_1))+"|rHume|"+str("{0:.2f}".format(rHume_1))+"|humeSuelo|"+str("{0:.2f}".format(humeSuelo_1))+"|date|"+str(ahora)  

endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5914"
payload2 = "temp|"+str("{0:.2f}".format(temp_2))+"|tempSuelo|"+str("{0:.2f}".format(tempSuelo_2))+"|rHume|"+str("{0:.2f}".format(rHume_2))+"|humeSuelo|"+str("{0:.2f}".format(humeSuelo_2))+"|date|"+str(ahora)

endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5914"
payload3 = "temp|"+str("{0:.2f}".format(temp_3))+"|tempSuelo|"+str("{0:.2f}".format(tempSuelo_3))+"|rHume|"+str("{0:.2f}".format(rHume_3))+"|humeSuelo|"+str("{0:.2f}".format(humeSuelo_3))+"|date|"+str(ahora) 

header = {"ContentType":"text/plain"} 


r1 = requests.post(url= endpoint1,headers=header, data=payload1)
time.sleep(2)
r2 = requests.post(url= endpoint2,headers=header, data=payload2)
time.sleep(2)
r3 = requests.post(url= endpoint3,headers=header, data=payload3)
time.sleep(2)
