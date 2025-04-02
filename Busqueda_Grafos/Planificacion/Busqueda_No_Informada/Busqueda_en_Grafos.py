#Se realizara un algoritmo de busqueda en grafos, el cual es un algoritmo de busqueda en profundidad.

# Búsqueda en Grafos (evitando estados repetidos)
# Utiliza una lista de visitados para evitar ciclos.

def graph_search(graph, start, goal):
    """
    Búsqueda en amplitud (BFS) evitando estados repetidos.
    :param graph: grafo como diccionario de listas de adyacencia.
    :param start: nodo inicial.
    :param goal: nodo objetivo.
    :return: camino desde start hasta goal, o None si no se encuentra.
    """
    from collections import deque

    visited = set()      # Nodos ya visitados
    queue = deque()      # Cola para BFS
    parent = {}          # Diccionario para reconstruir el camino

    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()
        if current == goal:
            # Reconstruir el camino
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Invertir para obtener start -> goal

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
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
start = 'A'
goal = 'F'
print("Graph search path:", graph_search(graph, start, goal))