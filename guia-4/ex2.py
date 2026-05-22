def area_rectangulo(base, altura):
    return base * altura

base = int(input("ingrese la base del rectangulo:"))
altura = int(input("ingrese la altura del rectangulo:"))

print(f"el area del rectangulo es: {area_rectangulo(base, altura)}")