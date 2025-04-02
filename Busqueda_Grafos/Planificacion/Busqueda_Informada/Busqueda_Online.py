import math
import random
from collections import defaultdict

class Node:
    """Nodo del árbol MCTS."""
    def __init__(self, state, parent=None):
        self.state = state  # Tablero actual (ej: [['X', ' ', 'O'], ...])
        self.parent = parent
        self.children = []
        self.wins = 0  # Victorias acumuladas en simulaciones
        self.visits = 0  # Veces que se visitó este nodo

def mcts(root_state, player, simulations=1000):
    """Algoritmo MCTS principal."""
    root = Node(root_state)
    
    for _ in range(simulations):
        # 1. Selección: Elegir nodo hasta llegar a uno no expandido
        node = select_node(root, player)
        
        # 2. Expansión: Añadir un hijo si el juego no ha terminado
        if not is_terminal(node.state):
            node = expand(node, player)
        
        # 3. Simulación: Jugar aleatoriamente hasta el final
        result = simulate(node.state, player)
        
        # 4. Retropropagación: Actualizar estadísticas
        backpropagate(node, result)
    
    # Elegir el mejor movimiento basado en visitas
    return best_child(root).state

def select_node(node, player):
    """Selección por UCB1 (balance entre exploración y explotación)."""
    while node.children:
        if not all(child.visits > 0 for child in node.children):
            # Seleccionar un hijo no visitado
            return next(child for child in node.children if child.visits == 0)
        # Fórmula UCB1
        node = max(node.children, key=lambda c: c.wins/c.visits + math.sqrt(2*math.log(node.visits)/c.visits))
    return node

def expand(node, player):
    """Expande el nodo con un nuevo estado hijo."""
    possible_moves = get_legal_moves(node.state)
    new_state = apply_move(node.state, random.choice(possible_moves), player)
    child = Node(new_state, parent=node)
    node.children.append(child)
    return child

def simulate(state, player):
    """Simula un juego aleatorio hasta el final."""
    current_state = state
    current_player = player
    while not is_terminal(current_state):
        moves = get_legal_moves(current_state)
        current_state = apply_move(current_state, random.choice(moves), current_player)
        current_player = 'O' if current_player == 'X' else 'X'
    return get_result(current_state)

def backpropagate(node, result):
    """Actualiza wins/visits desde el nodo hasta la raíz."""
    while node:
        node.visits += 1
        node.wins += result
        node = node.parent

def best_child(node):
    """Elige el hijo con más visitas (no solo el de mayor ratio de wins)."""
    return max(node.children, key=lambda c: c.visits)

# Funciones auxiliares para Tres en Raya:
def is_terminal(state):
    """Verifica si el juego terminó (victoria o empate)."""
    lines = [
        # Filas
        state[0], state[1], state[2],
        # Columnas
        [state[0][0], state[1][0], state[2][0]],
        # Diagonales
        [state[0][0], state[1][1], state[2][2]],
    ]
    for line in lines:
        if len(set(line)) == 1 and line[0] != ' ':
            return True
    return all(cell != ' ' for row in state for cell in row)

def get_legal_moves(state):
    """Obtiene movimientos legales (casillas vacías)."""
    return [(i, j) for i in range(3) for j in range(3) if state[i][j] == ' ']

def apply_move(state, move, player):
    """Aplica un movimiento al tablero."""
    new_state = [row.copy() for row in state]
    new_state[move[0]][move[1]] = player
    return new_state

def get_result(state):
    """Evalúa el resultado (1 para victoria de X, -1 para O, 0 empate)."""
    # Implementar lógica de evaluación según el juego.
    return 0

# Ejemplo de uso:
initial_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
best_move_state = mcts(initial_state, player='X', simulations=1000)
print("Mejor estado encontrado:", best_move_state)