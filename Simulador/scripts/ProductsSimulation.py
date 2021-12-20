# -*- coding: utf-8 -*-
"""
Created on Tue Dic 1 22:15:05 2021

@author: Jorge Capel
"""


import datetime
import time
import random
import requests

class ProductsSimulation:
    def sendData(iotagenturl,iotagentkey):

        
        devicename1 ="Product010"  
        devicename2 ="Product011"



        url = iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911
        endpoint1 = url+devicename1+"&k="+iotagentkey
        endpoint2 = url+devicename2+"&k="+iotagentkey
        header = {"ContentType":"text/plain"} 


        ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        price_1 = random.uniform(5, 100)
        size_1 = random.uniform(1, 50)
        payload1 = "p|"+str("{0:.2f}".format(price_1))
        r1 = requests.post(url= endpoint1,headers=header, data=payload1)
        print("datos sensor {} {} ".format(devicename1,payload1))
        time.sleep(1)
            
        price_2 = random.uniform(5, 100)
        size_2 = random.uniform(1, 50)
        payload2 = "p|"+str("{0:.2f}".format(price_2))
        r2 = requests.post(url= endpoint2,headers=header, data=payload2)
        print("datos sensor {} {}".format(devicename2,payload2))
        time.sleep(1)




