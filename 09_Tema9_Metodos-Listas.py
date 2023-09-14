#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:21:53 2023

@author: jairoescrito
"""

## Métodos de Listas (como atributos) ##

Lista_1 = [1,2,3,4,5,6,7,8,9]
Lista_2 = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g"]


# len(): calcular o conocer el tamaño de la lista, la cantidad de elementos que tiene
len(Lista_1)
print(len(Lista_2))

# append(): añadir un item o elemento a la lista, se úbica en una nueva posición quedando en la última
Lista_1.append(0)
print(Lista_1)
Lista_2.append("H")
Lista_2.append("h")
print(Lista_2)

# clear(): elimina todos los elementos de una lista, la deja vacía
print(Lista_2.clear())

# extend(): así como el uso de "+" en lista, extend permite "extender" dos listas en una
Lista_1.extend([-1,-2,-3])

# count(): cuenta la cantidad de veces que un elemento está en la lista
Lista_3 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
Lista_3.count(5)

# index(): muestra la posición en la que se encuentra un elemento dado en la lista. 
# Si el elemento está repetido, la primera posición en la que aparece
Lista_2.index("F")

# insert(): agrega un item o elemento a uns lista en una posición específica
Lista_1.insert(0,0)
Lista_1.insert(-2,"x")

# pop(): elimina un elemento de la lista. Le puedo agregar la posición a eliminar (índice) si no se le da un índice, se elimina el último
Lista_1.pop()
Lista_1.pop(Lista_1.index("x")) # index() me dice donde está x, es decir, en qué posición

# remove(): funciona similar a pop solo que en esta función se le entrega el elemento a eliminar y no su posición
# si el elemento proporcionado está repetido en la lista, entonces eliminará el primero (el del índice menor)
Lista_1.remove(-2)

# reverse(): le da un orden inverso a la lista, es decir, el primer elemento se convierte en el último, el segundo en el penúltimo y así sucesivamente

Lista_2.reverse()

# sort(): ordena la lista de menor a mayor o en órden alfabético (dependiento el tipo de elementos que incluya la lista)
Lista_2.sort()


## Métodos de Listas (como funciones) ##

# sum(): suma los elementos de una lista. Si los elementos de la lista no son TODOS numéricos, genera un error
sum(Lista_1)

# max(): entrega el valor mayor de los elementos de una lista. Depende de la jerarquía de los tipos de datos, por ejemplo, si son letras,
# asume la "a" como la menor y la "z" como la mayor. Genera error para las listas que incluyen elementos tipo número y tipo texto
max(Lista_2)

# min(): entrega el valor menor de los elementos de una lista. Usa la misma lógica de jerarquía mencionada en max()
# También genera error para las listas que incluyen elementos tipo número y tipo texto
min([1,"a",2,"b",3,"c",4,"d",5,"e"])


# Ejercicio 23: Crear una lista con los primeros 20 números de la secuencia Fibonnaci
# Crear dos nuevas listas: una con los números impares y otra con los números pares
# Las nuevas listas organizarlas en orden inverso



