#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

#図の大きさとフォントサイズを設定
plt.rcParams["font.size"] = 20
plt.rcParams['figure.figsize'] = 12,10 
 
 
def do_logistic_growth(t):
    #固定
    nat0=0.1
    nbt0=0.1
    p0=0.1
    s=0.1
    
    #捕食者に発見されて食べられる確率(da>db)
    da=0.9
    db=0.1
    
    #自己増加割合(ra>rb)
    ra=0.9
    rb=0.8
    
    a=0.1
    
    nat=nat0
    nbt=nbt0
    pt=p0
    datax=[]
    datay=[]
    dataz=[]
    dataf=[]
    datah=[]
    
 
    datax.append(0)
    dataf.append(nat)
    datah.append(nbt)
    datay.append(nat+nbt)
    dataz.append(pt)
 
    for i in range(t):
        x=nat+nbt
        q=da*nat+db*nbt
        
        copypt=pt
        pt=pt+a*pt*(q-s)
        
        nat= nat+a*nat*(ra-x-da*copypt)
        nbt= nbt+a*nbt*(rb-x-db*copypt)
        
        datax.append(i+1)
        datay.append(nat+nbt)
        dataz.append(pt)
        dataf.append(nat)
        datah.append(nbt)
 
    return(datax, datay, dataz,dataf,datah)

dataX, dataY, dataZ, dataF, dataH = do_logistic_growth(100000)

plt.plot(dataX, dataY,label = "preySum")
plt.plot(dataX, dataF,label = "prey1")
plt.plot(dataX, dataH,label = "prey2")
plt.plot(dataX, dataZ,label = "Predator")

plt.xlabel("time step")
plt.ylabel("population density")
plt.legend(loc = 'upper right')
plt.show()


# In[ ]:





# In[ ]:




