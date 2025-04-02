#Se realizara un algoritmo de busqueda bidireccional, el cual es una combinacion de busqueda en profundidad y busqueda en amplitud.

# Búsqueda Bidireccional
# Realiza BFS desde el inicio y el objetivo simultáneamente hasta que las dos búsquedas se encuentran.

from collections import deque

def bidirectional_search(graph, start, goal):
    """
    Implementación de Búsqueda Bidireccional.
    :param graph: grafo como diccionario de listas de adyacencia.
    :param start: nodo inicial.
    :param goal: nodo objetivo.
    :return: camino desde start hasta goal si existe, None en caso contrario.
    """
    if start == goal:
        return [start]

    # Colas para BFS desde start y goal
    queue_start = deque([start])
    queue_goal = deque([goal])

    # Diccionarios para registrar padres y nodos visitados
    parent_start = {start: None}
    parent_goal = {goal: None}

    # Mientras ambas colas tengan elementos
    while queue_start and queue_goal:
        # Expansión desde el inicio
        current_start = queue_start.popleft()
        for neighbor in graph[current_start]:
            if neighbor not in parent_start:
                parent_start[neighbor] = current_start
                queue_start.append(neighbor)
                # Si el nodo ha sido visitado por la búsqueda desde el objetivo
                if neighbor in parent_goal:
                    return merge_paths(parent_start, parent_goal, neighbor)

        # Expansión desde el objetivo
        current_goal = queue_goal.popleft()
        for neighbor in graph[current_goal]:
            if neighbor not in parent_goal:
                parent_goal[neighbor] = current_goal
                queue_goal.append(neighbor)
                # Si el nodo ha sido visitado por la búsqueda desde el inicio
                if neighbor in parent_start:
                    return merge_paths(parent_start, parent_goal, neighbor)
    return None

def merge_paths(parent_start, parent_goal, meeting_node):
    """
    Combina los caminos desde start y goal hasta el meeting_node.
    :param parent_start: diccionario de padres desde start.
    :param parent_goal: diccionario de padres desde goal.
    :param meeting_node: nodo donde se encuentran las búsquedas.
    :return: camino completo desde start hasta goal.
    """
    path = []
    # Camino desde meeting_node hasta start (en orden inverso)
    node = meeting_node
    while node is not None:
        path.append(node)
        node = parent_start[node]
    path = path[::-1]  # Invertir para obtener start -> meeting_node

    # Camino desde meeting_node hasta goal (excluyendo meeting_node)
    node = parent_goal[meeting_node]
    while node is not None:
        path.append(node)
        node = parent_goal[node]
    return path

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
goal = 'F'
print("Bidirectional path:", bidirectional_search(graph, start, goal))