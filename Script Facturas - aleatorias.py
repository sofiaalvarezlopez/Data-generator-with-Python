#!/usr/bin/env python
# coding: utf-8

# In[251]:


import numpy as np
import pandas as pd
import random 
import time
import datetime
import csv
import scipy.stats as stats


# In[252]:


numfactura = 370591


# In[253]:


estadias2017 = pd.read_csv("estadias-aleatorias-2017.csv")
fechaL2017 = estadias2017['FECHALLEGADA'].values
fechaS2017 = estadias2017['FECHASALIDA'].values
pagada2017 = estadias2017['PAGADO'].values
idEstadia2017 = estadias2017['IDESTADIA'].values

estadias2018 = pd.read_csv("estadias-aleatorias-2018.csv")
fechaL2018 = estadias2018['FECHALLEGADA'].values
fechaS2018 = estadias2018['FECHASALIDA'].values
pagada2018 = estadias2018['PAGADO'].values
idEstadia2018 = estadias2018['IDESTADIA'].values

estadias2019 = pd.read_csv("estadias-aleatorias-2019.csv")
fechaL2019 = estadias2019['FECHALLEGADA'].values
fechaS2019 = estadias2019['FECHASALIDA'].values
pagada2019 = estadias2019['PAGADO'].values
idEstadia2019 = estadias2019['IDESTADIA'].values

estadias2020 = pd.read_csv("estadias-aleatorias-2020.csv")
fechaL2020 = estadias2020['FECHALLEGADA'].values
fechaS2020 = estadias2020['FECHASALIDA'].values
pagada2020 = estadias2020['PAGADO'].values
idEstadia2020 = estadias2020['IDESTADIA'].values

estadias2021 = pd.read_csv("estadias-aleatorias-2021.csv")
fechaL2021 = estadias2021['FECHALLEGADA'].values
fechaS2021 = estadias2021['FECHASALIDA'].values
pagada2021 = estadias2021['PAGADO'].values
idEstadia2021 = estadias2021['IDESTADIA'].values

estadias2022 = pd.read_csv("estadias-aleatorias-2022.csv")
fechaL2022 = estadias2022['FECHALLEGADA'].values
fechaS2022 = estadias2022['FECHASALIDA'].values
pagada2022 = estadias2022['PAGADO'].values
idEstadia2022 = estadias2022['IDESTADIA'].values


estadias2023 = pd.read_csv("estadias-aleatorias-2023.csv")
fechaL2023 = estadias2023['FECHALLEGADA'].values
fechaS2023 = estadias2023['FECHASALIDA'].values
pagada2023 = estadias2023['PAGADO'].values
idEstadia2023 = estadias2023['IDESTADIA'].values


# In[254]:


def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%d/%m/%Y', prop)


# In[255]:


idEstadias = [*idEstadia2017, *idEstadia2018, *idEstadia2019, *idEstadia2020, *idEstadia2021, *idEstadia2022, *idEstadia2023]


# In[256]:


fechasLlegada = [*fechaL2017, *fechaL2018, *fechaL2019, *fechaL2020, *fechaL2021, *fechaL2022, *fechaL2023]


# In[257]:


fechasSalida = [*fechaS2017, *fechaS2018, *fechaS2019, *fechaS2020, *fechaS2021, *fechaS2022, *fechaS2023]


# In[258]:


cont = 0
listaFechasLlegadaAleatorias = []
while(cont < len(fechasLlegada)):
    fecha = randomDate(fechasLlegada[cont], fechasSalida[cont], random.random())
    listaFechasLlegadaAleatorias.append(fecha)
    cont += 1


# In[259]:


conti = 0
listaFechasLlegadaAleatorias1 = []
while(conti < len(fechasLlegada)):
    fecha1 = randomDate(fechasLlegada[conti], fechasSalida[conti], random.random())
    listaFechasLlegadaAleatorias1.append(fecha1)
    conti += 1


# In[260]:


print(len(listaFechasLlegadaAleatorias))
print(len(listaFechasLlegadaAleatorias1))


# In[261]:


pagadas = [*pagada2017, *pagada2018, *pagada2019, *pagada2020, *pagada2021, *pagada2022, *pagada2023]


# In[262]:


"""Aquí ya tengo todas las estadias, con sus fechas de salida, llegada y pago"""


# In[263]:


print (len(idEstadias))
print (len(fechasLlegada))
print (len(fechasSalida))
print (len(pagadas))


# In[264]:


"""Aquí voy a sacar un precio para el consumo de cada estadia"""
def precio(): 
    return random.randint(1000, 1000000)


# In[265]:


"""Estos son los servicios del hotel que puedo facturar"""
servs = [4, 5, 6, 17, 8, 18, 20, 22, 14, 13, 11, 12, 15]
prodsNormales = [2, 3, 4, 5, 6, 7, 8, 23]
prodsSpa = [14, 15, 16]
numDoEmpleado = [1010101589, 1010101590, 1010101591, 1010101592]


# In[266]:


"""Usando una distribución binomial, saco un idServicio"""
def idServicio():
    a = random.randint(0, 12)        
    return servs[a]


# In[267]:


"""Si el servicio es una spa, entonces tengo que coger un producto de los servicios"""
def idProducto():
    if idServicio() == 8:
        a = random.randint(0,2)
        return prodsSpa[a]
    else:
        b = random.randint(0,7)
        return prodsNormales[b]    
idProducto()


# In[268]:


def numDocEmpleado():
    a = random.randint(0,3)
    return numDoEmpleado[a]
numDocEmpleado()


# In[269]:


#row = [idestadia, fechaIni, fechaFini, numPersonas, idsplanes[idPlan], numhabitaciones[numHab], checkInYPagado, checkInYPagado, idsusuariostodos[cont], '']


# In[270]:


print(row)


# In[271]:


a = 0
pos = 0
listica = []
while(a < len(idEstadias)):
    row = [numfactura, listaFechasLlegadaAleatorias[pos], pagadas[pos], precio(), '', idServicio(), idEstadias[pos], numDocEmpleado(), idProducto(), '', '']
    numfactura += 1
    listica.append(row)
    row1 = [numfactura, listaFechasLlegadaAleatorias1[pos], pagadas[pos], precio(), '', idS, idEstadias[pos], numD, idP, '', '']
    numfactura += 1
    listica.append(row1)
    pos += 1
    a+=1


# In[272]:


print(len(listica))
print(numfactura - 370590)


# In[273]:


with open('facturas-aleatorias2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["NUMFACTURA", "FECHA", "FUEPAGADA", "PRECIO", "IDDOTACION", "IDSERVICIO", "IDESTADIA", "NUMDOCEMPLEADO", "IDPRODUCTO", "IDCONVENCION", "IDDOTACIONSALON"])
    for row in listica:
        writer.writerow(row)
f.close()


# In[ ]:




