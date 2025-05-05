# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ANÁLISIS SEMÁNTICO PARA IDENTIFICAR SIGNIFICADOS EN CONTEXTO
# ------------------------------------------------------------------------------------
# Este código utiliza WordNet, una base de datos léxica, para analizar el significado
# más relevante de una palabra en un contexto dado. El objetivo es determinar cómo
# una palabra puede interpretarse según las palabras relacionadas que la rodean.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LA BIBLIOTECA NECESARIA
# ------------------------------------------------------------------------------------
# - Importamos `wordnet` de la biblioteca `nltk` para trabajar con significados
#   (sinsets) y relaciones semánticas entre palabras.
# - WordNet es una herramienta poderosa para el procesamiento del lenguaje natural.
from nltk.corpus import wordnet

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR UNA FUNCIÓN PARA OBTENER SIGNIFICADOS
# ------------------------------------------------------------------------------------
# - Esta función toma una palabra como entrada y devuelve una lista de significados
#   (sinsets) asociados con esa palabra.
# - Es importante porque nos permite acceder a los posibles significados que WordNet
#   tiene registrados para una palabra específica.
def obtener_significados(palabra):
    """
    Esta funcion toma una palabra como entrada y devuelve una lista de significados
    (sinsets) asociados con esa palabra usando WordNet.
    """
    # Obtenemos los significados de la palabra desde WordNet
    significados = wordnet.synsets(palabra)
    return significados

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR UNA FUNCIÓN PARA ANALIZAR EL SIGNIFICADO EN UN CONTEXTO
# ------------------------------------------------------------------------------------
# - Esta función toma una palabra y un contexto (lista de palabras relacionadas).
# - Devuelve el significado más relevante de la palabra en ese contexto.
# - Es crucial porque compara los significados de la palabra con los significados
#   de las palabras del contexto para encontrar el más adecuado.
def analizar_significado(palabra, contexto):
    """
    Esta funcion toma una palabra y un contexto (lista de palabras relacionadas)
    y devuelve el significado mas relevante de la palabra en ese contexto.
    """
    # Obtenemos los significados de la palabra
    significados = obtener_significados(palabra)
    if not significados:
        return None  # Si no hay significados, devolvemos None
    
    # Inicializamos variables para almacenar el mejor significado y su puntaje
    mejor_significado = None
    mejor_puntaje = 0

    # --------------------------------------------------------------------------------
    # PASO 3.1: CALCULAR LA SIMILITUD ENTRE SIGNIFICADOS
    # --------------------------------------------------------------------------------
    # - Para cada significado de la palabra, calculamos su similitud con los
    #   significados de las palabras del contexto.
    # - Usamos la métrica `wup_similarity`, que mide la similitud semántica.
    for significado in significados:
        puntaje = 0  # Inicializamos el puntaje para este significado
        for palabra_contexto in contexto:
            for significado_contexto in wordnet.synsets(palabra_contexto):
                # Calculamos la similitud entre el significado y el contexto
                similitud = significado.wup_similarity(significado_contexto)
                if similitud:  # Si hay una similitud calculada
                    puntaje += similitud
        
        # --------------------------------------------------------------------------------
        # PASO 3.2: ACTUALIZAR EL MEJOR SIGNIFICADO
        # --------------------------------------------------------------------------------
        # - Si el puntaje del significado actual es mayor que el mejor puntaje
        #   registrado, actualizamos el mejor significado.
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_significado = significado
    
    # Devolvemos el significado más relevante
    return mejor_significado

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, analizamos la palabra "banco" en un contexto relacionado con
#   finanzas. El objetivo es identificar el significado más relevante.
if __name__ == "__main__":
    # Palabra a analizar
    palabra = "banco"
    
    # Contexto en el que aparece la palabra
    contexto = ["dinero", "finanzas", "ahorros"]
    
    # Analizamos el significado de la palabra en el contexto dado
    significado_relevante = analizar_significado(palabra, contexto)
    
    # Mostramos el resultado
    if significado_relevante:
        print(f"El significado mas relevante de '{palabra}' en el contexto dado es:")
        print(f"- Definicion: {significado_relevante.definition()}")
        print(f"- Ejemplo: {significado_relevante.examples()}")
    else:
        print(f"No se encontro un significado relevante para '{palabra}' en el contexto dado.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza WordNet para obtener los significados (sinsets) de una
#    palabra y calcular su similitud con los significados de palabras en un contexto.
# 2. La similitud se mide usando `wup_similarity`, que compara la distancia entre
#    conceptos en la jerarquía semántica de WordNet.
# 3. Ventajas:
#    - Permite desambiguar palabras polisémicas (con múltiples significados).
#    - Es útil en tareas de procesamiento del lenguaje natural.
# 4. Limitaciones:
#    - Depende de la calidad de los datos en WordNet.
#    - La métrica de similitud puede no capturar todos los matices del lenguaje.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Entrada:
# - Palabra: "banco"
# - Contexto: ["dinero", "finanzas", "ahorros"]
#
# Salida esperada:
# - Definición: "una institución financiera que acepta depósitos y canaliza el dinero hacia actividades de préstamo."
# - Ejemplo: ["El banco aprobó mi préstamo."]