from collections import deque

def tabu_search(graph, start, heuristic, tabu_size=3, max_iterations=100):
    current = start
    best = current
    tabu_list = deque(maxlen=tabu_size)  # Más eficiente que una lista
    best_candidates = []  # Memoria de mejores soluciones

    for _ in range(max_iterations):
        neighbors = [n for n in graph[current] if n not in tabu_list]
        if not neighbors:
            neighbors = graph[current]  # Relaja restricciones si no hay vecinos válidos
        
        # Selecciona el mejor vecino (incluso si está en tabú si mejora el global)
        current = min(neighbors, key=lambda x: heuristic[x])
        
        # Criterio de aspiración
        if heuristic[current] < heuristic[best]:
            best = current
            best_candidates.append(best)
        
        tabu_list.append(current)
    
    return best_candidates[-1] if best_candidates else best