# El comité organizador de un torneo de atletismo necesita ordenar las puntuaciones
# finales de los competidores. Dado que solo les interesa premiar rápido a los mejores,
# necesitan un método que garantice que, en las primeras pasadas, los puntajes más altos
# ya queden ubicados en sus posiciones definitivas.
# a) Implemente el algoritmo de Selection Sort para ordenar una lista de puntajes
# de mayor a menor.
# b) Modifique el algoritmo para que reciba un parámetro K. El programa no debe ordenar toda la lista, sino detenerse exactamente después de la pasada K e imprimir
# los K mejores puntajes ya asegurados en el inicio del arreglo.

def selection_sort(arr, k):
    n = len(arr)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:  # Cambia a > para ordenar de mayor a menor
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

        if i == k - 1:  # Detiene después de la pasada K
            print(f"Después de la pasada {k}: {arr[:k]} (K mejores puntajes)")
            break

puntajes = [85, 92, 78, 90, 88, 95, 80]
k = 6
selection_sort(puntajes, k)
