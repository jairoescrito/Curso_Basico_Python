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

### Data Tyding - Preparación, limpieza y organización de datos ###

Finan = pd.read_csv('df_Finan.csv')
Finan.head()
print(Finan.dtypes) # Verificar que cada columna corresponda al tipo de dato que almacena
Finan.FECHA = Finan.FECHA.astype("datetime64[ns]")
Finan.ASESOR = Finan.ASESOR.astype("category")
Finan.CIUDAD = Finan.CIUDAD.astype("category")
Finan.CLASIFICACION = Finan.CLASIFICACION.astype("category")
Finan.CATEGORIA = Finan.CATEGORIA.astype("category")

# 2) Trasformaciones en un conjunto de datos

# A) Agrupaciones: los DataFrame pueden agruparse por filas (axis = 0) o por columnas (axis = 1). Las agrupaciones se realizan por
# clave y esta genera un nuevo valor, la agrupación genera un nuevo objeto (array, dataframe, etc). Cuando se hace una agrupación
# tenemos un objeto "abstracto" "la agrupación" que se puede hacer visible al usar una función de agregación.

# Promedio de ventas por asesor:
Avg_A = Finan["VALOR_U"].groupby(Finan["ASESOR"])
Avg_A # objeto abstracto, tiene su espacio reservado en la memoria
Avg_A.mean()

# Promedio de ventas por asesor y ciudad
Avg_AC = Finan.VALOR_U.groupby([Finan.CIUDAD,Finan.ASESOR]).mean() # Cuando la agrupación es de más de 
# una columna el parámetro de "groupby" debe ser una lista de columnas
Avg_AC # El resultado entregado es una serie: las columnas de agrupación se convierten en índices.
# índices jerarquizados que están "apilados"
# Desapilar la serie en "indices por filas y columnas"
Avg_AC = Avg_AC.unstack() # se convierte en un dataframe, no obstante, la columna de ciudad pasa a ser el índice de la fila
Avg_AC = Avg_AC.reset_index() # Retomar la columna ciudad como datos y no como índice
# Frecuencia de observaciones
Freq_A = Finan.groupby(Finan.ASESOR).size()
Freq_AC = Finan.groupby([Finan.ASESOR,Finan.CIUDAD]).size()
Freq_AC = Freq_AC.unstack().reset_index()
# Bucle para generar subconjuntos de datos por asesor
for Asesor, Grupos  in Finan.groupby("ASESOR"): # Si no se selecciona una variable para agrupar,
# es decir, se selecciona todo el dataframe, se genera un subcojunto, no se requiere función de
# agregación
    print(Asesor)
    print(Grupos)
del(Asesor,Grupos) # Eliminar las variables temporales

''' dos formas de escribir lo mismo
Finan.groupby("ASESOR")[['VALOR_U']]
Finan["VALOR_U"].groupby(Finan["ASESOR"])
'''
# Crear una columna nueva con el total de las ventas
Finan["VENTA_TOTAL"] = round(Finan["VALOR_U"]*Finan["CANTIDAD"])
Finan.VENTA_TOTAL.head()

# Usar una función de agrupación personalizada
VentaT_AC = Finan.VENTA_TOTAL.groupby([Finan.CIUDAD,Finan.ASESOR]) # Objeto de agrupación
def Rangos(data): # Crear un función propia
    return (data.max() - data.min())
VentaT_AC = pd.DataFrame(VentaT_AC.agg(Rangos)) # Método agg para aplicar la función
VentaT_AC = VentaT_AC.reset_index() # Convertir las columnas índice en columnas de dataframe
VentaT_AC = VentaT_AC.rename(columns={"VENTA_TOTAL":'V_MAX - V_MIN'}) # Renombrar la columna

# Multiples agregaciones
Grupos = Finan.groupby(["ASESOR","CIUDAD"]) # Objeto de agrupación
Tabla_Resumen = Grupos["VENTA_TOTAL"] # Objeto con columna para agregación
# En el método de agregación recibe la lista de funciones a aplicar, en la lista se incluyen las tuplas
# (Nombre,Función), para agregar el nombre personalizado de cada columna de agregación
Tabla_Resumen = Tabla_Resumen.agg([('Promedio','mean'),('Máximo','max'),('Mínimo','min')])
Tabla_Resumen.head()

# Extracción de fecha para agregaciones por fecha
Finan['AÑO'] = Finan['FECHA'].dt.strftime('%Y')
Finan['MES'] = Finan['FECHA'].dt.strftime('%m')

# Ejercicio: crear una tabla de agregación para cada año, mes y ciudad calculando:
# 1) La cantidad de registros, 2) el promedio de ventas, 3) La venta máxima y 4) la venta mínima

Grupos = Finan.groupby(['AÑO','MES','CIUDAD'],as_index=False) # parámetro para evitar que se generen
# las agregaciones como indices para que estos se generen como columnas de datos en el Data Frame
Tabla_Resumen = Grupos["VENTA_TOTAL"]
Tabla_Resumen = Tabla_Resumen.agg([('Registros','size'),('Promedio','mean'),('Máximo','max'),('Mínimo','min')]) # función size o count entregan los mismos resultados
Tabla_Resumen.head()


# Tablas pivote: "Nombre del DataFrame".pivot_table
# Las tablas pivote se resumen por en valores promedio (no en suma como excel)
# En el parametro columns se definen las columnas de la tabla y en index las filas
# Para los totales se incluye el parámetro margins = True, adicionalmente, si se quiere
# modificar la función de agregación se debe agregar el parámetro "aggfunc"
# Si los cálculos generan NaN se usa el parámetro "fill_value=0" (por ejemplo para llenar con cero)

Finan.pivot_table('VENTA_TOTAL', index=['CIUDAD', 'CLASIFICACION'],
                 columns='ASESOR', aggfunc=['mean'], fill_value=0)

Finan.pivot_table('VENTA_TOTAL', index=['CIUDAD', 'CLASIFICACION'],
                 columns='ASESOR', aggfunc=['mean','count'], fill_value=0, margins = True)

Finan = Finan.iloc[:,[0,9,10,1,2,3,4,5,7,6,8]]

Finan.to_csv('dataset.csv', index=False, header=True,sep=',',decimal='.')

