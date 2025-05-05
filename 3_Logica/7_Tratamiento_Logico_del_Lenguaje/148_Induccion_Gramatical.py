# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: INDUCCIÓN GRAMATICAL PARA GENERAR UNA GRAMÁTICA SIMPLE
# ------------------------------------------------------------------------------------
# Este código realiza una inducción gramatical básica. Su objetivo es deducir una 
# gramática libre de contexto simple a partir de un conjunto de ejemplos positivos 
# (cadenas de texto). La gramática generada puede producir exactamente las cadenas 
# proporcionadas como ejemplos.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PARA INDUCIR UNA GRAMÁTICA
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada una lista de cadenas (ejemplos positivos).
# - Genera una gramática representada como un diccionario, donde cada regla tiene 
#   un identificador único (S1, S2, etc.) y está asociada a una cadena específica.
# - Es importante porque permite estructurar las cadenas en un formato formal 
#   que puede ser interpretado como una gramática.

def inducir_gramatica(ejemplos_positivos):
    """
    Esta función toma una lista de ejemplos positivos (cadenas) y genera una gramática
    libre de contexto simple que puede generar esas cadenas.

    :param ejemplos_positivos: Lista de cadenas que pertenecen al lenguaje.
    :return: Diccionario que representa la gramática generada.
    """
    # Inicializamos la gramática como un diccionario vacío
    gramatica = {}

    # Variable para contar las reglas generadas
    contador_reglas = 1

    # Iteramos sobre cada ejemplo positivo
    for ejemplo in ejemplos_positivos:
        # Creamos una regla para cada ejemplo positivo
        regla = f"S{contador_reglas}"  # S1, S2, S3, etc.
        gramatica[regla] = ejemplo  # Asociamos la regla con el ejemplo
        contador_reglas += 1

    return gramatica

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA FUNCIÓN PARA MOSTRAR LA GRAMÁTICA
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada la gramática generada (un diccionario).
# - Imprime las reglas de la gramática en un formato legible para el usuario.
# - Es importante porque permite visualizar el resultado del proceso de inducción 
#   gramatical de manera clara y comprensible.

def mostrar_gramatica(gramatica):
    """
    Esta función imprime la gramática generada en un formato legible.

    :param gramatica: Diccionario que representa la gramática.
    """
    print("Gramática generada:")
    for regla, produccion in gramatica.items():
        print(f"{regla} -> {produccion}")

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este bloque se define un conjunto de ejemplos positivos (cadenas de texto).
# - Se llama a la función `inducir_gramatica` para generar la gramática a partir 
#   de los ejemplos positivos.
# - Finalmente, se llama a la función `mostrar_gramatica` para imprimir la gramática 
#   generada.

if __name__ == "__main__":
    # Definimos un conjunto de ejemplos positivos
    ejemplos_positivos = [
        "aab",  # Ejemplo 1: cadena que pertenece al lenguaje
        "abb",  # Ejemplo 2: cadena que pertenece al lenguaje
        "abc"   # Ejemplo 3: cadena que pertenece al lenguaje
    ]

    # Llamamos a la función para inducir la gramática
    gramatica_generada = inducir_gramatica(ejemplos_positivos)

    # Mostramos la gramática generada
    mostrar_gramatica(gramatica_generada)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo toma una lista de cadenas (ejemplos positivos) y genera una gramática 
#    libre de contexto simple. Cada cadena se asocia con una regla única.
# 2. Suposiciones clave:
#    - Cada cadena de entrada pertenece al lenguaje que queremos modelar.
#    - La gramática generada es específica para los ejemplos proporcionados y no 
#      generaliza a cadenas no vistas.
# 3. Ventajas:
#    - Es fácil de implementar y entender.
#    - Útil para modelar lenguajes pequeños o específicos.
# 4. Limitaciones:
#    - No generaliza a cadenas no vistas.
#    - No considera ejemplos negativos (cadenas que no pertenecen al lenguaje).

# ------------------------------------------------------------------------------------
# EJEMPLO DE SALIDA
# ------------------------------------------------------------------------------------
# Si ejecutamos este código, la salida será:
# Gramática generada:
# S1 -> aab
# S2 -> abb
# S3 -> abc
# Esto significa que la gramática generada puede producir exactamente las cadenas 
# "aab", "abb" y "abc".