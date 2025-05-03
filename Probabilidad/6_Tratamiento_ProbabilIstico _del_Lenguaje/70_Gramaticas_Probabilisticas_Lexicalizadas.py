# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: GRAMÁTICAS PROBABILÍSTICAS LEXICALIZADAS PARA ANÁLISIS SINTÁCTICO
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo basado en Gramáticas Probabilísticas Lexicalizadas (GPL) 
# para analizar la estructura gramatical de oraciones en español. Utiliza una gramática 
# probabilística simple para generar árboles de análisis sintáctico con probabilidades asociadas.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `nltk`, una biblioteca para el procesamiento de lenguaje natural.
# - Usamos `PCFG` (Probabilistic Context-Free Grammar) para definir la gramática probabilística.
import nltk
from nltk import PCFG  # PCFG: Gramática libre de contexto probabilística

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA GRAMÁTICA PROBABILÍSTICA LEXICALIZADA
# ------------------------------------------------------------------------------------
# - Aquí definimos las reglas gramaticales con probabilidades asociadas.
# - Cada regla tiene una probabilidad que indica su frecuencia relativa.
# - Ejemplo:
#   - `S -> NP VP [1.0]` significa que una oración (S) siempre se divide en un sintagma nominal (NP) 
#     y un sintagma verbal (VP) con probabilidad 1.0 (100%).
#   - `NP -> 'Juan' [0.5] | 'Maria' [0.5]` significa que un sintagma nominal (NP) puede ser "Juan" 
#     o "Maria", cada uno con probabilidad 0.5 (50%).
gramatica = PCFG.fromstring("""
    S -> NP VP [1.0]  # La oración (S) se divide en un sintagma nominal (NP) y un sintagma verbal (VP) con probabilidad 1.0
    NP -> 'Juan' [0.5] | 'Maria' [0.5]  # El sintagma nominal puede ser 'Juan' o 'Maria', cada uno con probabilidad 0.5
    VP -> V NP [1.0]  # El sintagma verbal (VP) se divide en un verbo (V) y un sintagma nominal (NP) con probabilidad 1.0
    V -> 'ama' [1.0]  # El verbo (V) es 'ama' con probabilidad 1.0
""")

# ------------------------------------------------------------------------------------
# PASO 3: CREAR EL PARSER PARA ANALIZAR ORACIONES
# ------------------------------------------------------------------------------------
# - Usamos el parser de Viterbi, que encuentra el árbol de análisis sintáctico más probable 
#   para una oración basada en la gramática definida.
# - Este parser utiliza un enfoque probabilístico para seleccionar la estructura más adecuada.
parser = nltk.ViterbiParser(gramatica)

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR UNA ORACIÓN DE EJEMPLO
# ------------------------------------------------------------------------------------
# - Aquí definimos una oración que será analizada por el parser.
# - La oración está representada como una lista de palabras: ['Juan', 'ama', 'Maria'].
# - Esta oración corresponde a "Juan ama a Maria".
oracion = ['Juan', 'ama', 'Maria']  # Oración de ejemplo: "Juan ama a Maria"

# ------------------------------------------------------------------------------------
# PASO 5: ANALIZAR LA ORACIÓN UTILIZANDO EL PARSER
# ------------------------------------------------------------------------------------
# - El parser analiza la oración y genera árboles de análisis sintáctico.
# - Cada árbol tiene una probabilidad asociada basada en las reglas de la gramática.
# - Mostramos los árboles generados y sus probabilidades.
print("Árboles de análisis posibles con sus probabilidades:")
for arbol in parser.parse(oracion):
    print(arbol)  # Mostramos el árbol de análisis sintáctico en formato texto
    arbol.pretty_print()  # Mostramos el árbol de forma visual (gráfica)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Gramática Probabilística Lexicalizada**:
#    - Una gramática probabilística asigna probabilidades a las reglas gramaticales.
#    - Esto permite modelar la frecuencia relativa de las estructuras gramaticales en un lenguaje.
# 2. **Parser de Viterbi**:
#    - Este parser utiliza un enfoque probabilístico para encontrar el árbol de análisis más probable.
#    - Es eficiente para gramáticas probabilísticas y garantiza encontrar la mejor solución.
# 3. **Ventajas**:
#    - Permite modelar la ambigüedad en el lenguaje natural.
#    - Es útil para tareas como traducción automática y reconocimiento de voz.
# 4. **Limitaciones**:
#    - Las gramáticas simples, como la utilizada aquí, no capturan toda la complejidad del lenguaje natural.
#    - En aplicaciones reales, se requieren gramáticas más complejas y grandes conjuntos de datos.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que queremos analizar otra oración, como "Maria ama Juan".
# Podemos modificar la variable `oracion` y volver a ejecutar el análisis:
# oracion = ['Maria', 'ama', 'Juan']
# Esto generará un nuevo árbol de análisis sintáctico basado en la gramática definida.