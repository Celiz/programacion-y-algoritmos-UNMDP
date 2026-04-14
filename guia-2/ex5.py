#5. Realizar un programa que permita al usuario introducir cinco números y contar los
#números pares. Si el usuario no ingresó ningún par, mostrar un mensaje informandolo.

contador_pares = 0

#without for

num1 = int(input("Número 1: "))
if num1 % 2 == 0:
    contador_pares += 1

num2 = int(input("Número 2: "))
if num2 % 2 == 0:
    contador_pares += 1

num3 = int(input("Número 3: "))
if num3 % 2 == 0:
    contador_pares += 1

num4 = int(input("Número 4: "))
if num4 % 2 == 0:
    contador_pares += 1

num5 = int(input("Número 5: "))
if num5 % 2 == 0:
    contador_pares += 1


if contador_pares > 0:
    print("Cantidad de números pares:", contador_pares)
else:
    print("No se ingresaron números pares.")


