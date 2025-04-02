#Este algoritmo implementa la heuristica de Manhattan para el problema del 8 puzzle

def manhattan_distance(state, goal):
    """
    Calcula la heurística de Distancia Manhattan para el 8-puzzle.
    :param state: Estado actual del puzzle (ej: [1, 2, 3, 4, 5, 6, 7, 8, 0]).
    :param goal: Estado objetivo del puzzle.
    :return: Suma de las distancias Manhattan de todas las fichas.
    """
    distance = 0
    for i in range(9):  # Para cada posición en la cuadrícula 3x3
        if state[i] == 0:
            continue  # Ignorar el espacio vacío
        # Posición actual (fila, columna)
        current_row, current_col = i // 3, i % 3
        # Posición objetivo de la ficha state[i]
        goal_index = goal.index(state[i])
        goal_row, goal_col = goal_index // 3, goal_index % 3
        # Sumar distancia Manhattan
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

# Ejemplo de uso:
state = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Estado actual (0 = espacio vacío)
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]   # Estado objetivo
print("Heurística (Distancia Manhattan):", manhattan_distance(state, goal))