# Algoritmo de Búsqueda Voraz Primero el Mejor (Greedy Best-First Search)
# Este algoritmo utiliza una heurística para expandir primero el nodo más prometedor.
# La heurística es una estimación de la distancia al objetivo.

import heapq  # Biblioteca para manejar colas de prioridad (min-heaps)

def busqueda_voraz_primero_mejor(grafo, inicio, objetivo, heuristica):
    """
    Implementación del algoritmo de Búsqueda Voraz Primero el Mejor.
    :param grafo: Grafo representado como un diccionario de listas de adyacencia.
    :param inicio: Nodo inicial desde donde comienza la búsqueda.
    :param objetivo: Nodo objetivo al que se desea llegar.
    :param heuristica: Diccionario con valores heurísticos para cada nodo.
    :return: Lista con el camino desde el nodo inicial hasta el objetivo, o None si no se encuentra.
    """
    # Conjunto para almacenar los nodos visitados
    visitados = set()
    
    # Cola de prioridad para manejar los nodos según su valor heurístico
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica[inicio], inicio))  # Insertar el nodo inicial con su heurística
    
    # Diccionario para rastrear el nodo padre de cada nodo (para reconstruir el camino)
    padres = {inicio: None}

    # Mientras haya nodos en la cola de prioridad
    while cola_prioridad:
        # Extraer el nodo con la menor heurística
        _, actual = heapq.heappop(cola_prioridad)

        # Si el nodo actual es el objetivo, reconstruir y devolver el camino
        if actual == objetivo:
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            return camino[::-1]  # Devolver el camino en orden correcto

        # Marcar el nodo actual como visitado
        visitados.add(actual)

        # Explorar los vecinos del nodo actual
        for vecino in grafo[actual]:
            if vecino not in visitados:  # Solo considerar nodos no visitados
                padres[vecino] = actual  # Registrar el nodo padre
                # Insertar el vecino en la cola de prioridad con su valor heurístico
                heapq.heappush(cola_prioridad, (heuristica[vecino], vecino))
    
    # Si no se encuentra un camino al objetivo, devolver None
    return None

# Ejemplo práctico:
# Supongamos que queremos planificar una ruta desde una ciudad inicial hasta una ciudad objetivo.
# El grafo representa las conexiones entre ciudades, y la heurística es una estimación de la distancia
# en línea recta desde cada ciudad hasta la ciudad objetivo.

grafo = {
    'CiudadA': ['CiudadB', 'CiudadC'],
    'CiudadB': ['CiudadD', 'CiudadE'],
    'CiudadC': ['CiudadF'],
    'CiudadD': [],
    'CiudadE': ['CiudadF'],
    'CiudadF': []
}

# Heurística: estimación de la distancia en línea recta a la ciudad objetivo (CiudadF)
heuristica = {
    'CiudadA': 6,
    'CiudadB': 4,
    'CiudadC': 4,
    'CiudadD': 2,
    'CiudadE': 2,
    'CiudadF': 0  # La distancia al objetivo desde el objetivo es 0
}

# Nodo inicial y objetivo
inicio = 'CiudadA'
objetivo = 'CiudadF'

# Ejecutar el algoritmo y mostrar el resultado
camino = busqueda_voraz_primero_mejor(grafo, inicio, objetivo, heuristica)
print("Camino encontrado por Búsqueda Voraz Primero el Mejor:", camino)

# Explicación del ejemplo:
# 1. Comenzamos en 'CiudadA' (heurística = 6).
# 2. Expandimos 'CiudadB' (heurística = 4) y 'CiudadC' (heurística = 4).
# 3. Elegimos 'CiudadB' (porque tiene menor heurística o igual).
# 4. Expandimos 'CiudadD' (heurística = 2) y 'CiudadE' (heurística = 2).
# 5. Elegimos 'CiudadD' o 'CiudadE' (ambos tienen heurística = 2).
# 6. Finalmente, llegamos a 'CiudadF' (heurística = 0).