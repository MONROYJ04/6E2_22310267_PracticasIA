# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MODELO OCULTO DE MARKOV (HMM) PARA PREDICCIÓN DE ESTADOS OCULTOS
# ------------------------------------------------------------------------------------
# Este código implementa un Modelo Oculto de Markov (HMM) utilizando el algoritmo de Viterbi.
# El objetivo es predecir la secuencia más probable de estados ocultos (por ejemplo, clima)
# basándose en una secuencia de observaciones visibles (por ejemplo, uso de paraguas).

import numpy as np

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE PARÁMETROS DEL MODELO
# ------------------------------------------------------------------------------------
# - Aquí definimos las probabilidades iniciales, la matriz de transición y la matriz de emisión.
# - Estas probabilidades son esenciales para modelar el comportamiento del sistema.

# Probabilidades iniciales: Probabilidad de comenzar en cada estado.
# Ejemplo: 60% de probabilidad de comenzar en el estado 0 (soleado), 40% en el estado 1 (lluvioso).
prob_iniciales = np.array([0.6, 0.4])

# Matriz de transición: Probabilidad de cambiar de un estado a otro.
# Cada fila representa el estado actual, y cada columna representa el estado futuro.
matriz_transicion = np.array([
    [0.7, 0.3],  # Desde el estado 0 (soleado): 70% quedarse en 0, 30% cambiar a 1.
    [0.4, 0.6]   # Desde el estado 1 (lluvioso): 40% cambiar a 0, 60% quedarse en 1.
])

# Matriz de emisión: Probabilidad de observar un símbolo dado un estado.
# Cada fila representa un estado, y cada columna representa una observación posible.
matriz_emision = np.array([
    [0.5, 0.5],  # Desde el estado 0 (soleado): 50% observar "no paraguas", 50% "paraguas".
    [0.1, 0.9]   # Desde el estado 1 (lluvioso): 10% observar "no paraguas", 90% "paraguas".
])

# Secuencia de observaciones: Lo que observamos en el sistema.
# Ejemplo: 0 = no hay paraguas, 1 = hay paraguas.
observaciones = [0, 1, 0]

# ------------------------------------------------------------------------------------
# PASO 2: IMPLEMENTACIÓN DEL ALGORITMO DE VITERBI
# ------------------------------------------------------------------------------------
# - Este algoritmo encuentra la secuencia más probable de estados ocultos.
# - Utiliza programación dinámica para calcular las probabilidades de forma eficiente.

def algoritmo_viterbi(prob_iniciales, matriz_transicion, matriz_emision, observaciones):
    # --------------------------------------------------------------------------------
    # PASO 2.1: INICIALIZACIÓN
    # --------------------------------------------------------------------------------
    # - Inicializamos las matrices para almacenar las probabilidades y los caminos.
    # - `dp` almacena las probabilidades más altas para cada estado en cada paso.
    # - `camino` rastrea el estado previo más probable para reconstruir la secuencia.

    n_estados = len(prob_iniciales)  # Número de estados ocultos.
    n_observaciones = len(observaciones)  # Número de observaciones visibles.

    dp = np.zeros((n_estados, n_observaciones))  # Matriz de probabilidades.
    camino = np.zeros((n_estados, n_observaciones), dtype=int)  # Matriz de caminos.

    # Calculamos las probabilidades iniciales para el primer paso.
    for estado in range(n_estados):
        dp[estado, 0] = prob_iniciales[estado] * matriz_emision[estado, observaciones[0]]
        camino[estado, 0] = 0  # No hay estado previo en el primer paso.

    # --------------------------------------------------------------------------------
    # PASO 2.2: RECURSIÓN
    # --------------------------------------------------------------------------------
    # - Calculamos las probabilidades para las observaciones restantes.
    # - Para cada estado actual, buscamos el estado previo que maximiza la probabilidad.

    for t in range(1, n_observaciones):  # Iteramos sobre cada observación (excepto la primera).
        for estado in range(n_estados):  # Iteramos sobre cada estado actual.
            prob_max = -1  # Inicializamos la probabilidad máxima.
            estado_previo_max = 0  # Inicializamos el estado previo más probable.

            # Calculamos la probabilidad de llegar al estado actual desde cada estado previo.
            for estado_previo in range(n_estados):
                prob = dp[estado_previo, t - 1] * matriz_transicion[estado_previo, estado] * matriz_emision[estado, observaciones[t]]
                if prob > prob_max:  # Actualizamos si encontramos una probabilidad mayor.
                    prob_max = prob
                    estado_previo_max = estado_previo

            dp[estado, t] = prob_max  # Guardamos la probabilidad máxima.
            camino[estado, t] = estado_previo_max  # Guardamos el estado previo más probable.

    # --------------------------------------------------------------------------------
    # PASO 2.3: TERMINACIÓN
    # --------------------------------------------------------------------------------
    # - Identificamos el estado final más probable.
    # - Reconstruimos la secuencia más probable de estados ocultos.

    estado_final = np.argmax(dp[:, n_observaciones - 1])  # Estado con la probabilidad más alta al final.
    secuencia_estados = [0] * n_observaciones  # Inicializamos la secuencia de estados.
    secuencia_estados[-1] = estado_final  # El último estado es el estado final más probable.

    # Reconstruimos la secuencia de estados hacia atrás.
    for t in range(n_observaciones - 2, -1, -1):
        secuencia_estados[t] = camino[secuencia_estados[t + 1], t + 1]

    return secuencia_estados, dp

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Supongamos que queremos predecir el clima (soleado o lluvioso) basado en observaciones de paraguas.
# - Observaciones: 0 = no hay paraguas, 1 = hay paraguas.
# - Estados ocultos: 0 = soleado, 1 = lluvioso.

secuencia_estados, probabilidades = algoritmo_viterbi(prob_iniciales, matriz_transicion, matriz_emision, observaciones)

# Imprimimos los resultados.
print("Secuencia de estados más probable:", secuencia_estados)
print("Matriz de probabilidades:")
print(probabilidades)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo de Viterbi utiliza programación dinámica para encontrar la secuencia más probable
#    de estados ocultos en un Modelo Oculto de Markov.
# 2. Suposiciones clave:
#    - Las observaciones dependen únicamente del estado actual.
#    - La transición entre estados sigue una cadena de Markov (depende solo del estado previo).
# 3. Ventajas:
#    - Eficiente para secuencias largas.
#    - Encuentra la secuencia más probable de manera óptima.
# 4. Limitaciones:
#    - Requiere conocer las probabilidades iniciales, de transición y de emisión.