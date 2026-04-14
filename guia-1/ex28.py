persona = ()

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")
carrera = input("Ingresa tu carrera: ")

persona = (nombre, edad, ciudad, carrera)

# a) Mayor de edad
if persona[1] >= 18:
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")

# b) Carrera
if persona[3] == "Matemática" or persona[3] == "Ciencias de Datos":
    print("Excelente elección eligiendo", persona[3])
else:
    print("Carrera elegida:", persona[3])

# c) Ciudad
if persona[2] == "Mar del Plata":
    print(persona[0], "las materias se cursarán en la sede ubicada en Deán Funes 3350")
else:
    print("¡" + persona[0] + ", bienvenido a Mar del Plata!")