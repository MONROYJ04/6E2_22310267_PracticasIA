def forward_checking(graph, colors, node, color_assignment):
    """
    Reduce los dominios de los nodos adyacentes al asignar un color a 'node'.
    :param graph: Grafo representado como diccionario de adyacencia.
    :param colors: Lista de colores disponibles.
    :param node: Nodo actual que se está coloreando.
    :param color_assignment: Diccionario con {nodo: color asignado}.
    :return: True si no hay conflictos, False si algún dominio queda vacío.
    """
    for neighbor in graph[node]:
        if neighbor not in color_assignment:
            # Filtra los colores del vecino que son inconsistentes con 'color_assignment[node]'
            original_domain = colors.copy()
            new_domain = [c for c in original_domain if c != color_assignment[node]]
            
            # Si el dominio del vecino queda vacío, la asignación es inválida
            if not new_domain:
                return False
            
            # Simulación: Actualiza el dominio del vecino (aquí se integraría con AC-3 en una versión avanzada)
            # En esta versión simplificada, solo verificamos conflictos inmediatos.
    return True

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
color_assignment = {'A': 'Red'}  # Asignamos 'Red' al nodo 'A'

# Aplicamos Forward Checking para ver si la asignación es válida
is_valid = forward_checking(graph, colors, 'A', color_assignment)
print(f"¿La asignación es válida después de Forward Checking? {is_valid}")