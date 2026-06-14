# Se conocen los siguientes datos de tres atletas participantes de un triatlón (todos en
# minutos):
# Nombre
# Tiempo Natación
# Tiempo Ciclismo
# Tiempo Corriendo
# Desarrollar un programa que permita cargar los datos y:
# Informe tiempo promedio de cada competidor.
# Determine el podio, indicando el nombre del primero, el segundo y el tercer mejor
# promedio.


atletas = []
cantidad_atletas = 3

def cargar_datos():
    for i in range(cantidad_atletas):
        nombre= input("Ingrese el nombre del atleta: ")
        tiempo_natacion= int(input("Ingrese el tiempo de natacion: "))
        tiempo_ciclismo= int(input("Ingrese el tiempo de ciclismo: "))
        tiempo_corriendo= int(input("Ingrese el tiempo de corriendo: "))
        atletas.append((nombre, tiempo_natacion, tiempo_ciclismo, tiempo_corriendo))

def calcular_promedio(atleta):
    return (atleta[1] + atleta[2] + atleta[3]) / 3

def determinar_podio():
    promedio_atletas = []
    for atleta in atletas:
        promedio = calcular_promedio(atleta)
        promedio_atletas.append((atleta[0], promedio))
        
    promedio_atletas.sort(key=lambda x: x[1], reverse=True)
    return promedio_atletas[0:cantidad_atletas]
        
  
def main():
    cargar_datos()
    print("Tiempo promedio de cada competidor:")
    for atleta in atletas:
        print(atleta[0], "Tiempo promedio de natacion:", atleta[1], "Tiempo promedio de ciclismo:", atleta[2], "Tiempo promedio de corriendo:", atleta[3])
    print("Podio:")
    print(determinar_podio())
    
main()