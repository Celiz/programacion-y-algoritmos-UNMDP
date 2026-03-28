tupla = input("Ingrese una tupla de números separados por comas: ")
tupla = tuple(map(int, tupla.split(",")))   
print("La tupla ingresada es:", tupla * 3)
