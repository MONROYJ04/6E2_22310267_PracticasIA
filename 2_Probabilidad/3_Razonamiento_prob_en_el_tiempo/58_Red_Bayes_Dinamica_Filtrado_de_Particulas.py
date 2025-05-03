# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FILTRADO DE PARTÍCULAS PARA SEGUIMIENTO DE OBJETOS
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de Filtrado de Partículas, una técnica probabilística
# utilizada para estimar el estado de un sistema dinámico (como la posición de un objeto)
# a partir de observaciones ruidosas y un modelo de transición.

import numpy as np

# ------------------------------------------------------------------------------------
# PASO 1: INICIALIZACIÓN DE PARTÍCULAS
# ------------------------------------------------------------------------------------
# - Este bloque inicializa un conjunto de partículas distribuidas aleatoriamente dentro
#   de un rango definido (`rango_estado`).
# - Las partículas representan posibles estados iniciales del sistema.
# - Es importante porque establece la base para las estimaciones futuras.
def inicializar_particulas(num_particulas, rango_estado):
    """
    Inicializa las particulas de forma aleatoria dentro del rango de estados posibles.
    
    Args:
        num_particulas (int): Número de partículas a generar.
        rango_estado (tuple): Rango de valores posibles para el estado (min, max).
    
    Returns:
        numpy.ndarray: Partículas inicializadas.
    """
    return np.random.uniform(rango_estado[0], rango_estado[1], num_particulas)

# ------------------------------------------------------------------------------------
# PASO 2: PREDICCIÓN DEL ESTADO FUTURO
# ------------------------------------------------------------------------------------
# - Este bloque actualiza las partículas simulando el movimiento del sistema.
# - Se agrega ruido gaussiano para modelar la incertidumbre en el movimiento.
# - Es importante porque permite predecir cómo evolucionará el sistema en el tiempo.
def predecir(particulas, ruido_movimiento):
    """
    Predice el siguiente estado de las partículas agregando ruido de movimiento.
    
    Args:
        particulas (numpy.ndarray): Partículas actuales.
        ruido_movimiento (float): Desviación estándar del ruido de movimiento.
    
    Returns:
        numpy.ndarray: Partículas actualizadas.
    """
    return particulas + np.random.normal(0, ruido_movimiento, len(particulas))

# ------------------------------------------------------------------------------------
# PASO 3: CÁLCULO DE PESOS BASADO EN OBSERVACIONES
# ------------------------------------------------------------------------------------
# - Este bloque calcula los pesos de las partículas en función de qué tan bien
#   coinciden con la observación del sensor.
# - Se utiliza una función gaussiana para modelar la probabilidad de cada partícula.
# - Es importante porque permite identificar las partículas más probables.
def calcular_pesos(particulas, observacion, ruido_sensor):
    """
    Calcula los pesos de las partículas basado en la observación del sensor.
    
    Args:
        particulas (numpy.ndarray): Partículas actuales.
        observacion (float): Valor observado por el sensor.
        ruido_sensor (float): Desviación estándar del ruido del sensor.
    
    Returns:
        numpy.ndarray: Pesos normalizados de las partículas.
    """
    pesos = np.exp(-0.5 * ((particulas - observacion) / ruido_sensor) ** 2)
    return pesos / np.sum(pesos)

# ------------------------------------------------------------------------------------
# PASO 4: REMUESTREO DE PARTÍCULAS
# ------------------------------------------------------------------------------------
# - Este bloque selecciona partículas con probabilidad proporcional a sus pesos.
# - Se utiliza para evitar que las partículas con pesos bajos dominen el sistema.
# - Es importante porque mantiene la diversidad de partículas y mejora la estimación.
def remuestrear(particulas, pesos):
    """
    Realiza el remuestreo de las partículas basado en sus pesos.
    
    Args:
        particulas (numpy.ndarray): Partículas actuales.
        pesos (numpy.ndarray): Pesos de las partículas.
    
    Returns:
        numpy.ndarray: Nuevas partículas remuestreadas.
    """
    indices = np.random.choice(len(particulas), size=len(particulas), p=pesos)
    return particulas[indices]

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO - SEGUIMIENTO DE UN OBJETO EN UNA DIMENSIÓN
# ------------------------------------------------------------------------------------
# - Este bloque implementa un ejemplo práctico del algoritmo.
# - Simula el seguimiento de un objeto en una dimensión utilizando observaciones ruidosas.
# - Muestra cómo el algoritmo estima el estado real del objeto a lo largo del tiempo.
if __name__ == "__main__":
    # Parámetros del modelo
    num_particulas = 1000  # Número de partículas
    rango_estado = (0, 10)  # Rango de valores posibles para el estado
    ruido_movimiento = 0.5  # Ruido en el movimiento
    ruido_sensor = 1.0  # Ruido en el sensor

    # Inicialización
    particulas = inicializar_particulas(num_particulas, rango_estado)
    estado_real = 5.0  # Estado real inicial del objeto
    observaciones = [5.1, 5.3, 5.0, 4.8, 5.2]  # Observaciones del sensor

    # Seguimiento a través del tiempo
    for t, observacion in enumerate(observaciones):
        print(f"Tiempo {t + 1}:")
        
        # Predicción
        particulas = predecir(particulas, ruido_movimiento)
        
        # Actualización de pesos
        pesos = calcular_pesos(particulas, observacion, ruido_sensor)
        
        # Estimación del estado
        estimacion = np.sum(particulas * pesos)
        print(f"  Observación: {observacion}")
        print(f"  Estimación del estado: {estimacion}")
        
        # Remuestreo
        particulas = remuestrear(particulas, pesos)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El Filtrado de Partículas es un método de Monte Carlo que utiliza un conjunto de
#    partículas para representar la distribución de probabilidad del estado de un sistema.
# 2. Suposiciones clave:
#    - El sistema es dinámico y evoluciona con el tiempo.
#    - Las observaciones tienen ruido, pero están relacionadas con el estado real.
# 3. Ventajas:
#    - Puede manejar distribuciones no lineales y no gaussianas.
#    - Es flexible y fácil de implementar.
# 4. Limitaciones:
#    - Puede ser computacionalmente costoso para un gran número de partículas.
#    - Requiere un modelo adecuado del sistema y del ruido.