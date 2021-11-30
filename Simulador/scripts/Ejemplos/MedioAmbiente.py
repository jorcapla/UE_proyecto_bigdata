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

NO2_1 = random.uniform(5, 100)
SO2_1 = random.uniform(1, 50)
O3_1 = random.uniform(5, 240)
H2S_1 = random.uniform(0, 50)
CO_1 = random.uniform(0, 200)
Humi_1 = random.random()
temp_1 = random.uniform(0, 35) 
decib_1 = random.randint(0, 120) 

NO2_2 = random.uniform(5, 100)
SO2_2 = random.uniform(1, 50)
O3_2 = random.uniform(5, 240)
H2S_2 = random.uniform(0, 50)
CO_2 = random.uniform(0, 200)
Humi_2 = random.random()
temp_2 = random.uniform(0, 35) 
decib_2 = random.randint(0, 120) 

NO2_3 = random.uniform(5, 100)
SO2_3 = random.uniform(1, 50)
O3_3 = random.uniform(5, 240)
H2S_3 = random.uniform(0, 50)
CO_3 = random.uniform(0, 200)
Humi_3 = random.random()
temp_3 = random.uniform(0, 35) 
decib_3 = random.randint(0, 120) 

NO2_4 = random.uniform(5, 100)
SO2_4 = random.uniform(1, 50)
O3_4 = random.uniform(5, 240)
H2S_4 = random.uniform(0, 50)
CO_4 = random.uniform(0, 200)
Humi_4 = random.random()
temp_4 = random.uniform(0, 35) 
decib_4 = random.randint(0, 120)

devicename1 ="onda_arq_001"  
devicename2 ="onda_arq_002"
devicename3 ="onda_arq_003"
devicename4 ="onda_arq_004"


url = "http://iot-agent:7896/iot/d?i="

endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5911"
payload1 = "NO2|"+str("{0:.2f}".format(NO2_1))+"|SO2|"+str("{0:.2f}".format(SO2_1))+"|O3|"+str("{0:.2f}".format(O3_1))+"|H2S|"+str("{0:.2f}".format(H2S_1))+"|CO|"+str("{0:.2f}".format(CO_1)) +"|hum|"+str("{0:.2f}".format(Humi_1))+"|t|"+str("{0:.2f}".format(temp_1))+"|decib|"+str("{0:.2f}".format(decib_1))+"|date|"+str(ahora)
    
endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5911"
payload2 = "NO2|"+str("{0:.2f}".format(NO2_2))+"|SO2|"+str("{0:.2f}".format(SO2_2))+"|O3|"+str("{0:.2f}".format(O3_2))+"|H2S|"+str("{0:.2f}".format(H2S_2))+"|CO|"+str("{0:.2f}".format(CO_2)) +"|hum|"+str("{0:.2f}".format(Humi_2))+"|t|"+str("{0:.2f}".format(temp_2))+"|decib|"+str("{0:.2f}".format(decib_2))+"|date|"+str(ahora)

endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5911"
payload3 = "NO2|"+str("{0:.2f}".format(NO2_3))+"|SO2|"+str("{0:.2f}".format(SO2_3))+"|O3|"+str("{0:.2f}".format(O3_3))+"|H2S|"+str("{0:.2f}".format(H2S_3))+"|CO|"+str("{0:.2f}".format(CO_3)) +"|hum|"+str("{0:.2f}".format(Humi_3))+"|t|"+str("{0:.2f}".format(temp_3))+"|decib|"+str("{0:.2f}".format(decib_3))+"|date|"+str(ahora)

endpoint4 = url+devicename4+"&k=4jggokgpepnvsb2uv4s40d5911"
payload4 = "NO2|"+str("{0:.2f}".format(NO2_4))+"|SO2|"+str("{0:.2f}".format(SO2_4))+"|O3|"+str("{0:.2f}".format(O3_4))+"|H2S|"+str("{0:.2f}".format(H2S_4))+"|CO|"+str("{0:.2f}".format(CO_4)) +"|hum|"+str("{0:.2f}".format(Humi_4))+"|t|"+str("{0:.2f}".format(temp_4))+"|decib|"+str("{0:.2f}".format(decib_4))+"|date|"+str(ahora)

header = {"ContentType":"text/plain"} 


r1 = requests.post(url= endpoint1,headers=header, data=payload1)
time.sleep(2)
r2 = requests.post(url= endpoint2,headers=header, data=payload2)
time.sleep(2)
r3 = requests.post(url= endpoint3,headers=header, data=payload3)
time.sleep(2)
r4 = requests.post(url= endpoint4,headers=header, data=payload4)
time.sleep(2)


