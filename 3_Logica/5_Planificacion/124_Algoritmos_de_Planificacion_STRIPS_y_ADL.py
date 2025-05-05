# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE PLANIFICACIÓN CON STRIPS Y ADL
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de planificación basado en STRIPS (Sistema de Planificación de Tareas) 
# y ADL (Lenguaje de Descripción de Acciones). El objetivo es generar un plan (secuencia de acciones) 
# que permita alcanzar un estado deseado (metas) a partir de un estado inicial, utilizando un conjunto 
# de acciones definidas.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE "Accion"
# ------------------------------------------------------------------------------------
# - Aquí definimos una clase que representa una acción en el modelo STRIPS.
# - Cada acción tiene un nombre, un conjunto de precondiciones (lo que debe cumplirse para ejecutarla) 
#   y un conjunto de efectos (lo que cambia en el estado al ejecutarla).
# - Esto es importante porque las acciones son los bloques básicos que el algoritmo utiliza para planificar.

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        # Nombre de la acción (por ejemplo, "cortar_ingredientes").
        self.nombre = nombre
        # Precondiciones: conjunto de condiciones necesarias para ejecutar la acción.
        self.precondiciones = precondiciones
        # Efectos: conjunto de cambios que ocurren en el estado al ejecutar la acción.
        self.efectos = efectos

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PARA VERIFICAR PRECONDICIONES
# ------------------------------------------------------------------------------------
# - Esta función verifica si todas las precondiciones de una acción están presentes en el estado actual.
# - Es importante porque una acción solo puede ejecutarse si sus precondiciones están satisfechas.
# - Parámetros:
#   - `estado`: conjunto que representa el estado actual.
#   - `precondiciones`: conjunto de condiciones necesarias para ejecutar una acción.

def verificar_precondiciones(estado, precondiciones):
    # Recorremos todas las precondiciones y verificamos si están en el estado actual.
    for precondicion in precondiciones:
        if precondicion not in estado:
            return False  # Si alguna precondición no está presente, devolvemos False.
    return True  # Si todas las precondiciones están presentes, devolvemos True.

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN PARA APLICAR LOS EFECTOS DE UNA ACCIÓN
# ------------------------------------------------------------------------------------
# - Esta función aplica los efectos de una acción al estado actual.
# - Los efectos pueden ser positivos (agregar algo al estado) o negativos (eliminar algo del estado).
# - Parámetros:
#   - `estado`: conjunto que representa el estado actual.
#   - `efectos`: conjunto de cambios que ocurren al ejecutar la acción.

def aplicar_efectos(estado, efectos):
    # Creamos una copia del estado actual para no modificar el original.
    nuevo_estado = estado.copy()
    for efecto in efectos:
        # Si el efecto es positivo (indicado por un "+"), lo añadimos al estado.
        if efecto.startswith('+'):
            nuevo_estado.add(efecto[1:])
        # Si el efecto es negativo (indicado por un "-"), lo eliminamos del estado.
        elif efecto.startswith('-'):
            nuevo_estado.discard(efecto[1:])
    return nuevo_estado  # Retornamos el nuevo estado modificado.

# ------------------------------------------------------------------------------------
# PASO 4: ALGORITMO DE PLANIFICACIÓN
# ------------------------------------------------------------------------------------
# - Este es el núcleo del programa. Genera un plan (secuencia de acciones) para alcanzar las metas 
#   desde el estado inicial.
# - Utiliza las funciones anteriores para verificar precondiciones y aplicar efectos.
# - Parámetros:
#   - `estado_inicial`: conjunto que representa el estado inicial.
#   - `metas`: conjunto de condiciones que queremos alcanzar.
#   - `acciones`: lista de objetos `Accion` que representan las acciones disponibles.

def planificar(estado_inicial, metas, acciones):
    # Creamos una lista para almacenar el plan (secuencia de acciones).
    plan = []
    # Creamos una copia del estado inicial para trabajar con él.
    estado_actual = estado_inicial.copy()

    # Mientras no se hayan alcanzado todas las metas...
    while not metas.issubset(estado_actual):
        # Buscamos una acción que pueda ejecutarse y que acerque al estado deseado.
        accion_elegida = None
        for accion in acciones:
            # Verificamos si las precondiciones de la acción están satisfechas.
            if verificar_precondiciones(estado_actual, accion.precondiciones):
                # Verificamos si la acción ayuda a cumplir alguna meta.
                if any(meta in accion.efectos for meta in metas):
                    accion_elegida = accion
                    break

        # Si no encontramos una acción válida, no se puede planificar.
        if accion_elegida is None:
            raise Exception("No se puede encontrar un plan para alcanzar las metas.")

        # Añadimos la acción al plan.
        plan.append(accion_elegida.nombre)
        # Actualizamos el estado actual aplicando los efectos de la acción.
        estado_actual = aplicar_efectos(estado_actual, accion_elegida.efectos)

    # Retornamos el plan generado.
    return plan

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO - PLANIFICACIÓN PARA COCINAR UNA COMIDA
# ------------------------------------------------------------------------------------
# - Este ejemplo muestra cómo usar el algoritmo para planificar la preparación de una comida.
# - Estado inicial: tenemos ingredientes disponibles y utensilios limpios.
# - Metas: queremos tener una comida preparada.
# - Acciones disponibles: lavar utensilios, cortar ingredientes y cocinar.

if __name__ == "__main__":
    # Estado inicial: conjunto de condiciones iniciales.
    estado_inicial = {"ingredientes_disponibles", "utensilios_limpios"}

    # Metas: conjunto de condiciones que queremos alcanzar.
    metas = {"comida_preparada"}

    # Definimos las acciones disponibles.
    acciones = [
        Accion(
            "lavar_utensilios",
            precondiciones={"utensilios_sucios"},
            efectos={"+utensilios_limpios", "-utensilios_sucios"}
        ),
        Accion(
            "cortar_ingredientes",
            precondiciones={"ingredientes_disponibles", "utensilios_limpios"},
            efectos={"+ingredientes_cortados"}
        ),
        Accion(
            "cocinar",
            precondiciones={"ingredientes_cortados", "utensilios_limpios"},
            efectos={"+comida_preparada"}
        )
    ]

    # Generamos el plan utilizando el algoritmo de planificación.
    try:
        plan = planificar(estado_inicial, metas, acciones)
        print("Plan generado:", plan)  # Mostramos el plan generado.
    except Exception as e:
        print("Error:", e)  # Mostramos un mensaje de error si no se puede generar un plan.

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza un enfoque iterativo para buscar acciones que acerquen al estado deseado.
# 2. Las precondiciones aseguran que las acciones solo se ejecuten cuando sea posible.
# 3. Los efectos actualizan el estado para reflejar los cambios realizados por las acciones.
# 4. Ventajas:
#    - Es simple y fácil de entender.
#    - Funciona bien para problemas pequeños con un conjunto limitado de acciones.
# 5. Limitaciones:
#    - No es eficiente para problemas grandes o complejos.
#    - No considera costos asociados a las acciones (es decir, no optimiza el plan).