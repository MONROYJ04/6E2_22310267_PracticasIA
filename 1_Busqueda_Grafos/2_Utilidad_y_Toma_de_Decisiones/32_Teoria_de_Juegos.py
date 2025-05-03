# Importamos la librería numpy para trabajar con matrices y cálculos matemáticos
import numpy as np

# Definimos una función para calcular el Equilibrio de Nash
def calcular_equilibrio_nash(matriz_jugador1, matriz_jugador2):
    """
    Esta función calcula el Equilibrio de Nash para un juego de dos jugadores.
    Un Equilibrio de Nash ocurre cuando ningún jugador puede mejorar su resultado
    cambiando unilateralmente su estrategia.

    Parametros:
    - matriz_jugador1: Matriz de pagos del Jugador 1.
    - matriz_jugador2: Matriz de pagos del Jugador 2.

    Retorna:
    - Lista de estrategias que forman un Equilibrio de Nash.
    """
    # Convertimos las matrices en arreglos numpy para facilitar los cálculos
    matriz_j1 = np.array(matriz_jugador1)
    matriz_j2 = np.array(matriz_jugador2)

    # Obtenemos las dimensiones de las matrices (filas y columnas)
    filas, columnas = matriz_j1.shape

    # Creamos listas para almacenar las estrategias dominantes de cada jugador
    estrategias_j1 = []
    estrategias_j2 = []

    # Buscamos las estrategias dominantes para el Jugador 1
    for i in range(filas):
        if all(matriz_j1[i, j] >= matriz_j1[k, j] for k in range(filas) for j in range(columnas)):
            estrategias_j1.append(i)

    # Buscamos las estrategias dominantes para el Jugador 2
    for j in range(columnas):
        if all(matriz_j2[i, j] >= matriz_j2[i, k] for i in range(filas) for k in range(columnas)):
            estrategias_j2.append(j)

    # Buscamos los puntos donde las estrategias dominantes coinciden
    equilibrio_nash = []
    for i in estrategias_j1:
        for j in estrategias_j2:
            equilibrio_nash.append((i, j))

    return equilibrio_nash

# Ejemplo práctico: Juego del Dilema del Prisionero
# En este juego, dos jugadores (Prisionero A y Prisionero B) tienen dos opciones:
# - Cooperar (C)
# - Traicionar (T)
# Las recompensas se representan en matrices de pagos.

# Matriz de pagos del Jugador 1 (Prisionero A)
# Cada celda representa la recompensa del Jugador 1 dependiendo de las decisiones de ambos jugadores.
matriz_jugador1 = [
    [-1, -3],  # Si el Jugador 1 coopera (C) y el Jugador 2 coopera (C o T)
    [0, -2]    # Si el Jugador 1 traiciona (T) y el Jugador 2 coopera (C o T)
]

# Matriz de pagos del Jugador 2 (Prisionero B)
# Cada celda representa la recompensa del Jugador 2 dependiendo de las decisiones de ambos jugadores.
matriz_jugador2 = [
    [-1, 0],   # Si el Jugador 2 coopera (C) y el Jugador 1 coopera (C o T)
    [-3, -2]   # Si el Jugador 2 traiciona (T) y el Jugador 1 coopera (C o T)
]

# Calculamos el Equilibrio de Nash para este juego
equilibrio = calcular_equilibrio_nash(matriz_jugador1, matriz_jugador2)

# Mostramos el resultado
print("El Equilibrio de Nash es:", equilibrio)