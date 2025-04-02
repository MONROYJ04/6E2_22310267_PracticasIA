def hill_climbing(graph, start, heuristic, max_iterations=100):
    """
    Búsqueda de Ascensión de Colinas.
    :param graph: Grafo como diccionario de listas de adyacencia.
    :param start: Nodo inicial.
    :param heuristic: Diccionario de valores heurísticos (menor es mejor).
    :param max_iterations: Límite de iteraciones para evitar loops infinitos.
    :return: Nodo local óptimo.
    """
    current = start
    for _ in range(max_iterations):
        neighbors = graph[current]
        if not neighbors:
            break
        # Elegir el vecino con mejor heurística
        best_neighbor = min(neighbors, key=lambda x: heuristic[x])
        if heuristic[best_neighbor] >= heuristic[current]:
            break  # Óptimo local encontrado
        current = best_neighbor
    return current

# Ejemplo:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
start = 'A'
print("Hill Climbing best node:", hill_climbing(graph, start, heuristic))