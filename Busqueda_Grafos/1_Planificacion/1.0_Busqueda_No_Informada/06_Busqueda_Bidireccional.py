# Algoritmo de Búsqueda Bidireccional
# Este algoritmo busca un camino entre dos nodos (inicio y objetivo) en un grafo.
# Lo hace expandiendo nodos desde ambos extremos (inicio y objetivo) simultáneamente
# hasta que las dos búsquedas se encuentran.

from collections import deque  # Importamos deque para manejar las colas de nodos

def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Implementación de la búsqueda bidireccional.
    :param grafo: Grafo representado como un diccionario de listas de adyacencia.
    :param inicio: Nodo inicial desde donde comienza la búsqueda.
    :param objetivo: Nodo objetivo al que queremos llegar.
    :return: Camino desde inicio hasta objetivo si existe, None en caso contrario.
    """
    # Si el nodo inicial es el mismo que el objetivo, devolvemos el nodo como camino
    if inicio == objetivo:
        return [inicio]

    # Colas para realizar la búsqueda desde el inicio y el objetivo
    cola_inicio = deque([inicio])  # Cola para la búsqueda desde el inicio
    cola_objetivo = deque([objetivo])  # Cola para la búsqueda desde el objetivo

    # Diccionarios para registrar los padres de cada nodo y los nodos visitados
    padres_inicio = {inicio: None}  # Padres desde el inicio
    padres_objetivo = {objetivo: None}  # Padres desde el objetivo

    # Mientras ambas colas tengan elementos, seguimos buscando
    while cola_inicio and cola_objetivo:
        # Expansión desde el lado del inicio
        nodo_actual_inicio = cola_inicio.popleft()  # Sacamos el nodo actual de la cola
        for vecino in grafo[nodo_actual_inicio]:  # Iteramos sobre los vecinos del nodo actual
            if vecino not in padres_inicio:  # Si el vecino no ha sido visitado desde el inicio
                padres_inicio[vecino] = nodo_actual_inicio  # Registramos su padre
                cola_inicio.append(vecino)  # Agregamos el vecino a la cola
                # Si el vecino ya fue visitado desde el objetivo, encontramos el camino
                if vecino in padres_objetivo:
                    return combinar_caminos(padres_inicio, padres_objetivo, vecino)

        # Expansión desde el lado del objetivo
        nodo_actual_objetivo = cola_objetivo.popleft()  # Sacamos el nodo actual de la cola
        for vecino in grafo[nodo_actual_objetivo]:  # Iteramos sobre los vecinos del nodo actual
            if vecino not in padres_objetivo:  # Si el vecino no ha sido visitado desde el objetivo
                padres_objetivo[vecino] = nodo_actual_objetivo  # Registramos su padre
                cola_objetivo.append(vecino)  # Agregamos el vecino a la cola
                # Si el vecino ya fue visitado desde el inicio, encontramos el camino
                if vecino in padres_inicio:
                    return combinar_caminos(padres_inicio, padres_objetivo, vecino)

    # Si no se encuentra un camino, devolvemos None
    return None

def combinar_caminos(padres_inicio, padres_objetivo, nodo_encuentro):
    """
    Combina los caminos desde el inicio y el objetivo hasta el nodo de encuentro.
    :param padres_inicio: Diccionario de padres desde el inicio.
    :param padres_objetivo: Diccionario de padres desde el objetivo.
    :param nodo_encuentro: Nodo donde se encuentran las búsquedas.
    :return: Camino completo desde inicio hasta objetivo.
    """
    camino = []

    # Reconstruimos el camino desde el nodo de encuentro hasta el inicio
    nodo = nodo_encuentro
    while nodo is not None:
        camino.append(nodo)
        nodo = padres_inicio[nodo]
    camino = camino[::-1]  # Invertimos el camino para que sea inicio -> nodo_encuentro

    # Reconstruimos el camino desde el nodo de encuentro hasta el objetivo
    nodo = padres_objetivo[nodo_encuentro]
    while nodo is not None:
        camino.append(nodo)
        nodo = padres_objetivo[nodo]

    return camino

# Ejemplo práctico:
# Grafo representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],  # El nodo 'A' está conectado con 'B' y 'C'
    'B': ['A', 'D', 'E'],  # El nodo 'B' está conectado con 'A', 'D' y 'E'
    'C': ['A', 'F'],  # El nodo 'C' está conectado con 'A' y 'F'
    'D': ['B'],  # El nodo 'D' está conectado con 'B'
    'E': ['B', 'F'],  # El nodo 'E' está conectado con 'B' y 'F'
    'F': ['C', 'E']  # El nodo 'F' está conectado con 'C' y 'E'
}

# Definimos el nodo inicial y el nodo objetivo
inicio = 'A'
objetivo = 'F'

# Ejecutamos el algoritmo y mostramos el resultado
print("Camino bidireccional:", busqueda_bidireccional(grafo, inicio, objetivo))