#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:40:50 2023

@author: jairoescrito
"""
# Métodos de Tuplas
# Al igual que las listas podemos consultar atributos o hacer cálculos con los elemebntos de las tuplas

Tupla_3 = ((1,2,3),(4,5,6),(7,8,9),0)

# Tamaño de la tupla

len(Tupla_3)

# Index: para conocer la posición de un elemento dentro de la tupla

Tupla_3.index(0)

# Contar cuantas veces aparece un elemento dentro de una tupla

Tupla_3.count(0)

# Ordenar los elementos de una tupla

Tupla_x = (18,36,6,24,0,60)
sorted(Tupla_x)

# Sumar los elementos de una lista (si los elementos son numéricos)

sum(Tupla_3)
sum(Tupla_x)

# Maximo de los elementos de una tupla (el mismo tipo de elementos)

max(Tupla_x)

# Mínimo de los elementos de una tupla (el mimso tipos de elementos)

min(Tupla_x)
