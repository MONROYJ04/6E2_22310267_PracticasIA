#Se realizara un algoritmo de busqueda en profundidad limitada (DLS) para encontrar un camino en un grafo.

def dls(graph, start, goal, depth_limit):
    """
    Búsqueda en Profundidad Limitada (DLS).
    :param graph: Grafo representado como diccionario de listas de adyacencia.
    :param start: Nodo inicial.
    :param goal: Nodo objetivo.
    :param depth_limit: Límite máximo de profundidad para la búsqueda.
    :return: Camino desde 'start' hasta 'goal' si existe, de lo contrario None.
    """
    # Usamos una pila (stack) para DFS: cada elemento es una tupla (nodo, profundidad, camino)
    stack = [(start, 0, [start])]
    visited = set()

    while stack:
        node, depth, path = stack.pop()  # Extrae el último nodo añadido (LIFO)
        
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if depth >= depth_limit:
            continue  # Si superamos el límite, no expandimos este nodo
        
        if node not in visited:
            visited.add(node)
            # Expandimos los vecinos en orden inverso para mantener un orden natural (opcional)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1, path + [neighbor]))
    
    return None  # Si no se encuentra el objetivo

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
depth_limit = 3  # Profundidad máxima permitida

path = dls(graph, start, goal, depth_limit)
print(f"Camino encontrado (DLS, límite={depth_limit}): {path}")