# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RED DE HOPFIELD PARA RECUPERACIÓN DE PATRONES
# ------------------------------------------------------------------------------------
# Este código implementa una red de Hopfield, un tipo de red neuronal recurrente,
# diseñada para almacenar patrones y recuperarlos incluso si están incompletos o ruidosos.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Aquí importamos `numpy`, una librería para trabajar con matrices y operaciones matemáticas.
# - Es esencial para manejar los patrones y los pesos de la red neuronal.
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN DE ENTRENAMIENTO DE LA RED DE HOPFIELD
# ------------------------------------------------------------------------------------
# - Esta función entrena la red utilizando la regla de Hebb.
# - La regla de Hebb ajusta los pesos de la red para que almacene los patrones proporcionados.
# - Parámetro clave:
#   - `patrones`: Una matriz donde cada fila es un patrón binario (1 y -1).
def entrenar_red_hopfield(patrones):
    """
    Entrena una red de Hopfield utilizando los patrones proporcionados.
    :param patrones: Lista de patrones binarios (vectores) para entrenar la red.
    :return: Matriz de pesos entrenada.
    """
    # Obtenemos el número de neuronas (dimensión de los patrones)
    num_neuronas = patrones.shape[1]
    
    # Inicializamos la matriz de pesos con ceros
    pesos = np.zeros((num_neuronas, num_neuronas))
    
    # Aplicamos la regla de Hebb para calcular los pesos
    for patron in patrones:
        pesos += np.outer(patron, patron)
    
    # Eliminamos los pesos en la diagonal (no hay auto-conexiones)
    np.fill_diagonal(pesos, 0)
    
    return pesos

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN PARA RECUPERAR UN PATRÓN
# ------------------------------------------------------------------------------------
# - Esta función utiliza la red de Hopfield para recuperar un patrón almacenado.
# - Dado un patrón inicial (que puede estar ruidoso o incompleto), la red lo corrige.
# - Parámetros clave:
#   - `pesos`: Matriz de pesos entrenada.
#   - `patron_inicial`: Patrón que queremos recuperar.
#   - `iteraciones`: Número de veces que actualizamos las neuronas.
def recuperar_patron(pesos, patron_inicial, iteraciones=10):
    """
    Recupera un patrón utilizando la red de Hopfield.
    :param pesos: Matriz de pesos entrenada.
    :param patron_inicial: Patrón inicial (ruidoso o incompleto).
    :param iteraciones: Número de iteraciones para actualizar las neuronas.
    :return: Patrón recuperado.
    """
    # Copiamos el patrón inicial para no modificarlo directamente
    patron = np.copy(patron_inicial)
    
    # Iteramos para actualizar las neuronas
    for _ in range(iteraciones):
        # Actualizamos cada neurona utilizando la regla de activación
        for i in range(len(patron)):
            suma = np.dot(pesos[i], patron)
            patron[i] = 1 if suma >= 0 else -1
    
    return patron

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR LOS PATRONES DE ENTRENAMIENTO
# ------------------------------------------------------------------------------------
# - Aquí definimos los patrones que queremos almacenar en la red.
# - Cada patrón es un vector binario de 1 y -1, representando activaciones neuronales.
patrones_entrenamiento = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1],
    [1, 1, -1, -1]
])

# ------------------------------------------------------------------------------------
# PASO 5: ENTRENAR LA RED DE HOPFIELD
# ------------------------------------------------------------------------------------
# - Utilizamos la función `entrenar_red_hopfield` para calcular la matriz de pesos.
# - Esta matriz almacena la información de los patrones.
pesos_entrenados = entrenar_red_hopfield(patrones_entrenamiento)

# ------------------------------------------------------------------------------------
# PASO 6: DEFINIR UN PATRÓN RUIDOSO O INCOMPLETO
# ------------------------------------------------------------------------------------
# - Este es el patrón que queremos recuperar.
# - Puede contener errores o estar incompleto.
patron_ruidoso = np.array([1, -1, -1, -1])

# ------------------------------------------------------------------------------------
# PASO 7: RECUPERAR EL PATRÓN UTILIZANDO LA RED DE HOPFIELD
# ------------------------------------------------------------------------------------
# - Usamos la función `recuperar_patron` para corregir el patrón ruidoso.
# - La red utiliza los pesos entrenados para encontrar el patrón más cercano al original.
patron_recuperado = recuperar_patron(pesos_entrenados, patron_ruidoso)

# ------------------------------------------------------------------------------------
# PASO 8: MOSTRAR LOS RESULTADOS
# ------------------------------------------------------------------------------------
# - Imprimimos el patrón ruidoso y el patrón recuperado para comparar.
print("Patrón ruidoso:", patron_ruidoso)
print("Patrón recuperado:", patron_recuperado)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. La red de Hopfield es un tipo de red neuronal recurrente que almacena patrones en su matriz de pesos.
# 2. Durante el entrenamiento, utilizamos la regla de Hebb para calcular los pesos:
#    w_ij = Σ (x_i * x_j), donde x_i y x_j son las activaciones de las neuronas i y j.
# 3. Durante la recuperación, actualizamos cada neurona utilizando la regla de activación:
#    x_i = 1 si Σ (w_ij * x_j) >= 0, de lo contrario x_i = -1.
# 4. Ventajas:
#    - Puede corregir patrones ruidosos o incompletos.
#    - Es simple de implementar.
# 5. Limitaciones:
#    - La capacidad de almacenamiento es limitada (aproximadamente 0.15 * número de neuronas).
#    - No funciona bien con patrones muy similares entre sí.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Patrones de entrenamiento: [[1, -1, 1, -1], [-1, 1, -1, 1], [1, 1, -1, -1]]
# - Patrón ruidoso: [1, -1, -1, -1]
# - Resultado esperado: La red recupera el patrón más cercano al original almacenado.