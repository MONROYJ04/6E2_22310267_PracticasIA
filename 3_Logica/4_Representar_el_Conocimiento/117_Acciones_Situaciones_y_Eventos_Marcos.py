# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: REPRESENTACIÓN DE CONOCIMIENTO CON MARCOS
# ------------------------------------------------------------------------------------
# Este código implementa el concepto de "Marcos" para modelar situaciones, acciones y 
# eventos en un contexto específico. Los marcos son estructuras que permiten organizar 
# información de manera jerárquica y flexible, facilitando la representación de conocimiento.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE MARCO
# ------------------------------------------------------------------------------------
# - Este bloque define la clase `Marco`, que representa un marco de conocimiento.
# - Cada marco tiene un nombre y un conjunto de atributos que describen sus características.
# - Los atributos se almacenan en un diccionario, donde las claves son los nombres de los 
#   atributos y los valores son sus estados actuales.
class Marco:
    def __init__(self, nombre, atributos=None):
        """
        Inicializa un marco con un nombre y una lista de atributos.
        :param nombre: Nombre del marco (por ejemplo, "Cocina").
        :param atributos: Diccionario de atributos y sus valores (por ejemplo, {"luz": "apagada"}).
        """
        self.nombre = nombre  # Nombre del marco (ejemplo: "Cocina").
        self.atributos = atributos if atributos else {}  # Diccionario de atributos.

    # ------------------------------------------------------------------------------------
    # PASO 2: MÉTODO PARA ACTUALIZAR ATRIBUTOS
    # ------------------------------------------------------------------------------------
    # - Este método permite modificar el valor de un atributo específico dentro del marco.
    # - Es importante para modelar eventos que cambian el estado del marco.
    def actualizar_atributo(self, atributo, valor):
        """
        Actualiza el valor de un atributo en el marco.
        :param atributo: Nombre del atributo (por ejemplo, "luz").
        :param valor: Nuevo valor del atributo (por ejemplo, "encendida").
        """
        self.atributos[atributo] = valor  # Actualiza el valor del atributo en el diccionario.

    # ------------------------------------------------------------------------------------
    # PASO 3: MÉTODO PARA OBTENER ATRIBUTOS
    # ------------------------------------------------------------------------------------
    # - Este método permite consultar el valor actual de un atributo en el marco.
    # - Si el atributo no existe, devuelve "Desconocido" como valor predeterminado.
    def obtener_atributo(self, atributo):
        """
        Obtiene el valor de un atributo en el marco.
        :param atributo: Nombre del atributo (por ejemplo, "luz").
        :return: Valor del atributo (por ejemplo, "encendida").
        """
        return self.atributos.get(atributo, "Desconocido")  # Devuelve el valor o "Desconocido".

    # ------------------------------------------------------------------------------------
    # PASO 4: REPRESENTACIÓN EN TEXTO DEL MARCO
    # ------------------------------------------------------------------------------------
    # - Este método convierte el marco en una cadena de texto para facilitar su impresión.
    # - Es útil para visualizar el estado actual del marco y sus atributos.
    def __str__(self):
        """
        Representación en texto del marco para facilitar su impresión.
        """
        return f"Marco: {self.nombre}, Atributos: {self.atributos}"


# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO - MODELAR UNA SITUACIÓN EN UNA CASA
# ------------------------------------------------------------------------------------
# - Este bloque demuestra cómo usar la clase `Marco` para modelar una situación específica.
# - Se crea un marco llamado "Cocina" con atributos iniciales como "luz" y "puerta".
# - Se simulan eventos que modifican los atributos del marco, como encender la luz o abrir la puerta.
def ejemplo_practico():
    # Creamos un marco para representar la cocina
    cocina = Marco("Cocina", {"luz": "apagada", "puerta": "cerrada"})

    # Mostramos el estado inicial de la cocina
    print("Estado inicial de la cocina:")
    print(cocina)

    # Simulamos un evento: alguien enciende la luz
    print("\nEvento: Encender la luz de la cocina.")
    cocina.actualizar_atributo("luz", "encendida")

    # Simulamos otro evento: alguien abre la puerta
    print("\nEvento: Abrir la puerta de la cocina.")
    cocina.actualizar_atributo("puerta", "abierta")

    # Mostramos el estado final de la cocina
    print("\nEstado final de la cocina:")
    print(cocina)


# ------------------------------------------------------------------------------------
# PASO 6: EJECUCIÓN DEL EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque ejecuta el ejemplo práctico para demostrar el funcionamiento del algoritmo.
# - Si el archivo se ejecuta directamente, se llama a la función `ejemplo_practico`.
if __name__ == "__main__":
    ejemplo_practico()


# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza la clase `Marco` para modelar situaciones mediante atributos.
# 2. Los atributos representan características del marco y pueden ser modificados para 
#    simular eventos o cambios en el estado del marco.
# 3. Ventajas:
#    - Permite organizar información de manera estructurada.
#    - Es flexible y puede adaptarse a diferentes contextos.
# 4. Limitaciones:
#    - No incluye lógica avanzada para relaciones entre marcos.
#    - Es una representación básica que puede requerir extensiones para casos complejos.