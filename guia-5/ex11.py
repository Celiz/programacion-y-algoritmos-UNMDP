"""Ejercicio 11.

Dadas las siguientes funciones recursivas, analizar el codigo de cada una y responder:
a) Que error logico o conceptual presenta la funcion?
b) Que ocurriria si se ejecuta el codigo tal cual esta escrito?
c) Reescriba la funcion corrigiendo el error para que logre su objetivo esperado.
"""

# FUNCION A: sumar todos los numeros enteros desde 1 hasta N.
def suma_hasta(n):
	if n > 0:
		return n + suma_hasta(n - 1)
	return 0


# FUNCION B: imprimir una cuenta regresiva desde N hasta 1.
def cuenta_regresiva(n):
	if n <= 0:
		return
	print(n)
	cuenta_regresiva(n - 1)


# FUNCION C: calcular la potencia de una base elevada a un exponente.
# Asuma que el exponente siempre sera mayor o igual a 0.
def potencia(base, exp):
	if exp == 0:
		return 1
	return base * potencia(base, exp - 1)


# Respuestas:
# a) Analisis de errores:
# - FUNCION A: el error logico era llamar a la funcion con el mismo n, lo que causaba recursion infinita.
# - FUNCION B: el error logico era no tener condicion de parada.
# - FUNCION C: no presenta errores logicos con exp >= 0.