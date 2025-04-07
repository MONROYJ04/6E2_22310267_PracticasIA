# Este algoritmo implementa la busqueda en profundidad iterativa (IDS), 
# que combina las ventajas de la busqueda en profundidad (DFS) y la busqueda en amplitud (BFS).
# Es util para encontrar un camino en un grafo cuando no conocemos la profundidad del objetivo.

def busqueda_ids(grafo, inicio, objetivo): 
    """
    Implementacion de la Busqueda en Profundidad Iterativa (IDS).
    :param grafo: grafo representado como un diccionario de listas de adyacencia.
    :param inicio: nodo inicial desde donde comienza la busqueda.
    :param objetivo: nodo que queremos encontrar.
    :return: camino desde el nodo inicio hasta el nodo objetivo, o None si no se encuentra.
    """
    profundidad = 0  # Inicializamos la profundidad en 0
    while True:
        # Llamamos a la busqueda en profundidad limitada (DLS) con la profundidad actual
        resultado = busqueda_dls(grafo, inicio, objetivo, profundidad)
        if resultado is not None:  # Si encontramos el objetivo, devolvemos el camino
            return resultado
        profundidad += 1  # Incrementamos la profundidad para explorar niveles mas profundos

def busqueda_dls(grafo, nodo, objetivo, profundidad, camino=None):
    """
    Busqueda en Profundidad Limitada (DLS), utilizada por IDS.
    :param grafo: grafo representado como un diccionario de listas de adyacencia.
    :param nodo: nodo actual que estamos explorando.
    :param objetivo: nodo que queremos encontrar.
    :param profundidad: limite de profundidad para la busqueda.
    :param camino: lista que representa el camino recorrido hasta ahora.
    :return: camino si se encuentra el objetivo, None en caso contrario.
    """
    if camino is None:  # Si no hay un camino inicial, lo inicializamos como una lista vacia
        camino = []
    camino = camino + [nodo]  # Agregamos el nodo actual al camino
    if nodo == objetivo:  # Si el nodo actual es el objetivo, devolvemos el camino
        return camino
    if profundidad <= 0:  # Si alcanzamos el limite de profundidad, terminamos la busqueda
        return None
    # Recorremos los vecinos del nodo actual
    for vecino in grafo[nodo]:
        # Llamamos recursivamente a DLS con una profundidad reducida
        resultado = busqueda_dls(grafo, vecino, objetivo, profundidad - 1, camino)
        if resultado is not None:  # Si encontramos el objetivo en un vecino, devolvemos el camino
            return resultado
    return None  # Si no encontramos el objetivo, devolvemos None

# Ejemplo de uso:
# Representamos un grafo como un diccionario donde las claves son nodos y los valores son listas de vecinos
grafo = {
    'Casa': ['Escuela', 'Supermercado'],
    'Escuela': ['Parque', 'Biblioteca'],
    'Supermercado': ['Hospital'],
    'Parque': [],
    'Biblioteca': ['Hospital'],
    'Hospital': []
}
inicio = 'Casa'  # Nodo inicial
objetivo = 'Hospital'  # Nodo objetivo
print("Camino encontrado por IDS:", busqueda_ids(grafo, inicio, objetivo))

# Ejemplo practico:
# Imagina que estas en tu casa y necesitas llegar al hospital. 
# No sabes exactamente cuantas paradas intermedias hay, pero tienes un mapa de las conexiones posibles.
# Este algoritmo te ayuda a explorar todas las rutas posibles, comenzando con las mas cortas, 
# hasta encontrar el camino al hospital. 