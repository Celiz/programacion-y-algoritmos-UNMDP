# a) Escribir un programa iterativo.
def h_iterativo(n):
    result = 1
    for _ in range(n):
        result = result + result
    return result

# b) Escribir un programa recursivo.
def h_recursivo(n):
    if n == 0:
        return 1
    # Calculamos h(n-1) una sola vez para evitar la complejidad exponencial O(2^N)
    ant = h_recursivo(n - 1)
    return ant + ant

