# Problema
# Desarrollar un programa con menú de opciones para operar sobre un archivo de
# texto que permita:
# a) Crear el archivo y grabar texto cargado por teclado (si existía, borrar su
# contenido).
# b) Abrir el archivo, mostrarlo y permitir agregar texto al final (si no existe, crearlo).
# c) Crear un nuevo archivo con una copia del contenido del archivo original.
# d) Truncar el archivo para que solo conserve las primeras cl líneas (valor
# ingresado por teclado).

def crear_archivo(nombre):
    """Crea un archivo y graba texto ingresado por teclado."""
    with open(nombre, 'w') as f:
        while True:
            linea = input("Ingrese una línea de texto (o 'FIN' para terminar): ")
            if linea.upper() == 'FIN':
                break
            f.write(linea + '\n')

def mostrar_agregar_texto(nombre):
    """Abre el archivo, lo muestra y permite agregar texto al final."""
    try:
        with open(nombre, 'r') as f:
            print("Contenido actual del archivo:")
            print(f.read())
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
    
    with open(nombre, 'a') as f:
        while True:
            linea = input("Ingrese una línea de texto para agregar (o 'FIN' para terminar): ")
            if linea.upper() == 'FIN':
                break
            f.write(linea + '\n')

def copiar_archivo(origen, destino):
    """Crea un nuevo archivo con una copia del contenido del archivo original."""
    try:
        with open(origen, 'r') as f_origen, open(destino, 'w') as f_destino:
            for linea in f_origen:
                f_destino.write(linea)
        print(f"Archivo '{origen}' copiado a '{destino}'.")
    except FileNotFoundError:
        print("Archivo de origen no encontrado.")


def truncar_archivo(nombre, lineas):
    """Trunca el archivo para que solo conserve las primeras cl líneas."""
    try:
        with open(nombre, 'r') as f:
            lineas_contenido = f.readlines()
        
        with open(nombre, 'w') as f:
            f.writelines(lineas_contenido[:lineas])
        print(f"Archivo '{nombre}' truncado a las primeras {lineas} líneas.")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Crear archivo y grabar texto")
        print("2. Mostrar archivo y agregar texto")
        print("3. Copiar archivo")
        print("4. Truncar archivo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del archivo a crear: ")
            crear_archivo(nombre)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del archivo a mostrar y agregar texto: ")
            mostrar_agregar_texto(nombre)
        elif opcion == '3':
            origen = input("Ingrese el nombre del archivo de origen: ")
            destino = input("Ingrese el nombre del archivo de destino: ")
            copiar_archivo(origen, destino)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del archivo a truncar: ")
            lineas = int(input("Ingrese la cantidad de líneas a conservar: "))
            truncar_archivo(nombre, lineas)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
