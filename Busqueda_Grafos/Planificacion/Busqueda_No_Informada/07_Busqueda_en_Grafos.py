# Se realizará un algoritmo de búsqueda en grafos, el cual es un algoritmo de búsqueda en amplitud.

# Búsqueda en Grafos (evitando estados repetidos)
# Utiliza una lista de visitados para evitar ciclos.

def busqueda_grafos(grafo, inicio, objetivo):
    """
    Búsqueda en amplitud (BFS) evitando estados repetidos.
    :param grafo: grafo como diccionario de listas de adyacencia.
    :param inicio: nodo inicial.
    :param objetivo: nodo objetivo.
    :return: camino desde inicio hasta objetivo, o None si no se encuentra.
    """
    from collections import deque

    visitados = set()      # Nodos ya visitados
    cola = deque()         # Cola para BFS
    padres = {}            # Diccionario para reconstruir el camino

    cola.append(inicio)    # Agregamos el nodo inicial a la cola
    visitados.add(inicio)  # Marcamos el nodo inicial como visitado
    padres[inicio] = None  # El nodo inicial no tiene un nodo padre

    while cola:
        actual = cola.popleft()  # Extraemos el nodo al frente de la cola
        if actual == objetivo:
            # Reconstruir el camino
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            return camino[::-1]  # Invertir para obtener inicio -> objetivo

        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)       # Marcamos el vecino como visitado
                padres[vecino] = actual    # Registramos el nodo actual como padre del vecino
                cola.append(vecino)        # Agregamos el vecino a la cola
    return None

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
inicio = 'A'
objetivo = 'F'
print("Camino encontrado:", busqueda_grafos(grafo, inicio, objetivo))