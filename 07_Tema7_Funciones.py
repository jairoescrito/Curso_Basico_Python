#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 21:18:59 2023

@author: jairoescrito
"""

## Funciones ##
# Las funciones se usan para "re-utilizar" partes de script en tareas que pueden ser repetitivas
# y evitar escribir varias veces las mismas instrucciones
# Para crear funciones se debe tener en cuenta si la misma requiere parámetros o no

def NumeroEneroValido ():
    while True:
        try:
            Num = int(input("Ingrese un número entero: "))
        except Exception as E:
            print("El valor ingresado no es un número entero. Error:",type(E).__name__)
            continue
        else:
            print("Número entero verificado. ¡Gracias!")
            break
    return Num

a = NumeroEneroValido()


def NumeroPrimo(N):
    Num = N
    Div = 2
    Primo = 0
    while Div < Num:
        if Num % Div == 0:
            Primo += 1
        Div += 1
    if Primo == 0:
        print("El número",Num,"es primo.")
    else:
        print("El número",Num,"no es primo.")
        
NumeroPrimo(12)


def Potencia(N,a):
    Resultado = N**a
    return Resultado

X = Potencia(2,3)
X

# Ejercicio 17: Crear una función para imprimir la secuencia Fibonacci
# Ejercicio 18: Crear una función para verificar si un número es múltiplo de 9

# Ejercicio 19*: Crear una función para calcular el número Pi: formula Leibniz 
# Pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
# Se necesitan al menos 1 millon de términos para alcanzar una precisión de 5 decimales
def CalcularPi(n):
    div = 1
    signo = 1
    pi = 0
    i = 1
    while i <= n:
        pi = pi + (signo*(4/div))
        div += 2
        signo *= -1
        i += 1
    return pi


