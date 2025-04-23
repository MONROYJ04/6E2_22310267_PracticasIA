# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RED NEURONAL SIMPLE PARA APRENDIZAJE SUPERVISADO
# ------------------------------------------------------------------------------------
# Este código implementa una red neuronal básica con una sola capa oculta. 
# Su objetivo es aprender a predecir salidas a partir de entradas utilizando un conjunto de datos de ejemplo.

import numpy as np

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN DE ACTIVACIÓN
# ------------------------------------------------------------------------------------
# - La función sigmoide se utiliza como función de activación en las redes neuronales.
# - Convierte cualquier valor en un rango entre 0 y 1, lo que permite modelar probabilidades.
# - Es importante porque introduce no linealidad en la red neuronal.
def funcion_sigmoide(x):
    return 1 / (1 + np.exp(-x))

# ------------------------------------------------------------------------------------
# PASO 2: DERIVADA DE LA FUNCIÓN DE ACTIVACIÓN
# ------------------------------------------------------------------------------------
# - La derivada de la función sigmoide es necesaria para calcular los ajustes durante el aprendizaje.
# - Permite determinar cómo cambiar los pesos para reducir el error.
def derivada_sigmoide(x):
    return x * (1 - x)

# ------------------------------------------------------------------------------------
# PASO 3: DEFINICIÓN DE LA CLASE RED NEURONAL
# ------------------------------------------------------------------------------------
# - Esta clase implementa una red neuronal básica con métodos para entrenamiento y predicción.
# - Contiene los pesos, el sesgo y las funciones necesarias para el aprendizaje.

class RedNeuronal:
    def __init__(self, entradas, salidas):
        # ------------------------------------------------------------------------------------
        # INICIALIZACIÓN DE LA RED NEURONAL
        # ------------------------------------------------------------------------------------
        # - Se inicializan las entradas y las salidas esperadas.
        # - Los pesos y el sesgo se inicializan con valores aleatorios para romper la simetría.
        self.entradas = entradas
        self.salidas_esperadas = salidas
        self.pesos = np.random.rand(self.entradas.shape[1], 1)  # Pesos iniciales aleatorios
        self.sesgo = np.random.rand(1)  # Sesgo inicial aleatorio
        self.salidas_calculadas = np.zeros(self.salidas_esperadas.shape)  # Salidas inicializadas en 0

    # ------------------------------------------------------------------------------------
    # PASO 4: PROPAGACIÓN HACIA ADELANTE (FEEDFORWARD)
    # ------------------------------------------------------------------------------------
    # - Calcula la salida de la red neuronal para las entradas actuales.
    # - Utiliza la función sigmoide para obtener valores entre 0 y 1.
    def feedforward(self):
        self.salida_neta = np.dot(self.entradas, self.pesos) + self.sesgo  # Suma ponderada
        self.salidas_calculadas = funcion_sigmoide(self.salida_neta)  # Aplicación de la función sigmoide

    # ------------------------------------------------------------------------------------
    # PASO 5: RETROPROPAGACIÓN DEL ERROR (BACKPROPAGATION)
    # ------------------------------------------------------------------------------------
    # - Ajusta los pesos y el sesgo para reducir el error entre las salidas esperadas y calculadas.
    # - Utiliza la derivada de la función sigmoide para calcular los ajustes necesarios.
    def backpropagation(self, tasa_aprendizaje):
        error = self.salidas_esperadas - self.salidas_calculadas  # Error entre salida esperada y calculada
        ajuste = error * derivada_sigmoide(self.salidas_calculadas)  # Ajuste basado en el error y la derivada
        self.pesos += np.dot(self.entradas.T, ajuste) * tasa_aprendizaje  # Actualización de los pesos
        self.sesgo += np.sum(ajuste) * tasa_aprendizaje  # Actualización del sesgo

    # ------------------------------------------------------------------------------------
    # PASO 6: ENTRENAMIENTO DE LA RED NEURONAL
    # ------------------------------------------------------------------------------------
    # - Entrena la red neuronal durante un número determinado de iteraciones.
    # - En cada iteración, realiza una propagación hacia adelante y una retropropagación.
    def entrenar(self, iteraciones, tasa_aprendizaje):
        for _ in range(iteraciones):
            self.feedforward()
            self.backpropagation(tasa_aprendizaje)

# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO PRÁCTICO - PUERTA LÓGICA OR
# ------------------------------------------------------------------------------------
# - En este ejemplo, entrenamos la red neuronal para aprender el comportamiento de una puerta lógica OR.
# - La puerta OR devuelve 1 si al menos una de las entradas es 1, y 0 en caso contrario.

if __name__ == "__main__":
    # Datos de entrada (combinaciones de 0 y 1)
    entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
    salidas = np.array([[0], [1], [1], [1]])  # Salidas esperadas (comportamiento de la puerta OR)

    # Creación de la red neuronal
    red = RedNeuronal(entradas, salidas)

    # Entrenamiento de la red neuronal
    red.entrenar(iteraciones=10000, tasa_aprendizaje=0.1)

    # Prueba de la red neuronal
    print("Resultados después del entrenamiento:")
    for entrada in entradas:
        red.entradas = np.array([entrada])  # Ajustamos las entradas
        red.feedforward()  # Calculamos la salida
        print(f"Entrada: {entrada}, Salida calculada: {red.salidas_calculadas[0][0]:.4f}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. La red neuronal utiliza la propagación hacia adelante para calcular las salidas.
# 2. La retropropagación ajusta los pesos y el sesgo para minimizar el error.
# 3. La función sigmoide introduce no linealidad, permitiendo que la red aprenda relaciones complejas.
# 4. Este ejemplo utiliza una puerta lógica OR, pero el algoritmo puede aplicarse a otros problemas.
# 5. Limitaciones: Este modelo es muy básico y no incluye capas ocultas ni múltiples neuronas.