# Escriba un programa que solicite una contraseña y la vuelva a solicitar hasta que las
# dos contraseñas coincidan, con un límite de tres peticiones.

MAX_INTENTOS = 3
contrasena = input("Ingrese una contraseña: ")

for intento in range(1, MAX_INTENTOS + 1):
	confirmacion = input("Repita la contraseña: ")

	if contrasena == confirmacion:
		print("Contraseña confirmada.")
		break

	print("Las contraseñas no coinciden.")

	if intento == MAX_INTENTOS:
		print("Se alcanzó el límite de intentos.")


