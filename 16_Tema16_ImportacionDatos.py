#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:18:10 2023

@author: jairoescrito
"""
import os
import pandas as pd
# Cosultar el directorio de trabajo
os.getcwd() 
# Modificar el directorio de trabajo
# os.chdir('C:\Users\Lenovo\Downloads\Works\')
os.chdir('/home/jairoescrito/OneDrive/Documents/TeslaTeach/Python/Python_Basico/Curso_Basico')

# Importación de datos o archivos

# Lectura e impportación de archivos planos CSV
Bostoncsv = pd.read_csv('Boston.csv')
Bostoncsv
type(Bostoncsv)

# conda install openpyxl
# conda install xlrd

# Lectura e importación de archivos Excel
xlsx = pd.ExcelFile("Boston.xlsx")
Bostonxlsx = pd.read_excel(xlsx, 'Sheet 1')
type(Bostonxlsx) 