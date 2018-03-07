# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:40:30 2018

@author: jkuch_000
"""
import numpy as np
import matplotlib.pyplot as plt



def gr2(x):
    #2 -x+y
    return -x[0] + x[1]
 
def gr4(x):
    #4 x-y
    return x[0] - x[1]
def classify(x):
    if gr2(x) > gr4(x):
        return 2
    else:  
        return 4
N = 5
"""ty=9*np.random.rand(N)+0
tx=1*np.random.randn(N)-2"""
tx = np.random.rand(N,2)
ty = np.random.rand(N,2)-1
data=np.vstack((tx,ty))

kl2=[]
kl4=[]
for i in data:
    if classify(i) == 2:
        kl2.append(i)
    else:
        kl4.append(i)
plt.ylim(ymax = 1.5, ymin = -1.5)
plt.xlim(xmax = 1.5, xmin = -1.5)
plt.scatter(data[:,0],data[:,1])

y1=[gr2(data[i,:]) for i in range(2*N)]
y2=[gr4(data[i,:]) for i in range(2*N)]

y1=np.round(y1,2)
y2=np.round(y2,2)
labels=np.array([classify(data[i,:]) for i in range(2*N)])
c1 = (labels==1).nonzero()
c2 = (labels==2).nonzero()

plt.scatter(data[c1,0],data[c1,1],c='b')
plt.scatter(data[c2,0],data[c2,1],c='r')
plt.plot([-1.5, 1.5],[1.5, -1.5])
plt.show()
print(kl2)
print(kl4)