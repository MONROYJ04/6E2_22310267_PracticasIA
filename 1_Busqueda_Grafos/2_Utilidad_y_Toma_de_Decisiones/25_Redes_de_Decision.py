# Importamos las librerías necesarias
import numpy as np

# Clase que representa una Red de Decisión
class RedDecision:
    def __init__(self, nodos, probabilidades, utilidades):
        """
        Constructor de la clase RedDecision.

        :param nodos: Lista de nodos en la red.
        :param probabilidades: Diccionario que contiene las probabilidades condicionales de los nodos.
        :param utilidades: Diccionario que contiene las utilidades asociadas a los nodos.
        """
        self.nodos = nodos
        self.probabilidades = probabilidades
        self.utilidades = utilidades

    def calcular_utilidad_esperada(self, decisiones):
        """
        Calcula la utilidad esperada de una decisión.

        :param decisiones: Diccionario que contiene las decisiones tomadas para cada nodo.
        :return: La utilidad esperada calculada.
        """
        utilidad_esperada = 0

        # Iteramos sobre cada nodo para calcular la utilidad esperada
        for nodo, decision in decisiones.items():
            probabilidad = self.probabilidades.get((nodo, decision), 0)
            utilidad = self.utilidades.get(nodo, 0)
            utilidad_esperada += probabilidad * utilidad

        return utilidad_esperada


# Ejemplo práctico: Decidir si llevar paraguas o no
# Definimos los nodos de la red
nodos = ["Clima", "Paraguas"]

# Definimos las probabilidades condicionales
# Probabilidades del clima: Soleado (0.7), Lluvioso (0.3)
# Probabilidad de llevar paraguas dado el clima
probabilidades = {
    ("Clima", "Soleado"): 0.7,
    ("Clima", "Lluvioso"): 0.3,
    ("Paraguas", "Llevar"): 0.8,  # Probabilidad de estar preparado si llevas paraguas
    ("Paraguas", "NoLlevar"): 0.2  # Probabilidad de estar preparado si no llevas paraguas
}

# Definimos las utilidades asociadas
# Utilidad de estar preparado para la lluvia
utilidades = {
    "Clima": 0,  # El clima no tiene utilidad directa
    "Paraguas": 50  # Llevar paraguas tiene una utilidad de 50
}

# Creamos la red de decisión
red = RedDecision(nodos, probabilidades, utilidades)

# Definimos las decisiones tomadas
# Decisión: Llevar paraguas
decisiones = {
    "Clima": "Lluvioso",
    "Paraguas": "Llevar"
}

# Calculamos la utilidad esperada
utilidad_esperada = red.calcular_utilidad_esperada(decisiones)

# Mostramos el resultado
print(f"La utilidad esperada de la decisión es: {utilidad_esperada}")