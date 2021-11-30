# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:15:05 2019

@author: fer.bori
"""


import datetime
import time
import random
#from random import randint
import requests
    
ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
	
averageHeadwayTime1 = random.random()
averageHeadwayTime2 = random.random()
averageHeadwayTime3 = random.random()
	
occupancy1 = random.random()
occupancy2 = random.random()
occupancy3 = random.random()

intensity1 = random.randrange(0, 10, 1)
intensity2 = random.randrange(0, 10, 1)
intensity3 = random.randrange(0, 10, 1)

averageVehicleSpeed1 = random.uniform(0, 75)
averageVehicleSpeed2 = random.uniform(0, 75)
averageVehicleSpeed3 = random.uniform(0, 75)

devicename1 ="onda_trafico_traf001"  
devicename2 ="onda_trafico_traf002"
devicename3 ="onda_trafico_traf003"


url= "http://iot-agent:7896/iot/d?i="
endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5916"
payload1 = "avhHwTime|"+str("{0:.2f}".format(averageHeadwayTime1))+"|ocu|"+str("{0:.2f}".format(occupancy1))+"|int|"+str("{0:.2f}".format(intensity1))+"|avVehSp|"+str("{0:.2f}".format(averageVehicleSpeed1))+"|dateObserved|"+str(ahora)
    
endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5916"
payload2 = "avhHwTime|"+str("{0:.2f}".format(averageHeadwayTime2))+"|ocu|"+str("{0:.2f}".format(occupancy2))+"|int|"+str("{0:.2f}".format(intensity2))+"|avVehSp|"+str("{0:.2f}".format(averageVehicleSpeed2))+"|dateObserved|"+str(ahora)

    
endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5916"
payload3 = "avhHwTime|"+str("{0:.2f}".format(averageHeadwayTime3))+"|ocu|"+str("{0:.2f}".format(occupancy3))+"|int|"+str("{0:.2f}".format(intensity3))+"|avVehSp|"+str("{0:.2f}".format(averageVehicleSpeed3))+"|dateObserved|"+str(ahora)


header = {"ContentType":"text/plain"} 


r1 = requests.post(url= endpoint1,headers=header, data=payload1)
time.sleep(2)
r2 = requests.post(url= endpoint2,headers=header, data=payload2)
time.sleep(2)
r3 = requests.post(url= endpoint3,headers=header, data=payload3)
time.sleep(2)


