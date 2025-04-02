def conflict_directed_backjumping(csp, assignment={}):
    """
    Algoritmo CBJ para CSPs.
    :param csp: Diccionario con:
        - variables: Lista de variables.
        - domains: Diccionario de dominios {variable: [valores]}.
        - constraints: Función que retorna True si se cumplen las restricciones.
    :param assignment: Asignación actual {variable: valor}.
    :return: Asignación solución o None si no hay solución.
    """
    if len(assignment) == len(csp["variables"]):
        return assignment  # Solución encontrada

    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(csp, var, assignment):
        if is_consistent(csp, var, value, assignment):
            assignment[var] = value
            result = conflict_directed_backjumping(csp, assignment)
            if result is not None:
                return result
            del assignment[var]
        else:
            conflict_var = find_conflict(csp, var, value, assignment)
            if conflict_var != var:
                return None  # Salta al nivel del conflicto
    return None

# Funciones auxiliares:
def select_unassigned_variable(csp, assignment):
    """Selecciona la próxima variable sin asignar (heurística: MRV)."""
    unassigned = [v for v in csp["variables"] if v not in assignment]
    return min(unassigned, key=lambda v: len(csp["domains"][v]))  # MRV

def order_domain_values(csp, var, assignment):
    """Ordena los valores del dominio (heurística: LCV)."""
    return sorted(csp["domains"][var], key=lambda val: count_conflicts(csp, var, val, assignment))

def is_consistent(csp, var, value, assignment):
    """Verifica si 'value' es consistente con las restricciones."""
    assignment[var] = value  # Asignación temporal
    consistent = csp["constraints"](assignment)
    del assignment[var]  # Deshacer asignación temporal
    return consistent

def find_conflict(csp, var, value, assignment):
    """
    Encuentra la variable más reciente en el conflicto.
    :return: Variable en conflicto o 'var' si no hay conflicto previo.
    """
    assignment[var] = value  # Asignación temporal
    for v in reversed(list(assignment.keys())):  # De más reciente a más antigua
        if v == var:
            continue
        temp_assignment = assignment.copy()
        del temp_assignment[var]
        if not csp["constraints"](temp_assignment):
            del assignment[var]
            return v
    del assignment[var]
    return var

def count_conflicts(csp, var, value, assignment):
    """Cuenta conflictos potenciales para LCV."""
    assignment[var] = value
    conflicts = 0
    for neighbor in get_neighbors(csp, var):
        if neighbor not in assignment:
            for neighbor_value in csp["domains"][neighbor]:
                assignment[neighbor] = neighbor_value
                if not csp["constraints"](assignment):
                    conflicts += 1
                del assignment[neighbor]
    del assignment[var]
    return conflicts

def get_neighbors(csp, var):
    """Retorna variables relacionadas por restricciones (simulado)."""
    return [v for v in csp["variables"] if v != var]  # Todas las demás (ejemplo simplificado)

# Ejemplo de uso:
csp = {
    "variables": ["WA", "NT", "SA", "Q", "NSW", "V"],
    "domains": {
        "WA": ["Red", "Green", "Blue"],
        "NT": ["Red", "Green", "Blue"],
        "SA": ["Red", "Green", "Blue"],
        "Q": ["Red", "Green", "Blue"],
        "NSW": ["Red", "Green", "Blue"],
        "V": ["Red", "Green", "Blue"]
    },
    "constraints": lambda assignment: all(
        assignment.get(u) != assignment.get(v)
        for u in assignment
        for v in assignment
        if v in get_neighbors(csp, u)
    )
}

solution = conflict_directed_backjumping(csp)
print("Solución encontrada:", solution)