#5. Realizar un programa que permita al usuario introducir cinco números y contar los
#números pares. Si el usuario no ingresó ningún par, mostrar un mensaje informandolo.
contador_pares = 0

for i in range(5):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        contador_pares += 1

print(contador_pares, "numeros pares")    