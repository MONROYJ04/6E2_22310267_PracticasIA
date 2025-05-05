# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: PLANIFICACIÓN DE ORDEN PARCIAL PARA RESOLVER PROBLEMAS SECUENCIALES
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de planificación de orden parcial (POP) que busca 
# generar un plan de acciones para alcanzar un estado objetivo desde un estado inicial. 
# Las acciones tienen precondiciones y efectos, y el algoritmo selecciona las acciones 
# necesarias respetando las restricciones de orden.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE `Accion`
# ------------------------------------------------------------------------------------
# - Esta clase representa una acción en el plan.
# - Cada acción tiene un nombre, una lista de precondiciones (condiciones necesarias 
#   para ejecutarla) y una lista de efectos (cambios que produce en el estado actual).
# - Es importante porque define los elementos básicos que el algoritmo utilizará 
#   para construir el plan.

class Accion:
    def __init__(self, nombre: str, precondiciones: List[str], efectos: List[str]):
        # Nombre de la acción
        self.nombre = nombre
        # Lista de precondiciones que deben cumplirse antes de ejecutar la acción
        self.precondiciones = precondiciones
        # Lista de efectos que ocurren después de ejecutar la acción
        self.efectos = efectos

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE `PlanOrdenParcial`
# ------------------------------------------------------------------------------------
# - Esta clase implementa el algoritmo de planificación de orden parcial.
# - Contiene el estado inicial, el estado objetivo, las acciones disponibles, 
#   los pasos seleccionados para el plan y las restricciones de orden entre acciones.
# - Es el núcleo del algoritmo, ya que realiza la búsqueda del plan.

class PlanOrdenParcial:
    def __init__(self, estado_inicial: List[str], estado_objetivo: List[str], acciones: List[Accion]):
        # Estado inicial del problema
        self.estado_inicial = estado_inicial
        # Estado objetivo que queremos alcanzar
        self.estado_objetivo = estado_objetivo
        # Lista de acciones disponibles
        self.acciones = acciones
        # Lista de pasos en el plan (acciones seleccionadas)
        self.pasos = []
        # Restricciones de orden entre las acciones
        self.restricciones_orden = []

    # --------------------------------------------------------------------------------
    # PASO 3: MÉTODO `es_estado_objetivo`
    # --------------------------------------------------------------------------------
    # - Este método verifica si el estado actual cumple con el estado objetivo.
    # - Es importante porque determina si el algoritmo ha alcanzado la meta.
    def es_estado_objetivo(self, estado: List[str]) -> bool:
        # Verifica si todos los elementos del estado objetivo están en el estado actual
        return all(objetivo in estado for objetivo in self.estado_objetivo)

    # --------------------------------------------------------------------------------
    # PASO 4: MÉTODO `buscar_plan`
    # --------------------------------------------------------------------------------
    # - Este método busca un plan que permita alcanzar el estado objetivo.
    # - Selecciona acciones cuyas precondiciones se cumplan en el estado actual y 
    #   actualiza el estado con los efectos de esas acciones.
    # - Es el corazón del algoritmo, donde se construye el plan paso a paso.
    def buscar_plan(self):
        # Inicializamos el estado actual como el estado inicial
        estado_actual = self.estado_inicial[:]

        # Mientras no alcancemos el estado objetivo
        while not self.es_estado_objetivo(estado_actual):
            # Buscamos una acción que pueda ejecutarse en el estado actual
            for accion in self.acciones:
                # Verificamos si todas las precondiciones de la acción están en el estado actual
                if all(precondicion in estado_actual for precondicion in accion.precondiciones):
                    # Agregamos la acción al plan
                    self.pasos.append(accion)
                    # Actualizamos el estado actual con los efectos de la acción
                    estado_actual.extend(accion.efectos)
                    # Agregamos restricciones de orden (opcional)
                    self.restricciones_orden.append((accion.nombre, "Ejecutada"))
                    break
            else:
                # Si no encontramos una acción válida, el plan falla
                raise Exception("No se puede encontrar un plan válido.")

        # Retornamos los pasos del plan
        return self.pasos

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar el algoritmo para resolver un problema práctico.
# - El problema consiste en preparar una mesa en un orden específico.
# - Se define el estado inicial, el estado objetivo y las acciones disponibles.

if __name__ == "__main__":
    # Definimos el estado inicial
    estado_inicial = ["mesa_vacia"]

    # Definimos el estado objetivo
    estado_objetivo = ["mesa_lista"]

    # Definimos las acciones disponibles
    acciones = [
        Accion("poner_mantel", ["mesa_vacia"], ["mantel_puesto"]),
        Accion("poner_platos", ["mantel_puesto"], ["platos_puestos"]),
        Accion("poner_cubiertos", ["platos_puestos"], ["cubiertos_puestos"]),
        Accion("poner_vasos", ["cubiertos_puestos"], ["mesa_lista"])
    ]

    # Creamos una instancia del planificador de orden parcial
    planificador = PlanOrdenParcial(estado_inicial, estado_objetivo, acciones)

    # Buscamos un plan
    try:
        plan = planificador.buscar_plan()
        print("Plan encontrado:")
        for paso in plan:
            print(f"- {paso.nombre}")
    except Exception as e:
        print(f"Error: {e}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo comienza con un estado inicial y un estado objetivo.
# 2. Busca acciones cuyas precondiciones se cumplan en el estado actual.
# 3. Cada acción seleccionada actualiza el estado actual con sus efectos.
# 4. El proceso se repite hasta que el estado actual cumple con el estado objetivo.
# 5. Si no hay acciones válidas en algún punto, el algoritmo falla.
# 
# Ventajas:
# - Permite manejar problemas donde no todas las acciones tienen un orden estricto.
# - Es flexible y puede adaptarse a diferentes dominios.
# 
# Limitaciones:
# - Puede fallar si no hay acciones suficientes para alcanzar el estado objetivo.
# - No optimiza necesariamente el número de pasos en el plan.