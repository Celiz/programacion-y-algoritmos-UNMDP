#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es un número primo o no.

primo = True

n = int(input("Ingrese un número enetero: "))

if n < 2:
    primo = False

for i in range(2, n):
    if n % i == 0:
        primo = False
        break

print(f"{n} es primo: {primo}")
