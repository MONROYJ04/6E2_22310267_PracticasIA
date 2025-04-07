# Algoritmo de Búsqueda en Profundidad (DFS) para encontrar un camino en un grafo.
# Este algoritmo explora un grafo yendo lo más profundo posible desde un nodo inicial antes de retroceder.

# Importamos deque del módulo collections para usarlo como una pila eficiente
from collections import deque

def dfs(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda en Profundidad (DFS) para encontrar un camino en un grafo.
    
    Parámetros:
        grafo (dict): Representación del grafo como lista de adyacencia.
                      Ejemplo: {'A': ['B', 'C'], 'B': ['A', 'D']}
        inicio (str): Nodo desde donde comienza la búsqueda.
        objetivo (str): Nodo que queremos encontrar.
    
    Retorna:
        list: Camino desde el nodo inicial hasta el objetivo si existe, o None si no se encuentra.
    """
    
    # Creamos una pila (estructura LIFO - Last In, First Out) para almacenar los nodos por explorar.
    pila = deque()
    # Añadimos el nodo inicial a la pila junto con el camino recorrido hasta él (inicialmente solo contiene el nodo inicial).
    pila.append((inicio, [inicio]))
    
    # Creamos un conjunto para registrar los nodos visitados y evitar ciclos infinitos.
    visitados = set()
    
    # Imprimimos el estado inicial de la pila y los nodos visitados.
    print(f"\nIniciando DFS desde el nodo '{inicio}' hacia '{objetivo}'")
    print(f"Pila inicial: {list(pila)}")
    print(f"Visitados inicial: {visitados}\n")
    
    # Mientras haya nodos en la pila para explorar
    while pila:
        # Extraemos el último nodo añadido a la pila (LIFO).
        nodo_actual, camino = pila.pop()
        
        # Mostramos el nodo actual y el camino recorrido hasta él.
        print(f"\nNodo actual: {nodo_actual} | Camino: {camino}")
        
        # Si el nodo actual es el objetivo, retornamos el camino.
        if nodo_actual == objetivo:
            print(f"\n¡Objetivo '{objetivo}' encontrado!")
            return camino
        
        # Si el nodo actual no ha sido visitado
        if nodo_actual not in visitados:
            # Marcamos el nodo como visitado.
            visitados.add(nodo_actual)
            print(f"Marcando nodo {nodo_actual} como visitado")
            
            # Recorremos los vecinos del nodo actual en orden inverso para mantener el orden natural en la pila.
            for vecino in reversed(grafo[nodo_actual]):
                if vecino not in visitados:
                    # Creamos un nuevo camino extendiendo el camino actual con el vecino.
                    nuevo_camino = camino + [vecino]
                    # Añadimos el vecino a la pila para explorarlo más tarde.
                    pila.append((vecino, nuevo_camino))
                    print(f"Añadiendo a la pila: {vecino} | Camino: {nuevo_camino}")
    
    # Si la pila se vacía sin encontrar el objetivo, retornamos None.
    print("\nEl objetivo no fue encontrado en el grafo.")
    return None

# Ejemplo práctico: Definimos un grafo como lista de adyacencia.
grafo = {
    'A': ['B', 'C'],  # El nodo 'A' está conectado con 'B' y 'C'.
    'B': ['A', 'D', 'E'],  # El nodo 'B' está conectado con 'A', 'D' y 'E'.
    'C': ['A', 'F'],  # El nodo 'C' está conectado con 'A' y 'F'.
    'D': ['B'],  # El nodo 'D' está conectado con 'B'.
    'E': ['B', 'F'],  # El nodo 'E' está conectado con 'B' y 'F'.
    'F': ['C', 'E']  # El nodo 'F' está conectado con 'C' y 'E'.
}

# Representación visual del grafo:
#       A
#      / \
#     B   C
#    / \   \
#   D   E - F

if __name__ == "__main__":
    print("=== Algoritmo de Búsqueda en Profundidad (DFS) ===")
    print("Grafo:", grafo)
    
    # Nodo inicial y nodo objetivo
    inicio = 'A'
    objetivo = 'F'
    
    # Mostramos el propósito de la búsqueda.
    print(f"\nBuscando camino desde '{inicio}' hasta '{objetivo}'...")
    
    # Llamamos a la función DFS para encontrar el camino.
    camino = dfs(grafo, inicio, objetivo)
    
    # Mostramos el resultado final.
    print("\n--- Resultado Final ---")
    if camino:
        print(f"Camino encontrado: {camino}")
    else:
        print("No se encontró un camino al objetivo.")