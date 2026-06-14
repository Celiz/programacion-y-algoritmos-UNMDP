# Considerar el siguiente arreglo desordenado: [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]. Aplique el
# algoritmo de ordenamiento por Selección Directa (Selection Sort) y escriba el estado
# exacto del arreglo al finalizar la primera, la segunda y la tercera pasada del ciclo
# principal.

def selection_sort(arr):
    """Ordena el arreglo in-place con Selection Sort e imprime 3 pasadas."""
    n = len(arr)

    for i in range(n):
        # Supone que la posicion actual es el minimo
        min_index = i

        for j in range(i + 1, n):
            # Busca el minimo en la parte no ordenada
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambia el minimo encontrado con la posicion actual
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Reporta el estado del arreglo en las tres primeras pasadas
        if i == 0:
            print(f"Después de la primera pasada: {arr}")
        elif i == 1:
            print(f"Después de la segunda pasada: {arr}")
        elif i == 2:
            print(f"Después de la tercera pasada: {arr}")


arr = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]

# Ejecuta el ordenamiento y muestra las tres primeras pasadas
selection_sort(arr)