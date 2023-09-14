"""
Created on Mon Jul  3 18:15:33 2023

@author: jairoescrito
"""

# Operadores ariméticos

Entero = 5
Flotante = 9.5

# suma "+"
Suma = Entero + Flotante
# resta "-"
Resta = Flotante - Entero
# multiplicación "*"
Multiplicacion = Flotante*Entero
# división "/"
Division = Flotante/Entero
# modulo "%" (el residuo de una división)
Otro_Numero = 4
Modulo = Entero % Otro_Numero
# Potencia "**"
Potencia = Flotante ** Entero
Raiz_Cuadrada = Entero ** (1/2)
Raiz_Cubica = Entero ** (1/3)

# Ejercicio 3: solicitar por consola 2 números decimales
# dividirlos, imprimir el resultado
'input'
'print'
Decimal1 = float(input("Decimal 1: "))
Decimal2 = float(input("Decimal 2: "))
Total = Decimal1/Decimal2
print(Total)

#Ejercicio 4: solicitar un número entero por consola, calcular modulo 2
#imprimir el residuo
'%'
NumeroEntero = int(input("Número entero: "))
Modulo = NumeroEntero % 2
print(Modulo)

#Ejercicio 5: imprimir el resultado de la raíz cuadrada de 16
Numero1 =int(input("Raiz Cuadrada: "))
RaizCuadrada = Numero1 ** (1/2)
print(RaizCuadrada)

# Operadores relacionales

# Igual - Identico "=="
Igual = Flotante == Entero
print(Igual)
# Diferente, Distinto, No es igual "!="
Diferente = Flotante != Entero
print(Diferente)
# Mayor ">" y mayor o igual ">="
Mayor = Entero > Flotante
MayorIgual = Flotante >= Entero
# Menor "<" y menor o igual "<="
Menor = Entero < Flotante
MenorIgual = Flotante <= Entero
# Negación lógica "not"
print(Menor)
Negacion = not(Menor) 
print(Negacion)
# Conjunción lógica "and"
Mayor and Menor
# Distunción lógico "or"
Mayor or Menor

# Ejercicio 6: solicitar por consola dos números
# verificar si son diferentes (imprimir el resultado
# de la comparación)

Numero1 = int(input("primer número: "))
Numero2 = int(input("segundo número: "))
Diferentes = Numero1 != Numero2
print(Diferentes)

# Ejericicio 7: solicitar otros dos números por consola,
# 1) calcular el residuo de los números del ejercicio 6
# 2) calcular el residuo de los dos últimos números solicitados
# 3) verificar si el residuo de los dos primeros es menor que el
# residuo de los dos segundos. Usar "%"

Numero3 = int(input("tercer número: "))
Numero4 = int(input("cuarto número: "))
Residuo1 = Numero1 % Numero2
Residuo2 = Numero3 % Numero4
Menor = Residuo1<Residuo2
