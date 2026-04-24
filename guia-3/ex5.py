# Dada una lista de números ‘[5, 2, 0, 7, 9,-2,8]‘, insertar los elementos 10 y 11, despues
# del 2, desplazando al resto

numeros = [5, 2, 0, 7, 9, -2, 8]
numeros.insert(2, 10)  # Insertar 10 después del 2 (índice 1)
numeros.insert(3, 11)  # Insertar 11 después del 10 (índice 2)

print(numeros)