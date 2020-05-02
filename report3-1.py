#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

#図の大きさとフォントサイズを設定
plt.rcParams["font.size"] = 20
plt.rcParams['figure.figsize'] = 12,10 
 
 
def do_logistic_growth(a,r,s,n0,p0,t):
    nt= n0
    pt=p0
    datax=[]
    datay=[]
    dataz=[]
 
    datax.append(0)
    datay.append(nt)
    dataz.append(pt)
 
    for i in range(t):
        copynt=nt
        nt= nt+a*nt*(r-pt)
        pt=pt+a*pt*(copynt-s)
        datax.append(i+1)
        datay.append(nt)
        dataz.append(pt)
 
    return(datax, datay, dataz)

dataX, dataY, dataZ = do_logistic_growth(0.2,0.1,0.1,0.11,0.1,1000)

plt.plot(dataX, dataY,label = "Prey")
plt.plot(dataX, dataZ,label = "Predator")

plt.xlabel("time step")
plt.ylabel("population density")
plt.legend(loc = 'upper left')
plt.show()


# In[ ]:




