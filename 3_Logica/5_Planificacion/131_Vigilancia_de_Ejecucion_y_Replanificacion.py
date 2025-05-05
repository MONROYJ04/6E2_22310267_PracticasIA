# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: VIGILANCIA DE EJECUCIÓN Y REPLANIFICACIÓN
# ------------------------------------------------------------------------------------
# Este algoritmo implementa un sistema para monitorear la ejecución de un plan y 
# realizar ajustes dinámicos si se detectan fallos en la ejecución de las tareas.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos la librería `random` para simular el éxito o fallo de las tareas.
# - Esto permite que el algoritmo sea dinámico y no dependa de datos externos.
import random

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA CLASE `Plan`
# ------------------------------------------------------------------------------------
# - La clase `Plan` representa un conjunto de tareas que deben ejecutarse en orden.
# - Incluye métodos para obtener la tarea actual y avanzar a la siguiente tarea.
# - Esto es esencial para estructurar el flujo del plan y rastrear el progreso.

class Plan:
    def __init__(self, tareas):
        # Inicializamos el plan con una lista de tareas.
        self.tareas = tareas
        # Índice que rastrea la tarea actual en ejecución.
        self.tarea_actual = 0

    def obtener_tarea_actual(self):
        # Devuelve la tarea actual si no hemos llegado al final del plan.
        if self.tarea_actual < len(self.tareas):
            return self.tareas[self.tarea_actual]
        # Si no hay más tareas, devolvemos `None`.
        return None

    def avanzar_tarea(self):
        # Avanza al siguiente índice de tarea si no hemos terminado el plan.
        if self.tarea_actual < len(self.tareas):
            self.tarea_actual += 1

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN `ejecutar_tarea`
# ------------------------------------------------------------------------------------
# - Esta función simula la ejecución de una tarea.
# - Usa `random.choice` para determinar aleatoriamente si la tarea tiene éxito o falla.
# - Devuelve `True` si la tarea se completa con éxito y `False` si falla.

def ejecutar_tarea(tarea):
    print(f"Ejecutando tarea: {tarea}")
    # Simulamos el éxito o fallo de la tarea de forma aleatoria.
    exito = random.choice([True, False])
    if exito:
        print(f"Tarea '{tarea}' completada con éxito.")
    else:
        print(f"Tarea '{tarea}' falló.")
    return exito

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR LA FUNCIÓN `replanificar`
# ------------------------------------------------------------------------------------
# - Esta función se ejecuta cuando una tarea falla.
# - Simula la replanificación añadiendo una nueva tarea al final del plan.
# - Esto asegura que las tareas fallidas puedan ser reintentadas.

def replanificar(plan, tarea_fallida):
    print(f"Replanificando debido a fallo en la tarea: {tarea_fallida}")
    # Añadimos una nueva tarea al final del plan para reintentar la tarea fallida.
    plan.tareas.append(f"Reintentar {tarea_fallida}")
    print(f"Nuevo plan: {plan.tareas}")

# ------------------------------------------------------------------------------------
# PASO 5: DEFINIR LA FUNCIÓN PRINCIPAL `vigilancia_y_replanificacion`
# ------------------------------------------------------------------------------------
# - Esta función implementa el núcleo del algoritmo.
# - Monitorea la ejecución de las tareas y llama a `replanificar` si una tarea falla.
# - El ciclo continúa hasta que todas las tareas se hayan completado.

def vigilancia_y_replanificacion(plan):
    while plan.obtener_tarea_actual() is not None:
        # Obtenemos la tarea actual del plan.
        tarea_actual = plan.obtener_tarea_actual()
        # Intentamos ejecutar la tarea actual.
        exito = ejecutar_tarea(tarea_actual)
        if exito:
            # Si la tarea tiene éxito, avanzamos a la siguiente.
            plan.avanzar_tarea()
        else:
            # Si la tarea falla, replanificamos.
            replanificar(plan, tarea_actual)

# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos un plan inicial con tres tareas.
# - Ejecutamos el algoritmo de vigilancia y replanificación.
# - Observamos cómo el algoritmo maneja fallos y ajusta el plan dinámicamente.

if __name__ == "__main__":
    # Creamos un plan inicial con una lista de tareas.
    plan_inicial = Plan(["Tarea 1", "Tarea 2", "Tarea 3"])

    print("Iniciando vigilancia de ejecución y replanificación...")
    # Ejecutamos el algoritmo de vigilancia y replanificación.
    vigilancia_y_replanificacion(plan_inicial)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo sigue un enfoque iterativo para ejecutar un conjunto de tareas.
# 2. Si una tarea falla, se replanifica añadiendo una nueva tarea para reintentarla.
# 3. Suposiciones clave:
#    - Las tareas son independientes entre sí.
#    - El éxito o fallo de una tarea es aleatorio (simulado con `random.choice`).
# 4. Ventajas:
#    - El algoritmo es flexible y puede adaptarse a fallos inesperados.
#    - Es fácil de extender para incluir lógica de replanificación más compleja.
# 5. Limitaciones:
#    - La aleatoriedad puede no reflejar escenarios del mundo real.
#    - No considera dependencias entre tareas.

# ------------------------------------------------------------------------------------
# EJEMPLO DE SALIDA
# ------------------------------------------------------------------------------------
# Iniciando vigilancia de ejecución y replanificación...
# Ejecutando tarea: Tarea 1
# Tarea 'Tarea 1' completada con éxito.
# Ejecutando tarea: Tarea 2
# Tarea 'Tarea 2' falló.
# Replanificando debido a fallo en la tarea: Tarea 2
# Nuevo plan: ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Reintentar Tarea 2']
# Ejecutando tarea: Tarea 3
# Tarea 'Tarea 3' completada con éxito.
# Ejecutando tarea: Reintentar Tarea 2
# Tarea 'Reintentar Tarea 2' completada con éxito.