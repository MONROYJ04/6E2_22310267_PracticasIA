# Algoritmo de búsqueda A* y AO* explicado paso a paso

import heapq  # Biblioteca para manejar colas de prioridad (min-heaps)

# Algoritmo de búsqueda A*
def busqueda_a_estrella(grafo, inicio, objetivo, heuristica):
    """
    Algoritmo de búsqueda A*.
    Este algoritmo encuentra el camino más corto desde un nodo inicial hasta un nodo objetivo
    utilizando una combinación del costo acumulado (g) y una estimación heurística (h).

    :param grafo: Diccionario que representa el grafo como listas de adyacencia.
    :param inicio: Nodo inicial desde donde comienza la búsqueda.
    :param objetivo: Nodo objetivo al que se desea llegar.
    :param heuristica: Diccionario con valores heurísticos para cada nodo.
    :return: Lista con el camino desde el nodo inicial al objetivo, o None si no se encuentra.
    """
    # Cola de prioridad para los nodos abiertos (nodos por explorar)
    conjunto_abierto = []
    # Insertamos el nodo inicial con su costo f(n) = g(n) + h(n)
    heapq.heappush(conjunto_abierto, (0 + heuristica[inicio], inicio))

    # Diccionario para almacenar el costo acumulado desde el nodo inicial hasta cada nodo
    costos_g = {inicio: 0}

    # Diccionario para rastrear el nodo padre de cada nodo (para reconstruir el camino)
    padres = {inicio: None}

    # Mientras haya nodos por explorar
    while conjunto_abierto:
        # Extraemos el nodo con el menor valor f(n) de la cola de prioridad
        _, actual = heapq.heappop(conjunto_abierto)

        # Si llegamos al nodo objetivo, reconstruimos el camino desde el objetivo al inicio
        if actual == objetivo:
            camino = []
            while actual is not None:
                camino.append(actual)  # Agregamos el nodo al camino
                actual = padres[actual]  # Retrocedemos al nodo padre
            return camino[::-1]  # Devolvemos el camino en orden correcto (inicio -> objetivo)

        # Exploramos los vecinos del nodo actual
        for vecino in grafo[actual]:
            # Calculamos el costo acumulado g(n) para el vecino
            costo_tentativo = costos_g[actual] + 1  # Suponemos que el costo entre nodos es 1

            # Si el vecino no ha sido visitado o encontramos un mejor costo
            if vecino not in costos_g or costo_tentativo < costos_g[vecino]:
                # Actualizamos el costo acumulado g(n) del vecino
                costos_g[vecino] = costo_tentativo
                # Calculamos el valor f(n) = g(n) + h(n) para el vecino
                f_valor = costo_tentativo + heuristica[vecino]
                # Añadimos el vecino a la cola de prioridad
                heapq.heappush(conjunto_abierto, (f_valor, vecino))
                # Actualizamos el nodo padre del vecino
                padres[vecino] = actual

    # Si no se encuentra un camino al objetivo, devolvemos None
    return None


# Ejemplo práctico para A*
# Definimos un grafo como un diccionario donde las claves son nodos y los valores son listas de vecinos
grafo_a_estrella = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos una heurística (estimación de distancia al objetivo) para cada nodo
heuristica_a_estrella = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

# Nodo inicial y nodo objetivo
inicio_a_estrella = 'A'
objetivo_a_estrella = 'F'

# Ejecutamos el algoritmo A* y mostramos el resultado
print("Camino A*:", busqueda_a_estrella(grafo_a_estrella, inicio_a_estrella, objetivo_a_estrella, heuristica_a_estrella))


# Algoritmo AO* (para grafos AND-OR)
def busqueda_ao_estrella(grafo, inicio, objetivo, heuristica):
    """
    Algoritmo AO* para grafos AND-OR.
    Este algoritmo encuentra el camino óptimo en grafos donde los nodos pueden tener relaciones AND (todos los hijos deben cumplirse)
    o relaciones OR (solo un hijo debe cumplirse).

    :param grafo: Grafo AND-OR representado como un diccionario.
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :param heuristica: Diccionario con valores heurísticos.
    :return: Camino solución o None si no se encuentra.
    """
    from collections import defaultdict

    # Diccionario para almacenar los costos de cada nodo
    costos = defaultdict(int)

    # Diccionario para rastrear los padres de cada nodo
    padres = defaultdict(list)

    # Conjunto de nodos resueltos
    resueltos = set()

    def ao_estrella(nodo):
        """
        Función recursiva para evaluar los costos de los nodos.
        """
        if nodo in resueltos:
            return costos[nodo]
        if nodo == objetivo:
            resueltos.add(nodo)
            return 0
        if nodo not in grafo:  # Nodo hoja no objetivo
            return float('inf')

        # Evaluar todas las ramas (AND y OR)
        costo_minimo = float('inf')
        for sucesores in grafo[nodo]:
            if isinstance(sucesores, tuple):  # Rama AND
                costo_actual = sum(ao_estrella(s) for s in sucesores) + len(sucesores)
            else:  # Rama OR
                costo_actual = ao_estrella(sucesores) + 1

            if costo_actual < costo_minimo:
                costo_minimo = costo_actual
                padres[nodo] = sucesores if isinstance(sucesores, tuple) else [sucesores]

        costos[nodo] = costo_minimo
        if costo_minimo != float('inf'):
            resueltos.add(nodo)
        return costo_minimo

    ao_estrella(inicio)
    if objetivo not in resueltos:
        return None

    # Reconstruir el camino solución
    camino = []
    pila = [inicio]
    while pila:
        actual = pila.pop()
        camino.append(actual)
        if actual == objetivo:
            break
        if actual in padres:
            pila.extend(padres[actual][::-1])  # Añadir en orden inverso para recorrer en orden
    return camino


# Ejemplo práctico para AO*
grafo_ao_estrella = {
    'A': [('B', 'C'), ('D')],  # A puede lograrse con (B AND C) OR D
    'B': [('E')],
    'C': [('F')],
    'D': [('F')],
    'E': [],
    'F': []
}
heuristica_ao_estrella = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 0, 'F': 0}
inicio_ao_estrella, objetivo_ao_estrella = 'A', 'F'
print("Camino AO*:", busqueda_ao_estrella(grafo_ao_estrella, inicio_ao_estrella, objetivo_ao_estrella, heuristica_ao_estrella))