#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:34:24 2023

@author: jairoescrito
"""

import pandas as pd
import os

os.getcwd() # Consultar directorio de trabajo
# os.chdir('/home/jairoescrito/OneDrive/Documentos/TeslaTeach/Python/Python_Basico/Curso_Basico') # Modificar directorio de trabajo

Financiero = pd.read_excel(pd.ExcelFile("FINANCIERO_Python.xlsx"), 'VENTAS')

### Data Tyding - Preparación, limpieza y organización de datos ###

# 1) Missing Values, NA's (NaN) o Datos faltantes y modificación de valores

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

# Reemplazo de las variables string con imputación de la moda
# Eliminar duplicados
Financiero.ASESOR # creo un nuevo dataframe con la columna de asesores 
Financiero.ASESOR.mode()
sum(Financiero.ASESOR=="ANA MARIA")
Financiero.ASESOR.isnull().sum()
Financiero.ASESOR.fillna("ANA MARIA",inplace = True)
Financiero.ASESOR.drop_duplicates() # Se eliminan los duplicados y se dejan los valores únicos

# Imputación por KNN #
# Existen un método más desarrollado bajo el método KNN (K-Nearst Neighbor), mediante un calculo de
# distancias, localiza los k vecinos y con estos calcula el promedio para determinar el valor del NA
# Para el caso de las variables categóricas usa el valor más repetido o el más cercano entre los k vecinos

# Dato que el dataset es mixto (diferentes tipos de datos: string, float, tiempo) es necesaria una transformación de datos
# antes de la imputación 
Financiero.info()

# A) Modificar el tipo de formato de fecha 
Financiero.FECHA.head()
Financiero.FECHA = Financiero.FECHA.dt.date
Financiero.FECHA.head()

# B) Tratar las variables string: estandarización de los datos
# Es necesario verificar inicialmente si hay diferentes tipos de datos que signifiquen lo mismo
for i in range(1,len(Financiero.columns)):
    if Financiero.iloc[:,i].dtype == 'float64': # Consultar el tipo de datos de los valores de la columna
        continue
    else:
        print(Financiero.columns[i],":",Financiero.iloc[:,i].unique())
del(i) # Eliminar la variable temporal del bucle del entorno de variables
# Eliminar espacios en blanco
for i in range(1,len(Financiero.columns)):
    if Financiero.iloc[:,i].dtype == 'float64': 
        continue
    else:
        Financiero.iloc[:,i] = Financiero.iloc[:,i].str.strip() # Eliminar los espacios en blanco
del(i) # Eliminar la variable temporal del bucle del entorno de variables
# Reemplazar valores
Financiero.CIUDAD = Financiero.CIUDAD.replace(["MEDELLIN","BOGOTA"],["MEDELLÍN","BOGOTÁ"])
# Modificación de cadenas
# Cambiar a minúscula: Financiero.CIUDAD.str.lower()
# Cambiar a mayúsculas: Financiero.CIUDAD.str.upper()
for i in range(1,len(Financiero.columns)):
    if Financiero.iloc[:,i].dtype == 'float64': 
        continue
    else:
        Financiero.iloc[:,i] = Financiero.iloc[:,i].str.title() # Cambiar Texto a tipo Título
del(i) # Eliminar la variable temporal del bucle del entorno de variables
# C) Mapear (o categorizar) las variables categóricas a enteros
Financiero['ASESOR'].unique()
Financiero['AsesorMap'] = Financiero['ASESOR'].map({'Ana Maria': 1, 'Camila': 2, 'Juliana':3})
Financiero['CIUDAD'].unique()
Financiero['CiudadMap'] = Financiero['CIUDAD'].map({'Bogotá':1, 'Medellín':2, 'Cali':3, 'Barranquilla':4, 'Cartagena':5})
Financiero['CLASIFICACION'].unique()
Financiero['ClasifMap'] = Financiero['CLASIFICACION'].map({'Nacionales':1, 'Importados':2})
Financiero['CATEGORIA'].unique()
Financiero['CategMap'] = Financiero['CATEGORIA'].map({'Foliares':1, 'Coadyuvantes':2, 'Fertirrigación':3, 'Edáficos':4,'Bioestimulantes':5, 'Especiales':6})
df = Financiero.iloc[:,[8,9,10,11,6,7]] # Dataset con las variables numéricas

# D) Ejecutar la imputación
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5) # Crear el modelo de imputación con K = 5
df = pd.DataFrame(imputer.fit_transform(df)) # Imutación de los NaN
# Los valores imputados son decimales, no obstante la variable "ASESOR" y "CANTIDAD" son de tipo entero
# El df resultante no tiene nombre de columnas
df = df.rename(columns={0:'ASESOR',1:'CIUDAD',2:'CLASIFICACION',3:'CATEGORIA',4:'VALOR_U',5:'CANTIDAD'})
df.ASESOR = round(df.ASESOR)
df.CANTIDAD = round(df.CANTIDAD)
del(imputer)

# E) Regresar a los valores originales (del mapeo)
# Retornar a los valores originales
df.ASESOR = df['ASESOR'].map({1:'Ana Maria', 2:'Camila',3: 'Juliana'})
df.CIUDAD = df.CIUDAD.map({1:'Bogotá', 2:'Medellín', 3:'Cali', 4:'Barranquilla', 5:'Cartagena'})
df.CLASIFICACION = df.CLASIFICACION.map({1:'Nacionales', 2:'Importados'})
df.CATEGORIA = df.CATEGORIA.map({1:'Foliares', 2:'Coadyuvantes', 3:'Fertirrigación', 4:'Edáficos',5:'Bioestimulantes', 6:'Especiales'})
#Reconstruyendo el dataset original con los resultados de la imputación
df_Finan = pd.concat([Financiero.iloc[:,0],df.iloc[:,0:4],Financiero.iloc[:,5],df.iloc[:,4:6]],axis=1)
df_Finan.to_csv('df_Finan.csv', index=False, header=True,sep=',',decimal='.')
del(df)
