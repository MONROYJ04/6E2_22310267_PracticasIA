from collections import deque

def busqueda_tabu(grafo, inicio, heuristica, tamano_tabu=3, max_iteraciones=100):
    """
    Implementación del algoritmo de Búsqueda Tabú.
    
    Parámetros:
    - grafo: Diccionario que representa el grafo, donde las claves son nodos y los valores son listas de vecinos.
    - inicio: Nodo inicial desde donde comienza la búsqueda.
    - heuristica: Diccionario que asigna un valor heurístico a cada nodo (menor es mejor).
    - tamano_tabu: Tamaño máximo de la lista tabú (número de nodos prohibidos).
    - max_iteraciones: Número máximo de iteraciones para ejecutar el algoritmo.
    
    Retorna:
    - El mejor nodo encontrado según la heurística.
    """
    actual = inicio  # Nodo actual en la búsqueda
    mejor = actual  # Mejor nodo encontrado hasta ahora
    lista_tabu = deque(maxlen=tamano_tabu)  # Lista tabú para evitar ciclos
    mejores_candidatos = []  # Lista para almacenar los mejores nodos encontrados

    for _ in range(max_iteraciones):
        # Obtener los vecinos del nodo actual que no están en la lista tabú
        vecinos = [n for n in grafo[actual] if n not in lista_tabu]
        
        # Si no hay vecinos válidos, relajar la restricción y considerar todos los vecinos
        if not vecinos:
            vecinos = grafo[actual]
        
        # Seleccionar el vecino con el menor valor heurístico
        actual = min(vecinos, key=lambda x: heuristica[x])
        
        # Criterio de aspiración: actualizar el mejor nodo si encontramos uno mejor
        if heuristica[actual] < heuristica[mejor]:
            mejor = actual
            mejores_candidatos.append(mejor)
        
        # Agregar el nodo actual a la lista tabú
        lista_tabu.append(actual)
    
    # Retornar el último mejor nodo encontrado o el mejor nodo global
    return mejores_candidatos[-1] if mejores_candidatos else mejor


# Ejemplo práctico
if __name__ == "__main__":
    # Definición de un grafo como un diccionario
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Valores heurísticos para cada nodo (menor es mejor)
    heuristica = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 1
    }

    # Llamar al algoritmo de Búsqueda Tabú
    nodo_inicial = 'A'
    mejor_nodo = busqueda_tabu(grafo, nodo_inicial, heuristica, tamano_tabu=3, max_iteraciones=10)

    # Imprimir el resultado
    print(f"El mejor nodo encontrado es: {mejor_nodo}")