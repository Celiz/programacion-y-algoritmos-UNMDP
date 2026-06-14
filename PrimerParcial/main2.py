# Empresa: 3 sucursales, 4 trimestres. Ventas >= 0.
# Totales anuales, sucursal con mayor total, listado completo.

SUCURSALES = 3
TRIMESTRES = 4

sucursales = []
ventas = []

for i in range(SUCURSALES):
    nombre = input(f"Ingrese el nombre de la sucursal {i + 1}: ")
    sucursales.append(nombre)

    fila = []
    for j in range(TRIMESTRES):
        while True:
            valor = int(
                input(
                    f"Ventas de {nombre} en el trimestre {j + 1} (>= 0): "
                )
            )
            if valor >= 0:
                fila.append(valor)
                break
            print("Error: el valor debe ser mayor o igual a cero. Reintente.")

    ventas.append(fila)

totales_anuales = []
for i in range(SUCURSALES):
    total = sum(ventas[i])
    totales_anuales.append(total)

print()
print("--- Total anual por sucursal ---")
for i in range(SUCURSALES):
    print(f"{sucursales[i]}: {totales_anuales[i]}")

indice_mayor = 0
for i in range(1, SUCURSALES):
    if totales_anuales[i] > totales_anuales[indice_mayor]:
        indice_mayor = i

print()
print(
    f"Sucursal con mayor total anual: {sucursales[indice_mayor]} "
    f"({totales_anuales[indice_mayor]})"
)

print()
print("--- Ventas cargadas (sucursal x trimestre) ---")
for i in range(SUCURSALES):
    for j in range(TRIMESTRES):
        print(
            f"{sucursales[i]} | Trimestre {j + 1}: {ventas[i][j]}"
        )
