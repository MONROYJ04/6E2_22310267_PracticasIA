# Este algoritmo implementa un modelo de Decisión Parcialmente Observable (POMDP).
# Un POMDP es una extensión de un MDP (Modelo de Decisión de Markov) donde el agente no tiene
# acceso completo al estado actual del entorno, sino que recibe observaciones parciales.

import numpy as np

# Definimos las variables principales del POMDP
# Estados posibles en el entorno
estados = ["soleado", "lluvioso"]

# Acciones posibles que el agente puede tomar
acciones = ["llevar_paraguas", "no_llevar_paraguas"]

# Observaciones posibles que el agente puede recibir
observaciones = ["ver_sol", "ver_nubes"]

# Matriz de transicion de estados: P(s'|s, a)
# Probabilidad de pasar de un estado actual a un estado futuro dado una accion
transicion = {
    "soleado": {
        "llevar_paraguas": {"soleado": 0.8, "lluvioso": 0.2},
        "no_llevar_paraguas": {"soleado": 0.7, "lluvioso": 0.3},
    },
    "lluvioso": {
        "llevar_paraguas": {"soleado": 0.4, "lluvioso": 0.6},
        "no_llevar_paraguas": {"soleado": 0.3, "lluvioso": 0.7},
    },
}

# Matriz de observacion: P(o|s)
# Probabilidad de recibir una observacion dado un estado
observacion = {
    "soleado": {"ver_sol": 0.9, "ver_nubes": 0.1},
    "lluvioso": {"ver_sol": 0.2, "ver_nubes": 0.8},
}

# Recompensas: R(s, a)
# Recompensa obtenida al tomar una accion en un estado
recompensas = {
    "soleado": {"llevar_paraguas": -1, "no_llevar_paraguas": 1},
    "lluvioso": {"llevar_paraguas": 1, "no_llevar_paraguas": -3},
}

# Creemos una funcion para calcular la creencia inicial
def inicializar_creencia():
    # La creencia inicial es una distribucion de probabilidad sobre los estados
    return {"soleado": 0.5, "lluvioso": 0.5}

# Actualizacion de la creencia basada en la observacion recibida
def actualizar_creencia(creencia, accion, observacion_recibida):
    nueva_creencia = {}
    for estado in estados:
        prob_observacion = observacion[estado][observacion_recibida]
        prob_transicion = sum(
            creencia[estado_anterior]
            * transicion[estado_anterior][accion][estado]
            for estado_anterior in estados
        )
        nueva_creencia[estado] = prob_observacion * prob_transicion

    # Normalizamos la creencia para que sea una distribucion de probabilidad
    suma = sum(nueva_creencia.values())
    for estado in nueva_creencia:
        nueva_creencia[estado] /= suma

    return nueva_creencia

# Funcion para seleccionar la mejor accion basada en la creencia actual
def seleccionar_mejor_accion(creencia):
    mejor_accion = None
    mejor_valor = float("-inf")
    for accion in acciones:
        valor_accion = sum(
            creencia[estado] * recompensas[estado][accion] for estado in estados
        )
        if valor_accion > mejor_valor:
            mejor_valor = valor_accion
            mejor_accion = accion
    return mejor_accion

# Ejemplo practico
def ejemplo_practico():
    # Inicializamos la creencia
    creencia = inicializar_creencia()
    print("Creencia inicial:", creencia)

    # Iteramos por un numero de pasos
    for paso in range(3):
        print(f"\nPaso {paso + 1}:")
        # Seleccionamos la mejor accion basada en la creencia actual
        accion = seleccionar_mejor_accion(creencia)
        print("Accion seleccionada:", accion)

        # Simulamos una observacion (en un caso real, esto seria recibido del entorno)
        observacion_recibida = np.random.choice(observaciones)
        print("Observacion recibida:", observacion_recibida)

        # Actualizamos la creencia basada en la accion y la observacion
        creencia = actualizar_creencia(creencia, accion, observacion_recibida)
        print("Nueva creencia:", creencia)

# Ejecutamos el ejemplo practico
if __name__ == "__main__":
    ejemplo_practico()