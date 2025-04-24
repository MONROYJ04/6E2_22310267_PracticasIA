# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RETROPROPAGACIÓN DEL ERROR PARA ENTRENAR UNA RED NEURONAL SIMPLE
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de retropropagación del error para entrenar una red
# neuronal simple con una capa de entrada y una capa de salida. El objetivo es ajustar los
# pesos de la red para que pueda predecir correctamente las salidas esperadas a partir de
# las entradas proporcionadas.

import numpy as np

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN DE ACTIVACIÓN SIGMOIDE
# ------------------------------------------------------------------------------------
# - La función sigmoide se utiliza para convertir los valores de entrada en un rango entre 0 y 1.
# - Es importante porque introduce no linealidad en la red neuronal, permitiendo que aprenda
#   relaciones complejas entre las entradas y las salidas.
def funcion_sigmoide(x):
    # Calcula la salida de la función sigmoide
    return 1 / (1 + np.exp(-x))

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA DERIVADA DE LA FUNCIÓN SIGMOIDE
# ------------------------------------------------------------------------------------
# - La derivada de la función sigmoide es necesaria para calcular el ajuste de los pesos
#   durante la retropropagación del error.
# - Esto permite que la red neuronal aprenda ajustando los pesos en la dirección correcta.
def derivada_sigmoide(x):
    # Calcula la derivada de la función sigmoide
    return x * (1 - x)

# ------------------------------------------------------------------------------------
# PASO 3: IMPLEMENTACIÓN DEL ALGORITMO DE RETROPROPAGACIÓN DEL ERROR
# ------------------------------------------------------------------------------------
# - Este bloque entrena la red neuronal ajustando los pesos iterativamente.
# - Se realiza en tres pasos principales:
#   1. Propagación hacia adelante: Calcula la salida de la red.
#   2. Cálculo del error: Compara la salida calculada con la salida esperada.
#   3. Retropropagación del error: Ajusta los pesos para minimizar el error.
# - Parámetros clave:
#   - `entradas`: Matriz con los datos de entrada.
#   - `salidas_esperadas`: Matriz con las salidas esperadas.
#   - `tasa_aprendizaje`: Velocidad con la que se ajustan los pesos.
#   - `iteraciones`: Número de veces que se repite el proceso de entrenamiento.
def retropropagacion_errores(entradas, salidas_esperadas, tasa_aprendizaje, iteraciones):
    # Inicializamos los pesos con valores aleatorios
    np.random.seed(1)  # Fijamos la semilla para reproducibilidad
    pesos_entrada_salida = np.random.uniform(-1, 1, (entradas.shape[1], 1))

    # Iteramos para entrenar la red neuronal
    for i in range(iteraciones):
        # ------------------------------------------------------------------------------------
        # PASO 3.1: PROPAGACIÓN HACIA ADELANTE
        # ------------------------------------------------------------------------------------
        # - Calcula la entrada neta multiplicando las entradas por los pesos.
        # - Aplica la función sigmoide para obtener la salida calculada.
        entrada_neta = np.dot(entradas, pesos_entrada_salida)
        salida_calculada = funcion_sigmoide(entrada_neta)

        # ------------------------------------------------------------------------------------
        # PASO 3.2: CÁLCULO DEL ERROR
        # ------------------------------------------------------------------------------------
        # - Calcula la diferencia entre la salida esperada y la salida calculada.
        # - Este error se utiliza para ajustar los pesos.
        error = salidas_esperadas - salida_calculada

        # ------------------------------------------------------------------------------------
        # PASO 3.3: RETROPROPAGACIÓN DEL ERROR
        # ------------------------------------------------------------------------------------
        # - Calcula el ajuste necesario para los pesos utilizando el error y la derivada
        #   de la función sigmoide.
        # - Actualiza los pesos sumando el ajuste escalado por la tasa de aprendizaje.
        ajuste = error * derivada_sigmoide(salida_calculada)
        pesos_entrada_salida += np.dot(entradas.T, ajuste) * tasa_aprendizaje

    # Devuelve los pesos ajustados después del entrenamiento
    return pesos_entrada_salida

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: ENTRENAMIENTO DE UNA RED NEURONAL PARA UNA PUERTA LÓGICA OR
# ------------------------------------------------------------------------------------
# - En este ejemplo, entrenamos una red neuronal para aprender el comportamiento de
#   una puerta lógica OR. La puerta OR devuelve 1 si al menos una de las entradas es 1.
if __name__ == "__main__":
    # ------------------------------------------------------------------------------------
    # PASO 1: DEFINICIÓN DE LAS ENTRADAS Y SALIDAS ESPERADAS
    # ------------------------------------------------------------------------------------
    # - `entradas`: Matriz con las combinaciones de entrada para la puerta OR.
    # - `salidas_esperadas`: Matriz con las salidas correspondientes para cada entrada.
    entradas = np.array([[0, 0],
                          [0, 1],
                          [1, 0],
                          [1, 1]])
    salidas_esperadas = np.array([[0], [1], [1], [1]])

    # ------------------------------------------------------------------------------------
    # PASO 2: CONFIGURACIÓN DE LOS PARÁMETROS DEL ALGORITMO
    # ------------------------------------------------------------------------------------
    # - `tasa_aprendizaje`: Controla la velocidad con la que se ajustan los pesos.
    # - `iteraciones`: Número de veces que se repite el proceso de entrenamiento.
    tasa_aprendizaje = 0.1
    iteraciones = 10000

    # ------------------------------------------------------------------------------------
    # PASO 3: ENTRENAMIENTO DE LA RED NEURONAL
    # ------------------------------------------------------------------------------------
    # - Llamamos a la función `retropropagacion_errores` para entrenar la red neuronal.
    pesos_entrenados = retropropagacion_errores(entradas, salidas_esperadas, tasa_aprendizaje, iteraciones)

    # ------------------------------------------------------------------------------------
    # PASO 4: PRUEBA DE LA RED NEURONAL
    # ------------------------------------------------------------------------------------
    # - Calculamos las salidas de la red neuronal utilizando los pesos entrenados.
    salida_final = funcion_sigmoide(np.dot(entradas, pesos_entrenados))

    # ------------------------------------------------------------------------------------
    # PASO 5: MOSTRAR LOS RESULTADOS
    # ------------------------------------------------------------------------------------
    # - Mostramos los pesos entrenados y las salidas calculadas para verificar el
    #   rendimiento de la red neuronal.
    print("Pesos entrenados:")
    print(pesos_entrenados)
    print("\nSalidas calculadas:")
    print(salida_final)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza la función sigmoide para calcular las salidas de la red neuronal.
# 2. Ajusta los pesos iterativamente utilizando la retropropagación del error.
# 3. La tasa de aprendizaje controla la magnitud de los ajustes en cada iteración.
# 4. Este enfoque es adecuado para problemas simples como puertas lógicas, pero puede
#    requerir arquitecturas más complejas para problemas más avanzados.