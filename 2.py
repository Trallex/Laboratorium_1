# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:20:05 2018

@author: jkuch_000
"""
import math
file = open('iris.data')
iris_tab=[]

for line in file:
    row = line.split(',')
    iris_tab.append(row)

x1 = float(iris_tab[9][0])
y1 = float(iris_tab[9][1])
z1 = float(iris_tab[9][2])
k1 = float(iris_tab[9][3])

x2 = float(iris_tab[74][0])
y2 = float(iris_tab[74][1])
z2 = float(iris_tab[74][2])
k2 = float(iris_tab[74][3])

print("Wartosci probki 10:",iris_tab[9])
print("Wartosci probki 75:",iris_tab[74])
EuklDist = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2) + math.pow((z1-z2),2) + math.pow((k1-k2),2))
print("Odleglosc euklidesowa: ", EuklDist)