# Con acumulador (estilo clase 5)
t1 = int(input("Temperatura 1: "))
suma = 0
suma = suma + t1

t2 = int(input("Temperatura 2: "))
suma = suma + t2

t3 = int(input("Temperatura 3: "))
suma = suma + t3

t4 = int(input("Temperatura 4: "))
suma = suma + t4

promedio = suma / 4
print("Promedio:", promedio)
print("Máxima:", max(t1, t2, t3, t4))
print("Mínima:", min(t1, t2, t3, t4))