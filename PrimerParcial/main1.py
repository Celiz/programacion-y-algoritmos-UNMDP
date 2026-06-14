jugadores = []
puntajes = []
mejor_puntaje = 0
ganador = ""

cantidad_jugadores = int(input("Ingrese la cantidad de jugadores: "))

for i in range(cantidad_jugadores):
    nombre = input("Ingrese el nombre del jugador: ") 
    jugadores.append(nombre)
    
    puntaje = 0
    for j in range(5):
        respuesta = int(input("Ingrese la respuesta del jugador (1 si acierta, 0 si no acierta): "))
        
        if respuesta == 1:
            puntaje += 10


    puntajes.append(puntaje)
        
    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje
        ganador = nombre

print(f"El ganador es {ganador} con {mejor_puntaje} puntos")

for k in range(cantidad_jugadores):
    print(f"El jugador {jugadores[k]} tiene {puntajes[k]} puntos")