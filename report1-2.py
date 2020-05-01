#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
 
 
dataX, dataY= do_logistic_growth(100.0, 1.5, 1.0, 20)
plt.plot(dataX, dataY)
 
plt.xlabel("time")
plt.ylabel("population size")
plt.show()


# In[ ]:




