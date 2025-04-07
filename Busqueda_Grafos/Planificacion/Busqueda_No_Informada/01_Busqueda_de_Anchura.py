# Algoritmo de busqueda de anchura (BFS) para encontrar el camino mas corto entre dos nodos en un grafo.

# Importamos 'deque' de la biblioteca 'collections' para usar una cola eficiente.
# Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out).
from collections import deque

def busqueda_anchura(grafo, inicio, objetivo):
    """
    Implementacion del algoritmo BFS para encontrar un camino en un grafo.

    Parametros:
        grafo (dict): Diccionario donde las claves son nodos y los valores son listas de nodos vecinos.
        inicio (str): Nodo desde donde comenzamos la busqueda.
        objetivo (str): Nodo que queremos alcanzar.

    Retorna:
        list: Camino desde 'inicio' hasta 'objetivo' si existe, o None si no.
    """
    
    # Inicializamos una cola con una tupla: (nodo_actual, camino_hasta_ahora).
    # La cola es una estructura FIFO (First In, First Out), ideal para explorar niveles de un grafo.
    cola = deque([(inicio, [inicio])])
    
    # Conjunto para registrar nodos ya visitados y evitar ciclos infinitos.
    # Usamos un conjunto porque permite verificar si un nodo ya fue visitado de manera eficiente.
    visitados = set()
    visitados.add(inicio)  # Marcamos el nodo inicial como visitado.
    
    # Imprimimos el estado inicial de la busqueda.
    print(f"\n[Inicio] Busqueda de anchura desde '{inicio}' hacia '{objetivo}':")
    print(f" - Cola inicial: {list(cola)}")  # Mostramos el contenido inicial de la cola.
    print(f" - Visitados inicial: {visitados}\n")  # Mostramos los nodos visitados inicialmente.
    
    # Mientras haya nodos en la cola, seguimos explorando.
    while cola:
        # Extraemos el primer elemento de la cola (FIFO).
        nodo_actual, camino = cola.popleft()
        
        # Mostramos el nodo que estamos explorando y el camino recorrido hasta ahora.
        print(f"[Explorando] Nodo actual: '{nodo_actual}' | Camino recorrido: {camino}")
        
        # Si el nodo actual es el objetivo, retornamos el camino.
        if nodo_actual == objetivo:
            print(f"\n[Exito] ¡Objetivo '{objetivo}' encontrado!")
            print(f" - Camino final: {camino}")
            return camino
        
        # Recorremos todos los vecinos del nodo actual.
        for vecino in grafo[nodo_actual]:
            # Si el vecino no ha sido visitado...
            if vecino not in visitados:
                # Marcamos el vecino como visitado para evitar explorarlo nuevamente.
                visitados.add(vecino)
                
                # Construimos un nuevo camino que incluye al vecino.
                nuevo_camino = camino + [vecino]
                
                # Añadimos el vecino y el nuevo camino a la cola para explorarlo mas adelante.
                cola.append((vecino, nuevo_camino))
                
                # Mostramos el estado actualizado de la cola y los nodos visitados.
                print(f"[Actualizando] Añadiendo vecino: '{vecino}' a la cola.")
                print(f" - Nuevo camino: {nuevo_camino}")
                print(f" - Cola actualizada: {list(cola)}")
                print(f" - Visitados actualizados: {visitados}\n")
    
    # Si la cola se vacia y no encontramos el objetivo, significa que no hay camino.
    print("\n[Fin] El objetivo no fue encontrado en el grafo.")
    return None

# --- Definicion del grafo (ejemplo) ---
# Un grafo es una estructura de datos que representa conexiones entre nodos.
# En este caso, usamos un diccionario donde las claves son nodos y los valores son listas de nodos vecinos.
grafo = {
    'Casa': ['Escuela', 'Supermercado'],  # 'Casa' esta conectada a 'Escuela' y 'Supermercado'.
    'Escuela': ['Casa', 'Parque'],       # 'Escuela' esta conectada a 'Casa' y 'Parque'.
    'Supermercado': ['Casa', 'Hospital'], # 'Supermercado' esta conectado a 'Casa' y 'Hospital'.
    'Parque': ['Escuela'],               # 'Parque' esta conectado a 'Escuela'.
    'Hospital': ['Supermercado', 'Parque'] # 'Hospital' esta conectado a 'Supermercado' y 'Parque'.
}

# Ejemplo practico:
# Imaginemos que queremos encontrar el camino mas corto desde nuestra 'Casa' hasta el 'Hospital'.
# Visualizacion del grafo:
#       Casa
#      /    \
#  Escuela  Supermercado
#     |         |
#  Parque    Hospital

# --- Ejecucion ---
if __name__ == "__main__":
    # Nodo inicial desde donde comenzamos la busqueda.
    inicio = 'Casa'
    # Nodo objetivo que queremos alcanzar.
    objetivo = 'Hospital'
    
    print("=== Simulacion de Busqueda de Anchura ===")
    print(f"Grafo: {grafo}")
    print(f"Inicio: '{inicio}' | Objetivo: '{objetivo}'\n")
    
    # Llamamos a la funcion de busqueda de anchura.
    camino = busqueda_anchura(grafo, inicio, objetivo)
    
    # Mostramos el resumen final del resultado.
    print("\n--- Resumen ---")
    print(f"Camino encontrado: {camino}")