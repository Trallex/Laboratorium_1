# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
setosaX=[]
setosaY=[]
setosaZ=[]
setosaW=[]
versicolorX=[]
versicolorY=[]
versicolorZ=[]
versicolorW=[]
virginicaX=[]
virginicaY=[]
virginicaZ=[]
virginicaW=[]
t=0
for i in tab_type:
    if i == "Iris-virginica\n":
        virginicaX.append(tab_x[t])
        virginicaY.append(tab_y[t])
        virginicaZ.append(tab_z[t])
        virginicaW.append(tab_w[t])
    elif i == "Iris-versicolor\n":
        versicolorX.append(tab_x[t])
        versicolorY.append(tab_y[t])
        versicolorZ.append(tab_z[t])
        versicolorW.append(tab_w[t])
    elif i == "Iris-setosa\n":
        setosaX.append(tab_x[t])
        setosaY.append(tab_y[t])
        setosaZ.append(tab_z[t])
        setosaW.append(tab_w[t])
    t+=1

print("setosa average x: " + str(numpy.average(setosaX)))
print("setosa average y: " + str(numpy.average(setosaY)))
print("setosa average z: " + str(numpy.average(setosaZ)))
print("setosa average w: " + str(numpy.average(setosaW)))

print("versicolor average x: " + str(numpy.average(versicolorX)))
print("versicolor average y: " + str(numpy.average(versicolorY)))
print("versicolor average z: " + str(numpy.average(versicolorZ)))
print("versicolor average w: " + str(numpy.average(versicolorW)))