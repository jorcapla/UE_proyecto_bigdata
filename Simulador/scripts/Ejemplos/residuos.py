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

url = "http://iot-agent:7896/iot/d?i="

vect1 = ['ok', 'lidOpen', 'dropped', 'moved', 'vandalized', 'burning']
status1 = random.choice(vect1)
vect21 = ['organic', 'inorganic', 'glass', 'oil', 'plastic', 'paper', 'batteries', 'other']
storedWasteKind1 =random.choice(vect21)
batteryLevel1 = random.random()
fillingLevel1 = random.random()
temperature1 = random.uniform(0, 55)
devicename1 ="onda_wastecontainer_cont001"


endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5913"
payload1 = "st|"+str(status1)+"|tip|"+str(storedWasteKind1)+"|bat|"+str("{0:.2f}".format(batteryLevel1))+"|flev|"+str("{0:.2f}".format(fillingLevel1))+"|temp|"+str("{0:.2f}".format(temperature1))+"|date|"+str(ahora)

status2 = random.choice(vect1)
storedWasteKind2 =random.choice(vect21)
batteryLevel2 = random.random()
fillingLevel2 = random.random()
temperature2 = random.uniform(0, 55)
devicename2 ="onda_wastecontainer_cont002"

endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5913"
payload2 = "st|"+str(status2)+"|tip|"+str(storedWasteKind2)+"|bat|"+str("{0:.2f}".format(batteryLevel2))+"|flev|"+str("{0:.2f}".format(fillingLevel2))+"|temp|"+str("{0:.2f}".format(temperature2))+"|date|"+str(ahora)

status3 = random.choice(vect1)
storedWasteKind3 =random.choice(vect21)
batteryLevel3 = random.random()
fillingLevel3 = random.random()
temperature3 = random.uniform(0, 55)
devicename3 ="onda_wastecontainer_cont003"

endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5913"
payload3 = "st|"+str(status3)+"|tip|"+str(storedWasteKind3)+"|bat|"+str("{0:.2f}".format(batteryLevel3))+"|flev|"+str("{0:.2f}".format(fillingLevel3))+"|temp|"+str("{0:.2f}".format(temperature3))+"|date|"+str(ahora)

header = {"ContentType":"text/plain"} 
r1 = requests.post(url= endpoint1,headers=header, data=payload1)
time.sleep(2)
r2 = requests.post(url= endpoint2,headers=header, data=payload2)
time.sleep(2)
r3 = requests.post(url= endpoint3,headers=header, data=payload3)
time.sleep(2)

