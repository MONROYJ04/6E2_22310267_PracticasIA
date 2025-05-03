# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: LÓGICA POR DEFECTO PARA RAZONAMIENTO INCOMPLETO
# ------------------------------------------------------------------------------------
# Este código implementa un sistema de Lógica por Defecto, que permite razonar en 
# situaciones donde no se tiene información completa. Se basa en asumir que algo es 
# verdadero por defecto, a menos que se demuestre lo contrario mediante excepciones.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE LogicaPorDefecto
# ------------------------------------------------------------------------------------
# - Este bloque define una clase que encapsula la funcionalidad de la lógica por defecto.
# - Es importante porque organiza las reglas y excepciones, y permite evaluarlas.
# - La clase utiliza un diccionario (`reglas_por_defecto`) para almacenar las reglas 
#   generales y un conjunto (`excepciones`) para manejar las excepciones.

class LogicaPorDefecto:
    def __init__(self):
        # Inicializamos un diccionario para almacenar las reglas por defecto
        self.reglas_por_defecto = {}
        # Inicializamos un conjunto para almacenar las excepciones
        self.excepciones = set()

    # --------------------------------------------------------------------------------
    # PASO 2: MÉTODO agregar_regla
    # --------------------------------------------------------------------------------
    # - Este método permite agregar una regla por defecto al sistema.
    # - Es importante porque define las suposiciones generales del sistema.
    # - Parámetros:
    #   - `regla`: Describe la condición (ejemplo: "es un pajaro").
    #   - `conclusion`: Describe la conclusión por defecto (ejemplo: "puede volar").
    def agregar_regla(self, regla, conclusion):
        self.reglas_por_defecto[regla] = conclusion

    # --------------------------------------------------------------------------------
    # PASO 3: MÉTODO agregar_excepcion
    # --------------------------------------------------------------------------------
    # - Este método permite agregar excepciones a las reglas por defecto.
    # - Es importante porque define los casos en los que las reglas generales no aplican.
    # - Parámetros:
    #   - `regla`: La regla para la cual se agrega una excepción (ejemplo: "es un pinguino").
    def agregar_excepcion(self, regla):
        self.excepciones.add(regla)

    # --------------------------------------------------------------------------------
    # PASO 4: MÉTODO evaluar
    # --------------------------------------------------------------------------------
    # - Este método evalúa si una regla por defecto es aplicable.
    # - Es importante porque determina si se aplica la conclusión por defecto, 
    #   si hay una excepción, o si la regla es desconocida.
    # - Parámetros:
    #   - `regla`: La regla que se desea evaluar.
    # - Retorno:
    #   - "No aplica" si la regla tiene una excepción.
    #   - La conclusión por defecto si no hay excepciones.
    #   - "Regla desconocida" si la regla no está definida.
    def evaluar(self, regla):
        if regla in self.excepciones:
            # Si la regla tiene una excepción, no se aplica la conclusión por defecto
            return "No aplica"
        elif regla in self.reglas_por_defecto:
            # Si no hay excepción, se aplica la conclusión por defecto
            return self.reglas_por_defecto[regla]
        else:
            # Si la regla no existe, se indica que no se conoce
            return "Regla desconocida"

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar la clase LogicaPorDefecto para razonar sobre si 
#   los animales pueden volar basándose en reglas generales y excepciones.
# - Es importante porque ilustra el uso práctico del algoritmo.

# Creamos una instancia de la clase LogicaPorDefecto
logica = LogicaPorDefecto()

# Agregamos una regla por defecto: "Si es un pajaro, entonces puede volar"
logica.agregar_regla("es un pajaro", "puede volar")

# Agregamos una excepción: "Los pinguinos no pueden volar"
logica.agregar_excepcion("es un pinguino")

# Evaluamos diferentes casos
print("Caso 1: Un pajaro")
print(logica.evaluar("es un pajaro"))  # Salida esperada: "puede volar"

print("Caso 2: Un pinguino")
print(logica.evaluar("es un pinguino"))  # Salida esperada: "No aplica"

print("Caso 3: Un perro")
print(logica.evaluar("es un perro"))  # Salida esperada: "Regla desconocida"

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza un enfoque basado en reglas para razonar en situaciones 
#    donde no se tiene información completa.
# 2. Suposiciones clave:
#    - Las reglas por defecto son válidas a menos que exista una excepción explícita.
#    - Las excepciones tienen prioridad sobre las reglas generales.
# 3. Ventajas:
#    - Es simple y fácil de implementar.
#    - Útil para modelar sistemas con reglas generales y excepciones específicas.
# 4. Limitaciones:
#    - No maneja incertidumbre probabilística.
#    - No es adecuado para sistemas con reglas complejas o contradictorias.