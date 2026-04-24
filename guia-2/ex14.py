# Realice un programa que permita calcular el promedio de 1000 números aleatorios
# generados en el rango de [0, 100000].

import random

suma =0
promedio = 0
for i in range(1000):
        numero = random.randint(0, 100000)
        suma += numero
        promedio = suma / 1000
print("El promedio de los 1000 números aleatorios es: ", promedio)

    
        


