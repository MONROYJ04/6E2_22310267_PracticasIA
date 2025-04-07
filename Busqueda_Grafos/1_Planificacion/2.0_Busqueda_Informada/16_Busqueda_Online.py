import math
import random
from collections import defaultdict

class Nodo:
    """
    Clase que representa un nodo en el árbol de búsqueda MCTS.
    Cada nodo contiene información sobre el estado del juego, su nodo padre,
    sus nodos hijos, y estadísticas de simulaciones (victorias y visitas).
    """
    def __init__(self, estado, padre=None):
        self.estado = estado  # Estado actual del tablero (ejemplo: [['X', ' ', 'O'], ...])
        self.padre = padre  # Nodo padre en el árbol (None si es la raíz)
        self.hijos = []  # Lista de nodos hijos (estados derivados del actual)
        self.victorias = 0  # Número de victorias acumuladas en simulaciones
        self.visitas = 0  # Número de veces que este nodo fue visitado

def mcts(estado_inicial, jugador, simulaciones=1000):
    """
    Algoritmo principal de Monte Carlo Tree Search (MCTS).
    Este algoritmo busca el mejor movimiento posible desde un estado inicial
    utilizando simulaciones aleatorias para explorar el espacio de búsqueda.

    Parámetros:
    - estado_inicial: El estado inicial del tablero (matriz 3x3).
    - jugador: El jugador actual ('X' o 'O').
    - simulaciones: Número de simulaciones a realizar.

    Retorna:
    - El mejor estado del tablero después de las simulaciones.
    """
    # Crear el nodo raíz con el estado inicial
    raiz = Nodo(estado_inicial)

    # Realizar el número especificado de simulaciones
    for _ in range(simulaciones):
        # 1. Selección: Elegir un nodo hasta llegar a uno no expandido
        nodo = seleccionar_nodo(raiz, jugador)

        # 2. Expansión: Añadir un hijo si el juego no ha terminado
        if not es_terminal(nodo.estado):
            nodo = expandir(nodo, jugador)

        # 3. Simulación: Jugar aleatoriamente hasta el final
        resultado = simular(nodo.estado, jugador)

        # 4. Retropropagación: Actualizar estadísticas desde el nodo hasta la raíz
        retropropagar(nodo, resultado)

    # Elegir el mejor movimiento basado en el número de visitas
    return mejor_hijo(raiz).estado

def seleccionar_nodo(nodo, jugador):
    """
    Selección de un nodo utilizando la fórmula UCB1 (balance entre exploración y explotación).
    Este paso recorre el árbol de búsqueda hasta encontrar un nodo no expandido.

    Parámetros:
    - nodo: Nodo actual desde el cual se inicia la selección.
    - jugador: El jugador actual ('X' o 'O').

    Retorna:
    - El nodo seleccionado para expansión o simulación.
    """
    while nodo.hijos:
        # Si hay hijos no visitados, seleccionar uno de ellos
        if not all(hijo.visitas > 0 for hijo in nodo.hijos):
            return next(hijo for hijo in nodo.hijos if hijo.visitas == 0)
        # Aplicar la fórmula UCB1 para seleccionar el mejor hijo
        nodo = max(nodo.hijos, key=lambda h: h.victorias/h.visitas + math.sqrt(2 * math.log(nodo.visitas) / h.visitas))
    return nodo

def expandir(nodo, jugador):
    """
    Expande un nodo añadiendo un nuevo estado hijo.
    Esto simula un movimiento posible desde el estado actual.

    Parámetros:
    - nodo: Nodo actual que se desea expandir.
    - jugador: El jugador actual ('X' o 'O').

    Retorna:
    - El nuevo nodo hijo creado.
    """
    movimientos_posibles = obtener_movimientos_legales(nodo.estado)
    nuevo_estado = aplicar_movimiento(nodo.estado, random.choice(movimientos_posibles), jugador)
    hijo = Nodo(nuevo_estado, padre=nodo)
    nodo.hijos.append(hijo)
    return hijo

def simular(estado, jugador):
    """
    Simula un juego aleatorio desde el estado actual hasta el final.
    Este paso permite estimar el resultado de un movimiento sin explorar exhaustivamente.

    Parámetros:
    - estado: El estado actual del tablero.
    - jugador: El jugador actual ('X' o 'O').

    Retorna:
    - El resultado de la simulación (1 para victoria de 'X', -1 para 'O', 0 para empate).
    """
    estado_actual = estado
    jugador_actual = jugador
    while not es_terminal(estado_actual):
        movimientos = obtener_movimientos_legales(estado_actual)
        estado_actual = aplicar_movimiento(estado_actual, random.choice(movimientos), jugador_actual)
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'
    return obtener_resultado(estado_actual)

def retropropagar(nodo, resultado):
    """
    Actualiza las estadísticas de victorias y visitas desde el nodo hasta la raíz.
    Este paso permite que los nodos padres aprendan de los resultados de sus hijos.

    Parámetros:
    - nodo: Nodo desde el cual se inicia la retropropagación.
    - resultado: Resultado de la simulación (1, -1 o 0).
    """
    while nodo:
        nodo.visitas += 1
        nodo.victorias += resultado
        nodo = nodo.padre

def mejor_hijo(nodo):
    """
    Selecciona el hijo con el mayor número de visitas.
    Este paso determina el mejor movimiento basado en las simulaciones realizadas.

    Parámetros:
    - nodo: Nodo padre cuyos hijos se evaluarán.

    Retorna:
    - El nodo hijo con el mayor número de visitas.
    """
    return max(nodo.hijos, key=lambda h: h.visitas)

# Funciones auxiliares para el juego Tres en Raya:
def es_terminal(estado):
    """
    Verifica si el juego ha terminado (victoria o empate).
    """
    lineas = [
        # Filas
        estado[0], estado[1], estado[2],
        # Columnas
        [estado[0][0], estado[1][0], estado[2][0]],
        [estado[0][1], estado[1][1], estado[2][1]],
        [estado[0][2], estado[1][2], estado[2][2]],
        # Diagonales
        [estado[0][0], estado[1][1], estado[2][2]],
        [estado[0][2], estado[1][1], estado[2][0]],
    ]
    for linea in lineas:
        if len(set(linea)) == 1 and linea[0] != ' ':
            return True
    return all(celda != ' ' for fila in estado for celda in fila)

def obtener_movimientos_legales(estado):
    """
    Obtiene una lista de movimientos legales (casillas vacías).
    """
    return [(i, j) for i in range(3) for j in range(3) if estado[i][j] == ' ']

def aplicar_movimiento(estado, movimiento, jugador):
    """
    Aplica un movimiento al tablero y devuelve el nuevo estado.
    """
    nuevo_estado = [fila.copy() for fila in estado]
    nuevo_estado[movimiento[0]][movimiento[1]] = jugador
    return nuevo_estado

def obtener_resultado(estado):
    """
    Evalúa el resultado del juego (1 para victoria de X, -1 para O, 0 para empate).
    """
    if any(len(set(linea)) == 1 and linea[0] == 'X' for linea in estado):
        return 1  # Victoria de X
    if any(len(set(linea)) == 1 and linea[0] == 'O' for linea in estado):
        return -1  # Victoria de O
    return 0  # Empate

# Ejemplo práctico:
estado_inicial = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print("Estado inicial del tablero:")
for fila in estado_inicial:
    print(fila)

# Ejecutar MCTS para encontrar el mejor movimiento para el jugador 'X'
mejor_estado = mcts(estado_inicial, jugador='X', simulaciones=1000)

print("\nMejor estado encontrado después de aplicar MCTS:")
for fila in mejor_estado:
    print(fila)