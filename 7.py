# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:21:26 2018

@author: jakub.kucharz
"""
from sklearn import preprocessing
import numpy
file = open('iris.data')
iris_tab=[]

for line in file:
    row = line.split(',')
    iris_tab.append(row)
iris_tab.pop(len(iris_tab)-1)

tab_x=[]
tab_y=[]
tab_z=[]
tab_w=[]
tab_type=[]

for i in iris_tab:
    t=0
    for j in i:
        if t==0:
            tab_x.append(float(j))
        if t==1:
            tab_y.append(float(j))
        if t==2:
            tab_z.append(float(j))
        if t==3:
            tab_w.append(float(j))
        if t==4:
            tab_type.append(j)
        t+=1
tab_x=preprocessing.scale(tab_x)
tab_y=preprocessing.scale(tab_y)
tab_z=preprocessing.scale(tab_z)
tab_w=preprocessing.scale(tab_w)

print("Normalized min x: " + str(numpy.amin(tab_x)))
print("Normalized max x: " + str(numpy.amax(tab_x)))
print("Normalized average x: " + str(numpy.average(tab_x)))
print("Normalized standard deviation x: " + str(numpy.std(tab_x)))

print("Normalized min y: " + str(numpy.amin(tab_y)))
print("Normalized max y: " + str(numpy.amax(tab_y)))
print("Normalized average y: " + str(numpy.average(tab_y)))
print("Normalized standard deviation y: " + str(numpy.std(tab_y)))


print("Normalized min z: " + str(numpy.amin(tab_z)))
print("Normalized max z: " + str(numpy.amax(tab_z)))
print("Normalized average z: " + str(numpy.average(tab_z)))
print("Normalized standard deviation z: " + str(numpy.std(tab_z)))

print("Normalized min w: " + str(numpy.amin(tab_w)))
print("Normalized max w: " + str(numpy.amax(tab_w)))
print("Normalized average w: " + str(numpy.average(tab_w)))
print("Normalized standard deviation w: " + str(numpy.std(tab_w)))