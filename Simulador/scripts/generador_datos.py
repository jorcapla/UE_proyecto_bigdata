#!/usr/bin/python
from subprocess import call
from time import sleep
from Products import ProductsSimulation 
import os

IOT_AGENT_URL = os.getenv('IOT_AGENT_URL', 'http://localhost:7896/iot/d')
IOT_AGENT_KEY = os.getenv('IOT_AGENT_KEY', '4jggokgpepnvsb2uv4s40d5911')

i=0
while 1==1:
  ProductsSimulation.sendData(IOT_AGENT_URL,IOT_AGENT_KEY)
  i+=1
 
