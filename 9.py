# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:53:52 2018
Podać macierz odległości euklidesowych, mahalanobisa oraz Minkowskiego L1L1 dla wszystkich par elementów tego zbioru
@author: jakub.kucharz
"""
import numpy as np
from sklearn import metrics
N = 10
#próba losowa z rozkładu jednostajnego na przedziale [0,10]
ty=9*np.random.rand(N)+0
#próba losowa z rozkładu N(-2,1)
tx=1*np.random.randn(N)-2

data=np.vstack((tx,ty))
data=data.conj().transpose()

odl_eukl=metrics.pairwise.pairwise_distances(data, metric='euclidean')
print('Macierz odległości euklidesowych między elementami zbioru uczącego')
print (odl_eukl)

print('Macierz odległości Mahalanobisa między elementami zbioru uczącego')
odl_mah=metrics.pairwise.pairwise_distances(data, metric='mahalanobis')
print (odl_mah)

print('Macierz odległości L1L1 między elementami zbioru uczącego')
odl_min=metrics.pairwise.pairwise_distances(data, metric='minkowski')
print (odl_min)
