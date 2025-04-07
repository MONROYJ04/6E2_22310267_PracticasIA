def busqueda_ascension_colinas(grafo, inicio, heuristica, max_iteraciones=100):
    """
    Algoritmo de Búsqueda de Ascensión de Colinas.
    Este algoritmo busca encontrar un nodo óptimo local en un grafo basado en valores heurísticos.

    :param grafo: Diccionario que representa el grafo como listas de adyacencia.
    :param inicio: Nodo inicial desde donde comienza la búsqueda.
    :param heuristica: Diccionario con los valores heurísticos de cada nodo (valores más bajos son mejores).
    :param max_iteraciones: Número máximo de iteraciones para evitar bucles infinitos.
    :return: Nodo óptimo local encontrado.
    """
    # Nodo actual donde comienza la búsqueda
    nodo_actual = inicio

    # Iterar hasta el máximo de iteraciones permitido
    for _ in range(max_iteraciones):
        # Obtener los vecinos del nodo actual
        vecinos = grafo[nodo_actual]

        # Si no hay vecinos, se detiene la búsqueda (nodo sin salida)
        if not vecinos:
            break

        # Encontrar el vecino con el mejor valor heurístico (el menor)
        mejor_vecino = min(vecinos, key=lambda x: heuristica[x])

        # Si el mejor vecino no mejora la heurística, se detiene la búsqueda (óptimo local alcanzado)
        if heuristica[mejor_vecino] >= heuristica[nodo_actual]:
            break

        # Actualizar el nodo actual al mejor vecino encontrado
        nodo_actual = mejor_vecino

    # Retornar el nodo óptimo local encontrado
    return nodo_actual


# Ejemplo práctico:
# Definimos un grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],  # El nodo 'A' tiene como vecinos a 'B' y 'C'
    'B': ['D'],       # El nodo 'B' tiene como vecino a 'D'
    'C': ['E'],       # El nodo 'C' tiene como vecino a 'E'
    'D': [],          # El nodo 'D' no tiene vecinos
    'E': ['F'],       # El nodo 'E' tiene como vecino a 'F'
    'F': []           # El nodo 'F' no tiene vecinos
}

# Definimos una heurística para cada nodo (valores más bajos son mejores)
heuristica = {
    'A': 5,  # Heurística del nodo 'A'
    'B': 4,  # Heurística del nodo 'B'
    'C': 3,  # Heurística del nodo 'C'
    'D': 2,  # Heurística del nodo 'D'
    'E': 1,  # Heurística del nodo 'E'
    'F': 0   # Heurística del nodo 'F'
}

# Nodo inicial desde donde comienza la búsqueda
inicio = 'A'

# Ejecutar el algoritmo de Búsqueda de Ascensión de Colinas
resultado = busqueda_ascension_colinas(grafo, inicio, heuristica)

# Imprimir el resultado
print("El mejor nodo encontrado por Ascensión de Colinas es:", resultado)

# Explicación del ejemplo:
# 1. Comenzamos en el nodo 'A' (heurística 5).
# 2. Los vecinos de 'A' son 'B' (heurística 4) y 'C' (heurística 3). Elegimos 'C' porque tiene la mejor heurística.
# 3. Desde 'C', el único vecino es 'E' (heurística 1). Nos movemos a 'E'.
# 4. Desde 'E', el único vecino es 'F' (heurística 0). Nos movemos a 'F'.
# 5. El nodo 'F' no tiene vecinos, por lo que terminamos la búsqueda. El nodo óptimo local es 'F'.