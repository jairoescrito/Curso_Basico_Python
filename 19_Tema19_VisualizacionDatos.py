#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:30:03 2023

@author: jairoescrito
"""
import pandas as pd
import os

os.getcwd()
# Lectura e importación de archivos Excel
xlsx = pd.ExcelFile("FINANCIERO_Python.xlsx")
Financiero = pd.read_excel(xlsx, 'VENTAS')
Financiero.info()

# Visualización de datos 

Financiero.iloc[:,[1,7]].head(10)

boxplot = Financiero.iloc[:,[1,7]].boxplot(column = Financiero["ASESOR"].unique())
Financiero.iloc[:,[1,7]].info()

Prueba


import matplotlib.pyplot as plt

plt.scatter(Financiero.iloc[0:100,0],Financiero.iloc[0:100,7])


