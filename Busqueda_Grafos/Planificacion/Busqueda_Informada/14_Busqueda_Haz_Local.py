def busqueda_haz_local(grafo, inicio, objetivo, heuristica, ancho_haz=2, profundidad_maxima=100):
    """
    Algoritmo de Búsqueda de Haz Local.
    
    Este algoritmo busca una ruta desde un nodo inicial hasta un nodo objetivo en un grafo,
    utilizando una heurística para priorizar los nodos más prometedores. 
    Solo mantiene un número limitado de nodos en cada nivel (controlado por el ancho del haz).

    Parámetros:
    - grafo: Diccionario que representa el grafo, donde las claves son nodos y los valores son listas de vecinos.
    - inicio: Nodo inicial desde donde comienza la búsqueda.
    - objetivo: Nodo objetivo al que se desea llegar.
    - heuristica: Diccionario que asigna un valor heurístico a cada nodo.
    - ancho_haz: Número máximo de nodos a considerar en cada nivel (por defecto 2).
    - profundidad_maxima: Número máximo de niveles a explorar (por defecto 100).

    Retorna:
    - Una lista con la ruta desde el nodo inicial hasta el nodo objetivo, o None si no se encuentra una ruta.
    """
    from heapq import heappush, heappop  # Importamos funciones para manejar colas de prioridad

    # Inicializamos el nivel actual con el nodo inicial
    nivel_actual = [(0 + heuristica[inicio], inicio, [inicio])]  # (costo_total, nodo, ruta)
    visitados = set()  # Conjunto para rastrear nodos ya visitados

    # Iteramos hasta la profundidad máxima
    for _ in range(profundidad_maxima):
        siguiente_nivel = []  # Lista para almacenar los nodos del siguiente nivel

        # Procesamos cada nodo en el nivel actual
        for puntaje, nodo, ruta in nivel_actual:
            # Si encontramos el nodo objetivo, devolvemos la ruta
            if nodo == objetivo:
                return ruta

            # Si el nodo ya fue visitado, lo ignoramos
            if nodo in visitados:
                continue

            # Marcamos el nodo como visitado
            visitados.add(nodo)

            # Exploramos los vecinos del nodo actual
            for vecino in grafo[nodo]:
                nueva_ruta = ruta + [vecino]  # Extendemos la ruta actual
                costo_real = len(nueva_ruta)  # El costo real es el número de pasos
                costo_total = costo_real + heuristica[vecino]  # Costo total = costo real + heurística
                heappush(siguiente_nivel, (costo_total, vecino, nueva_ruta))  # Agregamos a la cola de prioridad

        # Limitamos el siguiente nivel al ancho del haz
        nivel_actual = siguiente_nivel[:ancho_haz]

    # Si no encontramos una ruta, devolvemos None
    return None


# Ejemplo práctico
if __name__ == "__main__":
    # Definimos un grafo como un diccionario
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": ["G"],
        "G": []
    }

    # Definimos una heurística para cada nodo
    heuristica = {
        "A": 6,
        "B": 4,
        "C": 4,
        "D": 3,
        "E": 2,
        "F": 2,
        "G": 0
    }

    # Llamamos al algoritmo de búsqueda de haz local
    ruta = busqueda_haz_local(grafo, inicio="A", objetivo="G", heuristica=heuristica, ancho_haz=2)

    # Mostramos el resultado
    if ruta:
        print("Ruta encontrada:", " -> ".join(ruta))
    else:
        print("No se encontró una ruta.")