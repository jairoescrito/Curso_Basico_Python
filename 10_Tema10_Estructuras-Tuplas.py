#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:40:50 2023

@author: jairoescrito
"""

# Es una estructura similar a las listas, es decir, permiten guardar datos, no obtante,
# No es modificable.
# La tupla se define con paréntesis

Tupla = (1,2,3,4,5)
Tupla

# Acceder a unos de los datos de la tupla a través de los índices (ubicación)
Tupla[2:]
Tupla[0]

Lista_1 = ["a","b","c"]
Lista_2 = [1,2,3]

Tupla_1 = (Lista_1,Lista_2)

Tupla_1[0][1]

Tupla_1[0] = Tupla # Error, porque no se puede modificar la tupla

Tupla_3 = ((1,2,3),(4,5,6),(7,8,9),0)

# Ejercicio: Crear tres listas
# La primera con los números pares de 1 a 100
# La segunda con los números impares de 1 a 100
# La tercera con los números primos de 1 a 100
# guardarlos en una tupla
# Imprimir la posición 25 de cada lista en la tupla


# Ejercicio: crear tres tuplas, con los datos de las tres listas del ejercicio anterior
# Guardarlos en una lista
# Imprimir la posición 25 de cada tupla en la lista
# Eliminar la tercera tupla de la lista
# Cambiar el orden de las tuplas dentro de la lista, que la primera sea segunda y la segunda sea primera


