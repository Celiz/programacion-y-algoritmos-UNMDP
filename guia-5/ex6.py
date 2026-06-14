# Un sensor meteorológico registra la temperatura cada hora y guarda los datos en un
# arreglo. Por la naturaleza del clima, los valores tienden a subir gradualmente durante
# la mañana. Sin embargo, hubo una pequeña falla en el sensor y un par de registros
# contiguos quedaron invertidos, aunque el 95 % del arreglo ya está ordenado de forma
# natural.
# a) Implemente el algoritmo de Bubble Sort Optimizado (con bandera lógica de
# corte) para ordenar los registros de menor a mayor.
# b) Incorpore un contador que indique cuántas “pasadas completas” (ciclos externos)
# necesitó el algoritmo para finalizar. Compárelo mentalmente: ¿cuántas pasadas
# habría hecho la versión sin optimizar?

def bubble_sort_optimized(arr):
    n = len(arr)
    count_passes = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        count_passes += 1

        if not swapped:
            break

    return count_passes

temperaturas = [15, 56, 18, 20, 19, 21, 22, 23]
pasadas = bubble_sort_optimized(temperaturas)
print(f"Temperaturas ordenadas: {temperaturas}")
print(f"Pasadas completas necesarias: {pasadas}")