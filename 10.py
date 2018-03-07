# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:26:25 2018

@author: jkuch_000
"""

import numpy as np
from sklearn import preprocessing
from sklearn import metrics

N = 10
ty=9*np.random.rand(N)+0
tx=1*np.random.randn(N)-2

data=np.vstack((tx,ty))
data=data.conj().transpose()


scale = preprocessing.MinMaxScaler((0,1))
data = scale.fit_transform(data)

odl_eukl=metrics.pairwise.pairwise_distances(data, metric='euclidean')
print('Macierz odległości euklidesowych między elementami przeskalowanego zbioru uczącego')
print (odl_eukl)

print('Macierz odległości Mahalanobisa między elementami przeskalowanego zbioru uczącego')
odl_mah=metrics.pairwise.pairwise_distances(data, metric='mahalanobis')
print (odl_mah)

print('Macierz odległości L1L1 między elementami przeskalowanego zbioru uczącego')
odl_min=metrics.pairwise.pairwise_distances(data, metric='minkowski')
print (odl_min)