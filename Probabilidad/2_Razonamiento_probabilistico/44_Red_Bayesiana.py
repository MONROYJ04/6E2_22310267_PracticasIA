# Importamos las librerías necesarias
from pgmpy.models import BayesianNetwork  # Para crear y trabajar con redes bayesianas
from pgmpy.factors.discrete import TabularCPD  # Para definir las tablas de probabilidad condicional (CPT)
from pgmpy.inference import VariableElimination  # Para realizar inferencias en la red

# Creamos una red bayesiana simple
# Una red bayesiana es un modelo probabilístico que representa relaciones de dependencia entre variables.
# En este caso, vamos a modelar un ejemplo práctico: 
# ¿Cuál es la probabilidad de que una persona tenga gripe dado que tiene fiebre y tos?

# Paso 1: Definir la estructura de la red
# La estructura se define como un grafo dirigido donde los nodos son las variables y las aristas representan dependencias.
red_bayesiana = BayesianNetwork([
    ('Gripe', 'Fiebre'),  # La gripe puede causar fiebre
    ('Gripe', 'Tos')      # La gripe puede causar tos
])

# Paso 2: Definir las tablas de probabilidad condicional (CPT)
# Estas tablas indican las probabilidades de cada variable dado el estado de sus padres.

# Probabilidad de tener gripe (sin condiciones, es un nodo raíz)
cpd_gripe = TabularCPD(variable='Gripe', variable_card=2, values=[[0.9], [0.1]])
# 90% de probabilidad de no tener gripe, 10% de probabilidad de tener gripe

# Probabilidad de tener fiebre dado que se tiene o no gripe
cpd_fiebre = TabularCPD(
    variable='Fiebre', variable_card=2,
    values=[
        [0.8, 0.2],  # Probabilidad de no tener fiebre
        [0.2, 0.8]   # Probabilidad de tener fiebre
    ],
    evidence=['Gripe'], evidence_card=[2]
)
# Si no hay gripe, 80% de probabilidad de no tener fiebre y 20% de tener fiebre
# Si hay gripe, 20% de probabilidad de no tener fiebre y 80% de tener fiebre

# Probabilidad de tener tos dado que se tiene o no gripe
cpd_tos = TabularCPD(
    variable='Tos', variable_card=2,
    values=[
        [0.7, 0.3],  # Probabilidad de no tener tos
        [0.3, 0.7]   # Probabilidad de tener tos
    ],
    evidence=['Gripe'], evidence_card=[2]
)
# Si no hay gripe, 70% de probabilidad de no tener tos y 30% de tener tos
# Si hay gripe, 30% de probabilidad de no tener tos y 70% de tener tos

# Paso 3: Asociar las tablas de probabilidad condicional con la red
red_bayesiana.add_cpds(cpd_gripe, cpd_fiebre, cpd_tos)

# Verificamos que la red esté bien definida
assert red_bayesiana.check_model(), "La red bayesiana no está bien definida."

# Paso 4: Realizar inferencias
# Usamos VariableElimination para calcular probabilidades condicionales
inferencia = VariableElimination(red_bayesiana)

# Ejemplo práctico: ¿Cuál es la probabilidad de que una persona tenga gripe dado que tiene fiebre y tos?
resultado = inferencia.query(variables=['Gripe'], evidence={'Fiebre': 1, 'Tos': 1})

# Imprimimos el resultado
print("Probabilidad de tener gripe dado que hay fiebre y tos:")
print(resultado)