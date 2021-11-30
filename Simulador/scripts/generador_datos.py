#!/usr/bin/python
from subprocess import call
from time import sleep
import Products
from Products import ProductsSimulation 

i=0
while i<=100:
  ProductsSimulation.sendData()
  i+=1
 
