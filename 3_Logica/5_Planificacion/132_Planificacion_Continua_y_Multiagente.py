# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: PLANIFICACIÓN CONTINUA Y MULTIAGENTE PARA MOVIMIENTOS ALEATORIOS
# ------------------------------------------------------------------------------------
# Este código implementa un sistema de planificación continua para agentes en un entorno.
# Cada agente puede moverse a una posición aleatoria dentro de un espacio definido.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Se importa la biblioteca `random` para generar números aleatorios.
# - Esto es esencial para asignar posiciones aleatorias a los agentes.
import random

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA CLASE AGENTE
# ------------------------------------------------------------------------------------
# - La clase `Agente` representa a un agente individual en el sistema.
# - Cada agente tiene un nombre y una posición inicial.
# - Incluye un método para mover al agente a una nueva posición.
class Agente:
    def __init__(self, nombre, posicion_inicial):
        """
        Inicializa un agente con un nombre y una posición inicial.
        :param nombre: Nombre del agente (cadena de texto).
        :param posicion_inicial: Posición inicial del agente (tupla con coordenadas x, y).
        """
        self.nombre = nombre  # Nombre del agente
        self.posicion = posicion_inicial  # Posición actual del agente

    def mover(self, nueva_posicion):
        """
        Mueve al agente a una nueva posición.
        :param nueva_posicion: Nueva posición del agente (tupla con coordenadas x, y).
        """
        # Imprime el movimiento del agente para seguimiento.
        print(f"{self.nombre} se mueve de {self.posicion} a {nueva_posicion}")
        self.posicion = nueva_posicion  # Actualizamos la posición del agente

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA CLASE ENTORNO
# ------------------------------------------------------------------------------------
# - La clase `Entorno` representa el espacio donde los agentes interactúan.
# - Tiene dimensiones definidas (ancho y alto) y una lista de agentes.
# - Incluye métodos para agregar agentes y planificar sus movimientos.
class Entorno:
    def __init__(self, dimensiones):
        """
        Inicializa el entorno con dimensiones específicas.
        :param dimensiones: Dimensiones del entorno (tupla con ancho y alto).
        """
        self.dimensiones = dimensiones  # Dimensiones del entorno
        self.agentes = []  # Lista de agentes en el entorno

    def agregar_agente(self, agente):
        """
        Agrega un agente al entorno.
        :param agente: Instancia de la clase Agente.
        """
        # Añade el agente a la lista y muestra un mensaje de confirmación.
        self.agentes.append(agente)
        print(f"Agente {agente.nombre} agregado al entorno en la posición {agente.posicion}")

    def planificar_movimientos(self):
        """
        Planifica los movimientos de todos los agentes en el entorno.
        Cada agente se moverá a una posición aleatoria dentro de las dimensiones del entorno.
        """
        for agente in self.agentes:
            # Genera una nueva posición aleatoria dentro de las dimensiones del entorno.
            nueva_posicion = (
                random.randint(0, self.dimensiones[0] - 1),
                random.randint(0, self.dimensiones[1] - 1)
            )
            # Mueve al agente a la nueva posición.
            agente.mover(nueva_posicion)

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque ejecuta el algoritmo con un ejemplo práctico.
# - Se crea un entorno de 10x10 y se agregan tres agentes con posiciones iniciales.
# - Luego, se planifican sus movimientos y se muestran las posiciones finales.

if __name__ == "__main__":
    # Creamos un entorno de 10x10
    entorno = Entorno((10, 10))

    # Creamos algunos agentes con posiciones iniciales
    agente1 = Agente("Agente1", (0, 0))
    agente2 = Agente("Agente2", (5, 5))
    agente3 = Agente("Agente3", (9, 9))

    # Agregamos los agentes al entorno
    entorno.agregar_agente(agente1)
    entorno.agregar_agente(agente2)
    entorno.agregar_agente(agente3)

    # Planificamos los movimientos de los agentes
    print("\nPlanificando movimientos...")
    entorno.planificar_movimientos()

    # Mostramos las posiciones finales de los agentes
    print("\nPosiciones finales:")
    for agente in entorno.agentes:
        print(f"{agente.nombre} está en la posición {agente.posicion}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo simula un sistema multiagente donde cada agente se mueve dentro de un entorno.
# 2. Los movimientos son aleatorios, generados con la biblioteca `random`.
# 3. Suposiciones clave:
#    - Los agentes no tienen restricciones de colisión (pueden ocupar la misma posición).
#    - El entorno es un espacio bidimensional con límites definidos.
# 4. Ventajas:
#    - Fácil de implementar y entender.
#    - Útil para simular sistemas simples de agentes autónomos.
# 5. Limitaciones:
#    - No considera interacciones entre agentes.
#    - Los movimientos son completamente aleatorios, sin objetivos específicos.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que queremos simular un entorno donde tres robots (agentes) se mueven
# aleatoriamente dentro de un almacén de 10x10. Este algoritmo puede ser usado para
# planificar sus movimientos iniciales antes de asignarles tareas específicas.