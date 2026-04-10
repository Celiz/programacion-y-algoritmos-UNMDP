temperatura = float(input("Ingrese temperatura: "))

aux = int(input("1 para Kelvins | 2 para Farenheint"))


if aux == 1:
    print(temperatura + 273.15, "K")
elif aux == 2:
    print(temperatura * (9/5) + 32, "F")

