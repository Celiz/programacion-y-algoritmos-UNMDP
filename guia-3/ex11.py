# Lista de números a ordenar
numeros = [15, 17, 7, -3, 3, 4, 1, 5, 0, 6, 11]

# Obtener la cantidad de elementos en la lista
n = len(numeros)

# Bucle externo: controla el número de pasadas necesarias para ordenar
# Se ejecuta n-1 veces porque en la última pasada solo quedan 1 o 2 elementos
for i in range(n-1):
    # Bucle interno: compara elementos adyacentes
    # En cada pasada, n-i-1 reduce el rango porque los elementos más grandes
    # ya están en su posición final
    for j in range(0, n-i-1):
        # Comparar dos elementos adyacentes
        if numeros[j] > numeros[j+1]:
            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            # (Intercambio simultáneo usando tuplas en Python)
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

# Mostrar la lista ordenada en pantalla
print(numeros)
