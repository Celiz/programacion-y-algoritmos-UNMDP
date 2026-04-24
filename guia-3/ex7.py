#  Invertir el orden de los elementos en la lista [1, 2, 3, 5, 7, 9, 11] sin usar métodos nativos
# de Python.

numeros = [1, 2, 3, 5, 7, 9, 11]
numeros_invertidos = []

for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])

print(numeros_invertidos)


