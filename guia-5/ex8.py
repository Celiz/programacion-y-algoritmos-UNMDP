# El municipio ha realizado un censo y almacenó las edades de 15.000 habitantes en un
# arreglo. El arreglo está completamente desordenado, con valores pequeños y grandes
# mezclados aleatoriamente de principio a fin.
# a) Escriba un programa que implemente el algoritmo de Shellsort para ordenar
# estas edades. Utilice la secuencia de saltos de la forma h = 3 · h + 1.
# b) Para demostrar cómo las distancias se van achicando, el programa debe imprimir
# en pantalla únicamente el valor de la distancia h cada vez que comienza un nuevo
# ciclo de agrupamiento, hasta llegar al paso final de h = 1.

def shell_sort(arr):
    n = len(arr)
    h = 1

    # Genera la secuencia de saltos h = 3 * h + 1
    while h < n // 3:
        h = 3 * h + 1

    while h >= 1:
        print(f"Distancia h: {h}")  # Imprime la distancia h al comenzar un nuevo ciclo

        for i in range(h, n):
            temp = arr[i]
            j = i

            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h

            arr[j] = temp

        h //= 3  # Reduce la distancia para el siguiente ciclo


edades = [34, 12, 45, 22, 9, 56, 18, 27, 3, 40, 29, 15, 8, 50, 19]
shell_sort(edades)

print(f"Edades ordenadas: {edades}")