# Algoritmo de Búsqueda de la Política (Policy Search)
# Este algoritmo se utiliza en Aprendizaje por Refuerzo para encontrar una política óptima
# que maximice la recompensa acumulada en un entorno dado.

import numpy as np

# Definimos una clase para la Búsqueda de la Política
class BusquedaDeLaPolitica:
    def __init__(self, estados, acciones, politica_inicial, tasa_aprendizaje, iteraciones):
        """
        Inicializa el algoritmo de Búsqueda de la Política.

        :param estados: Lista de estados posibles en el entorno.
        :param acciones: Lista de acciones posibles en el entorno.
        :param politica_inicial: Política inicial (puede ser aleatoria).
        :param tasa_aprendizaje: Tasa de aprendizaje para actualizar la política.
        :param iteraciones: Número de iteraciones para entrenar la política.
        """
        self.estados = estados
        self.acciones = acciones
        self.politica = politica_inicial
        self.tasa_aprendizaje = tasa_aprendizaje
        self.iteraciones = iteraciones

    def evaluar_politica(self, estado):
        """
        Evalúa la política actual para un estado dado.

        :param estado: Estado actual.
        :return: Acción recomendada por la política.
        """
        return self.politica.get(estado, np.random.choice(self.acciones))

    def actualizar_politica(self, estado, accion, recompensa):
        """
        Actualiza la política basada en la recompensa obtenida.

        :param estado: Estado actual.
        :param accion: Acción tomada.
        :param recompensa: Recompensa obtenida por tomar la acción.
        """
        if estado not in self.politica:
            self.politica[estado] = accion
        else:
            # Actualizamos la política si la recompensa es mayor
            if recompensa > 0:
                self.politica[estado] = accion

    def entrenar(self, entorno):
        """
        Entrena la política utilizando el entorno.

        :param entorno: Función que simula el entorno y devuelve la recompensa.
        """
        for _ in range(self.iteraciones):
            for estado in self.estados:
                # Elegimos una acción aleatoria
                accion = np.random.choice(self.acciones)
                # Obtenemos la recompensa del entorno
                recompensa = entorno(estado, accion)
                # Actualizamos la política basada en la recompensa
                self.actualizar_politica(estado, accion, recompensa)

# Ejemplo práctico
def entorno_simulado(estado, accion):
    """
    Simula un entorno simple donde se otorgan recompensas por acciones específicas.

    :param estado: Estado actual.
    :param accion: Acción tomada.
    :return: Recompensa obtenida.
    """
    # Definimos un entorno donde ciertas acciones son mejores en ciertos estados
    if estado == "A" and accion == "derecha":
        return 10
    elif estado == "B" and accion == "izquierda":
        return 5
    else:
        return -1

# Definimos los estados y acciones posibles
estados = ["A", "B", "C"]
acciones = ["izquierda", "derecha"]

# Creamos una política inicial vacía
politica_inicial = {}

# Creamos una instancia del algoritmo de Búsqueda de la Política
algoritmo = BusquedaDeLaPolitica(estados, acciones, politica_inicial, tasa_aprendizaje=0.1, iteraciones=100)

# Entrenamos la política utilizando el entorno simulado
algoritmo.entrenar(entorno_simulado)

# Mostramos la política aprendida
print("Política aprendida:")
for estado, accion in algoritmo.politica.items():
    print(f"En el estado {estado}, tomar la acción '{accion}'")