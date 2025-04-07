import random

def minimos_conflictos(tamano_tablero, max_pasos=1000):
    """
    Resuelve el problema de las N-Reinas usando el algoritmo de Mínimos-Conflictos.
    :param tamano_tablero: Tamaño del tablero (n x n).
    :param max_pasos: Número máximo de iteraciones permitidas.
    :return: Una asignación de reinas (fila para cada columna) o None si no se encuentra solución.
    """
    # Inicialización aleatoria: coloca una reina en una fila aleatoria de cada columna
    asignacion = [random.randint(0, tamano_tablero - 1) for _ in range(tamano_tablero)]
    
    # Iteramos hasta el número máximo de pasos
    for _ in range(max_pasos):
        # Encuentra las columnas donde las reinas están en conflicto
        columnas_conflictivas = encontrar_columnas_conflictivas(asignacion, tamano_tablero)
        
        # Si no hay columnas conflictivas, hemos encontrado una solución
        if not columnas_conflictivas:
            return asignacion
        
        # Selecciona una columna conflictiva al azar
        columna = random.choice(columnas_conflictivas)
        
        # Encuentra la fila con el menor número de conflictos para esta columna
        fila_min_conflictos = encontrar_fila_min_conflictos(asignacion, columna, tamano_tablero)
        
        # Mueve la reina a la fila con menos conflictos
        asignacion[columna] = fila_min_conflictos
    
    # Si no se encuentra solución en el número máximo de pasos, devuelve None
    return None

def encontrar_columnas_conflictivas(asignacion, tamano_tablero):
    """
    Encuentra todas las columnas donde las reinas están en conflicto.
    :param asignacion: Lista que representa la fila de cada reina en cada columna.
    :param tamano_tablero: Tamaño del tablero.
    :return: Lista de columnas conflictivas.
    """
    columnas_conflictivas = []
    for columna in range(tamano_tablero):
        if esta_en_conflicto(asignacion, columna, tamano_tablero):
            columnas_conflictivas.append(columna)
    return columnas_conflictivas

def esta_en_conflicto(asignacion, columna, tamano_tablero):
    """
    Verifica si la reina en una columna está en conflicto con otras reinas.
    :param asignacion: Lista que representa la fila de cada reina en cada columna.
    :param columna: Columna a verificar.
    :param tamano_tablero: Tamaño del tablero.
    :return: True si hay conflicto, False en caso contrario.
    """
    fila = asignacion[columna]
    for otra_columna in range(tamano_tablero):
        if otra_columna == columna:
            continue
        otra_fila = asignacion[otra_columna]
        # Conflicto si están en la misma fila o en la misma diagonal
        if otra_fila == fila or abs(otra_fila - fila) == abs(otra_columna - columna):
            return True
    return False

def encontrar_fila_min_conflictos(asignacion, columna, tamano_tablero):
    """
    Encuentra la fila en una columna que minimiza los conflictos.
    :param asignacion: Lista que representa la fila de cada reina en cada columna.
    :param columna: Columna a modificar.
    :param tamano_tablero: Tamaño del tablero.
    :return: Fila con el menor número de conflictos.
    """
    min_conflictos = float('inf')
    filas_candidatas = []
    
    for fila in range(tamano_tablero):
        conflictos = contar_conflictos(asignacion, columna, fila, tamano_tablero)
        if conflictos < min_conflictos:
            min_conflictos = conflictos
            filas_candidatas = [fila]
        elif conflictos == min_conflictos:
            filas_candidatas.append(fila)
    
    # Si hay empate, selecciona una fila al azar
    return random.choice(filas_candidatas)

def contar_conflictos(asignacion, columna, fila, tamano_tablero):
    """
    Cuenta cuántas reinas estarían en conflicto si colocamos una reina en (columna, fila).
    :param asignacion: Lista que representa la fila de cada reina en cada columna.
    :param columna: Columna donde se colocará la reina.
    :param fila: Fila donde se colocará la reina.
    :param tamano_tablero: Tamaño del tablero.
    :return: Número de conflictos.
    """
    conflictos = 0
    for otra_columna in range(tamano_tablero):
        if otra_columna == columna:
            continue
        otra_fila = asignacion[otra_columna]
        # Conflicto si están en la misma fila o en la misma diagonal
        if otra_fila == fila or abs(otra_fila - fila) == abs(otra_columna - columna):
            conflictos += 1
    return conflictos

# Ejemplo práctico:
tamano_tablero = 8  # Tablero 8x8 (problema de las 8 reinas)
solucion = minimos_conflictos(tamano_tablero)

if solucion:
    print(f"Solución encontrada para el problema de {tamano_tablero}-Reinas:")
    for columna, fila in enumerate(solucion):
        print(f"Columna {columna}: Fila {fila}")
else:
    print("No se encontró solución en el número máximo de pasos.")