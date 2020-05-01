#!/usr/bin/env python
# coding: utf-8

# In[38]:


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
 
for i in range(6):
    r=i*0.60
    dataX, dataY= do_logistic_growth(100.0, r, 1.0, 20)
    plt.plot(dataX, dataY, label='r=' + str(round(i*0.60,1)))
plt.xlabel("time")
plt.ylabel("population size")
plt.legend(loc = 'upper left')
plt.show()


# In[ ]:




