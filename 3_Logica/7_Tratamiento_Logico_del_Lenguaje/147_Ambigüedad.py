# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO PARA DETECTAR Y RESOLVER AMBIGÜEDADES EN FRASES LÓGICAS
# ------------------------------------------------------------------------------------
# Este programa analiza frases en español para identificar posibles ambigüedades lógicas.
# Una ambigüedad ocurre cuando una frase puede interpretarse de más de una manera.
# El algoritmo utiliza reglas simples basadas en palabras clave como "y" y "o" para generar
# interpretaciones alternativas de la frase.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Se importa la librería `re` (expresiones regulares) para dividir frases en partes.
# - Esto es importante porque permite identificar patrones específicos en el texto.
import re

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL PARA ANALIZAR AMBIGÜEDADES
# ------------------------------------------------------------------------------------
# - La función `analizar_ambiguedad` toma una frase como entrada y devuelve una lista
#   con posibles interpretaciones de la frase.
# - Utiliza reglas simples para detectar palabras clave ("y" y "o") que pueden generar
#   ambigüedad en el significado de la frase.

def analizar_ambiguedad(frase):
    """
    Analiza una frase para detectar ambigüedades lógicas.
    :param frase: La frase a analizar (cadena de texto).
    :return: Una lista con las posibles interpretaciones de la frase.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: INICIALIZAR UNA LISTA PARA GUARDAR LAS INTERPRETACIONES
    # --------------------------------------------------------------------------------
    # - Se crea una lista vacía llamada `interpretaciones` para almacenar las posibles
    #   versiones alternativas de la frase.
    # - Esto es importante porque el algoritmo puede generar múltiples interpretaciones.
    interpretaciones = []

    # --------------------------------------------------------------------------------
    # PASO 2.2: DETECTAR PALABRAS CLAVE ("Y" Y "O") EN LA FRASE
    # --------------------------------------------------------------------------------
    # - Se verifica si la frase contiene las palabras "y" o "o".
    # - Estas palabras son indicadores de posibles ambigüedades lógicas.
    if "y" in frase or "o" in frase:
        # ---------------------------------------------------------------------------
        # PASO 2.3: DIVIDIR LA FRASE EN PARTES USANDO EXPRESIONES REGULARES
        # ---------------------------------------------------------------------------
        # - La función `re.split` divide la frase en partes cada vez que encuentra
        #   las palabras "y" o "o" rodeadas de espacios.
        # - Esto permite analizar cada segmento de la frase por separado.
        partes = re.split(r'\s(y|o)\s', frase)

        # ---------------------------------------------------------------------------
        # PASO 2.4: GENERAR INTERPRETACIONES ALTERNATIVAS
        # ---------------------------------------------------------------------------
        # - Se recorre la lista de partes para crear nuevas versiones de la frase.
        # - Cada interpretación combina las partes con la palabra "y/o", que indica
        #   que ambas opciones son posibles.
        for i in range(len(partes) - 1):
            interpretacion = " ".join(partes[:i + 1]) + " y/o " + " ".join(partes[i + 1:])
            interpretaciones.append(interpretacion)

    # --------------------------------------------------------------------------------
    # PASO 2.5: DEVOLVER LA FRASE ORIGINAL SI NO HAY AMBIGÜEDADES
    # --------------------------------------------------------------------------------
    # - Si no se detectan palabras clave ("y" o "o"), se asume que la frase no tiene
    #   ambigüedades y se devuelve tal cual.
    if not interpretaciones:
        interpretaciones.append(frase)

    # --------------------------------------------------------------------------------
    # PASO 2.6: DEVOLVER LAS INTERPRETACIONES GENERADAS
    # --------------------------------------------------------------------------------
    # - La función devuelve la lista de interpretaciones (puede contener una o más).
    return interpretaciones

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En esta sección se utiliza una frase de ejemplo para demostrar cómo funciona
#   el algoritmo.
# - Se analiza la frase "Juan y Maria o Pedro van al cine" y se generan posibles
#   interpretaciones.
if __name__ == "__main__":
    # Frase de ejemplo que contiene ambigüedad
    frase_ambigua = "Juan y Maria o Pedro van al cine"

    # Llamamos a la función para analizar la frase
    resultado = analizar_ambiguedad(frase_ambigua)

    # Mostramos los resultados
    print("Frase original:")
    print(frase_ambigua)
    print("\nPosibles interpretaciones:")
    for interpretacion in resultado:
        print("-", interpretacion)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo identifica palabras clave ("y" y "o") que pueden generar ambigüedad.
# 2. Divide la frase en partes usando expresiones regulares para analizar cada segmento.
# 3. Genera interpretaciones alternativas combinando las partes con "y/o".
# 4. Si no se detectan ambigüedades, devuelve la frase original.
# 
# SUPOSICIONES CLAVE:
# - Las palabras clave ("y" y "o") son los únicos indicadores de ambigüedad.
# - La frase está escrita en español y sigue una estructura lógica básica.
# 
# VENTAJAS:
# - Fácil de entender y aplicar a frases simples.
# - Genera interpretaciones alternativas de manera automática.
# 
# LIMITACIONES:
# - No maneja ambigüedades más complejas (como el contexto o la gramática avanzada).
# - Solo funciona con frases que contienen "y" u "o".