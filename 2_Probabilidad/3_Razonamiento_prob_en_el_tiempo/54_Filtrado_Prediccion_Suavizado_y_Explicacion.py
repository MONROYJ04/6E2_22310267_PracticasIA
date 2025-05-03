# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FILTRADO, PREDICCIÓN, SUAVIZADO Y EXPLICACIÓN PARA RAZONAMIENTO PROBABILÍSTICO
# ------------------------------------------------------------------------------------
# Este código implementa un modelo probabilístico para estimar estados actuales, futuros y pasados
# en un sistema dinámico basado en observaciones. Utiliza matrices de transición y emisión para
# calcular probabilidades y proporciona explicaciones interpretables de los resultados.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Aquí se importa `numpy`, una biblioteca para cálculos matemáticos y manejo de matrices.
# - Es esencial para realizar operaciones como multiplicación de matrices y normalización.
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN DE FILTRADO
# ------------------------------------------------------------------------------------
# - QUÉ: Calcula la probabilidad del estado actual basado en el estado anterior y la observación.
# - POR QUÉ: Es útil para actualizar el conocimiento del sistema en tiempo real.
# - PARÁMETROS:
#   - `prob_estado_anterior`: Vector de probabilidades del estado anterior.
#   - `matriz_transicion`: Matriz que define las probabilidades de cambio entre estados.
#   - `observacion`: Índice de la observación actual.
#   - `matriz_emision`: Matriz que define las probabilidades de observaciones dado un estado.
def filtrado(prob_estado_anterior, matriz_transicion, observacion, matriz_emision):
    """
    Realiza el filtrado para calcular la probabilidad del estado actual.
    """
    # Predicción del estado actual basado en el estado anterior
    prediccion = np.dot(prob_estado_anterior, matriz_transicion)
    # Actualización con la observación actual
    prob_estado_actual = prediccion * matriz_emision[:, observacion]
    # Normalización para que las probabilidades sumen 1
    prob_estado_actual /= np.sum(prob_estado_actual)
    return prob_estado_actual

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN DE PREDICCIÓN
# ------------------------------------------------------------------------------------
# - QUÉ: Estima la probabilidad de estados futuros a partir del estado actual.
# - POR QUÉ: Permite anticipar el comportamiento del sistema en el futuro.
# - PARÁMETROS:
#   - `prob_estado_actual`: Vector de probabilidades del estado actual.
#   - `matriz_transicion`: Matriz que define las probabilidades de cambio entre estados.
#   - `pasos`: Número de pasos en el futuro a predecir.
def prediccion(prob_estado_actual, matriz_transicion, pasos):
    """
    Realiza la predicción de estados futuros.
    """
    prob_estado_futuro = prob_estado_actual
    for _ in range(pasos):
        prob_estado_futuro = np.dot(prob_estado_futuro, matriz_transicion)
    return prob_estado_futuro

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR LA FUNCIÓN DE SUAVIZADO
# ------------------------------------------------------------------------------------
# - QUÉ: Calcula la probabilidad de estados pasados dados estados futuros y observaciones.
# - POR QUÉ: Es útil para analizar eventos pasados con información adicional.
# - PARÁMETROS:
#   - `prob_estado_futuro`: Vector de probabilidades del estado futuro.
#   - `matriz_transicion`: Matriz que define las probabilidades de cambio entre estados.
#   - `observacion`: Índice de la observación actual.
#   - `matriz_emision`: Matriz que define las probabilidades de observaciones dado un estado.
def suavizado(prob_estado_futuro, matriz_transicion, observacion, matriz_emision):
    """
    Realiza el suavizado para calcular la probabilidad de estados pasados.
    """
    # Cálculo de la probabilidad del estado pasado
    prob_estado_pasado = prob_estado_futuro * matriz_emision[:, observacion]
    prob_estado_pasado /= np.sum(prob_estado_pasado)
    return prob_estado_pasado

# ------------------------------------------------------------------------------------
# PASO 5: DEFINIR LA FUNCIÓN DE EXPLICACIÓN
# ------------------------------------------------------------------------------------
# - QUÉ: Genera una interpretación legible de las probabilidades calculadas.
# - POR QUÉ: Facilita la comprensión de los resultados para usuarios no técnicos.
# - PARÁMETROS:
#   - `probabilidades`: Vector de probabilidades de los estados.
#   - `estados`: Lista de nombres de los estados.
def explicacion(probabilidades, estados):
    """
    Genera una explicación de las probabilidades calculadas.
    """
    explicacion = "Probabilidades de los estados:\n"
    for i, prob in enumerate(probabilidades):
        explicacion += f"Estado {estados[i]}: {prob:.2f}\n"
    return explicacion

# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - QUÉ: Se define un sistema con estados climáticos y observaciones para demostrar el algoritmo.
# - POR QUÉ: Permite visualizar cómo se aplican las funciones en un caso real.
if __name__ == "__main__":
    # Definimos los estados y las observaciones
    estados = ["Soleado", "Nublado", "Lluvioso"]
    observaciones = ["Seco", "Humedo"]
    
    # Matriz de transición entre estados (probabilidades de cambio de estado)
    matriz_transicion = np.array([
        [0.7, 0.2, 0.1],  # De Soleado a [Soleado, Nublado, Lluvioso]
        [0.3, 0.4, 0.3],  # De Nublado a [Soleado, Nublado, Lluvioso]
        [0.2, 0.3, 0.5]   # De Lluvioso a [Soleado, Nublado, Lluvioso]
    ])
    
    # Matriz de emisión (probabilidades de observaciones dado un estado)
    matriz_emision = np.array([
        [0.8, 0.2],  # Soleado genera [Seco, Humedo]
        [0.4, 0.6],  # Nublado genera [Seco, Humedo]
        [0.1, 0.9]   # Lluvioso genera [Seco, Humedo]
    ])
    
    # Probabilidad inicial de los estados
    prob_estado_inicial = np.array([0.5, 0.3, 0.2])  # [Soleado, Nublado, Lluvioso]
    
    # Observación actual (0 = Seco, 1 = Humedo)
    observacion_actual = 1  # Humedo
    
    # Filtrado
    prob_estado_actual = filtrado(prob_estado_inicial, matriz_transicion, observacion_actual, matriz_emision)
    print("Filtrado:")
    print(explicacion(prob_estado_actual, estados))
    
    # Predicción a 2 pasos en el futuro
    prob_estado_futuro = prediccion(prob_estado_actual, matriz_transicion, pasos=2)
    print("Predicción:")
    print(explicacion(prob_estado_futuro, estados))
    
    # Suavizado (estimación del estado pasado)
    prob_estado_pasado = suavizado(prob_estado_futuro, matriz_transicion, observacion_actual, matriz_emision)
    print("Suavizado:")
    print(explicacion(prob_estado_pasado, estados))

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza modelos de Markov ocultos (HMM) para estimar estados en el tiempo.
# 2. Supone que las transiciones entre estados y las observaciones son probabilísticas.
# 3. Ventajas: Es flexible y puede manejar incertidumbre. Limitaciones: Requiere matrices bien definidas.