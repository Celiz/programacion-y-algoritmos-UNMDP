# Cargar el tamaño de los vectores
n = int(input("Ingrese el tamaño de los vectores: "))

# Inicializar los vectores
vector1 = []
vector2 = []
vector3 = []

# Cargar el primer vector
print("\nIngrese los elementos del primer vector:")
for i in range(n):
    numero = int(input(f"vector1[{i}] = "))
    vector1.append(numero)

# Cargar el segundo vector
print("\nIngrese los elementos del segundo vector:")
for i in range(n):
    numero = int(input(f"vector2[{i}] = "))
    vector2.append(numero)

# Generar el tercer vector con los máximos valores
print("\nGenerando el vector con los máximos valores...")
for i in range(n):
    maximo = max(vector1[i], vector2[i])
    vector3.append(maximo)

# Mostrar los resultados
print("\n--- RESULTADOS ---")
print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Vector 3 (máximos): {vector3}")
