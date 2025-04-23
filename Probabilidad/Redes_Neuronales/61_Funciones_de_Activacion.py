# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FUNCIONES DE ACTIVACIÓN PARA REDES NEURONALES
# ------------------------------------------------------------------------------------
# Este código implementa varias funciones de activación utilizadas en redes neuronales.
# Las funciones de activación transforman las salidas de las neuronas para introducir 
# no linealidad y permitir que la red aprenda patrones complejos.

import numpy as np  # Importamos la librería numpy para realizar cálculos matemáticos

# ------------------------------------------------------------------------------------
# PASO 1: DEFINIR LA FUNCIÓN SIGMOIDE
# ------------------------------------------------------------------------------------
# - La función sigmoide convierte cualquier valor en un rango entre 0 y 1.
# - Es útil en problemas de clasificación binaria, ya que puede interpretarse como una probabilidad.
# - Fórmula: sigmoide(x) = 1 / (1 + e^(-x))
def funcion_sigmoide(x):
    """
    Calcula la función sigmoide para un valor o un arreglo.
    """
    return 1 / (1 + np.exp(-x))  # Aplicamos la fórmula de la función sigmoide

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN ReLU (Rectified Linear Unit)
# ------------------------------------------------------------------------------------
# - La función ReLU devuelve el valor original si es mayor que 0, de lo contrario devuelve 0.
# - Es ampliamente utilizada en redes neuronales profundas debido a su simplicidad y eficiencia.
# - Fórmula: ReLU(x) = max(0, x)
def funcion_relu(x):
    """
    Calcula la función ReLU para un valor o un arreglo.
    """
    return np.maximum(0, x)  # Aplicamos la fórmula de la función ReLU

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN TANGENTE HIPERBÓLICA (tanh)
# ------------------------------------------------------------------------------------
# - La función tanh convierte los valores en un rango entre -1 y 1.
# - Es útil cuando los datos están centrados en 0, ya que puede acelerar el aprendizaje.
# - Fórmula: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
def funcion_tanh(x):
    """
    Calcula la función tangente hiperbólica para un valor o un arreglo.
    """
    return np.tanh(x)  # Aplicamos la fórmula de la función tanh

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR LA FUNCIÓN SOFTMAX
# ------------------------------------------------------------------------------------
# - La función softmax convierte un conjunto de valores en probabilidades que suman 1.
# - Es útil en problemas de clasificación multiclase.
# - Fórmula: softmax(x) = e^(x_i) / sum(e^(x_j)) para todos los j
def funcion_softmax(x):
    """
    Calcula la función softmax para un arreglo.
    """
    exp_x = np.exp(x - np.max(x))  # Restamos el máximo para evitar problemas de desbordamiento
    return exp_x / np.sum(exp_x)  # Normalizamos los valores para que sumen 1

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, aplicamos las funciones de activación a un conjunto de valores.
# - Esto simula cómo las funciones de activación transformarían las salidas de una capa neuronal.
if __name__ == "__main__":
    # Creamos un arreglo de entrada (simula las salidas de una capa de una red neuronal)
    entradas = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

    # Aplicamos cada función de activación a las entradas
    salida_sigmoide = funcion_sigmoide(entradas)
    salida_relu = funcion_relu(entradas)
    salida_tanh = funcion_tanh(entradas)
    salida_softmax = funcion_softmax(entradas)

    # Mostramos los resultados
    print("Entradas:", entradas)
    print("Salida Sigmoide:", salida_sigmoide)
    print("Salida ReLU:", salida_relu)
    print("Salida Tanh:", salida_tanh)
    print("Salida Softmax:", salida_softmax)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Función Sigmoide**:
#    - Fórmula: sigmoide(x) = 1 / (1 + e^(-x))
#    - Convierte valores en un rango entre 0 y 1.
#    - Ventaja: útil para problemas de clasificación binaria.
#    - Limitación: puede causar el problema de gradientes desaparecidos.
#
# 2. **Función ReLU**:
#    - Fórmula: ReLU(x) = max(0, x)
#    - Devuelve 0 para valores negativos y el valor original para positivos.
#    - Ventaja: eficiente y evita el problema de gradientes desaparecidos.
#    - Limitación: puede causar "neuronas muertas" si muchas salidas son 0.
#
# 3. **Función Tanh**:
#    - Fórmula: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
#    - Convierte valores en un rango entre -1 y 1.
#    - Ventaja: útil para datos centrados en 0.
#    - Limitación: también puede sufrir de gradientes desaparecidos.
#
# 4. **Función Softmax**:
#    - Fórmula: softmax(x) = e^(x_i) / sum(e^(x_j)) para todos los j
#    - Convierte valores en probabilidades que suman 1.
#    - Ventaja: útil para problemas de clasificación multiclase.
#    - Limitación: puede ser computacionalmente costosa para grandes conjuntos de datos.