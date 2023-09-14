#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:40:50 2023

@author: jairoescrito
"""
# Se pueden aplicar diferentes "funciones" para manupular los datos que se tienen en un diccionarios
# Estos funcionan casi siempre a través de las claves


Edades = {"Jorge": 72, "Ximena": 35, "Johanna":39, "Dolly": 65, "Martina": 7, "Belen":3}

Afiliacion = [Edades]

Profesion = {"Jorge": "Contador", "Ximena": "Negocios Internacionales", "Johanna":"Profesora", "Dolly": "Comerciante", "Martina": "Estudiante", "Belen":"Estudiante", "Cristian": "Camarografo" }
Afiliacion.append(Profesion)
Ciudad = {"Jorge": "Bucaramanga", "Ximena": "Bogotá", "Johanna":"Medellín", "Dolly": "Cali", "Martina": "Bogotá", "Belen":"Bogotá", "Cristian": "Barranquilla" }
Afiliacion.append(Ciudad)
Estado = {"Jorge": "Activo", "Ximena": "Activo", "Johanna":"Activo", "Dolly": "Activo", "Martina": "Activo", "Belen":"Activo", "Cristian": "Inactivo" }
Afiliacion.append(Estado)
Tipo = {"Jorge": "Cotizante", "Ximena": "Cotizante", "Johanna":"Cotizante", "Dolly": "Beneficiario", "Martina": "Beneficiario", "Belen":"Beneficiario", "Cristian": "Cotizante" }
Afiliacion.append(Tipo)


# get() Buscar un valor a partir de su clave, funciona con dos parámetros 1) La clave y 2) la respuesta que se debe imprimir en caso tal la clave
# Entregada no se encuentre en el diccionario
Estado.get("Jorge", "No Existe")

# keys() entrega el listado de las claves de un diccionario
Estado.keys()

# values() Entrega una lista de los valores del diccionario (sin las claves)
Estado.values()

# items() proporciona la lista de los elementos "(clave,valor)" del diccionario
Estado.items()

#pop() al igual que en las listas sirve para extraer un valor (borrándolo). Funciona con dos parámetros 1) La clave y 2) la respuesta que se debe imprimir en caso tal la clave
Estado.pop("Cristian", "No Existe")

#clear() permite borrar todos los registros de un diccionario, lo deja vacío.
Estado.clear()


# 06/01/2017	Juan	Medellín	Correa	15	$ 235.724	$ 3.535.860
# 05/02/2017	Juan	Bogotá	Zapatos	25	$ 378.083	$ 9.452.075
# 18/09/2017	Juan	Medellín	Pantalón	23	$ 249.298	$ 5.733.854
# 12/08/2019	Alejandra	Medellín	Correa	19	$ 124.171	$ 2.359.249
# 11/11/2019	Alejandra	Pereira	Correa	4	$ 423.654	$ 1.694.616
# 20/03/2018	Alejandra	Bogotá	Camisa	17	$ 98.136	$ 1.668.312
# 30/09/2018	Mateo	Cali	Blusa	14	$ 242.978	$ 3.401.692
# 17/01/2019	Mateo	Manizales	Pantalón	28	$ 138.037	$ 3.865.036
# 10/05/2017	Mateo	Medellín	Correa	20	$ 112.327	$ 2.246.540

# Ejercicio: Crear una función que me permita hacer una lista de diccionarios que guarde 
# los registros del listado de ventas entregado
# Se debe digitar cada uno de los datos de las 9 ventas por consola como si se estuviese llenando una base de datos
# Se deben usar las siguientes claves: "Fecha", "Agente", "Ciudad", "Articulo", "Cantidad", "Valor Unitario", "Valor Total"
# Entregar el valor total de ventas
# El valor de las ventas por ciudad
# El valor de las ventas por asesor

# Crear diccionarios a partir de dos listas

Dias = ["lunes", "martes","miercoles", "jueves", "viernes","sábado","domingo"]
Menu = ["Sancocho de Gallina","Chuleta Valluna", "Badeja Paisa", "Ajiaco", "Cocido Boyacense", "Lechona", "Cuy Asado"]

Carta = {Dias:Menu for (Dias,Menu) in zip(Dias,Menu)}
# La función zip toma en elemento (del mismo índice) de cada lista y lo convierte en una tupla
# La versión abreviada del bucle for recorre todos los elementos de las listas y los convierte en puplas, los elementos de la tupla los usa para crear "clave:valor" en el diccionario
Carta

# Ejercicio Crear dos listas, una con los nombres de los meses en inglés y otra con los nombres en español
# Crear un diccionario con las dos claves teniendo como clave el nombre en español




