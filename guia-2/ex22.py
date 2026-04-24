# Dada la siguiente tupla de números (10, 15, 13, 85, 234, 155, 0, 2, 23, 44, 357, 333, 456, 501, 49),
# recorrerla e imprimir aquellos que cumplan las siguientes condiciones:
# El número debe ser divisible por cinco.
# Si el número es mayor que 150, omitirlo y pasar al siguiente.
# Si el número es mayor que 500, detener completamente el ciclo.

numeros = (10, 15, 13, 85, 234, 155, 0, 2, 23, 44, 357, 333, 456, 501, 49)
for numero in numeros:
    if numero > 500:
        print("Número mayor que 500 encontrado. Deteniendo el ciclo.")
        break
    if numero > 150:
        continue
    if numero % 5 == 0:
        print(numero)
