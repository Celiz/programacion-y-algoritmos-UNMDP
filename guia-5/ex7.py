# En un juego de naipes, un jugador recibe cartas una por una. A medida que toma
# una nueva carta, la inserta en su mano de forma tal que siempre mantiene sus cartas
# ordenadas.
# a) Simule este proceso utilizando la lógica de Insertion Sort. Comience con un
# arreglo vacío.
# b) El programa debe pedirle al usuario que ingrese 5 números enteros por teclado,
# uno por uno. Cada vez que se ingresa un número, el algoritmo debe insertarlo en
# la posición correcta dentro del arreglo y mostrar por pantalla cómo va quedando
# “la mano” ordenada tras cada nueva carta.

def insertion_sort(arr, new_card):
    """Inserta new_card en arr manteniendo el orden."""
    arr.append(new_card)  # Agrega la nueva carta al final
    i = len(arr) - 2  # Comienza a comparar desde el penúltimo elemento

    while i >= 0 and arr[i] > new_card:
        arr[i + 1] = arr[i]  # Desplaza el elemento hacia la derecha
        i -= 1

    arr[i + 1] = new_card  # Inserta la nueva carta en su posición correcta
    
mano = []
for _ in range(5):
    carta = int(input("Ingrese un número entero (carta): "))
    insertion_sort(mano, carta)
    print(f"Mano ordenada: {mano}")