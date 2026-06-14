# Problema de las Ocho Reinas con Backtracking (todas las soluciones)
#
# rc[col] = fila en la que ubicamos la reina de la columna "col"
# qr[fil] = True si la fila "fil" está libre (no tiene reina)
# qid[k] = True si la diagonal inversa k está libre
# qnd[k] = True si la diagonal normal k está libre

def intend(col):
    global rc, qr, qid, qnd, soluciones, contador

    fil = -1

    while fil != 7:
        fil += 1

        di = col + fil         # diagonal inversa
        dn = (col - fil) + 7   # diagonal normal

        if qr[fil] and qid[di] and qnd[dn]:
            rc[col] = fil
            qr[fil] = qid[di] = qnd[dn] = False

            if col < 7:
                intend(col + 1)
                qr[fil] = qid[di] = qnd[dn] = True
            else:
                contador += 1
                soluciones.append(rc.copy())
                print(f"Solución {contador}:")
                print("rc (fila de cada reina por columna):", rc.copy())
                print()
                mostrar_tablero()
                print()
                qr[fil] = qid[di] = qnd[dn] = True


def mostrar_tablero():
    for fil in range(8):
        fila = ""
        for col in range(8):
            fila += " R " if rc[col] == fil else " . "
        print(fila)


def main():
    global rc, qr, qid, qnd, soluciones, contador

    rc = [-1] * 8
    qr = [True] * 8
    qid = [True] * 15
    qnd = [True] * 15
    soluciones = []
    contador = 0

    print("Problema de las Ocho Reinas: Todas las soluciones con Backtracking")
    print()

    intend(0)

    print(f"Total de soluciones encontradas: {contador}")


if __name__ == "__main__":
    main()
