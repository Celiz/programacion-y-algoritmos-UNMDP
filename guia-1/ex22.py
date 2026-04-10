palabra = input("ingrese una palabra: ")

largo = len(palabra)

asteriscos = "*" * (largo - 2)

encriptada = palabra[0] + asteriscos + palabra[-1]

print("palabra encriptada: ", encriptada)