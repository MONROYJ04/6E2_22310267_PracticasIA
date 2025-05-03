# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA DE ONTOLOGÍAS PARA REPRESENTAR CONOCIMIENTO
# ------------------------------------------------------------------------------------
# Este código implementa un sistema básico de ontologías para representar conocimiento.
# Una ontología es una estructura que define conceptos y relaciones entre ellos en un 
# dominio específico, permitiendo organizar y estructurar información de manera jerárquica.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE ONTOLOGÍA
# ------------------------------------------------------------------------------------
# - Este bloque define la clase `Ontologia`, que será la estructura principal para 
#   almacenar conceptos y relaciones.
# - Es importante porque permite modelar un dominio de conocimiento de forma estructurada.
# - La clase utiliza un diccionario (`self.conceptos`) para almacenar los conceptos como 
#   claves y sus relaciones como valores.

class Ontologia:
    def __init__(self):
        # Diccionario para almacenar conceptos y sus relaciones
        self.conceptos = {}

    # ------------------------------------------------------------------------------------
    # PASO 2: MÉTODO PARA AGREGAR CONCEPTOS
    # ------------------------------------------------------------------------------------
    # - Este método permite agregar un concepto a la ontología.
    # - Si el concepto ya existe, se muestra un mensaje indicando que no se puede duplicar.
    # - Es importante porque los conceptos son la base de la ontología.
    def agregar_concepto(self, concepto):
        if concepto not in self.conceptos:
            self.conceptos[concepto] = []
        else:
            print(f"El concepto '{concepto}' ya existe en la ontología.")

    # ------------------------------------------------------------------------------------
    # PASO 3: MÉTODO PARA AGREGAR RELACIONES ENTRE CONCEPTOS
    # ------------------------------------------------------------------------------------
    # - Este método permite establecer una relación entre dos conceptos existentes.
    # - Las relaciones se almacenan como tuplas (concepto_destino, tipo_relacion).
    # - Es importante porque define cómo los conceptos están conectados entre sí.
    def agregar_relacion(self, concepto_origen, concepto_destino, tipo_relacion):
        if concepto_origen in self.conceptos and concepto_destino in self.conceptos:
            self.conceptos[concepto_origen].append((concepto_destino, tipo_relacion))
        else:
            print("Uno o ambos conceptos no existen en la ontología.")

    # ------------------------------------------------------------------------------------
    # PASO 4: MÉTODO PARA MOSTRAR LA ONTOLOGÍA
    # ------------------------------------------------------------------------------------
    # - Este método imprime todos los conceptos y sus relaciones en la ontología.
    # - Es importante porque permite visualizar la estructura de conocimiento creada.
    def mostrar_ontologia(self):
        for concepto, relaciones in self.conceptos.items():
            print(f"Concepto: {concepto}")
            for relacion in relaciones:
                print(f"  -> Relacion: {relacion[1]} con {relacion[0]}")

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO DE USO DE LA ONTOLOGÍA
# ------------------------------------------------------------------------------------
# - Este bloque crea una instancia de la clase `Ontologia` y la utiliza para modelar 
#   un dominio de conocimiento relacionado con animales.
# - Se agregan conceptos como "Animal", "Mamifero", "Ave", etc., y se establecen 
#   relaciones jerárquicas entre ellos.
# - Finalmente, se muestra la ontología completa.

def ejemplo_practico():
    # Crear una instancia de la ontología
    ontologia = Ontologia()

    # Agregar conceptos relacionados con animales
    ontologia.agregar_concepto("Animal")
    ontologia.agregar_concepto("Mamifero")
    ontologia.agregar_concepto("Ave")
    ontologia.agregar_concepto("Perro")
    ontologia.agregar_concepto("Gato")
    ontologia.agregar_concepto("Aguila")

    # Agregar relaciones entre los conceptos
    ontologia.agregar_relacion("Mamifero", "Animal", "es_un")
    ontologia.agregar_relacion("Ave", "Animal", "es_un")
    ontologia.agregar_relacion("Perro", "Mamifero", "es_un")
    ontologia.agregar_relacion("Gato", "Mamifero", "es_un")
    ontologia.agregar_relacion("Aguila", "Ave", "es_un")

    # Mostrar la ontología
    print("Ontología de animales:")
    ontologia.mostrar_ontologia()

# Llamar al ejemplo práctico
ejemplo_practico()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una estructura de datos basada en diccionarios para modelar 
#    conceptos y relaciones en un dominio específico.
# 2. Suposiciones clave:
#    - Los conceptos deben ser únicos.
#    - Las relaciones solo pueden establecerse entre conceptos existentes.
# 3. Ventajas:
#    - Permite estructurar información de manera jerárquica y clara.
#    - Es extensible: se pueden agregar más conceptos y relaciones fácilmente.
# 4. Limitaciones:
#    - No incluye validaciones avanzadas (ej: relaciones cíclicas).
#    - No soporta relaciones más complejas como propiedades o restricciones.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# En este ejemplo, se modela una ontología de animales. Los conceptos y relaciones 
# jerárquicas permiten entender cómo están organizados los animales en términos de 
# categorías generales y específicas.
#
# Salida esperada:
# Ontología de animales:
# Concepto: Animal
# Concepto: Mamifero
#   -> Relacion: es_un con Animal
# Concepto: Ave
#   -> Relacion: es_un con Animal
# Concepto: Perro
#   -> Relacion: es_un con Mamifero
# Concepto: Gato
#   -> Relacion: es_un con Mamifero
# Concepto: Aguila
#   -> Relacion: es_un con Ave