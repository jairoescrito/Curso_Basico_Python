#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:19:09 2023

@author: jairoescrito
"""

## Excepciones ##
# Es común encontrar errores en el script, estos (los más comunes) pueden ser:
# 1) de sintaxis (SyntaxError: que falta algo),
# 2) de nombre (NameError: función o método no definido), y
# 3) semánticos (IndexError, TypeError, ValueError: están asociados a la "lógica" de las instrucciones que estamos escribiendo)


# Bloque Try-Except 


try:
    Num = int(input("Ingrese un número entero: "))
except Exception as E:
    print("El valor ingresado no es un número entero. Error:",type(E).__name__)
else:
    print("Número entero verificado. ¡Gracias!")


while True:
    try:
        Num = int(input("Ingrese un número entero: "))
    except Exception as E:
        print("El dato ingresado no es un número entero. Error:",type(E).__name__)
        continue
    else:
        print("Número entero verificado. ¡Gracias!")
        break


while True:
    try:
        Cant = int(input("Ingresa la cantidad (número) de números con los que vamos a trabajar: "))
    except Exception as Error:
        print("El dato ingresado no es un número entero. Error:",type(Error).__name__)
        continue
    else:
        print("Entendido, vamos a trabajar con",Cant,"número(s)")
        k = 1
        while (k <= Cant):
            try:
                Num = float(input("Ingresa el número con el que quieres trabajar: "))
            except Exception as E:
                print("¡Atención!, el dato que ingresaste no es un número",type(E).__name__)
                print(k)
                continue
            else:
                print("el doble del número ingresado es:",Num*2)
                print("el cuadrado del número ingresado es:",Num**2)
                print (k)
                k += 1
        break


# Ejercicio 15: verificar si son números primos
# 1) Solicitar la cantidad de números a evaluar verificando que el valor si sea un número válido, si no es váliso solicitar de nuevo
# 2) Solicitar los números a evaluar verificando que si sea un número entero, si no es válido, solicitar de nuevo
# 3) Verificar si el número ingresado es primo e imprimir el resultado

Num = 137
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

# Ejercicio 16: imprimir la letra de una frase
# 1) Solicitar una frase por consola
# 2) Solicitar la posición de la letra que se necesita, verificar que sea un número válido (con try-except)
# 3) Se debe verificar que el número ingresado no sea mayor que el tamaño de la frase ni menor a 1 (con un if-elif-else)
# 4) Imprimir la letra o caracter de la posición solicitada (tener en cuenta que los indices inician en cero pero las posiciones el usuario las
# cuenta desde 1)


