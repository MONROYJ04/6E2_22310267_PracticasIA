def backtracking_sudoku(tablero):
    """
    Resuelve un Sudoku utilizando el algoritmo de Búsqueda de Vuelta Atrás.
    :param tablero: Matriz 9x9 que representa el Sudoku (0 = casilla vacía).
    :return: Matriz resuelta o None si no hay solución.
    """
    # Encuentra la próxima casilla vacía en el tablero
    fila, columna = encontrar_casilla_vacia(tablero)
    
    # Si no hay casillas vacías, el Sudoku está resuelto
    if fila == -1:
        return tablero
    
    # Intenta colocar números del 1 al 9 en la casilla vacía
    for numero in range(1, 10):
        # Verifica si el número es válido en la posición actual
        if es_valido(tablero, fila, columna, numero):
            # Asigna el número a la casilla
            tablero[fila][columna] = numero
            
            # Llama recursivamente al algoritmo para resolver el resto del tablero
            if backtracking_sudoku(tablero):
                return tablero
            
            # Si no lleva a una solución, deshace el cambio (retrocede)
            tablero[fila][columna] = 0
    
    # Si no se puede resolver, retorna None
    return None

# Función auxiliar para encontrar la próxima casilla vacía
def encontrar_casilla_vacia(tablero):
    """
    Busca la próxima casilla vacía en el tablero.
    :param tablero: Matriz 9x9 del Sudoku.
    :return: Coordenadas (fila, columna) de la casilla vacía o (-1, -1) si no hay.
    """
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:  # Si la casilla está vacía
                return i, j
    return -1, -1  # No hay casillas vacías

# Función auxiliar para verificar si un número es válido en una posición
def es_valido(tablero, fila, columna, numero):
    """
    Verifica si un número puede colocarse en una posición específica.
    :param tablero: Matriz 9x9 del Sudoku.
    :param fila: Fila de la casilla.
    :param columna: Columna de la casilla.
    :param numero: Número a verificar.
    :return: True si es válido, False en caso contrario.
    """
    # Verifica si el número ya está en la fila o columna
    for i in range(9):
        if tablero[fila][i] == numero or tablero[i][columna] == numero:
            return False
    
    # Verifica si el número ya está en la subcuadrícula 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_columna + j] == numero:
                return False
    
    # Si pasa todas las verificaciones, el número es válido
    return True

# Ejemplo práctico:
# Tablero inicial de Sudoku con algunas casillas llenas y otras vacías
tablero_sudoku = [
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

# Resuelve el Sudoku utilizando el algoritmo de Búsqueda de Vuelta Atrás
solucion = backtracking_sudoku(tablero_sudoku)

# Imprime el resultado
if solucion:
    print("Sudoku resuelto:")
    for fila in solucion:
        print(fila)
else:
    print("No hay solución para este Sudoku.")