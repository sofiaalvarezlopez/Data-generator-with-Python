#!/usr/bin/env python
# coding: utf-8

# In[231]:


import numpy as np
import pandas as pd
import random 
import time
import datetime
import csv
import scipy.stats as stats


# In[232]:


idhorario = 92630


# In[233]:


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


# In[234]:


def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%d/%m/%Y', prop)


def fin(start):
    date_1 = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = date_1 + datetime.timedelta(days=random.randint(0, 1))
    return end_date.strftime("%d/%m/%Y")



# In[235]:


idEstadias = [*idEstadia2017, *idEstadia2018, *idEstadia2019, *idEstadia2020, *idEstadia2021, *idEstadia2022, *idEstadia2023]


# In[236]:


fechasLlegada = [*fechaL2017, *fechaL2018, *fechaL2019, *fechaL2020, *fechaL2021, *fechaL2022, *fechaL2023]


# In[237]:


fechasSalida = [*fechaS2017, *fechaS2018, *fechaS2019, *fechaS2020, *fechaS2021, *fechaS2022, *fechaS2023]


# In[238]:


cont = 0
listaFechasInicio = []
while(cont < len(fechasLlegada)):
    fecha = randomDate(fechasLlegada[cont], fechasSalida[cont], random.random())
    listaFechasInicio.append(fecha)
    cont += 1
print(listaFechasInicio)


# In[239]:


conti = 0
listaFechasFin = []
while(conti < len(listaFechasInicio)):
    fecha = fin(listaFechasInicio[conti])
    listaFechasFin.append(fecha)
    conti += 1
print(listaFechasFin)


# In[240]:


print(len(listaFechasInicio))
print(len(listaFechasFin))


# In[241]:


pagadas = [*pagada2017, *pagada2018, *pagada2019, *pagada2020, *pagada2021, *pagada2022, *pagada2023]


# In[242]:


"""Aquí ya tengo todas las estadias, con sus fechas de salida, llegada y pago"""


# In[243]:


print (len(idEstadias))
print (len(fechasLlegada))
print (len(fechasSalida))
print (len(pagadas))


# In[244]:


"""Aquí voy a sacar una hora inicio para cada horario """
def horaInicio(): 
    return random.randint(0, 23)
horaInicio()


# In[245]:


"""Aquí voy a sacar una hora fin para cada horario """
def horaFin(): 
    return random.randint(horaInicio(), 24)
horaFin()


# In[246]:


"""Estos son los servicios del hotel que puedo facturar"""
servs = [4, 5, 17, 8, 18, 20, 22, 14, 13, 11, 12, 15]
prodsNormales = [2, 3, 4, 5, 6, 7, 8, 23]
prodsSpa = [14, 15, 16]
numDoEmpleado = [1010101589, 1010101590, 1010101591, 1010101592]


# In[247]:


"""Usando una distribución binomial, saco un idServicio"""
def idServicio():
    return servs[random.randint(0, 11)]
idServicio()


# In[248]:


#row = [idestadia, fechaIni, fechaFini, numPersonas, idsplanes[idPlan], numhabitaciones[numHab], checkInYPagado, checkInYPagado, idsusuariostodos[cont], '']


# In[249]:


print(row)


# In[250]:


a = 0
pos = 0
listica = []
while(a < len(listaFechasInicio)):
    s = idServicio()
    row = [idhorario, '', s, listaFechasInicio[pos], '', horaInicio(), horaFin(), listaFechasFin[pos]]
    idhorario += 1
    listica.append(row)
    pos += 1
    a+=1


# In[251]:


print(len(listica))
print(idhorario - 92630)


# In[252]:


with open('horarios-2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["IDHORARIO", "DURACION", "IDSERVICIO", "FECHAINICIO", "DIA", "HORAINICIO", "HORAFIN", "FECHAFIN"])
    for row in listica:
        writer.writerow(row)
f.close()

