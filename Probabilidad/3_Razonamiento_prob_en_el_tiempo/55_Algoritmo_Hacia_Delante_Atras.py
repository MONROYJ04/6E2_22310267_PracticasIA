# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO HACIA ADELANTE-ATRÁS PARA INFERENCIA EN HMM
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo Hacia Adelante-Atrás (Forward-Backward Algorithm),
# utilizado en Modelos Ocultos de Markov (HMM) para calcular la probabilidad de una 
# secuencia de estados ocultos dados una secuencia de observaciones. Es útil en problemas
# de inferencia probabilística, como reconocimiento de voz o predicción del clima.

# ------------------------------------------------------------------------------------
# DEFINICIÓN DE PARÁMETROS INICIALES
# ------------------------------------------------------------------------------------
# - `prob_inicial`: Probabilidades iniciales de comenzar en cada estado.
# - `prob_transicion`: Matriz que define las probabilidades de transición entre estados.
# - `prob_emision`: Matriz que define las probabilidades de observar un símbolo dado un estado.
# - `observaciones`: Secuencia de símbolos observados.

# Probabilidades iniciales: Probabilidad de comenzar en cada estado
prob_inicial = [0.6, 0.4]  # Ejemplo: Estado 0 tiene 60% de probabilidad, Estado 1 tiene 40%

# Matriz de transición: Probabilidad de pasar de un estado a otro
prob_transicion = [
    [0.7, 0.3],  # Desde el estado 0: 70% de quedarse en 0, 30% de ir a 1
    [0.4, 0.6]   # Desde el estado 1: 40% de ir a 0, 60% de quedarse en 1
]

# Matriz de emisión: Probabilidad de observar un símbolo dado un estado
prob_emision = [
    [0.5, 0.5],  # Desde el estado 0: 50% de observar símbolo 0, 50% de observar símbolo 1
    [0.1, 0.9]   # Desde el estado 1: 10% de observar símbolo 0, 90% de observar símbolo 1
]

# Secuencia de observaciones (símbolos observados)
observaciones = [0, 1, 0]  # Ejemplo: Observamos los símbolos 0, 1 y 0

# ------------------------------------------------------------------------------------
# PASO 1: HACIA ADELANTE (FORWARD)
# ------------------------------------------------------------------------------------
# - Calculamos las probabilidades hacia adelante para cada estado y cada tiempo.
# - Este paso evalúa la probabilidad acumulada de llegar a un estado dado la secuencia
#   de observaciones hasta ese punto.
# - Es importante porque nos permite calcular la probabilidad de las observaciones
#   dadas las probabilidades iniciales y de transición.

def hacia_adelante(prob_inicial, prob_transicion, prob_emision, observaciones):
    # Inicializamos la matriz de probabilidades hacia adelante
    n_estados = len(prob_inicial)
    n_tiempos = len(observaciones)
    matriz_forward = [[0] * n_estados for _ in range(n_tiempos)]

    # Paso base: Inicializamos el tiempo 0
    for estado in range(n_estados):
        matriz_forward[0][estado] = prob_inicial[estado] * prob_emision[estado][observaciones[0]]

    # Paso recursivo: Calculamos para cada tiempo y estado
    for t in range(1, n_tiempos):
        for estado_actual in range(n_estados):
            suma = 0
            for estado_anterior in range(n_estados):
                suma += matriz_forward[t-1][estado_anterior] * prob_transicion[estado_anterior][estado_actual]
            matriz_forward[t][estado_actual] = suma * prob_emision[estado_actual][observaciones[t]]

    return matriz_forward

# ------------------------------------------------------------------------------------
# PASO 2: HACIA ATRÁS (BACKWARD)
# ------------------------------------------------------------------------------------
# - Calculamos las probabilidades hacia atrás para cada estado y cada tiempo.
# - Este paso evalúa la probabilidad acumulada de observar el resto de la secuencia
#   desde un estado dado.
# - Es importante porque nos permite combinar estas probabilidades con las del paso
#   hacia adelante para obtener la probabilidad total.

def hacia_atras(prob_transicion, prob_emision, observaciones):
    # Inicializamos la matriz de probabilidades hacia atrás
    n_estados = len(prob_transicion)
    n_tiempos = len(observaciones)
    matriz_backward = [[0] * n_estados for _ in range(n_tiempos)]

    # Paso base: Inicializamos el último tiempo
    for estado in range(n_estados):
        matriz_backward[-1][estado] = 1  # Probabilidad de terminar en cualquier estado es 1

    # Paso recursivo: Calculamos hacia atrás
    for t in range(n_tiempos - 2, -1, -1):
        for estado_actual in range(n_estados):
            suma = 0
            for estado_siguiente in range(n_estados):
                suma += prob_transicion[estado_actual][estado_siguiente] * prob_emision[estado_siguiente][observaciones[t+1]] * matriz_backward[t+1][estado_siguiente]
            matriz_backward[t][estado_actual] = suma

    return matriz_backward

# ------------------------------------------------------------------------------------
# PASO 3: COMBINAR HACIA ADELANTE Y HACIA ATRÁS
# ------------------------------------------------------------------------------------
# - Combinamos las probabilidades hacia adelante y hacia atrás para calcular la
#   probabilidad de cada estado en cada tiempo.
# - Este paso es crucial porque normaliza las probabilidades y nos da una visión
#   completa de la probabilidad de los estados ocultos.

def combinar_forward_backward(matriz_forward, matriz_backward):
    n_tiempos = len(matriz_forward)
    n_estados = len(matriz_forward[0])
    probabilidades = [[0] * n_estados for _ in range(n_tiempos)]

    for t in range(n_tiempos):
        normalizador = sum(matriz_forward[t][estado] * matriz_backward[t][estado] for estado in range(n_estados))
        for estado in range(n_estados):
            probabilidades[t][estado] = (matriz_forward[t][estado] * matriz_backward[t][estado]) / normalizador

    return probabilidades

# ------------------------------------------------------------------------------------
# EJECUCIÓN DEL ALGORITMO
# ------------------------------------------------------------------------------------
# - Ejecutamos los pasos hacia adelante, hacia atrás y combinamos los resultados.
# - Finalmente, imprimimos las matrices y las probabilidades combinadas.

matriz_forward = hacia_adelante(prob_inicial, prob_transicion, prob_emision, observaciones)
matriz_backward = hacia_atras(prob_transicion, prob_emision, observaciones)
probabilidades = combinar_forward_backward(matriz_forward, matriz_backward)

# Imprimimos los resultados
print("Matriz Forward (Hacia Adelante):")
for fila in matriz_forward:
    print(fila)

print("\nMatriz Backward (Hacia Atrás):")
for fila in matriz_backward:
    print(fila)

print("\nProbabilidades combinadas (Hacia Adelante-Atrás):")
for t, fila in enumerate(probabilidades):
    print(f"Tiempo {t}: {fila}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza las probabilidades iniciales, de transición y de emisión
#    para calcular la probabilidad de una secuencia de observaciones.
# 2. Supone que las observaciones son independientes dado el estado actual.
# 3. Ventajas: Permite inferir estados ocultos en problemas complejos.
#    Limitaciones: Requiere conocer las matrices de transición y emisión.