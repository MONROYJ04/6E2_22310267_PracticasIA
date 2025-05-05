# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ESPACIO DE ESTADOS PARA RESOLVER PROBLEMAS
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de búsqueda en el Espacio de Estados. 
# Su objetivo es encontrar una secuencia de acciones que lleve desde un estado inicial 
# hasta un estado objetivo, utilizando un conjunto de reglas o acciones posibles.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE NODO
# ------------------------------------------------------------------------------------
# - La clase `Nodo` representa un estado en el espacio de estados.
# - Cada nodo contiene información sobre el estado actual, el nodo padre (de dónde vino),
#   la acción que llevó a este estado y el costo acumulado para llegar a él.
# - Es importante porque permite reconstruir el camino desde el estado inicial hasta el objetivo.

class Nodo:
    def __init__(self, estado, padre=None, accion=None, costo=0):
        # Estado actual del nodo
        self.estado = estado
        # Nodo padre desde el cual se llegó a este nodo
        self.padre = padre
        # Acción que llevó al estado actual
        self.accion = accion
        # Costo acumulado para llegar a este nodo
        self.costo = costo

    # Método para reconstruir el camino desde el estado inicial hasta este nodo
    def reconstruir_camino(self):
        # ------------------------------------------------------------------------------------
        # PASO 2: RECONSTRUCCIÓN DEL CAMINO
        # ------------------------------------------------------------------------------------
        # - Este método reconstruye la secuencia de acciones desde el estado inicial hasta
        #   el estado actual.
        # - Es importante porque permite entender cómo se llegó al estado objetivo.
        camino = []
        nodo_actual = self
        while nodo_actual is not None:
            camino.append((nodo_actual.accion, nodo_actual.estado))
            nodo_actual = nodo_actual.padre
        camino.reverse()  # Invertir el camino para que vaya del inicio al final
        return camino

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN DE BÚSQUEDA EN EL ESPACIO DE ESTADOS
# ------------------------------------------------------------------------------------
# - Esta función implementa la lógica de búsqueda para explorar el espacio de estados.
# - Utiliza una cola FIFO (First In, First Out) para explorar los nodos en orden.
# - Es importante porque define cómo se navega por los estados posibles y cómo se
#   determina si se ha alcanzado el objetivo.

def busqueda_espacio_estados(estado_inicial, es_objetivo, generar_sucesores):
    """
    Realiza una búsqueda en el espacio de estados.

    :param estado_inicial: El estado inicial del problema.
    :param es_objetivo: Función que verifica si un estado es el objetivo.
    :param generar_sucesores: Función que genera los sucesores de un estado.
    :return: El camino desde el estado inicial hasta el estado objetivo, o None si no se encuentra solución.
    """
    # Crear el nodo inicial
    nodo_inicial = Nodo(estado_inicial)
    # Cola de nodos por explorar (utilizamos una lista como cola FIFO)
    frontera = [nodo_inicial]
    # Conjunto de estados visitados para evitar ciclos
    visitados = set()

    while frontera:
        # ------------------------------------------------------------------------------------
        # PASO 4: EXPLORACIÓN DE LA FRONTERA
        # ------------------------------------------------------------------------------------
        # - Extraemos el primer nodo de la cola para explorar su estado.
        # - Si el estado actual cumple con el objetivo, reconstruimos el camino.
        # - Si no, generamos los sucesores y los añadimos a la cola.
        nodo_actual = frontera.pop(0)

        # Si el estado actual es el objetivo, reconstruir el camino y devolverlo
        if es_objetivo(nodo_actual.estado):
            return nodo_actual.reconstruir_camino()

        # Marcar el estado actual como visitado
        visitados.add(nodo_actual.estado)

        # Generar los sucesores del estado actual
        for accion, estado_sucesor in generar_sucesores(nodo_actual.estado):
            if estado_sucesor not in visitados:
                # Crear un nuevo nodo para el sucesor
                nuevo_nodo = Nodo(estado_sucesor, nodo_actual, accion, nodo_actual.costo + 1)
                # Agregar el nuevo nodo a la cola de exploración
                frontera.append(nuevo_nodo)

    # Si se agota la frontera sin encontrar el objetivo, devolver None
    return None

# ------------------------------------------------------------------------------------
# PASO 5: DEFINICIÓN DEL PROBLEMA DEL JARRÓN DE AGUA
# ------------------------------------------------------------------------------------
# - Este problema consiste en dos jarrones: uno de 4 litros y otro de 3 litros.
# - El objetivo es obtener exactamente 2 litros en el jarrón de 4 litros.
# - Definimos las funciones `es_objetivo` y `generar_sucesores` para modelar el problema.

def es_objetivo(estado):
    # El objetivo es tener exactamente 2 litros en el jarrón de 4 litros
    return estado[0] == 2

def generar_sucesores(estado):
    # Estado: (agua_en_jarron_4, agua_en_jarron_3)
    jarron_4, jarron_3 = estado
    sucesores = []

    # Llenar el jarrón de 4 litros
    sucesores.append(("Llenar jarron 4", (4, jarron_3)))
    # Llenar el jarrón de 3 litros
    sucesores.append(("Llenar jarron 3", (jarron_4, 3)))
    # Vaciar el jarrón de 4 litros
    sucesores.append(("Vaciar jarron 4", (0, jarron_3)))
    # Vaciar el jarrón de 3 litros
    sucesores.append(("Vaciar jarron 3", (jarron_4, 0)))
    # Verter agua del jarrón de 4 litros al de 3 litros
    transferir = min(jarron_4, 3 - jarron_3)
    sucesores.append(("Transferir de 4 a 3", (jarron_4 - transferir, jarron_3 + transferir)))
    # Verter agua del jarrón de 3 litros al de 4 litros
    transferir = min(jarron_3, 4 - jarron_4)
    sucesores.append(("Transferir de 3 a 4", (jarron_4 + transferir, jarron_3 - transferir)))

    return sucesores

# ------------------------------------------------------------------------------------
# PASO 6: EJECUCIÓN DEL ALGORITMO
# ------------------------------------------------------------------------------------
# - Definimos el estado inicial como `(0, 0)` (ambos jarrones vacíos).
# - Ejecutamos la búsqueda en el espacio de estados.
# - Imprimimos el camino encontrado o indicamos que no hay solución.

# Estado inicial: ambos jarrones están vacíos
estado_inicial = (0, 0)

# Ejecutar la búsqueda
camino = busqueda_espacio_estados(estado_inicial, es_objetivo, generar_sucesores)

# Imprimir el resultado
if camino:
    print("Camino encontrado:")
    for accion, estado in camino:
        print(f"{accion}: {estado}")
else:
    print("No se encontró solución.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una búsqueda en anchura (BFS) para explorar el espacio de estados.
# 2. Se asegura de no visitar estados repetidos para evitar ciclos.
# 3. Es eficiente para problemas pequeños como este, pero puede ser costoso para espacios de estados grandes.