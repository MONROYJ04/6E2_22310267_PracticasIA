#Se realizara un algoritmo de busqueda voraz primero mejor, el cual se basa en la heuristica de la distancia al objetivo.

# Búsqueda Voraz Primero el Mejor (Greedy Best-First Search)
# Utiliza una heurística para expandir el nodo más prometedor primero.

import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Búsqueda Voraz Primero el Mejor.
    :param graph: grafo como diccionario de listas de adyacencia.
    :param start: nodo inicial.
    :param goal: nodo objetivo.
    :param heuristic: diccionario con valores heurísticos para cada nodo.
    :return: camino desde start hasta goal, o None si no se encuentra.
    """
    visited = set()                      # Nodos visitados
    priority_queue = []                  # Cola de prioridad (min-heap)
    heapq.heappush(priority_queue, (heuristic[start], start))
    parent = {start: None}              # Para reconstruir el camino

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current == goal:
            # Reconstruir el camino
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    return None

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}
start = 'A'
goal = 'F'
print("Greedy Best-First path:", greedy_best_first_search(graph, start, goal, heuristic))