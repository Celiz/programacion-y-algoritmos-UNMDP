# Considerar el código del ejercicio anterior. Se pide aplicarlo a la siguiente lista [x for xin range(2,22,2)]. 
# ¿Tiene sentido?. Justificar.

numeros = [x for x in range(2, 22, 2)]
pares = 0
impares =0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

#