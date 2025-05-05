# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: PLANIFICACIÓN CONDICIONAL PARA ALCANZAR UN OBJETIVO
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de planificación condicional. 
# Su propósito es generar un plan de acciones que permita alcanzar un estado objetivo 
# a partir de un estado inicial, evaluando condiciones en cada paso.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Esta función realiza la planificación condicional.
# - Toma como entrada el estado inicial, el estado objetivo y una lista de acciones posibles.
# - Devuelve una lista de acciones que forman el plan para alcanzar el objetivo.
def planificacion_condicional(estado_inicial, objetivo, acciones):
    """
    Funcion que realiza una planificación condicional.
    
    :param estado_inicial: Estado inicial del sistema (diccionario con variables del entorno).
    :param objetivo: Estado deseado o meta (diccionario con variables del entorno).
    :param acciones: Lista de acciones posibles (cada accion es una funcion).
    :return: Plan generado (lista de acciones a ejecutar).
    """
    # Inicializamos el plan como una lista vacía
    plan = []

    # Variable para rastrear el estado actual
    estado_actual = estado_inicial.copy()

    # ------------------------------------------------------------------------------------
    # PASO 2: BUCLE PRINCIPAL PARA GENERAR EL PLAN
    # ------------------------------------------------------------------------------------
    # - Mientras el estado actual no cumpla con el objetivo, seguimos evaluando acciones.
    # - Este bucle asegura que el algoritmo intente alcanzar el objetivo paso a paso.
    while not cumple_objetivo(estado_actual, objetivo):
        # Bandera para verificar si se aplicó alguna acción
        accion_aplicada = False

        # ------------------------------------------------------------------------------------
        # PASO 3: EVALUACIÓN DE ACCIONES DISPONIBLES
        # ------------------------------------------------------------------------------------
        # - Iteramos sobre las acciones para verificar cuál es aplicable al estado actual.
        # - Si una acción es aplicable, se ejecuta y se actualiza el estado.
        for accion in acciones:
            # Verificamos si la acción es aplicable al estado actual
            if accion["condicion"](estado_actual):
                # Aplicamos la acción y actualizamos el estado actual
                estado_actual = accion["efecto"](estado_actual)
                # Agregamos la acción al plan
                plan.append(accion["nombre"])
                accion_aplicada = True
                break

        # ------------------------------------------------------------------------------------
        # PASO 4: VERIFICACIÓN DE BLOQUEO
        # ------------------------------------------------------------------------------------
        # - Si ninguna acción es aplicable, el algoritmo no puede continuar.
        # - Esto indica que el objetivo no es alcanzable desde el estado actual.
        if not accion_aplicada:
            print("No se puede alcanzar el objetivo desde el estado actual.")
            return None

    # ------------------------------------------------------------------------------------
    # PASO 5: RETORNO DEL PLAN GENERADO
    # ------------------------------------------------------------------------------------
    # - Si el bucle termina, significa que se alcanzó el objetivo.
    # - El plan generado se devuelve como una lista de acciones.
    return plan

# ------------------------------------------------------------------------------------
# PASO 6: FUNCIÓN AUXILIAR PARA VERIFICAR EL OBJETIVO
# ------------------------------------------------------------------------------------
# - Esta función verifica si el estado actual cumple con el estado objetivo.
# - Compara cada clave y valor del estado objetivo con el estado actual.
def cumple_objetivo(estado_actual, objetivo):
    """
    Verifica si el estado actual cumple con el objetivo.
    
    :param estado_actual: Estado actual del sistema.
    :param objetivo: Estado deseado o meta.
    :return: True si el estado actual cumple con el objetivo, False en caso contrario.
    """
    for clave, valor in objetivo.items():
        if estado_actual.get(clave) != valor:
            return False
    return True

# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este ejemplo muestra cómo usar el algoritmo para resolver un problema simple.
# - El objetivo es abrir una puerta que inicialmente está cerrada.
if __name__ == "__main__":
    # Estado inicial del entorno
    estado_inicial = {
        "llave": False,  # La llave no está en posesión
        "puerta_abierta": False  # La puerta está cerrada
    }

    # Estado objetivo (meta)
    objetivo = {
        "puerta_abierta": True  # Queremos que la puerta esté abierta
    }

    # ------------------------------------------------------------------------------------
    # PASO 8: DEFINICIÓN DE LAS ACCIONES POSIBLES
    # ------------------------------------------------------------------------------------
    # - Cada acción tiene un nombre, una condición para ejecutarse y un efecto sobre el estado.
    acciones = [
        {
            "nombre": "Tomar llave",
            "condicion": lambda estado: not estado["llave"],  # Solo si no tenemos la llave
            "efecto": lambda estado: {**estado, "llave": True}  # Actualizamos el estado para tener la llave
        },
        {
            "nombre": "Abrir puerta",
            "condicion": lambda estado: estado["llave"] and not estado["puerta_abierta"],  # Si tenemos la llave y la puerta está cerrada
            "efecto": lambda estado: {**estado, "puerta_abierta": True}  # Actualizamos el estado para abrir la puerta
        }
    ]

    # ------------------------------------------------------------------------------------
    # PASO 9: EJECUCIÓN DEL ALGORITMO
    # ------------------------------------------------------------------------------------
    # - Llamamos a la función de planificación condicional con los parámetros definidos.
    # - Mostramos el plan generado o un mensaje de error si no es posible generar un plan.
    plan = planificacion_condicional(estado_inicial, objetivo, acciones)

    # Mostramos el resultado
    if plan:
        print("Plan generado:", plan)
    else:
        print("No se pudo generar un plan.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza un enfoque iterativo para evaluar y aplicar acciones.
# 2. Supone que las acciones tienen condiciones claras y efectos deterministas.
# 3. Ventajas:
#    - Es simple y fácil de entender.
#    - Útil para problemas pequeños con un número limitado de acciones.
# 4. Limitaciones:
#    - No maneja incertidumbre en los efectos de las acciones.
#    - Puede quedarse atascado si no hay acciones aplicables.