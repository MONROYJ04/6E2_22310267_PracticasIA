#Se hara un algoritmo de busqueda en profundidad (DFS) para encontrar un camino en un grafo.
# Importamos el módulo deque de collections para una implementación eficiente de pila
from collections import deque

def dfs(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda en Profundidad (DFS) para encontrar un camino en un grafo.
    
    DFS explora un grafo yendo lo más profundo posible desde el nodo inicial antes de retroceder.
    Es útil cuando la solución puede estar en niveles profundos del grafo.
    
    Parámetros:
        grafo (dict): Diccionario que representa el grafo como lista de adyacencia.
                     Formato: {'A': ['B', 'C'], 'B': ['A', 'D']}
        inicio (str): Nodo desde donde comenzar la búsqueda
        objetivo (str): Nodo que queremos encontrar
    
    Retorna:
        list: Camino desde el inicio hasta el objetivo si existe, None en caso contrario
    """
    
    # Inicializamos una pila (LIFO) con el nodo inicial y su camino (que solo lo contiene a él)
    # Usamos deque para implementar la pila de manera eficiente
    pila = deque()
    pila.append((inicio, [inicio]))
    
    # Conjunto para registrar nodos ya visitados y evitar ciclos infinitos
    visitados = set()
    
    print(f"\nIniciando DFS desde el nodo '{inicio}' hacia '{objetivo}'")
    print(f"Pila inicial: {list(pila)}")
    print(f"Visitados inicial: {visitados}\n")
    
    # Mientras haya nodos en la pila para explorar
    while pila:
        # Extraemos el último nodo añadido (LIFO - Last In, First Out)
        nodo_actual, camino = pila.pop()
        
        print(f"\nNodo actual: {nodo_actual} | Camino: {camino}")
        
        # Si encontramos el nodo objetivo, retornamos el camino
        if nodo_actual == objetivo:
            print(f"\n¡Objetivo '{objetivo}' encontrado!")
            return camino
        
        # Si el nodo no ha sido visitado aún
        if nodo_actual not in visitados:
            # Marcamos el nodo como visitado
            visitados.add(nodo_actual)
            print(f"Marcando nodo {nodo_actual} como visitado")
            
            # Exploramos todos los vecinos del nodo actual
            # Los añadimos en orden inverso para mantener un orden natural en la pila
            for vecino in reversed(grafo[nodo_actual]):
                if vecino not in visitados:
                    # Creamos un nuevo camino extendiendo el actual
                    nuevo_camino = camino + [vecino]
                    # Añadimos el vecino a la pila para explorarlo después
                    pila.append((vecino, nuevo_camino))
                    print(f"Añadiendo a la pila: {vecino} | Camino: {nuevo_camino}")
    
    # Si la pila se vacía sin encontrar el objetivo
    print("\nEl objetivo no fue encontrado en el grafo.")
    return None

# Definición del grafo de ejemplo (lista de adyacencia)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Visualización del grafo:
#       A
#      / \
#     B   C
#    / \   \
#   D   E - F

if __name__ == "__main__":
    print("=== Algoritmo de Búsqueda en Profundidad (DFS) ===")
    print("Grafo:", grafo)
    
    inicio = 'A'
    objetivo = 'F'
    
    print(f"\nBuscando camino desde '{inicio}' hasta '{objetivo}'...")
    camino = dfs(grafo, inicio, objetivo)
    
    print("\n--- Resultado Final ---")
    if camino:
        print(f"Camino encontrado: {camino}")
    else:
        print("No se encontró un camino al objetivo.")