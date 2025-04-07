# Este programa implementa un algoritmo de Búsqueda en Profundidad Limitada (DLS) para encontrar un camino en un grafo.

def busqueda_profundidad_limitada(grafo, inicio, objetivo, limite_profundidad):
    """
    Algoritmo de Búsqueda en Profundidad Limitada (DLS).
    :param grafo: Grafo representado como un diccionario de listas de adyacencia.
    :param inicio: Nodo desde donde comienza la búsqueda.
    :param objetivo: Nodo que queremos encontrar.
    :param limite_profundidad: Profundidad máxima permitida para la búsqueda.
    :return: Lista con el camino desde 'inicio' hasta 'objetivo' si existe, de lo contrario None.
    """
    # Usamos una pila (stack) para realizar la búsqueda en profundidad.
    # Cada elemento de la pila es una tupla (nodo_actual, profundidad_actual, camino_actual).
    pila = [(inicio, 0, [inicio])]
    visitados = set()  # Conjunto para rastrear los nodos visitados.

    # Mientras haya nodos en la pila, seguimos explorando.
    while pila:
        # Extraemos el último nodo añadido a la pila (LIFO: Last In, First Out).
        nodo_actual, profundidad_actual, camino_actual = pila.pop()
        
        # Si encontramos el nodo objetivo, devolvemos el camino.
        if nodo_actual == objetivo:
            return camino_actual
        
        # Si la profundidad actual supera el límite, no expandimos este nodo.
        if profundidad_actual >= limite_profundidad:
            continue
        
        # Si el nodo actual no ha sido visitado, lo marcamos como visitado.
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            # Recorremos los vecinos del nodo actual en orden inverso para mantener un orden natural.
            for vecino in reversed(grafo[nodo_actual]):
                # Si el vecino no ha sido visitado, lo añadimos a la pila con la nueva profundidad y camino.
                if vecino not in visitados:
                    pila.append((vecino, profundidad_actual + 1, camino_actual + [vecino]))
    
    # Si no encontramos el nodo objetivo, devolvemos None.
    return None

# Ejemplo práctico:
# Definimos un grafo como un diccionario donde las claves son nodos y los valores son listas de nodos vecinos.
grafo_ejemplo = {
    'A': ['B', 'C'],  # El nodo 'A' tiene como vecinos a 'B' y 'C'.
    'B': ['D', 'E'],  # El nodo 'B' tiene como vecinos a 'D' y 'E'.
    'C': ['F'],       # El nodo 'C' tiene como vecino a 'F'.
    'D': [],          # El nodo 'D' no tiene vecinos.
    'E': ['F'],       # El nodo 'E' tiene como vecino a 'F'.
    'F': []           # El nodo 'F' no tiene vecinos.
}

# Definimos los parámetros de la búsqueda.
nodo_inicio = 'A'       # Nodo desde donde comenzamos la búsqueda.
nodo_objetivo = 'F'     # Nodo que queremos encontrar.
limite_profundidad = 2  # Límite máximo de profundidad para la búsqueda.

# Llamamos a la función de búsqueda en profundidad limitada.
camino_encontrado = busqueda_profundidad_limitada(grafo_ejemplo, nodo_inicio, nodo_objetivo, limite_profundidad)

# Mostramos el resultado.
if camino_encontrado:
    print(f"Camino encontrado (DLS, limite={limite_profundidad}): {camino_encontrado}")
else:
    print(f"No se encontró un camino desde '{nodo_inicio}' hasta '{nodo_objetivo}' con un límite de profundidad de {limite_profundidad}.")

# Explicación del ejemplo:
# En este caso, el grafo tiene un camino desde 'A' hasta 'F' a través de 'C'.
# Sin embargo, con un límite de profundidad de 2, no es posible alcanzar 'F' desde 'A'.
# Si aumentamos el límite de profundidad a 3, el algoritmo encontrará el camino ['A', 'C', 'F'].