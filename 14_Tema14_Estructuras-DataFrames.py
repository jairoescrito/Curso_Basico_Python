#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:18:10 2023

@author: jairoescrito
"""

# Instalación de la librerias
# Como estamos trabajando sobre la distribucion anaconda, la instsalación de librerías se hace así:
# conda install <nombre de la libreria>
# Si se requiere actualizar la librería, el comando a utilizar es:
# conda update <nombre de la libreria>
# Despues de instalar o actualizar la librería es aconsejable reiniciar el nucleo (kernel)

import pandas as pd # las libreías instaladas se deben "activar" o "cargar" en el entorno en el cual se está trabajando
# normalmente se le modifica el nombre a la libería para que en e uso se pueda escribir de manera más corta
# se usa "as" para modificar el nombre (la modificación se refiere al termino con el cual se va a usar en el script)

# Data Frames: representan tablas de datos que se componen de filas y columnas. Cada columna suele contener un solo tipo de dato.
# No necesariamente las columnas deben tener el mismo tipo de datos, el tipo puede varias de una columna a otra
# Las filas y las coumnas de un dataframe se pueden identificar por índices aunque las columnas tambien pueden ser identificadas por su
# encabezado

Ciudades = ["Bogotá","Medellín","Cali","Barranquilla","Cartagena","Cúcuta","Ibagué","Villavicencio","Bucaramanga"]
Departamentos = ["Distrito Capital","Antioquia","Valle del Cauca","Atlántico","Bolívar","Norte de Santander","Tolima","Meta","Santander"]
Poblaciones = [8.4,2.6,2.5,1.2,1.1,0.7,0.6,0.5,0.5]
Datos = {"Ciudad":Ciudades, "Departamento":Departamentos, "Poblacion":Poblaciones}
# Cuando un dataframe se construye a partir de un diccionario, todas las listas deben tener la misma cantidad de elementos
# Si el dataset se cnstruye desde listas y estas no tienen la misma cantidad de elementos, los datos faltantes se completan
# con NaN (Not a Number)


# Crear un dataframe a partir de un diccionario
Frame = pd.DataFrame(Datos)
Frame

# Cambiar el orden del dataframe creado a partir de la lista
Frame_2 = pd.DataFrame(Datos, columns = ["Departamento","Ciudad","Poblacion"])


# Crear un dataframe de las 10 ciuaddes más pobladas de Florida. Las variables son:
# Código, Ciudad_FL, Poblacion, Densidad
# "FL-01","FL-02","FL-03","FL-04","FL-05","FL-06","FL-07","FL-09","FL-10","FL-11","FL-12","FL-13","FL-14"
# "Jacksonville","Miami","Tampa","San Petersburgo","Orlando","Hialeah","Tallahassee","Fort Lauderdale","Port Saint Lucie","Pembroke Pines","Cabo Coral","Hollywood","Gainesville"
# 903072,481084,335709,244769,238300,224669,181376,165521,164603,154750,154305,140768,124354
# 11135.9,2960.2,3964.4,2327.3,10474.2,1809.3,4761.1,1444.5,4671.1,1460.2,5143.8,2028.5
# El dataframe se debe llamar "Florida"

Codigo = ["FL-01","FL-02","FL-03","FL-04","FL-05","FL-06","FL-07","FL-09","FL-10","FL-11","FL-12","FL-13","FL-14"]
Ciudad_FL = ["Jacksonville","Miami","Tampa","San Petersburgo","Orlando","Hialeah","Tallahassee","Fort Lauderdale","Port Saint Lucie","Pembroke Pines","Cabo Coral","Hollywood","Gainesville"]
Poblacion = [903072,481084,335709,244769,238300,224669,181376,165521,164603,154750,154305,140768,124354]
Densidad = [1100.01,11135.9,2960.2,3964.4,2327.3,10474.2,1809.3,4761.1,1444.5,4671.1,1460.2,5143.8,2028.5]
Data = {"Codigo" : Codigo,"Ciudad_FL" : Ciudad_FL,"Poblacion" : Poblacion,"Densidad" : Densidad}
Florida = pd.DataFrame(Data)
