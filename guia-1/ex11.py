# en 10m^2 se obtiene 200kg de trigo

lado = int(input("Ingrese el lado del terreno en metros: "))
altura = int(input("Ingrese la altura del terreno en metros: "))

area = lado * altura
trigo = (area / 10) * 200

print(f"En un terreno de {area}m^2 se obtiene {trigo}kg de trigo.")