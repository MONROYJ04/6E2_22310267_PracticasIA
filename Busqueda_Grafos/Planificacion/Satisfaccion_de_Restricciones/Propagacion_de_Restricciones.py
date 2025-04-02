from collections import deque

def ac3(graph, domains):
    """
    Algoritmo AC-3 para propagación de restricciones.
    :param graph: Grafo como diccionario de adyacencia (ej: {'A': ['B', 'C'], ...}).
    :param domains: Diccionario de dominios de cada variable (ej: {'A': ['Red', 'Green'], ...}).
    :return: Dominios actualizados (consistencia) o False si no hay solución.
    """
    queue = deque()
    # Inicializar la cola con todas las restricciones (aristas del grafo)
    for node in graph:
        for neighbor in graph[node]:
            queue.append((node, neighbor))

    while queue:
        (xi, xj) = queue.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False  # Dominio vacío → no hay solución
            for xk in graph[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return domains

def revise(domains, xi, xj):
    """
    Verifica si el dominio de xi necesita ser reducido debido a xj.
    :return: True si se modificó el dominio de xi.
    """
    revised = False
    for color in domains[xi].copy():
        # Si no hay color en xj que satisfaga la restricción xi != xj
        if all(color == c for c in domains[xj]):
            domains[xi].remove(color)
            revised = True
    return revised

# Ejemplo de uso:
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

domains = {
    'WA': ['Red', 'Green', 'Blue'],
    'NT': ['Red', 'Green', 'Blue'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q': ['Red', 'Green', 'Blue'],
    'NSW': ['Red', 'Green', 'Blue'],
    'V': ['Red', 'Green', 'Blue']
}

result = ac3(graph, domains)
print("Dominios después de AC-3:")
for node, colors in result.items():
    print(f"{node}: {colors}")