estudiantes = [
    ("Ana", 7, 8),
    ("Juan", 6, 9),
    ("Maria", 8, 7),
    ("Pedro", 9, 6),
]


def calcular_promedio(estudiante):
    promedio = (estudiante[1] + estudiante[2]) / 2
    return estudiante[0], promedio


def aprobado(promedio):
    return promedio >= 6


def buscar_mayor(nombre, promedio, mayor_actual, nombre_actual):
    if promedio > mayor_actual:
        return promedio, nombre
    return mayor_actual, nombre_actual


promedios = []
aprobados = 0
mayor = 0
nombre_mayor = ""

for estudiante in estudiantes:
    nombre, promedio = calcular_promedio(estudiante)
    promedios.append((nombre, promedio))
    if aprobado(promedio):
        aprobados += 1
    mayor, nombre_mayor = buscar_mayor(nombre, promedio, mayor, nombre_mayor)

print("Aprobados: ", aprobados)
print("Mayor promedio: ", nombre_mayor)
print("Promedios: ", promedios)
