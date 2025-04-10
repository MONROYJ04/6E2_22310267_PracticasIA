# Este algoritmo calcula la incertidumbre (entropia) de un conjunto de datos.
# La entropia mide el grado de incertidumbre o desorden en un sistema.
# Es ampliamente utilizada en teoría de la información y aprendizaje automático.

import math

def calcular_entropia(probabilidades):
    """
    Calcula la entropia de un conjunto de probabilidades.
    
    Parametros:
    probabilidades (list): Una lista de probabilidades (valores entre 0 y 1).
    
    Retorna:
    float: El valor de la entropia.
    """
    # Inicializamos la entropia en 0
    entropia = 0
    
    # Iteramos sobre cada probabilidad
    for probabilidad in probabilidades:
        # Verificamos que la probabilidad sea mayor que 0 para evitar errores matematicos
        if probabilidad > 0:
            # Aplicamos la formula de la entropia: -p * log2(p)
            entropia -= probabilidad * math.log2(probabilidad)
    
    # Retornamos el valor calculado de la entropia
    return entropia

# Ejemplo practico:
# Supongamos que tenemos un dado justo de 6 caras.
# La probabilidad de que salga cualquier cara es 1/6.
# Queremos calcular la incertidumbre asociada a este dado.

# Definimos las probabilidades de cada cara del dado
probabilidades_dado = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# Calculamos la entropia del dado
entropia_dado = calcular_entropia(probabilidades_dado)

# Mostramos el resultado
print("La entropia del dado es:", entropia_dado)

# Explicacion del resultado:
# La entropia del dado es alta porque todas las caras tienen la misma probabilidad,
# lo que significa que hay mucha incertidumbre sobre el resultado de lanzar el dado.