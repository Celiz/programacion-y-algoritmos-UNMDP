#Se debe registrar la asistencia de una clase y se necesita saber si algún alumno llegó
#tarde. ¿Cómo se puede utilizar una bandera en este caso? ¿Por qué sería más eficiente
#que usar un contador?

llego_tarde = False

cantidad_alumnos = int(input("Cantidad de alumnos: "))

for i in range(1, cantidad_alumnos + 1):
	nombre = input(f"Nombre del alumno {i}: ")
	respuesta = input(f"¿{nombre} llegó tarde? (si/no): ").strip().lower()

	if respuesta == "si":
		llego_tarde = True
		break

if llego_tarde:
	print("Sí, al menos un alumno llegó tarde.")
else:
	print("No, ningún alumno llegó tarde.")


