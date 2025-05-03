def comprobacion_hacia_adelante(grafo, colores_disponibles, nodo_actual, asignacion_colores):
    """
    Algoritmo de Comprobación Hacia Adelante (Forward Checking).
    Este algoritmo verifica si la asignación de un color a un nodo es válida,
    reduciendo los dominios de los nodos vecinos y detectando conflictos.

    :param grafo: Diccionario que representa el grafo como lista de adyacencia.
    :param colores_disponibles: Lista de colores disponibles para asignar.
    :param nodo_actual: Nodo al que se le asignó un color.
    :param asignacion_colores: Diccionario con la asignación actual de colores {nodo: color}.
    :return: True si la asignación es válida, False si algún dominio queda vacío.
    """
    # Iterar sobre los vecinos del nodo actual
    for vecino in grafo[nodo_actual]:
        # Verificar si el vecino aún no tiene un color asignado
        if vecino not in asignacion_colores:
            # Crear una copia del dominio original de colores
            dominio_original = colores_disponibles.copy()
            
            # Filtrar los colores que son inconsistentes con el color asignado al nodo actual
            nuevo_dominio = [color for color in dominio_original if color != asignacion_colores[nodo_actual]]
            
            # Si el dominio del vecino queda vacío, la asignación es inválida
            if not nuevo_dominio:
                return False
            
            # Nota: En una implementación más avanzada, aquí se actualizaría el dominio del vecino.
            # En este caso, solo verificamos si hay conflictos inmediatos.
    return True

# Ejemplo práctico:
# Representación de un grafo donde los nodos son ciudades y las aristas indican que son vecinas
grafo = {
    'Ciudad1': ['Ciudad2', 'Ciudad3'],
    'Ciudad2': ['Ciudad1', 'Ciudad3', 'Ciudad4'],
    'Ciudad3': ['Ciudad1', 'Ciudad2', 'Ciudad4'],
    'Ciudad4': ['Ciudad2', 'Ciudad3']
}

# Lista de colores disponibles para colorear las ciudades
colores_disponibles = ['Rojo', 'Verde', 'Azul']

# Asignación inicial de colores (asignamos 'Rojo' a 'Ciudad1')
asignacion_colores = {'Ciudad1': 'Rojo'}

# Aplicamos el algoritmo de Comprobación Hacia Adelante
es_valida = comprobacion_hacia_adelante(grafo, colores_disponibles, 'Ciudad1', asignacion_colores)

# Imprimimos el resultado
print(f"¿La asignación es válida después de la Comprobación Hacia Adelante? {es_valida}")

# Explicación del ejemplo:
# - 'Ciudad1' tiene asignado el color 'Rojo'.
# - Los vecinos de 'Ciudad1' son 'Ciudad2' y 'Ciudad3'.
# - El color 'Rojo' se elimina del dominio de 'Ciudad2' y 'Ciudad3'.
# - Si el dominio de algún vecino queda vacío, la asignación no es válida.