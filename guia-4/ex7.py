# Análisis exploratorio de datos: Promedio (o Media), Moda y la Mediana.

estaturas = [
    1.8, 1.75, 1.70, 1.68, 1.55, 1.68, 1.62, 1.63, 1.74,
    1.68, 1.60, 1.55, 1.70, 1.75, 1.63, 1.62,
]


def calcular_media(muestra):
    n = len(muestra)
    suma = 0
    for i in range(n):
        suma += muestra[i]
    return suma / n


def contar_arriba_debajo(muestra, prom):
    cont1 = cont2 = 0
    for i in range(len(muestra)):
        if muestra[i] >= prom:
            cont1 += 1
        else:
            cont2 += 1
    return cont1, cont2


def ordenar(muestra):
    ordenada = muestra.copy()
    n = len(ordenada)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ordenada[j] > ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]
    return ordenada


def calcular_mediana(muestra_ordenada):
    n = len(muestra_ordenada)
    if n % 2 == 0:
        elemento1 = muestra_ordenada[int(n / 2)]
        elemento2 = muestra_ordenada[int((n / 2) - 1)]
        return (elemento1 + elemento2) / 2
    index_mediana = int(n / 2)
    return muestra_ordenada[index_mediana]


def armar_contador(muestra_ordenada):
    contador = [[muestra_ordenada[0], 0]]
    posicion = 0
    for e in muestra_ordenada:
        if contador[posicion][0] == e:
            contador[posicion][1] += 1
        else:
            contador.append([e, 1])
            posicion += 1
    return contador


def calcular_moda(contador):
    max_repetidos = 0
    for c in contador:
        if max_repetidos < c[1]:
            max_repetidos = c[1]
    modo = []
    for c in contador:
        if max_repetidos == c[1]:
            modo.append(c)
    return modo


n = len(estaturas)
print("Cantidad de Muestras: ", n)

prom = calcular_media(estaturas)
cont1, cont2 = contar_arriba_debajo(estaturas, prom)

print("Media: ", round(prom, 2))
print("Cantidad x Arriba o igual: ", cont1)
print("Cantidad x Debajo: ", cont2)

estaturas_ordenadas = ordenar(estaturas)
mediana = calcular_mediana(estaturas_ordenadas)

print("Mediana:", mediana, " (separa la muestra en dos)")

contador = armar_contador(estaturas_ordenadas)
modo = calcular_moda(contador)

print("Moda (los valores mas repetidos - no necesariamente unicos)")
print(modo)
