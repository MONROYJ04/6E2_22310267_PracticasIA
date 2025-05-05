# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ANÁLISIS LÉXICO PARA DIVIDIR Y CLASIFICAR TEXTO
# ------------------------------------------------------------------------------------
# Este código realiza un análisis léxico básico. Su objetivo es dividir un texto en 
# unidades más pequeñas llamadas "tokens" (como palabras, números y símbolos) y 
# clasificarlos según su tipo. Esto es útil en tareas de procesamiento de lenguaje 
# natural (NLP) o compiladores.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos la librería `re` (expresiones regulares) para buscar patrones en el texto.
# - Las expresiones regulares permiten identificar palabras, números y símbolos.
import re

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Creamos una función llamada `analisis_lexico` que toma un texto como entrada.
# - Esta función divide el texto en tokens y los clasifica en tres categorías:
#   1. PALABRAS: Identificadores como nombres de variables o palabras clave.
#   2. NÚMEROS: Enteros o decimales.
#   3. SÍMBOLOS: Operadores o signos de puntuación.
def analisis_lexico(texto):
    """
    Realiza un análisis léxico de un texto dado.
    
    Parametros:
    texto (str): El texto a analizar.
    
    Retorna:
    list: Una lista de tokens clasificados.
    """
    # --------------------------------------------------------------------------------
    # PASO 3: INICIALIZAR VARIABLES
    # --------------------------------------------------------------------------------
    # - Creamos una lista vacía llamada `tokens` para almacenar los resultados.
    tokens = []

    # --------------------------------------------------------------------------------
    # PASO 4: DEFINIR PATRONES PARA LOS TOKENS
    # --------------------------------------------------------------------------------
    # - Usamos expresiones regulares para definir los patrones de cada tipo de token:
    #   1. `patron_palabra`: Coincide con palabras que comienzan con letras o guiones 
    #      bajos y pueden contener números.
    #   2. `patron_numero`: Coincide con números enteros o decimales.
    #   3. `patron_simbolo`: Coincide con cualquier símbolo que no sea una letra, 
    #      número o espacio.
    patron_palabra = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Palabras (identificadores)
    patron_numero = r'\d+(\.\d+)?'              # Números (enteros o decimales)
    patron_simbolo = r'[^\w\s]'                 # Símbolos (como operadores o puntuación)

    # --------------------------------------------------------------------------------
    # PASO 5: COMBINAR LOS PATRONES
    # --------------------------------------------------------------------------------
    # - Combinamos los tres patrones en una sola expresión regular llamada 
    #   `patron_general`. Esto permite buscar todos los tipos de tokens en una sola 
    #   operación.
    patron_general = f'({patron_palabra})|({patron_numero})|({patron_simbolo})'

    # --------------------------------------------------------------------------------
    # PASO 6: BUSCAR TOKENS EN EL TEXTO
    # --------------------------------------------------------------------------------
    # - Usamos `re.findall` para buscar todas las coincidencias del patrón general 
    #   en el texto. Esto devuelve una lista de tuplas, donde cada tupla contiene 
    #   los tokens encontrados.
    matches = re.findall(patron_general, texto)

    # --------------------------------------------------------------------------------
    # PASO 7: CLASIFICAR LOS TOKENS
    # --------------------------------------------------------------------------------
    # - Iteramos sobre cada coincidencia en `matches`.
    # - Clasificamos cada token según el patrón con el que coincide:
    #   1. Si coincide con `patron_palabra`, lo clasificamos como "PALABRA".
    #   2. Si coincide con `patron_numero`, lo clasificamos como "NUMERO".
    #   3. Si coincide con `patron_simbolo`, lo clasificamos como "SIMBOLO".
    for match in matches:
        if match[0]:  # Si coincide con el patrón de palabra
            tokens.append(('PALABRA', match[0]))
        elif match[1]:  # Si coincide con el patrón de número
            tokens.append(('NUMERO', match[1]))
        elif match[2]:  # Si coincide con el patrón de símbolo
            tokens.append(('SIMBOLO', match[2]))

    # --------------------------------------------------------------------------------
    # PASO 8: DEVOLVER LOS TOKENS
    # --------------------------------------------------------------------------------
    # - Retornamos la lista de tokens clasificados.
    return tokens

# ------------------------------------------------------------------------------------
# PASO 9: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, analizamos el texto "variable1 = 42 + 3.14".
# - Mostramos los tokens encontrados y su clasificación.
if __name__ == "__main__":
    # Texto de entrada para el análisis léxico
    texto_ejemplo = "variable1 = 42 + 3.14"

    # Llamamos a la función de análisis léxico
    resultado = analisis_lexico(texto_ejemplo)

    # Mostramos los tokens encontrados
    print("Tokens encontrados:")
    for tipo, valor in resultado:
        print(f"Tipo: {tipo}, Valor: {valor}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza expresiones regulares para dividir un texto en tokens.
# 2. Los tokens se clasifican en tres categorías: palabras, números y símbolos.
# 3. Es útil en tareas como:
#    - Procesamiento de lenguaje natural (NLP).
#    - Análisis de código fuente en compiladores.
# 4. Limitaciones:
#    - No reconoce estructuras gramaticales complejas.
#    - No distingue entre palabras clave y nombres de variables en lenguajes de 
#      programación.