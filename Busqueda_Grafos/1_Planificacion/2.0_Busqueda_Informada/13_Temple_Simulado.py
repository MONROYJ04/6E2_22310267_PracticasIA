import random  # Para generar números aleatorios
import math    # Para usar la función exponencial (exp)

def temple_simulado(grafo, inicio, heuristica, temp_inicial=1000, temp_minima=1, tasa_enfriamiento=0.95):
    """
    Algoritmo de Temple Simulado para encontrar una solución aproximada en un grafo.

    Parámetros:
    - grafo: Diccionario que representa el grafo. Las claves son nodos y los valores son listas de vecinos.
    - inicio: Nodo inicial desde donde comienza la búsqueda.
    - heuristica: Diccionario que asigna un valor heurístico a cada nodo (menor es mejor).
    - temp_inicial: Temperatura inicial para el algoritmo.
    - temp_minima: Temperatura mínima para detener el algoritmo.
    - tasa_enfriamiento: Factor por el cual se reduce la temperatura en cada iteración.

    Retorna:
    - El mejor nodo encontrado según la heurística.
    """
    actual = inicio  # Nodo actual
    mejor = actual   # Mejor nodo encontrado hasta ahora
    temperatura = temp_inicial  # Temperatura inicial
    reinicios = 0  # Contador de reinicios aleatorios

    # Mientras la temperatura sea mayor que la mínima y no se excedan los reinicios
    while temperatura > temp_minima and reinicios < 5:
        vecinos = grafo[actual]  # Obtener los vecinos del nodo actual

        # Si no hay vecinos, se realiza un reinicio aleatorio
        if not vecinos:
            actual = random.choice(list(grafo.keys()))  # Elegir un nodo aleatorio del grafo
            reinicios += 1  # Incrementar el contador de reinicios
            continue

        # Elegir un vecino aleatorio
        siguiente = random.choice(vecinos)

        # Calcular la diferencia de energía (heurística)
        delta_e = heuristica[siguiente] - heuristica[actual]

        # Decidir si se acepta el nuevo nodo
        if delta_e < 0 or random.random() < math.exp(-delta_e / temperatura):
            actual = siguiente  # Moverse al nodo siguiente
            # Actualizar el mejor nodo si el nuevo nodo tiene mejor heurística
            if heuristica[actual] < heuristica[mejor]:
                mejor = actual

        # Reducir la temperatura (enfriamiento adaptativo)
        temperatura *= tasa_enfriamiento if delta_e < 0 else tasa_enfriamiento * 0.9

    return mejor


# Ejemplo práctico
if __name__ == "__main__":
    # Definición de un grafo simple
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    # Heurística asociada a cada nodo (valores más bajos son mejores)
    heuristica = {
        "A": 10,
        "B": 8,
        "C": 5,
        "D": 7,
        "E": 3,
        "F": 1
    }

    # Nodo inicial
    inicio = "A"

    # Ejecutar el algoritmo de Temple Simulado
    mejor_nodo = temple_simulado(grafo, inicio, heuristica)

    # Mostrar el resultado
    print(f"El mejor nodo encontrado es: {mejor_nodo}")