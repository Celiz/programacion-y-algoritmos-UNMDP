# Una escuela necesita un programa que facilite la gestión de cupos de los cursos de primer
# grado. El usuario debe ingresar tres cursos con su respectivo código de identificación
# (por ejemplo, 1A, 1B, 1C). Además, debe ingresar la cantidad de niños y de niñas de
# cada curso, y cupo máximo (que es el mismo para los tres cursos). El programa debe
# devolver:
    # Código de identificación del curso que tenga menos alumnos inprogramaos.
    # Porcentaje de niñas de cada curso.
    # Porcentaje de niños de cada curso.
    # Promedio general de alumnos.
    # Si algunos de los tres cursos supera el cupo máximo, mostrar con un mensaje la
    # necesidad de apertura de una nueva división.


total_general = 0
curso_menos_codigo = ""
curso_menos_total = 0
supera_cupo = False

for i in range(1, 4):
   print(f"\nCurso {i}")
   codigo = input("Código del curso: ").strip()
   ninos = int(input("Cantidad de niños: "))
   ninas = int(input("Cantidad de niñas: "))

   total = ninos + ninas
   total_general += total

   if i == 1 or total < curso_menos_total:
      curso_menos_total = total
      curso_menos_codigo = codigo

   if total > 0:
      porcentaje_ninas = (ninas / total) * 100
      porcentaje_ninos = (ninos / total) * 100
   else:
      porcentaje_ninas = 0
      porcentaje_ninos = 0

   print(
      f"{codigo}: niñas {porcentaje_ninas:.2f}% - "
      f"niños {porcentaje_ninos:.2f}%"
   )

   if i == 1:
      cupo_maximo = int(input("\nCupo máximo por curso: "))

   if total > cupo_maximo:
      supera_cupo = True

promedio_general = total_general / 3

print(f"\nCurso con menos alumnos: {curso_menos_codigo}")
print(f"Promedio general de alumnos por curso: {promedio_general:.2f}")

if supera_cupo:
   print("Alguno de los cursos supera el cupo máximo. Se necesita abrir una nueva división.")
else:
   print("Ningún curso supera el cupo máximo.")




