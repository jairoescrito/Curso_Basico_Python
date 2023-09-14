#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:18:10 2023

@author: jairoescrito
"""

# Métodos de datframes

import pandas as pd

Codigo = ["FL-01","FL-02","FL-03","FL-04","FL-05","FL-06","FL-07","FL-09","FL-10","FL-11","FL-12","FL-13","FL-14"]
Ciudad_FL = ["Jacksonville","Miami","Tampa","San Petersburgo","Orlando","Hialeah","Tallahassee","Fort Lauderdale","Port Saint Lucie","Pembroke Pines","Cabo Coral","Hollywood","Gainesville"]
Poblacion = [903072,481084,335709,244769,238300,224669,181376,165521,164603,154750,154305,140768,124354]
Densidad = [1100.01,11135.9,2960.2,3964.4,2327.3,10474.2,1809.3,4761.1,1444.5,4671.1,1460.2,5143.8,2028.5]
Data = {"Codigo" : Codigo,"Ciudad_FL" : Ciudad_FL,"Poblacion" : Poblacion,"Densidad" : Densidad}
Florida = pd.DataFrame(Data)

# Cuando se quiere ver el detalle del conjunto de datos del dataframe en la consola se digita el nombre del dataframe
Florida

# head(). Para acceder a los primeros datos de un dataframe cuando el conjunto de datos es muy extenso
Florida.head() # presenta en consola los primeros 5 datos del dataframe
Florida.head(10) # Presenta los primeros 10 registros del conjunto de datos

# columns. Permite consultar los nombres de las columnas (variables) del dataframe
Florida.columns
# Cuando queremos acceder a la información de una columna (o variable) es posible mediante el nombre de la misma
# usandola como "índice" o atributo del objeto (objeto: dataframe)
Florida["Ciudad_FL"]
Florida.Ciudad_FL

# loc. Se usa para consultar la información de una fila (registro u observación)
Florida.loc[3]    

# iloc. Permite consultar información de filas y columnas
Florida.iloc[:,1:4] # Todas las filas (solo los ":") y las columnas 1 a 3 (se escribe de 1 a 4 pero el 4 no cuenta)

# Agregar una columna a un dataframe
Florida["Region"] = "NaN"

# del. Se utiliza para eliminar una columna del dataframe
del Florida["Region"]

# T. (en mayúscula) permite transponer el dataframe
Florida.T

# Asignar una de las columnas como índices de las observaciones
Florida = pd.DataFrame({"Ciudad_FL" : Ciudad_FL,"Poblacion" : Poblacion,"Densidad" : Densidad}, index=Codigo)

# index. Consulta los índices de un dataframe
Florida.index
# loc. Usando el ídice del registro
Florida.loc["FL-03"]

# values. convierte el dataframe en un arreglo (array) o vector de listas
Florida.values

# Para consultar una de las "celdas" del dataframe
Florida.Ciudad_FL[1]
Florida["Ciudad_FL"][1]
Florida.iloc[1,0]

# sort_index(). Permite organizar las filas del dataframe segun su índice
Florida.sort_index()

#  sum(). Se utiliza para sumar las columnas númericas del dataframe, las columnas de texto las concatena
Florida.sum() # Suma vertical
Florida.sum(0) # Suma vertical, esto es, suma por filas
Florida.sum(1) # Suma horizontal, es decir, suma las columnas

# cumsum(). Permite calcular la suma acumulada
Florida.cumsum()

# describe(). Es una de las funciones más impportantes, me entrega
# un resumen con parametros de estadística descriptiva básicos
# Solo aplica para variables numéricas
Florida.describe()

# pct_change(). Permite calcular porcentajes de variación fila a fila
# aplica solo para variables numéricas
Florida.iloc[:,1:3].pct_change()

# Existen otros métodos de estadística descriptiva:
# count, cantidad de observaciones no nulas
# min, max; máximo y mínimo de un conjunto de valores
# argmin, argmax; índice del valor mínimo y máximo respectivamente
# idxmin, idxmax; similar al anterior, se obtiene el noombre del índice
# mean, media de un conjunto de datos numéricos
# median, mediana de los datos, esto es, la mitad arimética de los datos
# var, varianza de los datos
# std, desviación estándar de los datos
# diff, diferencia entre datos conjuntos.

# .corr(), correlación de dos variables y matriz de correlación
Florida["Poblacion"].corr(Florida["Densidad"])
Florida.corr()

# .cov(), covarianza de dos variables y matriz de covarianza
Florida["Poblacion"].cov(Florida["Densidad"])
Florida.cov()

# .corrwith(), correlación de las variables respecto a una específica
Florida.corrwith(Florida.Densidad)

# unique(), "elimina duplicados", entrega un arreglo con los valores únicos
# de una de las variables del dataframe
Florida["Ciudad_FL"].unique()


# value_counts(), proporciona la cantidad de veces que aparece un dato específico
# Sirve también para identificar observaciones repetidas
Florida.value_counts()

# isin. es una función que me permite consultar si un dato hace parte de un 
# dataset específico. La conuslta puede usarse para filtrar el conjunto de datos
resultado = Florida.Ciudad_FL.isin(["Tampa"])
Florida[resultado]
