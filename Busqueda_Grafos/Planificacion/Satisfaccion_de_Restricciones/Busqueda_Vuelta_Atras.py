def backtracking_sudoku(grid):
    """
    Resuelve un Sudoku usando backtracking.
    :param grid: Matriz 9x9 representando el Sudoku (0 = casilla vacía).
    :return: Matriz resuelta o None si no hay solución.
    """
    # Encuentra la próxima casilla vacía (función select_unassigned_variable)
    row, col = find_empty_cell(grid)
    
    # Si no hay casillas vacías, el Sudoku está resuelto
    if row == -1:
        return grid
    
    # Prueba números del 1 al 9 (función order_domain_values)
    for num in range(1, 10):
        # Verifica si el número es válido (función is_consistent)
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Asigna el número
            
            # Llama recursivamente a backtracking
            if backtracking_sudoku(grid):
                return grid
            
            # Si no lleva a una solución, deshace el cambio (backtrack)
            grid[row][col] = 0
    
    return None  # No hay solución

# Funciones auxiliares:

def find_empty_cell(grid):
    """Selecciona la próxima casilla vacía (select_unassigned_variable)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return -1, -1  # Si no hay casillas vacías

def is_valid(grid, row, col, num):
    """Verifica si num es válido en (row, col) (is_consistent)."""
    # Verifica fila y columna
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    # Verifica subcuadrícula 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Ejemplo de uso:
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved = backtracking_sudoku(sudoku_grid)
if solved:
    for row in solved:
        print(row)
else:
    print("No hay solución")