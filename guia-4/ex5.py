#Desarrollar una función que reciba los coeficientes de un polinomio de grado 2, resuelva
#el mismo y devuelva None si no tiene solucion real, y si la tiene devuelva las soluciones

def resolver_polinomio(a,b,c):
    soluciones = []

    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    else:
        soluciones.append((-b + discriminante**0.5) / (2*a))
        soluciones.append((-b - discriminante**0.5) / (2*a))
    return soluciones


a = int(input("ingrese el coeficiente a:"))
b = int(input("ingrese el coeficiente b:"))
c = int(input("ingrese el coeficiente c:"))


print(resolver_polinomio(a,b,c))