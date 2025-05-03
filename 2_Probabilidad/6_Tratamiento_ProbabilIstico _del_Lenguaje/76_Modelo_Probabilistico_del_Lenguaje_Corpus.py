# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MODELO PROBABILÍSTICO DEL LENGUAJE BASADO EN UN CORPUS
# ------------------------------------------------------------------------------------
# Este algoritmo implementa un modelo probabilístico del lenguaje. Su propósito es 
# calcular la probabilidad de una palabra o una secuencia de palabras basándose en 
# la frecuencia de aparición en un corpus de texto.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Aquí se importa la biblioteca `collections` que contiene la clase `Counter`.
# - `Counter` es útil para contar la frecuencia de elementos en una lista, en este 
#   caso, las palabras del corpus.
from collections import Counter

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA PROCESAR EL CORPUS
# ------------------------------------------------------------------------------------
# - Esta función toma un texto (corpus) como entrada y devuelve un diccionario donde
#   las claves son las palabras y los valores son las frecuencias de esas palabras.
# - Es importante para calcular las probabilidades, ya que necesitamos las frecuencias
#   de las palabras para el modelo probabilístico.
def procesar_corpus(corpus):
    """
    Procesa el corpus de texto para calcular la frecuencia de cada palabra.
    
    Args:
        corpus (str): Texto del corpus.
    
    Returns:
        dict: Diccionario con palabras como claves y sus frecuencias como valores.
    """
    # Convertimos el texto a minúsculas para evitar diferencias entre palabras como 
    # "Este" y "este".
    texto_minusculas = corpus.lower()
    
    # Dividimos el texto en palabras usando espacios como separadores.
    palabras = texto_minusculas.split()
    
    # Usamos Counter para contar la frecuencia de cada palabra.
    frecuencias = Counter(palabras)
    
    return frecuencias

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN PARA CALCULAR LA PROBABILIDAD DE UNA PALABRA
# ------------------------------------------------------------------------------------
# - Esta función calcula la probabilidad de una palabra dividiendo su frecuencia entre
#   el total de palabras en el corpus.
# - Es clave para el modelo probabilístico, ya que permite estimar la probabilidad de
#   ocurrencia de una palabra en el corpus.
def calcular_probabilidad(palabra, frecuencias, total_palabras):
    """
    Calcula la probabilidad de una palabra en el corpus.
    
    Args:
        palabra (str): Palabra cuya probabilidad se desea calcular.
        frecuencias (dict): Diccionario con las frecuencias de las palabras.
        total_palabras (int): Número total de palabras en el corpus.
    
    Returns:
        float: Probabilidad de la palabra.
    """
    # Obtenemos la frecuencia de la palabra. Si no está en el corpus, la frecuencia es 0.
    frecuencia_palabra = frecuencias.get(palabra, 0)
    
    # Calculamos la probabilidad dividiendo la frecuencia entre el total de palabras.
    probabilidad = frecuencia_palabra / total_palabras
    
    return probabilidad

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En esta sección se muestra un ejemplo práctico del uso del modelo.
# - Se define un corpus de texto, se procesan las frecuencias de las palabras y se 
#   calculan las probabilidades de algunas palabras seleccionadas.
if __name__ == "__main__":
    # Definimos un corpus de ejemplo.
    corpus_ejemplo = """
    este es un ejemplo de un corpus de texto. este corpus contiene palabras repetidas
    como este, corpus y texto. este es un ejemplo sencillo.
    """
    
    # Procesamos el corpus para obtener las frecuencias de las palabras.
    frecuencias_palabras = procesar_corpus(corpus_ejemplo)
    
    # Calculamos el número total de palabras en el corpus.
    total_palabras = sum(frecuencias_palabras.values())
    
    # Mostramos las frecuencias de las palabras.
    print("Frecuencias de palabras en el corpus:")
    for palabra, frecuencia in frecuencias_palabras.items():
        print(f"{palabra}: {frecuencia}")
    
    # Calculamos la probabilidad de algunas palabras.
    palabras_a_calcular = ["este", "corpus", "ejemplo", "palabra"]
    print("\nProbabilidades de las palabras:")
    for palabra in palabras_a_calcular:
        probabilidad = calcular_probabilidad(palabra, frecuencias_palabras, total_palabras)
        print(f"Probabilidad de '{palabra}': {probabilidad:.4f}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este modelo probabilístico del lenguaje utiliza un enfoque basado en frecuencias.
#    La probabilidad de una palabra se calcula como:
#        P(palabra) = frecuencia(palabra) / total_palabras
# 2. Suposiciones clave:
#    - Todas las palabras son independientes entre sí (modelo de bolsa de palabras).
#    - Las palabras se procesan en minúsculas para evitar duplicados por mayúsculas.
# 3. Ventajas:
#    - Es simple y fácil de implementar.
#    - Útil para tareas básicas de procesamiento del lenguaje natural.
# 4. Limitaciones:
#    - No considera el contexto de las palabras (por ejemplo, "banco" como institución
#      financiera o como asiento).
#    - No maneja palabras desconocidas (frecuencia 0).