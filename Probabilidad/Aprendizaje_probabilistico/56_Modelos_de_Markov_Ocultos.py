# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MODELO DE MARKOV OCULTO (HMM) PARA INFERENCIA DE ESTADOS OCULTOS
# ------------------------------------------------------------------------------------
# Este código implementa un Modelo de Markov Oculto (HMM) para predecir la secuencia más probable
# de estados ocultos dada una secuencia de observaciones, utilizando el algoritmo de Viterbi.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Se importa `numpy` para realizar cálculos matriciales y operaciones numéricas.
# - `numpy` es esencial para manejar las matrices de transición, emisión y probabilidades iniciales.
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE DEL MODELO DE MARKOV OCULTO
# ------------------------------------------------------------------------------------
# - Esta clase encapsula la lógica del HMM, incluyendo su inicialización y el algoritmo de Viterbi.
# - Los parámetros clave son:
#   - `estados_ocultos`: Lista de posibles estados ocultos.
#   - `observaciones`: Lista de posibles observaciones.
#   - `matriz_transicion`: Matriz de probabilidades de transición entre estados ocultos.
#   - `matriz_emision`: Matriz de probabilidades de emisión (observaciones dadas los estados ocultos).
#   - `distribucion_inicial`: Vector de probabilidades iniciales para los estados ocultos.
class ModeloMarkovOculto:
    def __init__(self, estados_ocultos, observaciones, matriz_transicion, matriz_emision, distribucion_inicial):
        """
        Inicializa el modelo con los parámetros necesarios.

        estados_ocultos: Lista de estados ocultos posibles.
        observaciones: Lista de observaciones posibles.
        matriz_transicion: Matriz de probabilidades de transición entre estados ocultos.
        matriz_emision: Matriz de probabilidades de emisión (observaciones dadas los estados ocultos).
        distribucion_inicial: Vector de probabilidades iniciales para los estados ocultos.
        """
        self.estados_ocultos = estados_ocultos
        self.observaciones = observaciones
        self.matriz_transicion = np.array(matriz_transicion)
        self.matriz_emision = np.array(matriz_emision)
        self.distribucion_inicial = np.array(distribucion_inicial)

    # ------------------------------------------------------------------------------------
    # PASO 3: IMPLEMENTACIÓN DEL ALGORITMO DE VITERBI
    # ------------------------------------------------------------------------------------
    # - Este método encuentra la secuencia más probable de estados ocultos dada una secuencia de observaciones.
    # - Utiliza programación dinámica para calcular las probabilidades acumuladas y rastrear los estados previos.
    def algoritmo_viterbi(self, secuencia_observaciones):
        """
        Implementa el algoritmo de Viterbi para encontrar la secuencia más probable de estados ocultos
        dada una secuencia de observaciones.

        secuencia_observaciones: Lista de observaciones realizadas.
        """
        # Número de estados ocultos y observaciones
        n_estados = len(self.estados_ocultos)
        n_observaciones = len(secuencia_observaciones)

        # ------------------------------------------------------------------------------------
        # PASO 3.1: INICIALIZACIÓN DE MATRICES
        # ------------------------------------------------------------------------------------
        # - `dp`: Matriz para almacenar las probabilidades más altas hasta cada punto.
        # - `rastreo`: Matriz para rastrear los estados previos que llevaron a las probabilidades máximas.
        dp = np.zeros((n_estados, n_observaciones))
        rastreo = np.zeros((n_estados, n_observaciones), dtype=int)

        # ------------------------------------------------------------------------------------
        # PASO 3.2: INICIALIZACIÓN DE LA PRIMERA COLUMNA
        # ------------------------------------------------------------------------------------
        # - Calculamos las probabilidades iniciales multiplicando la distribución inicial
        #   por las probabilidades de emisión de la primera observación.
        for i in range(n_estados):
            dp[i, 0] = self.distribucion_inicial[i] * self.matriz_emision[i, self.observaciones.index(secuencia_observaciones[0])]
            rastreo[i, 0] = 0

        # ------------------------------------------------------------------------------------
        # PASO 3.3: LLENADO DE LAS MATRICES `dp` Y `rastreo`
        # ------------------------------------------------------------------------------------
        # - Para cada observación (a partir de la segunda), calculamos las probabilidades acumuladas
        #   para cada estado oculto considerando las transiciones desde los estados previos.
        for t in range(1, n_observaciones):
            for j in range(n_estados):
                probabilidades = [
                    dp[i, t - 1] * self.matriz_transicion[i, j] * self.matriz_emision[j, self.observaciones.index(secuencia_observaciones[t])]
                    for i in range(n_estados)
                ]
                dp[j, t] = max(probabilidades)  # Guardamos la probabilidad máxima
                rastreo[j, t] = np.argmax(probabilidades)  # Guardamos el índice del estado previo

        # ------------------------------------------------------------------------------------
        # PASO 3.4: RECONSTRUCCIÓN DE LA SECUENCIA MÁS PROBABLE
        # ------------------------------------------------------------------------------------
        # - A partir de la última columna de `dp`, identificamos el estado con la probabilidad máxima.
        # - Retrocedemos utilizando la matriz `rastreo` para reconstruir la secuencia completa.
        estados_ocultos_probables = []
        ultimo_estado = np.argmax(dp[:, -1])
        estados_ocultos_probables.append(self.estados_ocultos[ultimo_estado])

        for t in range(n_observaciones - 1, 0, -1):
            ultimo_estado = rastreo[ultimo_estado, t]
            estados_ocultos_probables.insert(0, self.estados_ocultos[ultimo_estado])

        return estados_ocultos_probables

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, se define un modelo HMM con dos estados ocultos ("Soleado" y "Lluvioso")
#   y tres posibles observaciones ("Caminar", "Comprar", "Limpiar").
# - Se utiliza el algoritmo de Viterbi para predecir la secuencia más probable de estados ocultos
#   dada una secuencia de observaciones.
if __name__ == "__main__":
    # Definimos los estados ocultos y las observaciones
    estados_ocultos = ["Soleado", "Lluvioso"]
    observaciones = ["Caminar", "Comprar", "Limpiar"]

    # Definimos la matriz de transición (probabilidades de pasar de un estado oculto a otro)
    matriz_transicion = [
        [0.8, 0.2],  # Soleado -> [Soleado, Lluvioso]
        [0.4, 0.6]   # Lluvioso -> [Soleado, Lluvioso]
    ]

    # Definimos la matriz de emisión (probabilidades de observar algo dado un estado oculto)
    matriz_emision = [
        [0.6, 0.3, 0.1],  # Soleado -> [Caminar, Comprar, Limpiar]
        [0.1, 0.4, 0.5]   # Lluvioso -> [Caminar, Comprar, Limpiar]
    ]

    # Definimos la distribución inicial (probabilidades iniciales de los estados ocultos)
    distribucion_inicial = [0.7, 0.3]  # [Soleado, Lluvioso]

    # Creamos una instancia del modelo
    hmm = ModeloMarkovOculto(estados_ocultos, observaciones, matriz_transicion, matriz_emision, distribucion_inicial)

    # Definimos una secuencia de observaciones
    secuencia_observaciones = ["Caminar", "Comprar", "Limpiar"]

    # Calculamos la secuencia más probable de estados ocultos
    secuencia_estados = hmm.algoritmo_viterbi(secuencia_observaciones)

    # Mostramos el resultado
    print("Secuencia de observaciones:", secuencia_observaciones)
    print("Secuencia más probable de estados ocultos:", secuencia_estados)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo de Viterbi utiliza programación dinámica para calcular la secuencia más probable
#    de estados ocultos en un HMM.
# 2. Supone que las probabilidades de transición y emisión son conocidas y que las observaciones
#    son independientes dado el estado oculto.
# 3. Ventajas:
#    - Encuentra la secuencia óptima de estados ocultos.
#    - Es eficiente en términos de tiempo y espacio.
# 4. Limitaciones:
#    - Requiere que las matrices de transición y emisión sean precisas.
#    - No maneja bien datos con alta incertidumbre o ruido.