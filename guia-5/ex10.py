# Escribir un programa que genere un única lista de 5000 números enteros aleatorios,
# luego:
# a) Importe los módulos time (para medir tiempo), tracemalloc (para medir el
# consumo de memoria).
# b) Utilizar los algoritmos de ordenamiento vistos para ordenar la lista generada.
# IMPORTANTE: utilizar siempre una copia de la lista original desordenada para
# cada algoritmo.
# c) Envuelvar la ejecución de cada algoritmo con las funciones de medición de tiempo
# y memoria. Registre el tiempo transcurrido (en segundos) y el pico máximo de
# memoria asignada (peak memory).
# d) Construya una pequeña tabla comparativa con los resultados obtenidos y concluya: ¿Qué algoritmo fue el más rápido? ¿Hubo diferencias significativas en el uso
# de la memoria entre ellos?

import time
import tracemalloc
import random

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
    
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def measure_time_and_memory(sort_func, arr):
    tracemalloc.start()
    start_time = time.time()
    
    sort_func(arr)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return end_time - start_time, peak

# Generar una lista de 5000 números enteros aleatorios
original_list = [random.randint(1, 10000) for _ in range(5000)]
# Medir tiempo y memoria para cada algoritmo
selection_time, selection_memory = measure_time_and_memory(selection_sort, original_list.copy())
insertion_time, insertion_memory = measure_time_and_memory(insertion_sort, original_list.copy())
bubble_time, bubble_memory = measure_time_and_memory(bubble_sort, original_list.copy())


# Imprimir resultados
print(f"Selection Sort: Tiempo = {selection_time:.4f} segundos, Memoria = {selection_memory} bytes")
print(f"Insertion Sort: Tiempo = {insertion_time:.4f} segundos, Memoria = {insertion_memory} bytes")
print(f"Bubble Sort: Tiempo = {bubble_time:.4f} segundos, Memoria = {bubble_memory} bytes")


