# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:32:38 2018

@author: jkuch_000
"""

import matplotlib.pyplot as plt

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
setosaZ=[]
versicolorX=[]
versicolorZ=[]
virginicaX=[]
virginicaZ=[]
t=0
for i in tab_type:
    if i == "Iris-virginica\n":
        virginicaX.append(tab_x[t])
        virginicaZ.append(tab_z[t])
    elif i == "Iris-versicolor\n":
        versicolorX.append(tab_x[t])
        versicolorZ.append(tab_z[t])
    elif i == "Iris-setosa\n":
        setosaX.append(tab_x[t])
        setosaZ.append(tab_z[t])
    t+=1
    
plt.plot(setosaX, setosaZ, 'mh', versicolorX, versicolorZ, 'ch', virginicaX, virginicaZ, 'rh')
plt.show() 