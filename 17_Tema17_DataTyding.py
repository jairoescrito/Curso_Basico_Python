#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:34:24 2023

@author: jairoescrito
"""

import pandas as pd
import os

os.getcwd() # Consultar directorio de trabajo
os.chdir('/home/jairoescrito/OneDrive/Documentos/TeslaTeach/Python/Python_Basico/Curso_Basico') # Modificar directorio de trabajo


Financiero = pd.read_excel(pd.ExcelFile("FINANCIERO_Python.xlsx"), 'VENTAS')



# Data Tyding - Preparación, limpieza y organización de datos

# 1) Missing Values, NA's (NaN) o Datos faltantes

# Los NA's hacen referencia a datos inexistentes o datos no observados durante la recolección de la captura del registro
# Un NA no es lo mismo que NULL, en el caso del segundo este obedece más a un valor "vació" en el registro
# Es decir, no significa que no existe, este existe pero es vacío. Esto en términos de las bases de datos

# Identificación de los NA's

# isnull() es una función que me permite conocer si el dato incluido en el dataset es o no NA
Financiero.isnull()
Financiero.isnull().sum() # me permite calcular el dato de la cantidad de NA's que existen por columnas
Financiero.isnull().sum().sum() # Genera el valor total de NA's
Financiero.isnull().sum(axis=1) # si quiero calcular los NA's por filas, modifico el parámetro "axis" a 1, no obstante, 
# este resultado visualmente no es muy practico
Financiero.isnull().any() # Identifico que columnas tienen NA's (aquellas que generan True)
Filas_nas = Financiero[Financiero.isnull().any(axis=1)] # Genero un dataframe solo con las filas que contienen los NA's
indices_nas = Financiero[Financiero.isnull().any(axis=1)].index # obtengo los ídices de las filas donde aparece un NA
# notnull() contrario a isnull
Financiero.notnull().sum() # me muestra la cantidad de valores no nulos

# Tratamiento de NA's: eliminación de los NA

# dropna() elimina las filas que contiene NaN
Filas_no_nas = Financiero.dropna() # creo un dataset con excluyendo las filas que tienen al menos un NA's
# dropna(thresh=) elimina las filas bajo cierta condición de cantidad de NA's que incluya
Filas_no_nas = Financiero.dropna(thresh=2) # elimino las filas que tienen dos NA's 
 
# Tratamiento de NA's: reemplazo de los NA

# fillna() permite impputar o reemplazar los NA por un valor que se determine
Financiero.fillna(0) # Identifica todos los NA's en el dataset y los reemplaza por un cero
Financiero.fillna(0,inplace = True) # Reemplaza los valores NA por cero y modifica el dataframe original
Financiero.CANTIDAD.fillna(0) # Reemplazo los NA's de una columna específica

# La decisión de tratamiento de los NA's depende de las condiciones del negocio: 1) eliminar los registros
# que contienen al menos un NA puede ser adecuado para cierto tipo de datos pero para otros no.
# Se podría decidir eliminar un registro del dataset si se tienen más de x números de NA's en el mismo 
# registro.
# La imputación de NA's (atribuir un valor a los NA's) se puede hacer también con parámetros de 
# Estadística descriptiva como la Moda, la Mediana o la Media. La decisión del parámetro a usar va a 
# está asociada al análisis previo del comportamiento de los datos, específicamente su dispersión

round(Financiero.CANTIDAD.mean()) # Así se calcularía el valor de la media con redondeo
Financiero.CANTIDAD.fillna(round(Financiero.CANTIDAD.mean()))
Financiero.CANTIDAD.mode() # Cálculo de la moda
Financiero.CANTIDAD.median() # Cálculo de la mediana 

# Existen un método más desarrollado bajo el método KNN (K-Nearst Neighbor), mediante un calculo de
# distancias, localiza los k vecinos y con estos calcula el promedio para determinar el valor del NA
# Para el caso de las variables categóricas usa el valor más repetido o el más cercano entre los k vecinos

# 2) Trasformaciones en en un conjunto de datos
# para trabajar en dataframes es necesario llamar, antes de aplicar una función, el atributo .str
# con el fin de "informar" que la función se va a aplicar a un objeti tipo cadena de texto
# Se usa cuando se requiere trabajar sobre la cadena y no global sobre el valor

# Eliminar espacios en blanco
Financiero.ASESOR.str.strip() # Del dataset "llamo" los objetos str (string) y le aplico eliminar espacios en blanco
# Verificar los datos registrados en una columna
Financiero.CIUDAD.unique() # Es posible observar la diferencia que existe en los diferentes tipos de 
# formas que contiene cada "valor" en el conjunto de datos. En primera instancia es necesario eliminar
# espacios en blanco
Financiero.CIUDAD.str.strip().unique() #Elimino los espacios en blanco

# Eliminar duplicados
Financiero.ASESOR # creo un nuevo dataframe con la columna de asesores 
Financiero.ASESOR.mode()
sum(Financiero.ASESOR=="ANA MARIA")
Financiero.ASESOR.isnull().sum()
Financiero.ASESOR.fillna("ANA MARIA",inplace = True)
Financiero.ASESOR.drop_duplicates() # Se eliminan los duplicados y se dejan los valores únicos

# Modificación de cadenas
# Cambiar a minúscula
Financiero.CIUDAD.str.lower()
# Cambiar a mayúsculas
Financiero.CIUDAD.str.upper()
# Cambiar a mayúscula inicial 
Financiero.CIUDAD.str.title()

# Reemplazar valores
Financiero.CIUDAD = Financiero.CIUDAD.str.strip()
Financiero.CIUDAD.unique()
Financiero.CIUDAD.replace("MEDELLIN","MEDELLÍN")
Financiero.CIUDAD.replace(["MEDELLIN","BOGOTA"],["MEDELLÍN","BOGOTÁ"])

# Cambiar los nombres de las columnas
Financiero.rename(columns=str.title) # Cambio a mayúscula inicial
Financiero.rename(columns={"FECHA":"Fecha_Venta"}) # Cambio el nombre de una columna
