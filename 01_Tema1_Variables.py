"""
Created on Mon Jul  3 12:32:41 2023

@author: jairoescrito
"""

## 2.1 Variables ##
# Identificador que ocupa espacio en la memoria

Entero = 9

Flotante = 0.5 #esto es, variable de tipo número decimal
Cadena = "Esto es Python"
Caracter ="@"
Boleana = True
Otra_Boleana= False
Vacia = None # Una variable vacía para apartar un espacio en la memoria

# Verificar el tipo de variable y modificar la misma
type(Entero) 
Decimal = float(Entero)
type(Decimal)
Decimal # En python el separador decimal es el punto 

## 2.1.1 Detalles de las variables tipo cadena

len(Cadena) # Para conocer la cantidad de caracteres que tiene la cadena (incluye espacios)
Cadena[0] # Las cadenas tienen indices, en python el conteno SIEMPRE empieza en cero
Cadena[0:3] # Se seleccionan las posiciones de cero a 3 (no incluye el 3) en la cadena
Cadena[-1] # Se selecciona la primera letra de del final hacia el principio
Cadena[-3]

Palabra1 = "Hola Mundo"
Palabra2 = "Soy Python"
Palabra1+Palabra2
Palabra1+" "+Palabra2 # Concatenar

### 2.1.2 Entrada de datos y salida de datos ###
# Se incluye en el script una "orden" que nos permite intercatuar para ingresar datos
# para esto se usa la función input()

Dato = input("escribe cualquier dato: ") 

# Usar input tiene lógica si almacenamos ese dato a introducir en una variable, de lo contrario se van a perder apenas se ingresen
# Insertar datos de manera "manual" (a través de la consola), nos permite darle dinámica a nuestra lista de 
# instrucciones, los datos pueden ser ajustados conforme a las necesidades, por ejemplo convertir a texto, entero,
# decimal, etc

Dato = float(Dato) # Convertir a decimal
Dato = int(Dato) # Convertir a entero
Dato = str(Dato) # Convertir a texto

Numero=float(input("escribe un número entero o decimal: "))
print("El doble del número que escribiste es: ", Numero*2)

'Ejercicio 1: Solicitar por consola dos palabras, unirlas e imprimirlas'
'Ejercicio 2: Solicitar por consola dos números enteros, convertirlos a texto, unirlos' 
'concatenar, calcular el tamaño de la cadena, imprimirlo y luego imprimir la primera posición de la cadena'
