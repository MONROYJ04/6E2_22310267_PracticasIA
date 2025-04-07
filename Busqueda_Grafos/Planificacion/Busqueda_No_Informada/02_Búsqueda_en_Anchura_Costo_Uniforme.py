# En este codigo se implementa la busqueda en anchura con costo uniforme (UCS).

import heapq  # Importamos heapq para usar una cola de prioridad.

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    """
    Implementacion del algoritmo de Busqueda de Costo Uniforme (UCS).
    
    UCS encuentra el camino de menor costo desde un nodo inicial hasta un nodo objetivo
    en un grafo donde las conexiones (aristas) tienen costos asociados.
    
    Parametros:
        grafo (dict): Diccionario donde las claves son nodos y los valores son
                      diccionarios de nodos vecinos con sus respectivos costos.
                      Ejemplo: {'A': {'B': 1, 'C': 3}}
        inicio (str): Nodo desde donde comienza la busqueda.
        objetivo (str): Nodo que queremos alcanzar.
    
    Retorna:
        tuple: (costo_total, camino) si se encuentra el objetivo, o None si no se encuentra.
    """
    
    # Inicializamos la cola de prioridad (estructura que siempre extrae el elemento con menor costo).
    # Cada elemento de la cola es una tupla: (costo_acumulado, nodo_actual, camino_recorrido).
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio, [inicio]))  # Insertamos el nodo inicial con costo 0.
    
    # Conjunto para registrar los nodos ya visitados y evitar procesarlos nuevamente.
    visitados = set()
    
    # Mostramos el estado inicial de la busqueda.
    print(f"\n[Inicio] Busqueda de Costo Uniforme desde '{inicio}' hacia '{objetivo}'")
    print(f" - Cola inicial: {cola_prioridad}")
    
    # Mientras haya nodos en la cola de prioridad, seguimos explorando.
    while cola_prioridad:
        # Extraemos el nodo con el menor costo acumulado (propiedad de la cola de prioridad).
        costo_actual, nodo_actual, camino = heapq.heappop(cola_prioridad)
        
        # Mostramos el nodo que estamos explorando y el costo acumulado hasta ahora.
        print(f"\n[Explorando] Nodo actual: '{nodo_actual}' | Costo acumulado: {costo_actual} | Camino: {camino}")
        
        # Si el nodo actual es el objetivo, hemos encontrado el camino de menor costo.
        if nodo_actual == objetivo:
            print(f"\n[Exito] ¡Objetivo '{objetivo}' encontrado con costo total {costo_actual}!")
            return (costo_actual, camino)
        
        # Si el nodo actual no ha sido visitado, lo procesamos.
        if nodo_actual not in visitados:
            # Marcamos el nodo como visitado para evitar explorarlo nuevamente.
            visitados.add(nodo_actual)
            print(f" - Marcando nodo '{nodo_actual}' como visitado.")
            
            # Recorremos todos los vecinos del nodo actual.
            for vecino, costo_arista in grafo[nodo_actual].items():
                # Si el vecino no ha sido visitado, lo añadimos a la cola de prioridad.
                if vecino not in visitados:
                    # Calculamos el nuevo costo acumulado al llegar al vecino.
                    nuevo_costo = costo_actual + costo_arista
                    # Construimos el nuevo camino que incluye al vecino.
                    nuevo_camino = camino + [vecino]
                    # Añadimos el vecino a la cola de prioridad con su costo acumulado.
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino, nuevo_camino))
                    print(f"   - Añadiendo vecino '{vecino}' con costo {nuevo_costo} y camino {nuevo_camino}.")
    
    # Si la cola de prioridad se vacia y no encontramos el objetivo, no hay camino posible.
    print("\n[Fin] No se encontro un camino hacia el objetivo.")
    return None

# --- Ejemplo de grafo con costos ---
# Este grafo representa lugares conectados por caminos con costos asociados (por ejemplo, distancias).
grafo_con_costos = {
    'Casa': {'Escuela': 2, 'Supermercado': 5},
    'Escuela': {'Casa': 2, 'Parque': 3},
    'Supermercado': {'Casa': 5, 'Hospital': 6},
    'Parque': {'Escuela': 3, 'Hospital': 2},
    'Hospital': {'Supermercado': 6, 'Parque': 2}
}

# Visualizacion del grafo con costos:
#       Casa
#     2/    \5
#  Escuela  Supermercado
#    3|         |6
#  Parque ---- Hospital
#       2

# --- Ejecucion ---
if __name__ == "__main__":
    print("=== Busqueda de Costo Uniforme (UCS) ===")
    print("Grafo con costos:", grafo_con_costos)
    
    # Nodo inicial desde donde comenzamos la busqueda.
    inicio = 'Casa'
    # Nodo objetivo que queremos alcanzar.
    objetivo = 'Hospital'
    
    # Llamamos a la funcion de busqueda de costo uniforme.
    resultado = busqueda_costo_uniforme(grafo_con_costos, inicio, objetivo)
    
    # Mostramos el resumen final del resultado.
    print("\n--- Resultado Final ---")
    if resultado:
        costo_total, camino = resultado
        print(f"Camino encontrado: {camino} con costo total: {costo_total}")
    else:
        print("No se encontro un camino al objetivo.")