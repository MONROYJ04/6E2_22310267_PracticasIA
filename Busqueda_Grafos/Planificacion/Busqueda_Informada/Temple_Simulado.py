import random  # Para generar números aleatorios
import math    # Para usar exp (exponencial)

def simulated_annealing(graph, start, heuristic, initial_temp=1000, min_temp=1, cooling_rate=0.95):
    current = start
    best = current
    temp = initial_temp
    restart_count = 0

    while temp > min_temp and restart_count < 5:
        neighbors = graph[current]
        if not neighbors:
            current = random.choice(list(graph.keys()))  # Reinicio aleatorio
            restart_count += 1
            continue
        
        next_node = random.choice(neighbors)
        delta_e = heuristic[next_node] - heuristic[current]
        
        if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
            current = next_node
            if heuristic[current] < heuristic[best]:
                best = current
        
        # Enfriamiento adaptativo (disminuye más rápido si no hay mejora)
        temp *= cooling_rate if delta_e < 0 else cooling_rate * 0.9
    
    return best