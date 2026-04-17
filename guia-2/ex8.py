# La conjetura de Collatz, tambiC)n conocida como conjetura 3n + 1, es uno de los
# problemas matemC!ticos sin resolver mC!s famosos.
# SegC:n esta conjetura, al tomar un nC:mero entero positivo mayor a 1 y aplicarle el
# siguiente procedimiento, siempre se termina llegando al nC:mero 1, sin importar con
# quC) nC:mero se comience:
# Si el nC:mero es par, se divide por 2.
# Si el nC:mero es impar, se multiplica por 3 y se le suma 1.
# Este proceso se repite una y otra vez con el nuevo valor que se obtiene.
# Realizar un programa que solicite al usuario un nC:mero entero positivo mayor a 1
# (validar este dato) y aplique la secuencia de Collatz paso a paso hasta llegar al nC:mero
# Debe mostrarse al final:
#   Cantidad total de pasos realizados hasta llegar a 1.
#   El nC:mero mC!s alto que apareciC3 en la secuencia.
#   Los 4 C:ltimos nC:meros que aparecen en la secuencia.

n = int(input("Ingrese un numero positivo mayor a 1:"))

while n <= 1:
    n = int(input("Error. Ingrese un numero positivo mayor a 1:"))

count_pasos = 0
maximo = n
ultimo1 = 0
ultimo2 = 0
ultimo3 = 0
ultimo4 = 0

while n != 1:

    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

    count_pasos += 1

    if n > maximo:
        maximo = n

    ultimo4 = ultimo3
    ultimo3 = ultimo2
    ultimo2 = ultimo1
    ultimo1 = n


print("Pasos: ", count_pasos)
print("Numero mas alto", maximo)
print("Ultimos 4 numeros", ultimo4, ultimo3, ultimo2, ultimo1)
