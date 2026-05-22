def mcd(a,b):
    while b:
        a,b = b, a%b
    return a

def mcm(a,b):
    return a*b//mcd(a,b)

a = int(input("ingrese el primer numero:"))
b = int(input("ingrese el segundo numero:"))


frase = input("ingrese una frase: ")

def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    count = 0
    for char in frase:
        if char in vocales:
            count += 1
    return count

print(f"el mcd de {a} y {b} es: {mcd(a,b)}")
print(f"el mcm de {a} y {b} es: {mcm(a,b)}")

print(f"la cantidad de vocales en la frase es: {contar_vocales(frase)}")
