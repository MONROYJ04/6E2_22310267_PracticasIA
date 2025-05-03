# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA DE REGLAS, REDES SEMÁNTICAS Y LÓGICA DESCRIPTIVA
# ------------------------------------------------------------------------------------
# Este código implementa un sistema básico que combina redes semánticas y reglas para 
# representar conocimiento y realizar inferencias simples. Utiliza relaciones entre 
# conceptos y reglas lógicas para derivar conclusiones a partir de hechos conocidos.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE RED SEMÁNTICA
# ------------------------------------------------------------------------------------
# - Esta clase permite representar conceptos y las relaciones entre ellos.
# - Utiliza un diccionario para almacenar las relaciones en forma de "sujeto -> (relación, objeto)".
# - Es importante porque organiza el conocimiento en una estructura que puede ser consultada.
class RedSemantica:
    def __init__(self):
        # Diccionario para almacenar relaciones entre conceptos
        self.relaciones = {}

    def agregar_relacion(self, sujeto, relacion, objeto):
        """
        Agrega una relación entre dos conceptos.
        :param sujeto: El concepto principal (nodo inicial).
        :param relacion: La relación entre los conceptos (arista).
        :param objeto: El concepto relacionado (nodo final).
        """
        # Si el sujeto no existe en el diccionario, se inicializa con una lista vacía
        if sujeto not in self.relaciones:
            self.relaciones[sujeto] = []
        # Se agrega la relación como una tupla (relación, objeto)
        self.relaciones[sujeto].append((relacion, objeto))

    def obtener_relaciones(self, sujeto):
        """
        Obtiene todas las relaciones de un concepto dado.
        :param sujeto: El concepto del cual se quieren obtener las relaciones.
        :return: Lista de relaciones asociadas al concepto.
        """
        # Devuelve las relaciones asociadas al sujeto o una lista vacía si no existe
        return self.relaciones.get(sujeto, [])

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE REGLAS
# ------------------------------------------------------------------------------------
# - Esta clase permite manejar reglas lógicas en formato "SI -> ENTONCES".
# - Las reglas se almacenan como pares (condición, conclusión).
# - Es importante porque permite realizar inferencias basadas en hechos conocidos.
class Reglas:
    def __init__(self):
        # Lista para almacenar reglas en formato "SI -> ENTONCES"
        self.reglas = []

    def agregar_regla(self, condicion, conclusion):
        """
        Agrega una regla al sistema.
        :param condicion: La condición que debe cumplirse (parte SI).
        :param conclusion: La conclusión que se deriva si la condición se cumple (parte ENTONCES).
        """
        # Se agrega la regla como una tupla (condición, conclusión)
        self.reglas.append((condicion, conclusion))

    def evaluar(self, hechos):
        """
        Evalúa las reglas basándose en un conjunto de hechos.
        :param hechos: Lista de hechos conocidos.
        :return: Lista de conclusiones derivadas.
        """
        conclusiones = []
        # Se recorren todas las reglas para verificar si la condición está en los hechos
        for condicion, conclusion in self.reglas:
            if condicion in hechos:
                # Si la condición se cumple, se agrega la conclusión a las conclusiones derivadas
                conclusiones.append(conclusion)
        return conclusiones

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar las clases RedSemantica y Reglas para representar 
#   conocimiento y realizar inferencias.
# - Incluye la creación de relaciones, reglas y la evaluación de hechos.

if __name__ == "__main__":
    # --------------------------------------------------------------------------------
    # CREACIÓN DE LA RED SEMÁNTICA
    # --------------------------------------------------------------------------------
    # - Se crea una instancia de la clase RedSemantica.
    # - Se agregan relaciones entre conceptos como "perro es_un animal".
    red = RedSemantica()

    # Agregamos relaciones a la red semántica
    red.agregar_relacion("perro", "es_un", "animal")
    red.agregar_relacion("gato", "es_un", "animal")
    red.agregar_relacion("animal", "tiene", "vida")

    # Mostramos las relaciones de un concepto
    print("Relaciones del concepto 'perro':")
    print(red.obtener_relaciones("perro"))

    # --------------------------------------------------------------------------------
    # CREACIÓN DEL SISTEMA DE REGLAS
    # --------------------------------------------------------------------------------
    # - Se crea una instancia de la clase Reglas.
    # - Se agregan reglas lógicas como "si es_un animal entonces tiene vida".
    sistema_reglas = Reglas()

    # Agregamos reglas al sistema
    sistema_reglas.agregar_regla("es_un animal", "tiene vida")
    sistema_reglas.agregar_regla("es_un mamifero", "es de sangre caliente")

    # --------------------------------------------------------------------------------
    # EVALUACIÓN DE HECHOS
    # --------------------------------------------------------------------------------
    # - Se define un conjunto de hechos conocidos.
    # - Se evalúan las reglas para derivar conclusiones basadas en los hechos.
    hechos = ["es_un animal", "es_un mamifero"]
    conclusiones = sistema_reglas.evaluar(hechos)

    # Mostramos las conclusiones derivadas
    print("\nConclusiones derivadas:")
    for conclusion in conclusiones:
        print(conclusion)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo combina redes semánticas (para representar relaciones entre conceptos)
#    y reglas lógicas (para realizar inferencias basadas en hechos).
# 2. Las redes semánticas organizan el conocimiento en una estructura de grafo, donde 
#    los nodos son conceptos y las aristas son relaciones.
# 3. Las reglas permiten derivar nueva información a partir de hechos conocidos.
# 4. Ventajas:
#    - Fácil de entender y extender.
#    - Útil para sistemas de inferencia simples.
# 5. Limitaciones:
#    - No maneja incertidumbre ni contradicciones.
#    - Escalabilidad limitada para grandes conjuntos de datos.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO ADICIONAL
# ------------------------------------------------------------------------------------
# Supongamos que queremos agregar un nuevo concepto y evaluar nuevas reglas:
# - Relación: "pez es_un animal".
# - Regla: "si es_un animal entonces respira".
# - Hecho: "es_un pez".

# Código adicional:
# red.agregar_relacion("pez", "es_un", "animal")
# sistema_reglas.agregar_regla("es_un pez", "respira")
# hechos = ["es_un pez"]
# conclusiones = sistema_reglas.evaluar(hechos)
# print("\nNuevas conclusiones derivadas:")
# for conclusion in conclusiones:
#     print(conclusion)