# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: AGENTE LÓGICO PARA TOMA DE DECISIONES BASADAS EN REGLAS
# ------------------------------------------------------------------------------------
# Este código implementa un agente lógico que toma decisiones basadas en reglas predefinidas.
# El agente evalúa percepciones del entorno y selecciona una acción según las reglas de su base de conocimiento.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE AGENTE LÓGICO
# ------------------------------------------------------------------------------------
# - Este bloque define la clase `AgenteLogico`, que representa un agente con una base de conocimiento.
# - La base de conocimiento contiene reglas que relacionan condiciones con acciones.
# - Es importante porque encapsula la lógica del agente y permite agregar reglas dinámicamente.

class AgenteLogico:
    def __init__(self):
        # Base de conocimiento del agente (reglas y hechos)
        self.base_conocimiento = []  # Lista que almacena las reglas del agente.

    def agregar_regla(self, regla):
        # Agrega una regla a la base de conocimiento
        # Cada regla es un diccionario con una condición (función) y una acción (resultado).
        self.base_conocimiento.append(regla)

    def razonar(self, percepcion):
        # Evalúa las percepciones del entorno y aplica las reglas
        # - Recorre todas las reglas en la base de conocimiento.
        # - Si la condición de una regla se cumple para la percepción actual, retorna la acción asociada.
        for regla in self.base_conocimiento:
            if regla["condicion"](percepcion):  # Evalúa la condición de la regla.
                return regla["accion"]  # Retorna la acción si la condición es verdadera.
        return "No se encontró una acción válida"  # Retorna un mensaje si no hay reglas aplicables.

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DEL EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque implementa un ejemplo práctico para demostrar cómo funciona el agente lógico.
# - Simula un robot que navega en una cuadrícula y toma decisiones basadas en percepciones del entorno.
# - Es importante porque muestra cómo se aplican las reglas en un caso real.

def ejemplo_practico():
    # Crear una instancia del agente lógico
    robot = AgenteLogico()  # Se crea un agente lógico llamado "robot".

    # Definir reglas para el agente
    # - Cada regla tiene una condición (lambda) y una acción asociada.
    # - Estas reglas definen el comportamiento del robot en función de las percepciones.
    robot.agregar_regla({
        "condicion": lambda percepcion: percepcion == "obstaculo",  # Si hay un obstáculo...
        "accion": "girar_derecha"  # ...el robot gira a la derecha.
    })
    robot.agregar_regla({
        "condicion": lambda percepcion: percepcion == "camino_libre",  # Si el camino está libre...
        "accion": "avanzar"  # ...el robot avanza.
    })

    # Simular percepciones del entorno
    # - Lista que representa las percepciones del entorno en diferentes momentos.
    entorno = ["camino_libre", "obstaculo", "camino_libre", "camino_libre"]

    # El agente toma decisiones basadas en las percepciones
    # - Para cada percepción en el entorno, el agente evalúa las reglas y selecciona una acción.
    for percepcion in entorno:
        accion = robot.razonar(percepcion)  # El agente razona con base en la percepción actual.
        print(f"Percepción: {percepcion} -> Acción: {accion}")  # Muestra la percepción y la acción tomada.

# ------------------------------------------------------------------------------------
# PASO 3: EJECUCIÓN DEL EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque ejecuta el ejemplo práctico si el archivo se ejecuta directamente.
# - Es importante porque permite probar el funcionamiento del agente lógico.

if __name__ == "__main__":
    ejemplo_practico()  # Llama a la función que ejecuta el ejemplo práctico.

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El agente lógico utiliza una base de conocimiento para almacenar reglas.
#    Cada regla tiene una condición (función que evalúa una percepción) y una acción asociada.
# 2. Cuando el agente recibe una percepción, evalúa todas las reglas en su base de conocimiento.
#    Si una regla cumple su condición, el agente ejecuta la acción asociada.
# 3. Si ninguna regla es aplicable, el agente retorna un mensaje indicando que no encontró una acción válida.
# 
# SUPOSICIONES CLAVE:
# - Las percepciones son valores simples (como cadenas de texto) que representan el estado del entorno.
# - Las condiciones de las reglas son funciones lambda que evalúan estas percepciones.
# 
# VENTAJAS:
# - El algoritmo es modular y fácil de extender añadiendo nuevas reglas.
# - Es intuitivo y fácil de entender para principiantes.
# 
# LIMITACIONES:
# - No maneja conflictos entre reglas (por ejemplo, si dos reglas son aplicables al mismo tiempo).
# - No incluye aprendizaje automático; las reglas deben definirse manualmente.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: SALIDA ESPERADA
# ------------------------------------------------------------------------------------
# Si ejecutas este código, obtendrás una salida como esta:
# 
# Percepción: camino_libre -> Acción: avanzar
# Percepción: obstaculo -> Acción: girar_derecha
# Percepción: camino_libre -> Acción: avanzar
# Percepción: camino_libre -> Acción: avanzar
# 
# Esto demuestra cómo el agente lógico toma decisiones basadas en reglas predefinidas.