# Ejercicio 14 - Guía 5
# Técnicas de Diseño de Algoritmos

"""
Escenario A:
Se necesita explorar un laberinto para encontrar la salida. Si se llega a un callejón
sin salida, se debe retroceder hasta la última bifurcación y probar otro camino.

Técnica más adecuada: BACKTRACKING (Vuelta Atrás)
Justificación:
El Backtracking es un método de búsqueda sistemática de soluciones que explora un árbol
de decisión (en este caso, los caminos del laberinto). Su propiedad fundamental es la
capacidad de retroceder (hacer "backtrack"): cuando el algoritmo determina que el camino
actual no conduce a una solución (callejón sin salida), vuelve sobre sus pasos al estado anterior
(la última bifurcación) para probar una alternativa distinta, evitando así explorar caminos
inútiles de manera redundante.
"""

"""
Escenario B:
Se busca calcular la ruta más corta entre múltiples ciudades, pero se sabe que el problema
original se puede dividir en subproblemas que se superponen (rutas intermedias que se calculan
varias veces). Para no repetir cálculos, se desea guardar los resultados intermedios en una tabla.

Técnica más adecuada: PROGRAMACIÓN DINÁMICA
Justificación:
Este escenario cumple con las dos condiciones esenciales para la Programación Dinámica:
1. Subestructura óptima: La ruta más corta entre dos ciudades se compone de rutas más cortas
   entre subetapas intermedias.
2. Subproblemas superpuestos: El cálculo de rutas intermedias se repite en múltiples caminos mayores.
El uso de una tabla para almacenar resultados de subproblemas ya resueltos (memorización o tabulación)
y evitar recalcularlos es la característica distintiva de esta técnica, mejorando drásticamente la
eficiencia temporal.
"""

"""
Escenario C:
Se debe dar el vuelto utilizando el sistema monetario de Argentina (billetes de $1000, $500,
$200, $100, etc.). En cada paso se quiere tomar la mejor decisión local sin evaluar todas las
combinaciones posibles.

Técnica más adecuada: ALGORITMOS ÁVIDOS (Greedy)
Justificación:
Un algoritmo ávido toma decisiones de manera secuencial eligiendo en cada paso la opción que parece
óptima en ese momento (óptimo local), sin retroceder ni evaluar el árbol completo de posibilidades.
Para el problema del cambio con el sistema monetario argentino (que es un sistema "canónico"), la estrategia
ávida consistente en entregar siempre el billete de mayor valor posible que no supere el vuelto restante
garantiza obtener el vuelto óptimo (con la menor cantidad de billetes) de forma muy rápida y eficiente.
"""
