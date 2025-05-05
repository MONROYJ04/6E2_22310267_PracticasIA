# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO GRAPHPLAN PARA PLANIFICACIÓN AUTOMÁTICA
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de Grafos de Planificación (GRAPHPLAN), utilizado 
# en inteligencia artificial para resolver problemas de planificación. Su objetivo es 
# encontrar un plan que permita alcanzar un conjunto de objetivos a partir de un estado inicial.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE "ACCION"
# ------------------------------------------------------------------------------------
# - Esta clase representa una acción en el problema de planificación.
# - Cada acción tiene un nombre, un conjunto de precondiciones (lo que necesita para ejecutarse)
#   y un conjunto de efectos (lo que produce al ejecutarse).
# - Es importante porque las acciones son los elementos que transforman el estado inicial
#   en el estado objetivo.

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        # Nombre de la acción
        self.nombre = nombre
        # Lista de precondiciones necesarias para ejecutar la acción
        self.precondiciones = precondiciones
        # Lista de efectos que ocurren al ejecutar la acción
        self.efectos = efectos

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE "GRAFO DE PLANIFICACIÓN"
# ------------------------------------------------------------------------------------
# - Esta clase representa el grafo de planificación, que es el núcleo del algoritmo GRAPHPLAN.
# - El grafo se construye nivel por nivel, donde cada nivel contiene estados y acciones.
# - Es importante porque permite modelar la evolución de los estados y verificar si los 
#   objetivos son alcanzables.

class GrafoPlanificacion:
    def __init__(self, estado_inicial, objetivos, acciones):
        # Estado inicial del problema
        self.estado_inicial = estado_inicial
        # Conjunto de objetivos que se desean alcanzar
        self.objetivos = objetivos
        # Lista de acciones disponibles
        self.acciones = acciones
        # Lista de niveles del grafo (cada nivel contiene estados y acciones)
        self.niveles = []

    # ------------------------------------------------------------------------------------
    # PASO 3: CONSTRUCCIÓN DEL GRAFO DE PLANIFICACIÓN
    # ------------------------------------------------------------------------------------
    # - Este método construye el grafo nivel por nivel.
    # - En cada nivel, se generan nuevos estados aplicando las acciones disponibles.
    # - Se detiene cuando se alcanzan los objetivos o cuando no hay cambios entre niveles
    #   (lo que indica que los objetivos no son alcanzables).
    def construir_grafo(self):
        # Nivel inicial del grafo: el estado inicial
        nivel_actual = self.estado_inicial
        self.niveles.append(nivel_actual)

        while True:
            # Generar el siguiente nivel del grafo
            nuevo_nivel = self.generar_nivel(nivel_actual)
            self.niveles.append(nuevo_nivel)

            # Verificar si los objetivos están en el nivel actual
            if self.verificar_objetivos(nuevo_nivel):
                print("Objetivos alcanzados en el grafo.")
                return True

            # Verificar si no hay cambios entre niveles (estancamiento)
            if nivel_actual == nuevo_nivel:
                print("No se pueden alcanzar los objetivos.")
                return False

            # Avanzar al siguiente nivel
            nivel_actual = nuevo_nivel

    # ------------------------------------------------------------------------------------
    # PASO 4: GENERACIÓN DE UN NUEVO NIVEL DEL GRAFO
    # ------------------------------------------------------------------------------------
    # - Este método genera un nuevo nivel del grafo basado en el nivel anterior.
    # - Aplica todas las acciones disponibles cuyas precondiciones se cumplen en el nivel actual.
    # - Es importante porque permite modelar cómo evolucionan los estados al aplicar acciones.
    def generar_nivel(self, nivel_anterior):
        # Crear un nuevo nivel copiando el nivel anterior
        nuevo_nivel = set(nivel_anterior)

        for accion in self.acciones:
            # Verificar si la acción es aplicable (sus precondiciones están en el nivel actual)
            if all(precondicion in nivel_anterior for precondicion in accion.precondiciones):
                # Agregar los efectos de la acción al nuevo nivel
                nuevo_nivel.update(accion.efectos)

        return nuevo_nivel

    # ------------------------------------------------------------------------------------
    # PASO 5: VERIFICACIÓN DE LOS OBJETIVOS
    # ------------------------------------------------------------------------------------
    # - Este método verifica si todos los objetivos están presentes en el nivel actual.
    # - Es importante porque determina si el algoritmo ha encontrado una solución.
    def verificar_objetivos(self, nivel):
        # Verifica si todos los objetivos están presentes en el nivel actual
        return all(objetivo in nivel for objetivo in self.objetivos)

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: PROBLEMA DE PLANIFICACIÓN
# ------------------------------------------------------------------------------------
# - En este ejemplo, se define un problema de planificación simple con:
#   - Estado inicial: {A, B}
#   - Objetivos: {C, D}
#   - Acciones disponibles:
#       - accion1: precondiciones = {A}, efectos = {C}
#       - accion2: precondiciones = {B}, efectos = {D}

# Definir el estado inicial
estado_inicial = {"A", "B"}

# Definir los objetivos
objetivos = {"C", "D"}

# Definir las acciones
acciones = [
    Accion("accion1", {"A"}, {"C"}),  # Acción que transforma A en C
    Accion("accion2", {"B"}, {"D"})   # Acción que transforma B en D
]

# Crear el grafo de planificación
grafo = GrafoPlanificacion(estado_inicial, objetivos, acciones)

# Construir el grafo y verificar si se pueden alcanzar los objetivos
resultado = grafo.construir_grafo()

# Imprimir el resultado
if resultado:
    print("Se encontró un plan para alcanzar los objetivos.")
else:
    print("No se encontró un plan para alcanzar los objetivos.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo GRAPHPLAN construye un grafo de planificación nivel por nivel.
# 2. Cada nivel contiene los estados alcanzables y las acciones aplicables.
# 3. Se detiene cuando:
#    - Los objetivos están presentes en el nivel actual.
#    - No hay cambios entre niveles (indica que los objetivos no son alcanzables).
# 4. Ventajas:
#    - Es eficiente para problemas de planificación estructurados.
# 5. Limitaciones:
#    - Puede ser ineficiente para problemas con muchos estados o acciones.