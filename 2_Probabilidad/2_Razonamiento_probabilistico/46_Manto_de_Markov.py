# Este programa implementa un modelo de cadenas de Markov.
# Las cadenas de Markov son un modelo matemático que describe un sistema que cambia de estado
# de acuerdo con ciertas probabilidades. Este modelo es útil para predecir el próximo estado
# basado únicamente en el estado actual.

import random

# Definimos una funcion para generar una cadena de Markov
def generar_cadena_markov(transiciones, estado_inicial, pasos):
    """
    Genera una secuencia de estados basada en una cadena de Markov.

    :param transiciones: Diccionario que define las probabilidades de transicion entre estados.
    :param estado_inicial: Estado inicial de la cadena.
    :param pasos: Numero de pasos a simular.
    :return: Lista con la secuencia de estados generados.
    """
    # Lista para almacenar la secuencia de estados
    secuencia = [estado_inicial]
    
    # Variable que almacena el estado actual
    estado_actual = estado_inicial

    # Iteramos para generar la cantidad de pasos solicitados
    for _ in range(pasos):
        # Obtenemos las probabilidades de transicion del estado actual
        probabilidades = transiciones[estado_actual]
        
        # Elegimos el siguiente estado basado en las probabilidades
        siguiente_estado = random.choices(
            list(probabilidades.keys()),  # Lista de posibles estados
            list(probabilidades.values()) # Lista de probabilidades asociadas
        )[0]
        
        # Agregamos el siguiente estado a la secuencia
        secuencia.append(siguiente_estado)
        
        # Actualizamos el estado actual
        estado_actual = siguiente_estado

    return secuencia

# Ejemplo practico: Prediccion del clima
# Estados posibles: Soleado, Nublado, Lluvioso
# Matriz de transicion: Define las probabilidades de cambiar de un estado a otro
transiciones_clima = {
    "Soleado": {"Soleado": 0.8, "Nublado": 0.15, "Lluvioso": 0.05},
    "Nublado": {"Soleado": 0.2, "Nublado": 0.6, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.1, "Nublado": 0.3, "Lluvioso": 0.6}
}

# Estado inicial: Comenzamos con un dia soleado
estado_inicial_clima = "Soleado"

# Numero de dias a predecir
dias_a_predecir = 10

# Generamos la secuencia de estados (prediccion del clima)
prediccion_clima = generar_cadena_markov(transiciones_clima, estado_inicial_clima, dias_a_predecir)

# Mostramos la prediccion
print("Prediccion del clima para los proximos dias:")
print(prediccion_clima)

# Explicacion del ejemplo:
# Este ejemplo simula el clima durante 10 dias. Comienza con un dia soleado y utiliza
# las probabilidades definidas en la matriz de transicion para determinar si el siguiente
# dia sera soleado, nublado o lluvioso. La salida es una lista con la secuencia de estados
# (clima) para los proximos dias.