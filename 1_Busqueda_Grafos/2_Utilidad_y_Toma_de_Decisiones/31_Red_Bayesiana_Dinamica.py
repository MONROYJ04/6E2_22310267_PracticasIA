# Importamos la biblioteca necesaria para trabajar con probabilidades y redes bayesianas
from pomegranate import *

# Definimos las variables del modelo
# En este caso, modelaremos el clima con dos estados: soleado y lluvioso

# Probabilidad inicial de que el clima sea soleado o lluvioso
# Esto representa el conocimiento inicial antes de observar cualquier dato
estado_inicial = DiscreteDistribution({'soleado': 0.7, 'lluvioso': 0.3})

# Matriz de transición
# Define cómo cambia el clima de un día a otro
# Cada fila representa la probabilidad de transición de un estado actual a un estado futuro
matriz_transicion = ConditionalProbabilityTable(
    [
        ['soleado', 'soleado', 0.8],  # Si hoy es soleado, mañana es soleado con probabilidad 0.8
        ['soleado', 'lluvioso', 0.2],  # Si hoy es soleado, mañana es lluvioso con probabilidad 0.2
        ['lluvioso', 'soleado', 0.4],  # Si hoy es lluvioso, mañana es soleado con probabilidad 0.4
        ['lluvioso', 'lluvioso', 0.6]  # Si hoy es lluvioso, mañana es lluvioso con probabilidad 0.6
    ],
    [estado_inicial]  # La matriz depende del estado inicial
)

# Creamos los nodos de la red bayesiana dinámica
# Un nodo representa un estado o una variable en el modelo
nodo_estado_inicial = State(estado_inicial, name="estado_inicial")
nodo_transicion = State(matriz_transicion, name="transicion")

# Construimos el modelo de la Red Bayesiana Dinámica
# Usamos un modelo oculto de Markov (Hidden Markov Model) para representar la dinámica
modelo = HiddenMarkovModel('Modelo_Clima')

# Agregamos los nodos al modelo
modelo.add_states(nodo_estado_inicial, nodo_transicion)

# Definimos las transiciones entre los nodos
# Estas transiciones representan cómo se mueve el sistema entre estados
modelo.add_transition(modelo.start, nodo_estado_inicial, 1.0)  # Transición inicial desde el inicio al primer estado
modelo.add_transition(nodo_estado_inicial, nodo_transicion, 1.0)  # Transición del estado inicial a la matriz de transición
modelo.add_transition(nodo_transicion, nodo_transicion, 1.0)  # Transición recurrente dentro de la matriz de transición

# Finalizamos la construcción del modelo
modelo.bake()

# Ejemplo práctico: Predecir el clima para los próximos 7 días
# Usamos el modelo para generar una secuencia probable de estados (clima) para los próximos días
dias = 7  # Número de días a predecir
secuencia_probable = modelo.sample(dias)

# Mostramos los resultados de la predicción
print("Predicción del clima para los próximos 7 días:")
for i, estado in enumerate(secuencia_probable):
    print(f"Día {i + 1}: {estado}")

# Explicación del ejemplo práctico:
# Este ejemplo genera una secuencia de estados (soleado o lluvioso) para los próximos 7 días
# basándose en las probabilidades definidas en el modelo. No se utilizan observaciones,
# por lo que el modelo predice únicamente en función de las probabilidades iniciales y de transición.