# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:19:14 2018

@author: jkuch_000
"""

file = open('iris.data')
iris_tab=[]

for line in file:
    row = line.split(',')
    iris_tab.append(row)

print("ilosc probek: " + str(len(iris_tab)))
print("ilosc atrybutow: " + str(len(iris_tab[1])))   