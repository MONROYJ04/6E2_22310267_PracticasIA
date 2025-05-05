# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: GRAMÁTICA CAUSAL DEFINIDA PARA MODELAR RELACIONES CAUSALES
# ------------------------------------------------------------------------------------
# Este programa implementa una Gramática Causal Definida, que se utiliza para modelar
# relaciones causales entre eventos o conceptos. El objetivo es definir reglas que 
# describan cómo ciertos eventos (causas) generan otros eventos (efectos).

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE GRAMÁTICA CAUSAL
# ------------------------------------------------------------------------------------
# - Este bloque define una clase llamada `GramaticaCausalDefinida`.
# - La clase contiene métodos para agregar reglas causales, obtener efectos de una causa
#   y mostrar todas las reglas definidas.
# - Es importante porque encapsula toda la lógica de la gramática causal en un solo lugar.

class GramaticaCausalDefinida:
    def __init__(self):
        # ------------------------------------------------------------------------------------
        # PASO 2: INICIALIZACIÓN DE LA GRAMÁTICA
        # ------------------------------------------------------------------------------------
        # - Aquí se inicializa un diccionario vacío llamado `reglas`.
        # - Este diccionario almacenará las relaciones causales en el formato:
        #   {causa: [efecto1, efecto2, ...]}.
        # - Es importante porque permite organizar las reglas de manera estructurada.
        self.reglas = {}

    def agregar_regla(self, causa, efecto):
        # ------------------------------------------------------------------------------------
        # PASO 3: AGREGAR UNA REGLA CAUSAL
        # ------------------------------------------------------------------------------------
        # - Este método permite agregar una nueva relación causal a la gramática.
        # - Si la causa no existe en el diccionario, se inicializa con una lista vacía.
        # - Luego, se agrega el efecto a la lista correspondiente a la causa.
        # - Es importante porque define cómo se relacionan los eventos.
        # - Parámetros:
        #   - `causa`: Evento que genera otros eventos (cadena de texto).
        #   - `efecto`: Evento generado por la causa (cadena de texto).
        if causa not in self.reglas:
            self.reglas[causa] = []  # Si la causa no existe, la inicializamos con una lista vacía
        self.reglas[causa].append(efecto)  # Agregamos el efecto a la lista de la causa

    def obtener_efectos(self, causa):
        # ------------------------------------------------------------------------------------
        # PASO 4: OBTENER LOS EFECTOS DE UNA CAUSA
        # ------------------------------------------------------------------------------------
        # - Este método devuelve una lista de efectos asociados a una causa específica.
        # - Si la causa no existe en el diccionario, retorna una lista vacía.
        # - Es importante porque permite consultar las relaciones causales definidas.
        # - Parámetros:
        #   - `causa`: Evento del cual queremos conocer los efectos (cadena de texto).
        # - Retorno:
        #   - Lista de efectos asociados a la causa.
        return self.reglas.get(causa, [])  # Retorna los efectos asociados a la causa o una lista vacía si no existe

    def mostrar_reglas(self):
        # ------------------------------------------------------------------------------------
        # PASO 5: MOSTRAR TODAS LAS REGLAS DEFINIDAS
        # ------------------------------------------------------------------------------------
        # - Este método imprime todas las reglas causales almacenadas en el diccionario.
        # - Es importante porque permite visualizar las relaciones causales definidas.
        for causa, efectos in self.reglas.items():
            print(f"{causa} causa: {', '.join(efectos)}")


# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO DE USO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar la clase `GramaticaCausalDefinida`.
# - Se crean reglas causales, se muestran las reglas definidas y se consultan los efectos
#   de eventos específicos.
if __name__ == "__main__":
    # ------------------------------------------------------------------------------------
    # PASO 6.1: CREAR UNA INSTANCIA DE LA GRAMÁTICA
    # ------------------------------------------------------------------------------------
    # - Aquí se crea un objeto de la clase `GramaticaCausalDefinida`.
    # - Es importante porque permite usar los métodos definidos en la clase.
    gramatica = GramaticaCausalDefinida()

    # ------------------------------------------------------------------------------------
    # PASO 6.2: AGREGAR REGLAS CAUSALES
    # ------------------------------------------------------------------------------------
    # - Se agregan relaciones causales entre eventos.
    # - Ejemplo:
    #   - "lluvia" causa "suelo_mojado" y "trafico_lento".
    #   - "suelo_mojado" causa "resbalones".
    #   - "trafico_lento" causa "llegada_tardia".
    gramatica.agregar_regla("lluvia", "suelo_mojado")
    gramatica.agregar_regla("lluvia", "trafico_lento")
    gramatica.agregar_regla("suelo_mojado", "resbalones")
    gramatica.agregar_regla("trafico_lento", "llegada_tardia")

    # ------------------------------------------------------------------------------------
    # PASO 6.3: MOSTRAR LAS REGLAS DEFINIDAS
    # ------------------------------------------------------------------------------------
    # - Se imprimen todas las reglas causales definidas.
    print("Reglas causales definidas:")
    gramatica.mostrar_reglas()

    # ------------------------------------------------------------------------------------
    # PASO 6.4: CONSULTAR LOS EFECTOS DE UNA CAUSA
    # ------------------------------------------------------------------------------------
    # - Se consultan los efectos de eventos específicos.
    # - Ejemplo:
    #   - Efectos de "lluvia": ["suelo_mojado", "trafico_lento"].
    #   - Efectos de "suelo_mojado": ["resbalones"].
    print("\nEfectos de 'lluvia':")
    efectos_lluvia = gramatica.obtener_efectos("lluvia")
    print(efectos_lluvia)

    print("\nEfectos de 'suelo_mojado':")
    efectos_suelo_mojado = gramatica.obtener_efectos("suelo_mojado")
    print(efectos_suelo_mojado)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo modela relaciones causales entre eventos mediante un diccionario.
# 2. Suposiciones clave:
#    - Cada causa puede tener múltiples efectos.
#    - Las relaciones son unidireccionales (de causa a efecto).
# 3. Ventajas:
#    - Fácil de implementar y entender.
#    - Útil para modelar sistemas simples de relaciones causales.
# 4. Limitaciones:
#    - No considera relaciones bidireccionales o efectos compuestos.
#    - No incluye probabilidades o incertidumbre en las relaciones.