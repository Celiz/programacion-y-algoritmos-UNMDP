# Una profesora de matemáticas tiene un programa que toma un número entero n e
# imprime el cubo de cada número desde 1 hasta n, mostrando por pantalla el siguiente
# mensaje “El cubo del número x es el número y”, donde x es un número en el rango
# dado e y el resultado de x
# 3
# .
# a) Realizar la identificación de resultados, datos y procesos, diagrama de flujo y
# pseudocódigo.
# b) Realizar el programa en Python

n = int(input("Introduce un número entero: "))
for x in range(1, n + 1):
    y = x ** 3
    print(f"El cubo del número {x} es el número {y}.")