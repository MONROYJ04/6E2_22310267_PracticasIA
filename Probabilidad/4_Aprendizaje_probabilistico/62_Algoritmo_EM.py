# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO EM (EXPECTATION-MAXIMIZATION) PARA MEZCLAS GAUSSIANAS
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo EM para estimar los parámetros de una mezcla 
# de dos distribuciones gaussianas. El objetivo es ajustar el modelo a los datos 
# observados, incluso cuando algunos datos son incompletos o desconocidos.

import numpy as np

# ------------------------------------------------------------------------------------
# PASO 1: INICIALIZAR LOS PARÁMETROS DEL MODELO
# ------------------------------------------------------------------------------------
# - Este paso inicializa los parámetros del modelo: medias, varianzas y pesos de las 
#   dos distribuciones gaussianas.
# - Es importante porque estos valores iniciales sirven como punto de partida para 
#   el algoritmo EM. Aunque los valores iniciales pueden ser arbitrarios, afectan 
#   la convergencia del algoritmo.
def inicializar_parametros():
    # Inicializamos las medias, varianzas y pesos de las dos gaussianas
    media1 = 0.0  # Media de la primera gaussiana
    media2 = 1.0  # Media de la segunda gaussiana
    varianza1 = 1.0  # Varianza de la primera gaussiana
    varianza2 = 1.0  # Varianza de la segunda gaussiana
    peso1 = 0.5  # Peso de la primera gaussiana
    peso2 = 0.5  # Peso de la segunda gaussiana
    return media1, media2, varianza1, varianza2, peso1, peso2

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN DE DENSIDAD DE PROBABILIDAD DE UNA GAUSSIANA
# ------------------------------------------------------------------------------------
# - Este paso define la función de densidad de probabilidad (PDF) de una distribución 
#   gaussiana. Calcula la probabilidad de un valor `x` dado una media y varianza.
# - Es crucial porque el algoritmo EM utiliza esta función para calcular las 
#   responsabilidades en el paso de Expectación.
def densidad_gaussiana(x, media, varianza):
    # Fórmula de la densidad de probabilidad de una gaussiana:
    # f(x) = (1 / sqrt(2 * pi * varianza)) * exp(-0.5 * ((x - media)^2 / varianza))
    return (1 / np.sqrt(2 * np.pi * varianza)) * np.exp(-0.5 * ((x - media) ** 2) / varianza)

# ------------------------------------------------------------------------------------
# PASO 3: PASO DE EXPECTACIÓN (E-STEP)
# ------------------------------------------------------------------------------------
# - Este paso calcula las responsabilidades (probabilidades) de cada punto de datos 
#   para cada una de las dos gaussianas.
# - Es importante porque asigna probabilidades a los datos, indicando a qué gaussiana 
#   es más probable que pertenezcan.
def paso_expectacion(datos, media1, media2, varianza1, varianza2, peso1, peso2):
    # Calcula las responsabilidades para cada gaussiana
    responsabilidad1 = peso1 * densidad_gaussiana(datos, media1, varianza1)
    responsabilidad2 = peso2 * densidad_gaussiana(datos, media2, varianza2)
    suma_responsabilidades = responsabilidad1 + responsabilidad2
    gamma1 = responsabilidad1 / suma_responsabilidades  # Probabilidad de pertenecer a la primera gaussiana
    gamma2 = responsabilidad2 / suma_responsabilidades  # Probabilidad de pertenecer a la segunda gaussiana
    return gamma1, gamma2

# ------------------------------------------------------------------------------------
# PASO 4: PASO DE MAXIMIZACIÓN (M-STEP)
# ------------------------------------------------------------------------------------
# - Este paso actualiza los parámetros del modelo (medias, varianzas y pesos) 
#   basándose en las responsabilidades calculadas en el paso anterior.
# - Es esencial porque ajusta los parámetros para que se adapten mejor a los datos.
def paso_maximizacion(datos, gamma1, gamma2):
    # Actualiza los parámetros del modelo
    peso1 = np.mean(gamma1)  # Nuevo peso de la primera gaussiana
    peso2 = np.mean(gamma2)  # Nuevo peso de la segunda gaussiana
    media1 = np.sum(gamma1 * datos) / np.sum(gamma1)  # Nueva media de la primera gaussiana
    media2 = np.sum(gamma2 * datos) / np.sum(gamma2)  # Nueva media de la segunda gaussiana
    varianza1 = np.sum(gamma1 * (datos - media1) ** 2) / np.sum(gamma1)  # Nueva varianza de la primera gaussiana
    varianza2 = np.sum(gamma2 * (datos - media2) ** 2) / np.sum(gamma2)  # Nueva varianza de la segunda gaussiana
    return media1, media2, varianza1, varianza2, peso1, peso2

# ------------------------------------------------------------------------------------
# PASO 5: ALGORITMO EM COMPLETO
# ------------------------------------------------------------------------------------
# - Este paso combina los pasos de Expectación y Maximización en un bucle iterativo.
# - Es importante porque permite que el modelo converja hacia los parámetros óptimos.
def algoritmo_em(datos, iteraciones):
    # Inicializa los parámetros
    media1, media2, varianza1, varianza2, peso1, peso2 = inicializar_parametros()
    
    # Itera entre los pasos de Expectación y Maximización
    for i in range(iteraciones):
        # Paso de Expectación
        gamma1, gamma2 = paso_expectacion(datos, media1, media2, varianza1, varianza2, peso1, peso2)
        
        # Paso de Maximización
        media1, media2, varianza1, varianza2, peso1, peso2 = paso_maximizacion(datos, gamma1, gamma2)
        
        # Imprime los parámetros en cada iteración para observar la convergencia
        print(f"Iteracion {i + 1}:")
        print(f"Media1: {media1}, Media2: {media2}")
        print(f"Varianza1: {varianza1}, Varianza2: {varianza2}")
        print(f"Peso1: {peso1}, Peso2: {peso2}")
        print("-" * 30)
    
    return media1, media2, varianza1, varianza2, peso1, peso2

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Generamos datos simulados a partir de una mezcla de dos gaussianas.
# - Ejecutamos el algoritmo EM para estimar los parámetros de las gaussianas.
if __name__ == "__main__":
    # Generamos datos simulados
    np.random.seed(42)  # Fijamos la semilla para reproducibilidad
    datos_gaussiana1 = np.random.normal(0, 1, 100)  # 100 puntos con media 0 y varianza 1
    datos_gaussiana2 = np.random.normal(5, 1, 100)  # 100 puntos con media 5 y varianza 1
    datos = np.concatenate([datos_gaussiana1, datos_gaussiana2])  # Mezclamos los datos
    
    # Ejecutamos el algoritmo EM
    iteraciones = 10  # Número de iteraciones del algoritmo
    algoritmo_em(datos, iteraciones)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo EM alterna entre dos pasos:
#    - Expectación: Calcula las responsabilidades basándose en los parámetros actuales.
#    - Maximización: Ajusta los parámetros para maximizar la probabilidad de los datos.
# 2. Suposiciones clave:
#    - Los datos provienen de una mezcla de distribuciones gaussianas.
#    - Las responsabilidades se calculan bajo la suposición de independencia.
# 3. Ventajas:
#    - Maneja datos incompletos o ruidosos.
#    - Converge a un óptimo local.
#    Limitaciones:
#    - Sensible a los valores iniciales.
#    - Puede converger a un óptimo local en lugar del global.