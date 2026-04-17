#Un profesor quiere estudiar las de notas de un curso. Un programa brindado pir el
#colegio pide al docente que ingrese notas (entre 1 y 10,-1 para finalizar). Al terminar,
#mostrará:

#La cantidad de notas aprobadas (mayores o iguales a 6).
#La cantidad de notas desaprobadas.
#El promedio de todas las notas

count_aprobados, count_desaprobados, suma, cantidad = 0,0,0,0

nota = int(input("Ingrese nota (-1 para terminar)"))

while nota != -1: 
    if nota < 6:
        count_desaprobados += 1
    else:
        count_aprobados += 1
    suma += nota
    cantidad += 1
    nota = int(input("Ingrese nota (-1 para terminar)"))

promedio = suma/cantidad

print("Aprobados: ", count_aprobados)
print("Desaprobados: ", count_desaprobados)
print("Promedio: ", promedio)


    
    
    
    