# Usted es el encargado del sistema de un banco. Al final del día, recibe dos lotes de
# transacciones (identificadas por un ID numérico único):
# Lote A: Contiene 50 transacciones realizadas en la última hora. Debido a la
# latencia de la red, están completamente desordenadas.

# Lote B: Contiene la base de datos histórica con 500.000 transacciones acumuladas
# en el mes. Este lote ya se encuentra rigurosamente ordenado de menor a
# mayor por ID.
# Se le solicitan dos tareas urgentes: ordenar el Lote A de menor a mayor, y verificar si
# el ID 984501 se encuentra registrado dentro del masivo Lote B.
# a) Seleccionar el método de ordenamiento más adecuado para el Lote A y escriba su implementación. Justificar brevemente por qué lo eligió frente a las otras
# alternativas directas o compuestas.
# b) Seleccionar el método de búsqueda más eficiente para encontrar el ID en el Lote
# B y escribir su implementación. ¿Por qué utilizar una búsqueda secuencial sería
# una mala decisión en este caso?

def selection_sort(arr):
    """Ordena el arreglo in-place con Selection Sort."""
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Lote A: 50 transacciones desordenadas
lote_a = [23, 5, 12, 45, 3, 34, 8, 19, 27, 1, 14, 9, 30, 17, 6, 11, 22, 4, 28, 2, 10, 16, 7, 13, 20, 18, 24, 26, 15, 29, 21, 25, 31, 32, 33, 36, 35, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50]

# Lote B: 500.000 transacciones ordenadas
lote_b = list(range(1, 500001))

# a) Ordenar el Lote A
selection_sort(lote_a)
print(f"Lote A ordenado: {lote_a}")

# b) Verificar si el ID 984501 se encuentra en el Lote B
id_to_find = 984501
found = binary_search(lote_b, id_to_find)
print(f"ID {id_to_find} encontrado en Lote B: {found}")
