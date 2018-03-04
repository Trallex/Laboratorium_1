# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:06:35 2018

@author: jkuch_000
"""

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

print("min x: " + str(numpy.amin(tab_x)))
print("max x: " + str(numpy.amax(tab_x)))
print("average x: " + str(numpy.average(tab_x)))
print("standard deviation x: " + str(numpy.std(tab_x)))

print("min y: " + str(numpy.amin(tab_y)))
print("max y: " + str(numpy.amax(tab_y)))
print("average y: " + str(numpy.average(tab_y)))
print("standard deviation y: " + str(numpy.std(tab_y)))


print("min z: " + str(numpy.amin(tab_z)))
print("max z: " + str(numpy.amax(tab_z)))
print("average z: " + str(numpy.average(tab_z)))
print("standard deviation z: " + str(numpy.std(tab_z)))

print("min w: " + str(numpy.amin(tab_w)))
print("max w: " + str(numpy.amax(tab_w)))
print("average w: " + str(numpy.average(tab_w)))
print("standard deviation w: " + str(numpy.std(tab_w)))
