p1 = int(input("Nota parcial 1: "))
p2 = int(input("Nota parcial 2: "))
p3 = int(input("Nota parcial 3: "))
practico = int(input("Nota práctico: "))


parciales_aprobados = 0
if p1 >= 4:
    parciales_aprobados += 1
if p2 >= 4:
    parciales_aprobados += 1
if p3 >= 4:
    parciales_aprobados += 1

promedio = (p1 + p2 + p3) / 3

todos_altos = False
if p1 >= 7 and p2 >= 7 and p3 >= 7:
    todos_altos = True

# Determinar estado
if todos_altos and practico >= 8 and promedio >= 9:
    print("Estado: Aprobado")
elif todos_altos and practico >= 8 and promedio >= 8:
    print("Estado: Promocionado")
elif parciales_aprobados >= 2 and practico >= 4:
    print("Estado: Regular")
else:
    print("Estado: Libre")


############################################
p1 = int(input("Nota parcial 1: "))
p2 = int(input("Nota parcial 2: "))
p3 = int(input("Nota parcial 3: "))
practico = int(input("Nota práctico: "))

parciales_aprobados = (p1 >= 4) + (p2 >= 4) + (p3 >= 4)

promedio = (p1 + p2 + p3) / 3

todos_altos = p1 >= 7 and p2 >= 7 and p3 >= 7

# Determinar estado
if todos_altos and practico >= 8 and promedio >= 9:
    estado = "Aprobado"
elif todos_altos and practico >= 8 and promedio >= 8:
    estado = "Promocionado"
elif parciales_aprobados >= 2 and practico >= 4:
    estado = "Regular"
else:
    estado = "Libre"

print("Estado:", estado)