## Ciclo While ##: "mientras se cumpla algo, haga esto"
# Iteraciones, variable iterativa

# Contar la cantidad de letras "o" en la frase 3
Frase_1 = "Hola Mundo"
Frase_2 = "Soy Python"
Frase_3 = Frase_1 + " " + Frase_2
Cantidad = 0
i = 0
len(Frase_3)
while (i<len(Frase_3)):
    Letra = Frase_3[i]
    if (Letra == "o"):
        Cantidad += 1 # Cantidad = Cantidad + 1
    i += 1
print("El número de 'o's' en la frase es de", Cantidad)


# Imprimir letra por letra de la que ingresa el usuario preguntandole si quiere continuar después de
# la impresión de cada letra
Palabra = input("Escriba una palabra: ")
Indice = 0
while (Indice < len(Palabra)):
    print("\n")
    print("La letra número",Indice+1," de la palabra ingresada es: ", Palabra[Indice])
    Seguir = input("¿imprimos la siguiente letra? reponde S o N: ")
    if (Seguir == "S"):       
        Indice += 1 #  es lo mismo que Indice = Indice + 1
    elif (Seguir == "N"):
        print("\nOk, eso es todo!")
        break
    else:
        print("\nLo siento, no entiendo la respuesta")
        break
else:
   print("\nEsas son todas las letras que podíamos imprimir")     

# / Slash
# \ Backslash

# Construir una palabra a partir de las letras que ingresa el usuario hasta que el usuario mencione que dese finalizar
i = 0
Palabra =""
while True:
    Letra = input("Escribe una letra (si no quieres escribir mas letras escribe 'fin' para terminar): ")
    if (Letra == "fin"):
        print ("\n Hasta aquí llegamos")
        print ("La palbra que construimos es: ", Palabra)
        break
    else:
        Palabra = Palabra + Letra

# Ejercicio 11: Hacer un bucle while infinito que imprima el cuadrado
# de un número que se ingrese por consola
# El ciclo debe seguir pidiendo números hasta tanto el usuario no le de
# una orden de finalizar

while True:
    Num = int(input("Ingresa un número entero (si quiere parar ingrese un 0):"))
    if (Num == 0):
        print("Fin")
        break
    else:
        print ("El cuadrado es: ", Num ** 2)