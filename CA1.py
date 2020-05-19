#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import random as rnd

def calcEntropy(data):
    dic= {}
    for d in data:
        if d in dic:
            dic[d]= dic[d]+1
        else:
            dic[d]= 1
    probdist= np.array(list(dic.values()))/(float)(len(data))
    return(np.sum([-p * np.log2(p) for p in probdist]))


def calcJointEntropy(datax, datay):
    #dic = {(0,0),(0,1),(1,0), (1,1)}
    dic = {}
    for i in range(len(datax)):
        if (datax[i], datay[i]) in dic:
            dic[(datax[i], datay[i])] =  dic[(datax[i], datay[i])] + 1
        else:
            dic[(datax[i], datay[i])] = 1
    probdist= np.array(list(dic.values()))/(float)(len(datax))
    return(np.sum([-p * np.log2(p) for p in probdist]))


def calcMI(x,y):
    h_x = calcEntropy(x)
    h_y = calcEntropy(y)
    h_xy = calcJointEntropy(x,y)
    
    return(h_x+h_y-h_xy)

def calcCAMIList(dataxy):
    data = []
    
    for j in range(len(dataxy)):
        data_j= [dataXY[i][j] for i in range(len(dataXY))]
        data_x = []
        data_y = []
        for p in range(len(data_j)-1):
            data_x.append(data_j[p])
            data_y.append(data_j[p+1])
        data.append(calcMI(data_x,data_y))
    return(data)


def calcCAMI(data):
    list = calcCAMIList(data)
    sum=0
    for i in range(len(list)):
        sum += list[i]
    return(sum/(float)(len(data)))


def ca_1d(l, t, rule, cell_i):
    cell= cell_i
    data= [cell]
    for i in range(t):
        cell_next= [0 for i in range(l)]
        for j in range(l):
            neighboringstate= cell[(j-1+l)%l]*4+cell[j]*2+cell[(j+1)%l]
            cell_next[j]= rule[neighboringstate]
        cell= cell_next
        data.append(cell)
    return(data)
 
L=101
T=100
SEED=100
rnd.seed(SEED)
 
RNO= 90
RULE= [(RNO>>i)&1 for i in range(8)]
 
#[0, 0, ..., 0, 1, 0, ..., 0, 0]
cell_init= [0 for i in range(L)]
cell_init[L//2]= 1
 
#random
#cell_init= [rnd.randint(0, 1) for i in range(L)]
 
 
dataXY= ca_1d(L, T, RULE, cell_init)
MI = calcCAMI(dataXY)

fig= plt.figure(figsize=(10, 6))
ax= fig.add_subplot(1,2,1)
ax.pcolor(np.array(dataXY), vmin = 0, vmax = 1,  cmap= plt.cm.binary)
ax.set_xlim(0, L)
ax.set_ylim(T-1, 0)
ax.set_xlabel("cell number")
ax.set_ylabel("step")
ax.set_title("rule" + str(RNO) + ", MI=" + str(MI))

ax2=fig.add_subplot(1,2,2)
ax2.plot(calcCAMIList(dataXY))
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 0.18)
ax2.set_xlabel("cell number")
ax2.set_ylabel("MI")
plt.show()


# In[ ]:





# In[ ]:




