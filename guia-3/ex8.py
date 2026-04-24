#  Contar números pares e impares de la lista generada por [x for x in range(0,21)].

numeros = [x for x in range(0, 21)]

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")



    


