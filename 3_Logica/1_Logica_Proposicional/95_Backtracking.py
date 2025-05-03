# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE BACKTRACKING PARA EL PROBLEMA DE LAS N-REINAS
# ------------------------------------------------------------------------------------
# Este código resuelve el problema de las N-Reinas utilizando la técnica de Backtracking.
# El objetivo es colocar N reinas en un tablero de ajedrez de NxN de manera que ninguna
# reina pueda atacar a otra. Esto significa que no pueden estar en la misma fila, columna
# o diagonal.

# ------------------------------------------------------------------------------------
# PASO 1: FUNCIÓN PARA VERIFICAR SI UNA POSICIÓN ES SEGURA
# ------------------------------------------------------------------------------------
# - Esta función (`es_seguro`) verifica si es seguro colocar una reina en una posición
#   específica del tablero (fila, columna).
# - Es importante porque asegura que las reinas no se ataquen entre sí.
# - Parámetros clave:
#   - `tablero`: Lista que representa el tablero de ajedrez.
#   - `fila`: Fila donde se quiere colocar la reina.
#   - `columna`: Columna donde se quiere colocar la reina.
#   - `n`: Tamaño del tablero (NxN).

def es_seguro(tablero, fila, columna, n):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila - 1, -1, -1), range(columna - 1, -1, -1)):
        if tablero[i] == j:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila - 1, -1, -1), range(columna + 1, n)):
        if tablero[i] == j:
            return False

    # Si pasa todas las verificaciones, es seguro colocar la reina
    return True

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PRINCIPAL PARA RESOLVER EL PROBLEMA DE LAS N-REINAS
# ------------------------------------------------------------------------------------
# - Esta función (`resolver_n_reinas`) utiliza Backtracking para intentar colocar todas
#   las reinas en el tablero.
# - Es importante porque implementa la lógica recursiva para explorar todas las posibles
#   configuraciones del tablero.
# - Parámetros clave:
#   - `tablero`: Lista que representa el tablero de ajedrez.
#   - `fila`: Fila actual donde se intenta colocar una reina.
#   - `n`: Tamaño del tablero (NxN).

def resolver_n_reinas(tablero, fila, n):
    # Caso base: si todas las reinas están colocadas, devolver True
    if fila == n:
        return True

    # Intentar colocar una reina en cada columna de la fila actual
    for columna in range(n):
        if es_seguro(tablero, fila, columna, n):
            # Colocar la reina en la columna actual
            tablero[fila] = columna

            # Llamar recursivamente para colocar el resto de las reinas
            if resolver_n_reinas(tablero, fila + 1, n):
                return True

            # Si no se encuentra solución, retirar la reina (Backtracking)
            tablero[fila] = -1

    # Si no se puede colocar una reina en ninguna columna, devolver False
    return False

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN PARA IMPRIMIR EL TABLERO
# ------------------------------------------------------------------------------------
# - Esta función (`imprimir_tablero`) imprime el tablero de ajedrez con las reinas
#   colocadas.
# - Es importante porque permite visualizar la solución encontrada.
# - Parámetros clave:
#   - `tablero`: Lista que representa el tablero de ajedrez.
#   - `n`: Tamaño del tablero (NxN).

def imprimir_tablero(tablero, n):
    for i in range(n):
        # Crear una fila vacía con puntos
        fila = ["." for _ in range(n)]
        # Colocar una reina ("Q") en la posición correspondiente
        if tablero[i] != -1:
            fila[tablero[i]] = "Q"
        # Imprimir la fila como una cadena de texto
        print(" ".join(fila))
    print("\n")

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO - RESOLVER EL PROBLEMA DE LAS 4 REINAS
# ------------------------------------------------------------------------------------
# - Este ejemplo resuelve el problema de las 4 reinas (tablero de 4x4).
# - Inicializa el tablero con -1 (sin reinas colocadas) y llama a la función principal.
# - Si encuentra una solución, la imprime; de lo contrario, indica que no hay solución.

n = 4  # Tamaño del tablero (4x4)
tablero = [-1] * n  # Inicializar el tablero con -1 (sin reinas colocadas)

if resolver_n_reinas(tablero, 0, n):
    print("Se encontró una solución para el problema de las 4 reinas:")
    imprimir_tablero(tablero, n)
else:
    print("No se encontró solución para el problema de las 4 reinas.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza Backtracking, una técnica que explora todas las posibles
#    configuraciones del tablero de manera recursiva.
# 2. En cada paso, intenta colocar una reina en una posición válida de la fila actual.
# 3. Si no es posible colocar una reina, retrocede (backtrack) y prueba otra posición.
# 4. Ventajas:
#    - Encuentra todas las soluciones posibles (si se modifica para no detenerse en la primera).
#    - Es eficiente para problemas combinatorios como este.
# 5. Limitaciones:
#    - Puede ser lento para valores grandes de N debido al crecimiento exponencial del espacio
#      de búsqueda.

# ------------------------------------------------------------------------------------
# EJEMPLO DE SALIDA
# ------------------------------------------------------------------------------------
# Se encontró una solución para el problema de las 4 reinas:
# . Q . .
# . . . Q
# Q . . .
# . . Q .