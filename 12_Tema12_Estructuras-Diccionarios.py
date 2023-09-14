#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:40:50 2023

@author: jairoescrito
"""

# Son un tipo de estructura en los que cada elemento está asociado a una clave
# la estructura tiene un orden clave:valor
# Los diccionarios son mutables (modificables), similar a lo que sucede con las
# listas
# En cada diccionarios las claves deben ser únicas, no se pueden repetir

Edades = {"Jorge": 72, "Ximena": 35, "Johanna":39, "Dolly": 65, "Martina": 7, "Belen":3}
Edades

Vacio = {}

Edades[1] # A diferencia de las listas y las tuplas, no podemos consultar los elementos por índices,
# debe hacerse por las claves

Edades["Dolly"]

Edades["Dolly"] = 66 # Se pueden modificar los valores que tienen los elementos de una lista
Edades

Edades["Cristian"] = 38 # Se pueden agregar elementos adicionales al diccionarios especificando la clave
Edades

# Una forma de entender los diccionarios es cada elemento es una especie de variable identificada con un
# nombre específico (clave), así, podemos hacer "trabajos" sobre los elementos del diccionarios

Edades["Cristian"] += 1 
Edades

Edades["Cristian"] - Edades["Ximena"]

# Recorrido de un diccionarios a través de bucles.
# A diferencia de las listas y las tuplas, los diccionarios suelen recorrerse con un bucle for
# Esto debido a que como ya se mencionó no se maneja por índices sino por claves, esto es, elementos
# El bucle for nos ayuda a recorrer una estructura de datos por elementos

for Edad in Edades:
    print(Edad)

# En este esquema se van a imprimir las claves de los diccionarios, es decir, la variable para reccorrer
# los elementos va a guardar las claves, por esto, si queremos el valor (y no la clave), la manera de 
# acceder a ellos es

for Edad in Edades:
    print(Edades[Edad])

# Ahora, si deseamos ambos datos, entonces

for Edad in Edades:
    print(Edad,Edades[Edad])

# Existe un método especial para acceder a los elementos de un diccionario para combinar con el uso de un
# bucle for, este es items()

for Clave, Valor in Edades.items():
    print(Clave,Valor)

# Listas de diccionarios: podemos crear estructuras de datos avanzadas combinando listas y diccionarios
# Las listas se usan paera unir los diccionarios en un conjunto y los diccionarios para guardar los
# Los detalles de cada registro  

Afiliacion = [Edades]

Profesion = {"Jorge": "Contador", "Ximena": "Negocios Internacionales", "Johanna":"Profesora", "Dolly": "Comerciante", "Martina": "Estudiante", "Belen":"Estudiante", "Cristian": "Camarografo" }
Afiliacion.append(Profesion)
Ciudad = {"Jorge": "Bucaramanga", "Ximena": "Bogotá", "Johanna":"Medellín", "Dolly": "Cali", "Martina": "Bogotá", "Belen":"Bogotá", "Cristian": "Barranquilla" }
Afiliacion.append(Ciudad)
Estado = {"Jorge": "Activo", "Ximena": "Activo", "Johanna":"Activo", "Dolly": "Activo", "Martina": "Activo", "Belen":"Activo", "Cristian": "Inactivo" }
Afiliacion.append(Estado)
Tipo = {"Jorge": "Cotizante", "Ximena": "Cotizante", "Johanna":"Cotizante", "Dolly": "Beneficiario", "Martina": "Beneficiario", "Belen":"Beneficiario", "Cristian": "Cotizante" }
Afiliacion.append(Tipo)

# Ejercicio: imprimir los datos de cada diccionario, guardados en la lista, para cada una de las claves haciendo uso de bucle o bucles


