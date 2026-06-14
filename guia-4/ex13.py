# Desarrollar una función que convierta de Fahrenheit a Celsius o a Kelvin; de forma tal

# que si el usuario de la misma no aclara cual debe ser el formato de salida, el mismo

# sea Celsius.

def convertir_temp(temp, unidad="C"):

    if unidad == "K":

        return (temp - 32) * 5/9 + 273.15

    return (temp - 32) * 5/9



temp = float(input("Ingrese la temperatura en Fahrenheit: "))

unidad = input("Unidad de salida (C o K, Enter = Celsius): ").strip().upper()

print(convertir_temp(temp, unidad))


