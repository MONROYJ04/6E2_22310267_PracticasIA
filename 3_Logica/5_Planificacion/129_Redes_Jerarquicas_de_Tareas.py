# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: REDES JERÁRQUICAS DE TAREAS (HTN) PARA PLANIFICACIÓN DE TAREAS
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de Redes Jerárquicas de Tareas (HTN), que permite 
# descomponer una tarea compleja en subtareas más simples y ejecutarlas de manera ordenada.
# Es útil para resolver problemas de planificación en inteligencia artificial.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE TAREA
# ------------------------------------------------------------------------------------
# - Este bloque define la estructura básica de una tarea.
# - Cada tarea puede ser atómica (sin subtareas) o compuesta (con subtareas).
# - La clase incluye métodos para verificar si una tarea es atómica y para almacenar 
#   acciones asociadas a tareas atómicas.

class Tarea:
    def __init__(self, nombre, subtareas=None, accion=None):
        # Nombre de la tarea (por ejemplo, "Lavar verduras").
        self.nombre = nombre
        # Lista de subtareas (si la tarea es compuesta).
        self.subtareas = subtareas if subtareas else []
        # Acción que se ejecutará si la tarea es atómica.
        self.accion = accion

    def es_tarea_atomica(self):
        # Verifica si la tarea no tiene subtareas (es atómica).
        return len(self.subtareas) == 0

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PARA EJECUTAR UNA TAREA
# ------------------------------------------------------------------------------------
# - Esta función ejecuta una tarea, ya sea atómica o compuesta.
# - Si la tarea es atómica, ejecuta su acción asociada.
# - Si la tarea es compuesta, descompone la tarea en subtareas y las ejecuta recursivamente.
# - Este paso es clave para implementar la planificación jerárquica.

def ejecutar_tarea(tarea):
    # Si la tarea es atómica, ejecuta su acción.
    if tarea.es_tarea_atomica():
        print(f"Ejecutando tarea: {tarea.nombre}")
        if tarea.accion:
            tarea.accion()
    else:
        # Si la tarea tiene subtareas, descompón y ejecuta cada una.
        print(f"Descomponiendo tarea: {tarea.nombre}")
        for subtarea in tarea.subtareas:
            ejecutar_tarea(subtarea)

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO - PREPARAR UNA COMIDA
# ------------------------------------------------------------------------------------
# - Este bloque define un ejemplo práctico de cómo usar el algoritmo HTN.
# - La tarea principal es "Preparar comida", que se descompone en subtareas como 
#   "Lavar verduras", "Cortar verduras", "Cocinar ingredientes" y "Servir comida".
# - Cada subtarea tiene una acción específica que se ejecuta.

def ejemplo_preparar_comida():
    # Definimos las acciones atómicas
    def lavar_verduras():
        print("Lavando las verduras...")

    def cortar_verduras():
        print("Cortando las verduras...")

    def cocinar_ingredientes():
        print("Cocinando los ingredientes...")

    def servir_comida():
        print("Sirviendo la comida...")

    # Creamos las tareas atómicas
    tarea_lavar = Tarea("Lavar verduras", accion=lavar_verduras)
    tarea_cortar = Tarea("Cortar verduras", accion=cortar_verduras)
    tarea_cocinar = Tarea("Cocinar ingredientes", accion=cocinar_ingredientes)
    tarea_servir = Tarea("Servir comida", accion=servir_comida)

    # Creamos una tarea compuesta que agrupa las subtareas
    tarea_preparar_comida = Tarea(
        "Preparar comida",
        subtareas=[tarea_lavar, tarea_cortar, tarea_cocinar, tarea_servir]
    )

    # Ejecutamos la tarea principal
    ejecutar_tarea(tarea_preparar_comida)

# ------------------------------------------------------------------------------------
# PASO 4: EJECUCIÓN DEL EJEMPLO
# ------------------------------------------------------------------------------------
# - Este bloque ejecuta el ejemplo práctico definido anteriormente.
# - Llama a la función `ejemplo_preparar_comida` para iniciar la planificación y ejecución.

if __name__ == "__main__":
    ejemplo_preparar_comida()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo HTN descompone tareas complejas en subtareas más simples, siguiendo 
#    una estructura jerárquica.
# 2. Suposiciones clave:
#    - Las tareas compuestas pueden descomponerse completamente en tareas atómicas.
#    - Las tareas atómicas tienen acciones definidas que pueden ejecutarse directamente.
# 3. Ventajas:
#    - Permite manejar problemas complejos dividiéndolos en partes más manejables.
#    - Es flexible y extensible para diferentes dominios.
# 4. Limitaciones:
#    - Requiere que las tareas y subtareas estén bien definidas de antemano.
#    - No maneja incertidumbre ni cambios dinámicos en el entorno.

# ------------------------------------------------------------------------------------
# EJEMPLO DE SALIDA
# ------------------------------------------------------------------------------------
# Al ejecutar este código, se obtiene la siguiente salida:
# 
# Descomponiendo tarea: Preparar comida
# Ejecutando tarea: Lavar verduras
# Lavando las verduras...
# Ejecutando tarea: Cortar verduras
# Cortando las verduras...
# Ejecutando tarea: Cocinar ingredientes
# Cocinando los ingredientes...
# Ejecutando tarea: Servir comida
# Sirviendo la comida...