#Realizar un programa que solicite al usuario un número entero. Si el número ingresado
#es menor que 9, el programa deberá imprimir en pantalla todos los números 
#consecutivos comenzando desde ese valor inclusive, aumentando de a 1 en cada paso.

num = int(input("Ingrese un numero:"))

if num < 9:
    for i in range(num):
       print(i + 1)
    