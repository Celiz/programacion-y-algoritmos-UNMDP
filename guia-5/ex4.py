# 4. Dado el siguiente arreglo: [ G, A, F, B, D, H, E, C ], se desea ordenarlo alfabéticamente aplicando Selection Sort, Insertion Sort y Bubble Sort.
# a) Escribir el estado del arreglo al finalizar la tercera pasada completa en cada uno
# de los métodos.
# b) Observando los tres resultados anteriores, justifique brevemente: ¿En qué extremo
# o sector del arreglo concentra su ordenamiento inicial cada algoritmo?

def selection_sort(arr):
    """Ordena el arreglo in-place con Selection Sort e imprime 3 pasadas."""
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        if i == 2:  # Imprime después de la tercera pasada
            print(f"Después de la tercera pasada (Selection Sort): {arr}")

def insertion_sort(arr):
    """Ordena el arreglo in-place con Insertion Sort e imprime 3 pasadas."""
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        if i == 2:  # Imprime después de la tercera pasada
            print(f"Después de la tercera pasada (Insertion Sort): {arr}")

def bubble_sort(arr):
    """Ordena el arreglo in-place con Bubble Sort e imprime 3 pasadas."""
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if i == 2:  # Imprime después de la tercera pasada
            print(f"Después de la tercera pasada (Bubble Sort): {arr}")

arr_selection = ['G', 'A', 'F', 'B', 'D', 'H', 'E', 'C']
arr_insertion = arr_selection.copy()
arr_bubble = arr_selection.copy()

selection_sort(arr_selection)
insertion_sort(arr_insertion)
bubble_sort(arr_bubble)
