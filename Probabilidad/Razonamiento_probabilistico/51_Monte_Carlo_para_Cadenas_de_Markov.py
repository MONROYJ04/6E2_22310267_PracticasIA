# Este algoritmo implementa un método de Monte Carlo para simular una Cadena de Markov.
# Una Cadena de Markov es un modelo matemático que describe un sistema que cambia de estado
# de acuerdo con ciertas probabilidades de transición.

import random  # Importamos la librería random para generar números aleatorios.

# Definimos una función para simular una Cadena de Markov.
def simulacion_cadena_markov(matriz_transicion, estado_inicial, pasos):
    """
    Simula una Cadena de Markov utilizando el método de Monte Carlo.

    Args:
        matriz_transicion (list of list): Matriz de transición que define las probabilidades de cambio entre estados.
        estado_inicial (int): Estado inicial de la cadena.
        pasos (int): Número de pasos a simular.

    Returns:
        list: Lista de estados visitados durante la simulación.
    """
    # Lista para almacenar los estados visitados.
    estados_visitados = [estado_inicial]

    # Iteramos por el número de pasos especificado.
    for _ in range(pasos):
        # Obtenemos el estado actual.
        estado_actual = estados_visitados[-1]

        # Generamos un número aleatorio entre 0 y 1.
        numero_aleatorio = random.random()

        # Calculamos el siguiente estado basado en la matriz de transición.
        suma_probabilidades = 0
        for siguiente_estado, probabilidad in enumerate(matriz_transicion[estado_actual]):
            suma_probabilidades += probabilidad
            # Si el número aleatorio cae dentro del rango de la probabilidad acumulada,
            # seleccionamos el siguiente estado.
            if numero_aleatorio < suma_probabilidades:
                estados_visitados.append(siguiente_estado)
                break

    # Retornamos la lista de estados visitados.
    return estados_visitados

# Ejemplo práctico:
# Supongamos que tenemos una cadena de Markov con 3 estados: 0, 1 y 2.
# La matriz de transición define las probabilidades de moverse de un estado a otro.
# Por ejemplo, desde el estado 0, hay un 50% de probabilidad de quedarse en 0,
# un 30% de ir al estado 1 y un 20% de ir al estado 2.

matriz_transicion = [
    [0.5, 0.3, 0.2],  # Probabilidades desde el estado 0
    [0.2, 0.6, 0.2],  # Probabilidades desde el estado 1
    [0.1, 0.3, 0.6]   # Probabilidades desde el estado 2
]

# Estado inicial de la cadena.
estado_inicial = 0

# Número de pasos a simular.
pasos = 10

# Llamamos a la función para simular la cadena de Markov.
resultado_simulacion = simulacion_cadena_markov(matriz_transicion, estado_inicial, pasos)

# Mostramos los resultados.
print("Estados visitados durante la simulación:", resultado_simulacion)

# Explicación del ejemplo:
# En este ejemplo, comenzamos en el estado 0 y simulamos 10 pasos.
# La matriz de transición define cómo se mueve la cadena entre los estados.
# El resultado es una lista de estados visitados, que muestra cómo evoluciona
# el sistema a lo largo del tiempo.