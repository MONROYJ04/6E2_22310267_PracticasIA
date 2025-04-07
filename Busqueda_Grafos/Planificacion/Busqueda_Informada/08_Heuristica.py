# Este algoritmo implementa la heurística de Manhattan para resolver el problema del 8-puzzle.
# Una heurística es una técnica que nos ayuda a resolver problemas de manera más eficiente,
# proporcionando una "estimación" o "guía" para tomar decisiones en un algoritmo de búsqueda.

def distancia_manhattan(estado, objetivo):
    """
    Calcula la heurística de Distancia Manhattan para el problema del 8-puzzle.
    La distancia Manhattan mide cuántos movimientos (arriba, abajo, izquierda, derecha)
    necesita cada ficha para llegar a su posición objetivo.

    :param estado: Lista que representa el estado actual del puzzle (ej: [1, 2, 3, 4, 5, 6, 7, 8, 0]).
                   El número 0 representa el espacio vacío.
    :param objetivo: Lista que representa el estado objetivo del puzzle.
    :return: La suma de las distancias Manhattan de todas las fichas.
    """
    # Inicializamos la variable que almacenará la distancia total
    distancia = 0

    # Recorremos cada posición del puzzle (9 posiciones en una cuadrícula 3x3)
    for i in range(9):
        # Si la posición actual contiene el espacio vacío (0), lo ignoramos
        if estado[i] == 0:
            continue  # Saltamos a la siguiente iteración

        # Calculamos la fila y columna actuales de la ficha en el estado actual
        fila_actual, columna_actual = i // 3, i % 3

        # Buscamos la posición objetivo de la ficha en el estado objetivo
        indice_objetivo = objetivo.index(estado[i])
        fila_objetivo, columna_objetivo = indice_objetivo // 3, indice_objetivo % 3

        # Calculamos la distancia Manhattan para esta ficha
        # Es la suma de las diferencias absolutas entre filas y columnas
        distancia += abs(fila_actual - fila_objetivo) + abs(columna_actual - columna_objetivo)

    # Retornamos la distancia total calculada
    return distancia

# Ejemplo práctico:
# Estado inicial del puzzle (el 0 representa el espacio vacío)
estado_inicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]

# Estado objetivo del puzzle (la solución deseada)
estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Calculamos la heurística (distancia Manhattan) para el estado inicial
resultado = distancia_manhattan(estado_inicial, estado_objetivo)

# Imprimimos el resultado con una explicación
print("Estado inicial:", estado_inicial)
print("Estado objetivo:", estado_objetivo)
print("Heurística (Distancia Manhattan):", resultado)

# Explicación del ejemplo:
# En el estado inicial, las fichas 7 y 8 están fuera de lugar:
# - La ficha 7 está en la posición (2, 1) pero debería estar en (2, 0). Distancia = 1.
# - La ficha 8 está en la posición (2, 2) pero debería estar en (2, 1). Distancia = 1.
# La suma de estas distancias es 1 + 1 = 2, que es el resultado calculado.