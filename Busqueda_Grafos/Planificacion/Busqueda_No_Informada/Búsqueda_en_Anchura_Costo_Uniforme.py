#En este codigo se implementa la busqueda en anchura y el algoritmo de costo uniforme

import heapq  # Necesario para la cola de prioridad

def ucs(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda de Costo Uniforme (UCS).
    
    UCS es un algoritmo que encuentra el camino de menor costo desde un nodo inicial
    hasta un nodo objetivo en un grafo con costos en las aristas.
    
    Parámetros:
        grafo (dict): Diccionario donde las claves son nodos y los valores son
                     diccionarios de nodos vecinos con sus respectivos costos.
                     Ejemplo: {'A': {'B': 1, 'C': 3}}
        inicio (str): Nodo de inicio de la búsqueda
        objetivo (str): Nodo objetivo a encontrar
    
    Retorna:
        tuple: (costo_total, camino) si se encuentra el objetivo, None en caso contrario
    """
    
    # Inicializamos la cola de prioridad (heap) con el nodo inicial
    # Cada elemento es una tupla: (costo_acumulado, nodo_actual, camino)
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio, [inicio]))
    
    # Conjunto para llevar registro de nodos ya visitados
    visitados = set()
    
    print(f"\nIniciando UCS desde '{inicio}' hacia '{objetivo}'")
    print(f"Cola inicial: {cola_prioridad}")
    
    while cola_prioridad:
        # Extraemos el nodo con menor costo acumulado
        costo, nodo, camino = heapq.heappop(cola_prioridad)
        
        print(f"\nNodo actual: {nodo} | Costo acumulado: {costo} | Camino: {camino}")
        
        # Si encontramos el objetivo, retornamos el resultado
        if nodo == objetivo:
            print(f"\n¡Objetivo '{objetivo}' encontrado con costo {costo}!")
            return (costo, camino)
        
        if nodo not in visitados:
            # Marcamos el nodo como visitado
            visitados.add(nodo)
            print(f"Marcando nodo {nodo} como visitado")
            
            # Exploramos todos los vecinos del nodo actual
            for vecino, costo_arista in grafo[nodo].items():
                if vecino not in visitados:
                    # Calculamos el nuevo costo acumulado
                    nuevo_costo = costo + costo_arista
                    # Creamos el nuevo camino
                    nuevo_camino = camino + [vecino]
                    # Añadimos a la cola de prioridad
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino, nuevo_camino))
                    print(f"Añadiendo vecino {vecino} con costo {nuevo_costo} y camino {nuevo_camino}")
    
    # Si llegamos aquí, no se encontró el objetivo
    print("\nEl objetivo no fue encontrado en el grafo.")
    return None

# Ejemplo de grafo con costos
grafo_con_costos = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# Visualización del grafo con costos:
#        A
#     1/   \4
#     B     C
#  2/ \5  3/
# D     E
#     1/
#       F

if __name__ == "__main__":
    print("=== Búsqueda de Costo Uniforme (UCS) ===")
    print("Grafo con costos:", grafo_con_costos)
    
    inicio = 'A'
    objetivo = 'F'
    resultado = ucs(grafo_con_costos, inicio, objetivo)
    
    print("\n--- Resultado Final ---")
    if resultado:
        costo, camino = resultado
        print(f"Camino encontrado: {camino} con costo total: {costo}")
    else:
        print("No se encontró un camino al objetivo.")