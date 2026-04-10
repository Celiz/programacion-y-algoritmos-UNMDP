import random

paciente1 = (10, "Juan perez", 30, "Diabetes")
paciente2 = (11, "Maria Gomez", 19, "Hipotiroidismo")
paciente3 = (12, "Jorge Gonzales", 39, "insuficiencia cardíaca")
paciente4 = (13, "Juana Garcia", 42, "escoliosis")
paciente5 = (14, "Martin López", 37, "lupus")

numero = random.randint(1,5)

if numero == 1:
    mostrar = paciente1
elif numero == 2:
    mostrar = paciente2
elif numero == 3:
    mostrar = paciente3
elif numero == 4:
    mostrar = paciente4
elif numero == 5:
    mostrar = paciente5
    
print("Codigo: ", mostrar[0], "Nombre:", mostrar[1], "Edad:", mostrar[2], "Diagnostico:", mostrar[3])

