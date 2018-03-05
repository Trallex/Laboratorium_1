# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:35:10 2018

@author: jakub.kucharz
"""
import matplotlib.pyplot as plt
import numpy as np
N = 10
#próba losowa z rozkładu jednostajnego na przedziale [0,10]
ty=9*np.random.rand(N)+0
#próba losowa z rozkładu N(-2,1)
tx=1*np.random.randn(N)-2

plt.plot(tx, ty, 'rh')
plt.show()
#