#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt

#図の大きさとフォントサイズを設定
plt.rcParams["font.size"] = 20
plt.rcParams['figure.figsize'] = 12,10 
 
 
def do_logistic_growth(k, r, n0, t):
    nt= n0
    datax=[]
    datay=[]
 
    datax.append(0)
    datay.append(nt)
 
    for i in range(t):
        nt= nt+r*nt*(1.0-nt/k)
        datax.append(i+1)
        datay.append(nt)
 
    return(datax, datay)

bifX = []
bifY = []

for i in range(201):
    r=1.0 + i*0.01
    dataX, dataY= do_logistic_growth(100.0, r, 1.0, 300)
    for i in range(50):
        bifX.append(r)
        bifY.append(dataY[251 + i])
    plt.plot(bifX, bifY, '.')

plt.xlabel("r")
plt.ylabel("population size")
#plt.legend(loc = 'upper left')
plt.show()


# In[ ]:




