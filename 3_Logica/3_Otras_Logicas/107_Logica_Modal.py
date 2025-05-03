# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: LÓGICA MODAL PARA RAZONAMIENTO EN MUNDOS POSIBLES
# ------------------------------------------------------------------------------------
# Este código implementa un modelo básico de lógica modal, que permite razonar sobre 
# proposiciones en diferentes mundos posibles y verificar si son posibles o necesarias 
# en un contexto dado. Se utiliza para modelar situaciones donde las proposiciones 
# pueden variar dependiendo del mundo en el que se evalúan.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE `MundoPosible`
# ------------------------------------------------------------------------------------
# - Esta clase representa un mundo posible en la lógica modal.
# - Cada mundo tiene un nombre único y una lista de proposiciones que son verdaderas en él.
# - Es importante porque define la estructura básica de los mundos que se usarán en el modelo.

class MundoPosible:
    def __init__(self, nombre: str, proposiciones: List[str]):
        # Nombre del mundo posible (por ejemplo, "Mundo1").
        self.nombre = nombre
        # Lista de proposiciones verdaderas en este mundo.
        self.proposiciones = proposiciones

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE `LogicaModal`
# ------------------------------------------------------------------------------------
# - Esta clase implementa la lógica modal, incluyendo la gestión de mundos posibles y 
#   las relaciones de accesibilidad entre ellos.
# - Permite agregar mundos, definir relaciones y verificar si una proposición es 
#   posible o necesaria en un mundo dado.

class LogicaModal:
    def __init__(self):
        # Lista de mundos posibles.
        self.mundos = []
        # Diccionario que representa las relaciones de accesibilidad entre mundos.
        self.relaciones = {}

    # --------------------------------------------------------------------------------
    # PASO 3: MÉTODO `agregar_mundo`
    # --------------------------------------------------------------------------------
    # - Este método agrega un mundo posible a la lista de mundos.
    # - También inicializa las relaciones de accesibilidad para este mundo.
    def agregar_mundo(self, mundo: MundoPosible):
        self.mundos.append(mundo)
        self.relaciones[mundo.nombre] = []

    # --------------------------------------------------------------------------------
    # PASO 4: MÉTODO `agregar_relacion`
    # --------------------------------------------------------------------------------
    # - Este método define una relación de accesibilidad entre dos mundos.
    # - Es importante porque las relaciones determinan qué mundos son accesibles 
    #   desde un mundo dado.
    def agregar_relacion(self, mundo_origen: str, mundo_destino: str):
        if mundo_origen in self.relaciones:
            self.relaciones[mundo_origen].append(mundo_destino)

    # --------------------------------------------------------------------------------
    # PASO 5: MÉTODO `es_posible`
    # --------------------------------------------------------------------------------
    # - Este método verifica si una proposición es posible en un mundo dado.
    # - Una proposición es posible si es verdadera en al menos uno de los mundos 
    #   accesibles desde el mundo de origen.
    def es_posible(self, mundo_origen: str, proposicion: str) -> bool:
        if mundo_origen not in self.relaciones:
            return False
        for mundo_destino in self.relaciones[mundo_origen]:
            for mundo in self.mundos:
                if mundo.nombre == mundo_destino and proposicion in mundo.proposiciones:
                    return True
        return False

    # --------------------------------------------------------------------------------
    # PASO 6: MÉTODO `es_necesario`
    # --------------------------------------------------------------------------------
    # - Este método verifica si una proposición es necesaria en un mundo dado.
    # - Una proposición es necesaria si es verdadera en todos los mundos accesibles 
    #   desde el mundo de origen.
    def es_necesario(self, mundo_origen: str, proposicion: str) -> bool:
        if mundo_origen not in self.relaciones:
            return False
        for mundo_destino in self.relaciones[mundo_origen]:
            for mundo in self.mundos:
                if mundo.nombre == mundo_destino and proposicion not in mundo.proposiciones:
                    return False
        return True

# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar la lógica modal con un ejemplo práctico.
# - Creamos mundos posibles, definimos relaciones de accesibilidad y verificamos 
#   si ciertas proposiciones son posibles o necesarias.

if __name__ == "__main__":
    # Creamos una instancia de la lógica modal.
    logica = LogicaModal()

    # Creamos mundos posibles con sus proposiciones verdaderas.
    mundo1 = MundoPosible("Mundo1", ["p", "q"])
    mundo2 = MundoPosible("Mundo2", ["q"])
    mundo3 = MundoPosible("Mundo3", ["p"])

    # Agregamos los mundos a la lógica modal.
    logica.agregar_mundo(mundo1)
    logica.agregar_mundo(mundo2)
    logica.agregar_mundo(mundo3)

    # Definimos las relaciones de accesibilidad entre los mundos.
    logica.agregar_relacion("Mundo1", "Mundo2")
    logica.agregar_relacion("Mundo1", "Mundo3")

    # Verificamos si una proposición es posible o necesaria.
    print("¿Es posible 'p' en Mundo1?", logica.es_posible("Mundo1", "p"))  # True
    print("¿Es necesario 'q' en Mundo1?", logica.es_necesario("Mundo1", "q"))  # False

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Lógica Modal**: Es una extensión de la lógica proposicional que permite razonar 
#    sobre proposiciones en diferentes mundos posibles.
# 2. **Relaciones de Accesibilidad**: Determinan qué mundos son accesibles desde un 
#    mundo dado, lo que afecta la evaluación de las proposiciones.
# 3. **Posibilidad y Necesidad**:
#    - Una proposición es posible si es verdadera en al menos un mundo accesible.
#    - Una proposición es necesaria si es verdadera en todos los mundos accesibles.
# 4. **Ventajas**: Este modelo es útil para representar incertidumbre, razonamiento 
#    hipotético y sistemas multiagente.
# 5. **Limitaciones**: Este ejemplo no incluye operadores temporales ni cuantificadores, 
#    que son comunes en lógicas modales más avanzadas.