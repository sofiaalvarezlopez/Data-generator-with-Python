#!/usr/bin/env python
# coding: utf-8

# In[525]:


import pandas as pd
import random 
import time
import datetime
import csv


# In[526]:


idestadia = 76042


# In[527]:


planes = pd.read_csv("planes-individuales.csv")
idsplanes = planes['IDPLAN'].values;

habitaciones = pd.read_csv("habitaciones.csv")
numhabitaciones = habitaciones['NUMEROHABITACION'].values;

usuarios = pd.read_csv("usuarios-0.csv")
idsusuarios = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-1.csv")
idsusuarios1 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-2.csv")
idsusuarios2 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-3.csv")
idsusuarios3 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-4.csv")
idsusuarios4 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-5.csv")
idsusuarios5 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-6.csv")
idsusuarios6 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-7.csv")
idsusuarios7 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-8.csv")
idsusuarios8 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-9.csv")
idsusuarios9 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-10.csv")
idsusuarios10 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-11.csv")
idsusuarios11 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-12.csv")
idsusuarios12 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-13.csv")
idsusuarios13 = usuarios['NUMERODOCUMENTO'].values;

usuarios = pd.read_csv("usuarios-14.csv")
idsusuarios14 = usuarios['NUMERODOCUMENTO'].values;


# In[528]:


print(idsplanes)


# In[529]:


print(numhabitaciones)


# In[530]:


print(idsusuarios)


# In[531]:


idsusuariostodos = [*idsusuarios, *idsusuarios1, *idsusuarios2, *idsusuarios3, *idsusuarios4, *idsusuarios5, *idsusuarios6, *idsusuarios7, *idsusuarios8, *idsusuarios9, *idsusuarios10, *idsusuarios11, *idsusuarios12, *idsusuarios13, *idsusuarios14]    


# In[532]:


#Aqui ya tengo todos los ids de todos los usuarios
print (idsusuariostodos)


# In[533]:


#Esto me da las fechas en un año determinado
def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%d/%m/%Y', prop)


def fin(start):
    date_1 = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = date_1 + datetime.timedelta(days=random.randint(1, 15))
    return end_date.strftime("%d/%m/%Y")


# In[534]:


fechaIn = randomDate('31/12/2019', '31/12/2019', random.random())
print(fechaIn)
#fechaFin = randomDate(fechaIni, "31/12/2019", random.random())
fechaFin = fin(fechaIn)
print(fechaFin)


# In[535]:


numPersonas = random.randint(1,4)


# In[536]:


idPlan = random.randint(0,99)
numHab = random.randint(0, 299)
cont = 0


# In[537]:


checkInYPagado = random.randint(0,1)


# In[538]:


print (idsplanes[idPlan])
print (numhabitaciones[numHab])


# In[539]:


#row = [idestadia, fechaIni, fechaFini, numPersonas, idsplanes[idPlan], numhabitaciones[numHab], checkInYPagado, checkInYPagado, idsusuariostodos[cont], '']


# In[540]:


print(row)


# In[541]:


a = 0
listica = []
while(a < 14999):
    chechInYPagado = 1
    fechaIni = randomDate("1/1/2018", "31/12/2018", random.random())
    fechaFini = fin(fechaIni)
    row = [idestadia, fechaIni, fechaFini, random.randint(1,4), idsplanes[random.randint(0,99)], numhabitaciones[random.randint(0, 299)], chechInYPagado, chechInYPagado, idsusuariostodos[cont], '']
    cont += 1
    listica.append(row)
    idestadia += 1
    a+=1


# In[542]:


print(listica)


# In[543]:


with open('estadias-aleatorias-2018.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["IDESTADIA", "FECHALLEGADA", "FECHASALIDA", "NUMEROPERSONAS", "IDPLAN", "IDHABITACION", "CHECKIN", "PAGADO", "IDCLIENTE", "IDCONVENCION"])
    for row in listica:
        writer.writerow(row)
f.close()


# In[ ]:




