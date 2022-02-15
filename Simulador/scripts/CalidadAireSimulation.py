# -*- coding: utf-8 -*-
"""
Created on Tue Dic 1 22:15:05 2021

@author: Jorge Capel
"""


import datetime
import time
import random
import requests

class CalidadAireSimulation:

    percentage=0; 
    battery =0;
    temperature = 0;
    iotagenturl="";
    iotagentkey="";
    
    def __init__(self,iotagenturl,iotagentkey):
        self.iotagenturl = iotagenturl
        self.iotagentkey = iotagentkey
        

    
    def payload(self,devicename,date):
        #p|80|b|50|t|85|d|%Y-%m-%dT%H:%M:%SZ
        #NO2|80|SO2|50|CO|85|O3|80|H2S|50|DB|85|d|%Y-%m-%dT%H:%M:%SZ
        ahora = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.NO2 = random.uniform(1, 500)
        self.SO2 = random.uniform(1, 50)
        self.CO = random.uniform(1, 15)
        self.O3 = random.uniform(5, 100)
        self.H2S = random.uniform(1, 50)
        self.DB = random.uniform(1, 50)
        payloadStr = "n|"+devicename+"|NO2|"+str("{0:.2f}".format(self.NO2))+"|SO2|"+str("{0:.2f}".format(self.SO2))+"|CO|"+str("{0:.2f}".format(self.CO))
        payloadStr= payloadStr+ "|O3|"+str("{0:.2f}".format(self.O3))+"|H2S|"+str("{0:.2f}".format(self.H2S))+"|DB|"+str("{0:.2f}".format(self.DB))+"|d|"+str(ahora) 
        return payloadStr

    def sendData(self):
        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Calidad0"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            payload1 = self.payload(devicename,datetime.datetime.now())
            r1 = requests.post(url= endpoint1,headers=header, data=payload1)
            print("datos sensor {} {} ".format(devicename,payload1))
            time.sleep(0.5)
            i+=1
            
    def sendHistoricalData(self):
        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Contenedor"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            idays = 30
           
            while idays >=1:
                date=datetime.datetime.now() + datetime.timedelta(days=idays*-1)
                payload1 = self.payload(devicename,date)
                r1 = requests.post(url= endpoint1,headers=header, data=payload1)
                print("datos sensor {} {} ".format(devicename,payload1))
                idays-=1
                time.sleep(0.5)
            i+=1



