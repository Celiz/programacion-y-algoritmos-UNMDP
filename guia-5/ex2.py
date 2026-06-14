# Crear un programa que modele un sistema de becas para estudiantes. Se deberá cargar
# los siguientes datos de n estudiantes:
# Legajo
# Nombre
# Promedio
# Carrera
# Luego, el programa deberá:
# Mostrar los datos de aquellos alumnos cuyo promedio sea mayor o igual a 8.
# Calcular y mostrar el promedio general de alumnos.

estudiantes = []
cantidad_estudiantes = int(input("ingrese la cantidad de estudiantes: "))


def cargar_datos():
    for i in range(cantidad_estudiantes):
        legajo = int(input("Ingrese el legajo del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        promedio = float(input("Ingrese el promedio del estudiante: "))
        carrera = input("Ingrese la carrera del estudiante: ")
        estudiantes.append((legajo, nombre, promedio, carrera))

def mostrar_datos():
    print("\nEstudiantes con promedio mayor o igual a 8:")
    for estudiante in estudiantes:
        if estudiante[2] >= 8:
            print(f"Legajo: {estudiante[0]}, Nombre: {estudiante[1]}, Promedio: {estudiante[2]}, Carrera: {estudiante[3]}")

def calcular_promedio_general():
    promedio = sum(estudiante[2] for estudiante in estudiantes) / len(estudiantes)
    return promedio

def main():
    cargar_datos()
    mostrar_datos()
    print("Promedio general de alumnos:", calcular_promedio_general())
    
main()