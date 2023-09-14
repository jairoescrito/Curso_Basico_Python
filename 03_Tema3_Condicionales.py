## Condicionales -if-

Numero = float(input("Escribe un número entero: "))
Residuo = Numero%2
if (Residuo == 0):
    print("El número que ingresaste es par")
else:
    print("El número que ingresaste no es par")


Num1 = int(input("Ingrese el primer número entero: "))
Num2 = int(input("Ingrese el segundo número entero: "))    

Res1 = Num1 % 2 
Res2 = Num2 % 2

if (Res1 == 0 and Res2 == 0):
    print("El primer y segundo número son pares")
elif (Res1 == 0 and Res2 != 0):
    print("El primer número es par y el segundo no es par")
elif (Res1 != 0 and Res2 == 0):
    print("El primer número no es par y el segundo número es par")
else:
    ("El primer y segundo número no son pares")
   
# Ejercicio 9: Ingresar dos números por consola y verificar
# 1) que los dos números sean mayores a 5
# 2) que el primero sea mayor a 5 y el segundo no
# 3) que el primero no sea mayor a 5 y el segundo si
# 4) que ninguno de los dos sea mayor a 5

# Ejercicio 10: Ingresar una frase por consola
# 1) Verificar si el tamaño del texto es superior a 10 caracteres
# 2) Verificar si la primera letra de la frase es una "A"

Frase = input("Ingrese un texto: ")

if (len(Frase) > 10):
    print("Mayor a 10")
else:
    print("Menor o igual a 10")

PrimerDigito = Frase[0]

if (PrimerDigito == "A"):
    print("La primera letra de la frase es una A")
else:
    print("La primera letra no es una A")