# Búsqueda A*
# Combina costo real (g) y heurística (h) para expandir nodos: f(n) = g(n) + h(n).

import heapq

def a_star_search(graph, start, goal, heuristic):
    """
    Búsqueda A*.
    :param graph: grafo como diccionario de listas de adyacencia.
    :param start: nodo inicial.
    :param goal: nodo objetivo.
    :param heuristic: diccionario con valores heurísticos para cada nodo.
    :return: camino desde start hasta goal, o None si no se encuentra.
    """
    open_set = []                        # Cola de prioridad (min-heap)
    heapq.heappush(open_set, (0 + heuristic[start], start))
    g_values = {start: 0}               # Costo real desde start
    parent = {start: None}              # Para reconstruir el camino

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            # Reconstruir el camino
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in graph[current]:
            tentative_g = g_values[current] + 1  # Costo entre nodos asumido como 1
            if neighbor not in g_values or tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_value, neighbor))
                parent[neighbor] = current
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
print("A* path:", a_star_search(graph, start, goal, heuristic))
print()
print()
print()


# Búsqueda AO* (para grafos AND-OR)
def ao_star_search(graph, start, goal, heuristic):
    """
    Implementación simplificada de AO* para grafos AND-OR.
    :param graph: Grafo AND-OR (ej: {'A': [('B', 'C'), ('D')]} significa 'A' → 'B' AND 'C' OR 'D').
    :param start: Nodo inicial.
    :param goal: Nodo objetivo.
    :param heuristic: Diccionario de valores heurísticos.
    :return: Camino solución o None.
    """
    from collections import defaultdict

    # Estructuras para almacenar costos y padres
    cost = defaultdict(int)
    parent = defaultdict(list)
    solved = set()

    def ao_star(node):
        if node in solved:
            return cost[node]
        if node == goal:
            solved.add(node)
            return 0
        if node not in graph:  # Nodo hoja no objetivo
            return float('inf')

        # Evaluar todos los sucesores (OR) y sus conjunciones (AND)
        min_cost = float('inf')
        for successors in graph[node]:
            if isinstance(successors, tuple):  # Rama AND (todos los sucesores deben resolverse)
                current_cost = sum(ao_star(succ) for succ in successors) + len(successors)
            else:  # Rama OR (cualquier sucesor)
                current_cost = ao_star(successors) + 1

            if current_cost < min_cost:
                min_cost = current_cost
                parent[node] = successors if isinstance(successors, tuple) else [successors]

        cost[node] = min_cost
        if min_cost != float('inf'):
            solved.add(node)
        return min_cost

    ao_star(start)
    if goal not in solved:
        return None

    # Reconstruir el camino (simplificado)
    path = []
    stack = [start]
    while stack:
        current = stack.pop()
        path.append(current)
        if current == goal:
            break
        if current in parent:
            stack.extend(parent[current][::-1])  # Añadir en orden inverso para recorrer en orden
    return path

# Ejemplo de grafo AND-OR:
graph = {
    'A': [('B', 'C'), ('D')],  # A puede lograrse con (B AND C) OR D
    'B': [('E')],
    'C': [('F')],
    'D': [('F')],
    'E': [],
    'F': []
}
heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 0, 'F': 0}
start, goal = 'A', 'F'
print("AO* path:", ao_star_search(graph, start, goal, heuristic))