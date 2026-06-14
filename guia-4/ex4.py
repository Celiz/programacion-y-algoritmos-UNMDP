def superposicion(lista1, lista2):
    flag = False
    for i in lista1:
        for j in lista2:
            if i==j:
                flag = True
    return flag

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 2, 10]

print(superposicion(lista1, lista2))
    