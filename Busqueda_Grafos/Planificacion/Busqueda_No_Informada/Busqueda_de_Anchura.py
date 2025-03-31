#Se hara un algoritmo de busqueda de anchura para encontrar el camino mas corto entre dos nodos en un grafo

# Importamos 'deque' de la biblioteca 'collections' para usar una cola eficiente.
# Las colas en Python son lentas si se usan listas, pero 'deque' es optimizado.
from collections import deque

def BFS(grafo, inicio, objetivo):
    """
    Función que implementa el algoritmo BFS para encontrar un camino en un grafo.
    
    Parámetros:
        grafo (dict): Diccionario donde las claves son nodos y los valores son listas de nodos vecinos.
        inicio (str): Nodo desde donde comenzamos la búsqueda.
        objetivo (str): Nodo que queremos alcanzar.
    
    Retorna:
        list: Camino desde 'inicio' hasta 'objetivo' si existe, o None si no.
    """
    
    # Inicializamos una cola con una tupla: (nodo_actual, camino_hasta_ahora)
    # Empezamos con el nodo inicial y un camino que solo lo contiene a él.
    cola = deque([(inicio, [inicio])])
    
    # Conjunto para registrar nodos ya visitados y evitar ciclos infinitos.
    visitados = set()
    visitados.add(inicio)  # Marcamos el nodo inicial como visitado.
    
    print(f"\n[Paso 1] Iniciando BFS desde el nodo '{inicio}' hacia '{objetivo}':")
    print(f" - Cola inicial: {list(cola)}")
    print(f" - Visitados inicial: {visitados}\n")
    
    # Mientras haya nodos en la cola, seguimos explorando.
    while cola:
        # Extraemos el primer elemento de la cola (FIFO: First In, First Out).
        nodo_actual, camino = cola.popleft()
        
        print(f"[Paso 2] Nodo actual: '{nodo_actual}' | Camino recorrido: {camino}")
        
        # Si el nodo actual es el objetivo, retornamos el camino.
        if nodo_actual == objetivo:
            print(f"\n[Paso 3] ¡Objetivo '{objetivo}' encontrado!")
            print(f" - Camino final: {camino}")
            return camino
        
        # Exploramos todos los vecinos del nodo actual.
        for vecino in grafo[nodo_actual]:
            # Si el vecino no ha sido visitado...
            if vecino not in visitados:
                visitados.add(vecino)  # Lo marcamos como visitado.
                nuevo_camino = camino + [vecino]  # Construimos el nuevo camino.
                cola.append((vecino, nuevo_camino))  # Añadimos a la cola.
                
                print(f"[Paso 4] Añadiendo vecino: '{vecino}' a la cola.")
                print(f" - Nuevo camino: {nuevo_camino}")
                print(f" - Cola actualizada: {list(cola)}")
                print(f" - Visitados actualizados: {visitados}\n")
    
    # Si la cola se vacía y no encontramos el objetivo...
    print("\n[Paso 5] El objetivo no fue encontrado en el grafo.")
    return None

# --- Definición del grafo (ejemplo) ---
grafo = {
    'A': ['B', 'C'],  # 'A' está conectado a 'B' y 'C'.
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

# --- Ejecución ---
if __name__ == "__main__":
    inicio = 'A'
    objetivo = 'F'
    print("=== Simulación de BFS ===")
    print(f"Grafo: {grafo}")
    print(f"Inicio: '{inicio}' | Objetivo: '{objetivo}'\n")
    
    camino = BFS(grafo, inicio, objetivo)
    
    print("\n--- Resumen ---")
    print(f"Camino encontrado: {camino}")