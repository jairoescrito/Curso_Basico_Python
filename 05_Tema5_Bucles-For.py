## Ciclo For ##
# Variable iterativa
# Elementos

Palabra = input("Escribe una palabra: ")
# Iterativa: cantidad de letras (len-tamaño) en la variable y sus posiciones (índices)
# Elementos: las letras cada una por aparte

# for por elementos
for x in Palabra:
    print(x)

# variable iterativa
# En python los rangos nunca toman el último valor
# (0,4): entre cero y 4, python toma los datos entre 0 y 3
len(Palabra)

# Por variable iterativa
j = 0
for j in range(len(Palabra)):
    print(Palabra[j])
    
# Ejercicio 12: Pedir por consola una palabra 
# Imprimir las letras de la palabra en orden inverso

Letras = input("Ingrese un texto: ")
len(Letras)-1
len(Letras)-2
# última posición: len(Letras)-1
# penúltima posición len(Letras)-2

i = 0
for i in range(len(Letras)):
    print(Letras[len(Letras)-(i+1)])
     
# Hola Mundo
Letras[-1]
Letras[-2]
Letras[-10]
len(Letras)
i = 0
for i in range(len(Letras)):
    print(Letras[-(i+1)])
        
# Ejercicio 13: Para los números de 1 a 10
# Imprimir el cuadrado + 1
# range(10)

for i in range(10):
    print(((i+1)**2)+1)
    

# Ejercicio 14: Imprimir los números de la secuencia fibonacci. La cantidad a imprimir debe solicitarse por consola

#F(1) -> 1
#F(2) -> 1,1
#F(3) -> 1,1,2
#F(4) -> 1,1,2,3 
#F(5) -> 1,1,2,3,5
#F(6) -> 1,1,2,3,5,8
#F(7) -> 1,1,2,3,5,8,13
#F(8) -> 1,1,2,3,5,8,13,21
#F(9) -> 1,1,2,3,5,8,13,21,34
#F(10) -> 1,1,2,3,5,8,13,21,34,55


Num = int(input("Ingrese el número para la serie Fibonacci: "))

# Usando tres variables
Fo = 0
F = 1 
for x in range(Num):
    if x <= 1:
        print ("El número",x+1,"de la secuencia Fibonacci es:",F)
        Fo = F
    else:
        Fn = Fo + F
        print("El número",x+1,"de la secuencia Fibonacci es:",Fn)
        Fo = F
        F = Fn      
# Usando dos variables       
Fa = 0
Fb = 1
for x in range(Num):
    if (x == 0) :
        print(Fb)
    else:
        Fb = Fb + Fa
        Fa = Fb - Fa
        print(Fb)