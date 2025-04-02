#Se realizara un algoritmo de busqueda en profundidad iterativa, el cual es una combinacion de busqueda en profundidad y busqueda en amplitud.

# Búsqueda en Profundidad Iterativa (IDS)
# Combina BFS y DFS: realiza DFS con límite de profundidad incrementado iterativamente.

def ids(graph, start, goal):
    """
    Implementación de Búsqueda en Profundidad Iterativa (IDS).
    :param graph: grafo como diccionario de listas de adyacencia.
    :param start: nodo inicial.
    :param goal: nodo objetivo.
    :return: camino desde start hasta goal, o None si no se encuentra.
    """
    depth = 0
    while True:
        result = dls(graph, start, goal, depth)
        if result is not None:
            return result
        depth += 1

def dls(graph, node, goal, depth, path=None):
    """
    Búsqueda en Profundidad Limitada (DLS) utilizada por IDS.
    :param node: nodo actual.
    :param goal: nodo objetivo.
    :param depth: profundidad máxima permitida.
    :param path: camino recorrido hasta ahora.
    :return: camino si se encuentra el objetivo, None en caso contrario.
    """
    if path is None:
        path = []
    path = path + [node]
    if node == goal:
        return path
    if depth <= 0:
        return None
    for neighbor in graph[node]:
        result = dls(graph, neighbor, goal, depth - 1, path)
        if result is not None:
            return result
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
print("IDS path:", ids(graph, start, goal))