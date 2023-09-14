#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:21:53 2023

@author: jairoescrito
"""

## Listas ##

# Las listas son un tipo de variable que pueden guardar varios tipos de datos. Se ubican entre corchetes '[ ]'
# cada dato en la lista se separa por comas. Cada item de una lista se identifica con un índice, los índices inician el conteo en cero
# Una lista puede entenderse como un conjunto de datos sencillo.
# Su principal característica es que son modificables, puedo modificar el valor de una posición haciendo uso del índice

Lista = [1,2,3]
print(Lista[0])
print(Lista[1])
print(Lista[2])

Lista = Lista + Lista # Union de dos listas 
Lista

Lista = Lista * 3 # Multiplicar la lista en una sola lista
Lista

ListaVacia = [] # Crear una lista vacía

Lista = [1,2,3]
sum(Lista) # Si todos los elementos de una lista son números los puedo sumar

Lista = [Lista,Lista,Lista] # Listas anidadas
Lista

def CrearLista ():
    try:
        N= int(input("Vamos a crear una lista con el tamaño que desee. Por favor ingresa el tamaño de la lista que crearemos: "))
    except Exception as E:
        print("el valor ingresado no es un número entero. Error: ", type(E).__name__)
    else:
        Lista=[]
        Rta=input("¿la lista a crear es de elementos numéricos? Si/No: ")
        if Rta=="Si":
            i=0
            while i<N:
                try:
                    print("\n")
                    print("Ingresaremos en la posición",i+1,"de la lista el número: ")
                    Lista.append(int(input("Ingrese el valor numérico para esa posición: ")))
                    i+=1
                except Exception as E:
                    print("el valor que intenta ingresar a la lista no es numérico. Error:", type(E).__name__)
                    break
        elif Rta=="No":
            i=0
            while i<N:
                print("\n")
                print("Ingresaremos en la posición",i+1,"de la lista.")
                Lista.append(input("Ingrese el elemento o item para esa posición: "))
                i+=1
        else:
            print("No entiendo la respuesta, por favor responde 'Si' o 'No'")
    return Lista

A = CrearLista()
B = CrearLista()
C = CrearLista()
D = CrearLista()

# Ejercicio 20: Crear una lista con los números de 1 a 100
# Ejercicio 21: Imprimir los números primos de la lista del ejercicio 20
# Ejercicio 22: Crear cuatro listas: Nombre, Sueldo, Deducción y Bonificación con 5 elementos cada una
# Crear una quinta lista con el calculo del neto a pagar