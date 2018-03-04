# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:21:30 2018

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

for i in iris_tab:
    t=0
    for j in i:
        if t==0:
            tab_x.append(float(j))
        if t==1:
            tab_y.append(float(j))
        t+=1
plt.plot(tab_x, tab_y, 'mo')
plt.show()