# Este código implementa un Proceso de Decisión de Markov (MDP).
# Un MDP es un modelo matemático que se utiliza para tomar decisiones en un entorno incierto.
# Se basa en estados, acciones, recompensas y transiciones probabilísticas.

# Importamos la biblioteca numpy para realizar cálculos numéricos
import numpy as np

# Definimos las variables principales del MDP
# Estados posibles en el entorno
estados = ["Inicio", "Intermedio", "Final"]

# Acciones posibles que el agente puede tomar
acciones = ["Moverse", "Esperar"]

# Matriz de recompensas: define la recompensa por tomar una acción en un estado
# Filas representan estados, columnas representan acciones
recompensas = {
    "Inicio": {"Moverse": -1, "Esperar": 0},
    "Intermedio": {"Moverse": 10, "Esperar": -1},
    "Final": {"Moverse": 0, "Esperar": 0}
}

# Matriz de transiciones: define la probabilidad de moverse de un estado a otro
# Cada fila representa un estado actual, y cada columna un estado futuro
transiciones = {
    "Inicio": {"Inicio": 0.1, "Intermedio": 0.9, "Final": 0.0},
    "Intermedio": {"Inicio": 0.0, "Intermedio": 0.5, "Final": 0.5},
    "Final": {"Inicio": 0.0, "Intermedio": 0.0, "Final": 1.0}
}

# Factor de descuento (gamma): determina cuánto valoramos las recompensas futuras
factor_descuento = 0.9

# Inicializamos los valores de utilidad para cada estado
utilidades = {estado: 0 for estado in estados}

# Número de iteraciones para calcular las utilidades
iteraciones = 10

# Algoritmo de iteración de valores para resolver el MDP
# Este algoritmo calcula las utilidades de cada estado basándose en las recompensas y transiciones
for i in range(iteraciones):
    # Creamos una copia de las utilidades actuales para actualizarlas
    nuevas_utilidades = utilidades.copy()
    for estado in estados:
        # Calculamos la utilidad máxima para el estado actual
        max_utilidad = float("-inf")
        for accion in acciones:
            # Calculamos el valor esperado de tomar esta acción
            valor_esperado = 0
            for estado_siguiente in estados:
                probabilidad = transiciones[estado][estado_siguiente]
                recompensa = recompensas[estado][accion]
                valor_esperado += probabilidad * (recompensa + factor_descuento * utilidades[estado_siguiente])
            # Actualizamos la utilidad máxima si encontramos un valor mayor
            max_utilidad = max(max_utilidad, valor_esperado)
        # Actualizamos la utilidad del estado actual
        nuevas_utilidades[estado] = max_utilidad
    # Reemplazamos las utilidades antiguas con las nuevas
    utilidades = nuevas_utilidades

# Mostramos las utilidades finales de cada estado
print("Utilidades finales de los estados:")
for estado, utilidad in utilidades.items():
    print(f"Estado: {estado}, Utilidad: {utilidad:.2f}")

# Ejemplo práctico:
# Supongamos que un robot debe decidir si moverse o esperar en un entorno con tres estados:
# - Inicio: donde comienza
# - Intermedio: donde puede ganar una recompensa alta
# - Final: donde termina el proceso
# El robot utiliza este algoritmo para calcular la mejor estrategia y maximizar su recompensa.