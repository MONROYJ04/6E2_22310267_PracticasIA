import random

def min_conflicts(n, max_steps=1000):
    """
    Resuelve el problema de las N-Reinas usando Mínimos-Conflictos.
    :param n: Tamaño del tablero (n x n).
    :param max_steps: Número máximo de iteraciones.
    :return: Una asignación de reinas (fila para cada columna) o None si no se encuentra solución.
    """
    # Inicialización aleatoria: cada reina en una fila aleatoria de su columna
    assignment = [random.randint(0, n-1) for _ in range(n)]
    
    for _ in range(max_steps):
        conflicted_columns = find_conflicted_columns(assignment, n)
        if not conflicted_columns:
            return assignment  # Solución encontrada
        
        # Selecciona una columna conflictiva al azar
        col = random.choice(conflicted_columns)
        
        # Encuentra la fila con mínimos conflictos para esta columna
        min_conflict_row = find_min_conflict_row(assignment, col, n)
        
        # Mueve la reina a la fila con menos conflictos
        assignment[col] = min_conflict_row
    
    return None  # No se encontró solución en max_steps

def find_conflicted_columns(assignment, n):
    """
    Encuentra todas las columnas con reinas en conflicto.
    :return: Lista de columnas conflictivas.
    """
    conflicted = []
    for col in range(n):
        if is_conflicted(assignment, col, n):
            conflicted.append(col)
    return conflicted

def is_conflicted(assignment, col, n):
    """
    Verifica si la reina en 'col' está en conflicto con otras.
    """
    row = assignment[col]
    for other_col in range(n):
        if other_col == col:
            continue
        other_row = assignment[other_col]
        if other_row == row or abs(other_row - row) == abs(other_col - col):
            return True
    return False

def find_min_conflict_row(assignment, col, n):
    """
    Encuentra la fila en la columna 'col' que minimiza los conflictos.
    """
    min_conflicts = float('inf')
    candidates = []
    
    for row in range(n):
        conflicts = count_conflicts(assignment, col, row, n)
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            candidates = [row]
        elif conflicts == min_conflicts:
            candidates.append(row)
    
    return random.choice(candidates)  # Desempate aleatorio

def count_conflicts(assignment, col, row, n):
    """
    Cuenta cuántas reinas entran en conflicto si colocamos una reina en (col, row).
    """
    conflicts = 0
    for other_col in range(n):
        if other_col == col:
            continue
        other_row = assignment[other_col]
        if other_row == row or abs(other_row - row) == abs(other_col - col):
            conflicts += 1
    return conflicts

# Ejemplo de uso:
n = 8  # Tablero 8x8 (8 reinas)
solution = min_conflicts(n)
if solution:
    print(f"Solución encontrada para {n}-Reinas:")
    for col, row in enumerate(solution):
        print(f"Columna {col}: Fila {row}")
else:
    print("No se encontró solución en el número máximo de pasos.")