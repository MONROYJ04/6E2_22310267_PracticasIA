# Importamos las bibliotecas necesarias
import random

# Clase que implementa el Aprendizaje por Refuerzo Pasivo
class AprendizajePorRefuerzoPasivo:
    def __init__(self, estados, acciones, recompensas, estado_inicial):
        """
        Inicializa el algoritmo de Aprendizaje por Refuerzo Pasivo.
        :param estados: Lista de todos los estados posibles.
        :param acciones: Lista de todas las acciones posibles.
        :param recompensas: Diccionario que asigna recompensas a cada estado.
        :param estado_inicial: Estado inicial del agente.
        """
        self.estados = estados  # Lista de estados
        self.acciones = acciones  # Lista de acciones
        self.recompensas = recompensas  # Recompensas asociadas a cada estado
        self.estado_actual = estado_inicial  # Estado inicial del agente
        self.valores = {estado: 0 for estado in estados}  # Valores iniciales de los estados
        self.contador_visitas = {estado: 0 for estado in estados}  # Contador de visitas por estado

    def elegir_accion(self):
        """
        Selecciona una accion aleatoria (en este caso, el agente es pasivo y no toma decisiones activas).
        """
        return random.choice(self.acciones)

    def actualizar_valores(self, estado_anterior, estado_actual):
        """
        Actualiza los valores de los estados basados en las recompensas observadas.
        :param estado_anterior: Estado en el que estaba el agente antes de la transicion.
        :param estado_actual: Estado al que se movio el agente.
        """
        # Incrementamos el contador de visitas del estado anterior
        self.contador_visitas[estado_anterior] += 1

        # Calculamos el valor promedio del estado anterior
        tasa_aprendizaje = 1 / self.contador_visitas[estado_anterior]
        recompensa = self.recompensas.get(estado_actual, 0)
        self.valores[estado_anterior] += tasa_aprendizaje * (recompensa + self.valores[estado_actual] - self.valores[estado_anterior])

    def ejecutar_paso(self):
        """
        Ejecuta un paso del algoritmo: elige una accion, transiciona a un nuevo estado y actualiza los valores.
        """
        # Elegimos una accion (aunque no afecta directamente en este caso)
        accion = self.elegir_accion()

        # Simulamos una transicion a un nuevo estado (aleatorio para este ejemplo)
        nuevo_estado = random.choice(self.estados)

        # Actualizamos los valores de los estados
        self.actualizar_valores(self.estado_actual, nuevo_estado)

        # Actualizamos el estado actual del agente
        self.estado_actual = nuevo_estado

# Ejemplo practico
if __name__ == "__main__":
    # Definimos los estados, acciones y recompensas
    estados = ["A", "B", "C", "D"]
    acciones = ["moverse"]
    recompensas = {"A": 0, "B": -1, "C": 1, "D": 10}  # Recompensas asociadas a cada estado
    estado_inicial = "A"

    # Creamos una instancia del algoritmo
    agente = AprendizajePorRefuerzoPasivo(estados, acciones, recompensas, estado_inicial)

    # Ejecutamos varios pasos del algoritmo
    for paso in range(10):  # Ejecutamos 10 pasos
        print(f"Paso {paso + 1}:")
        print(f"Estado actual: {agente.estado_actual}")
        print(f"Valores actuales: {agente.valores}")
        agente.ejecutar_paso()
        print("-" * 30)

    # Mostramos los valores finales de los estados
    print("Valores finales de los estados:")
    for estado, valor in agente.valores.items():
        print(f"Estado {estado}: Valor {valor}")