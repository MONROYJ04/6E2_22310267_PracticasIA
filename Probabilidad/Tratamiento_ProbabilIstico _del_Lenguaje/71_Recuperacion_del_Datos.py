# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RECUPERACIÓN DE DATOS PARA BÚSQUEDA DE INFORMACIÓN
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo básico de recuperación de datos. Su objetivo es 
# buscar y recuperar información relevante de un conjunto de datos basado en una consulta.
# Utiliza un enfoque simple para ilustrar cómo se pueden procesar y buscar datos.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `nltk` para el procesamiento de texto.
# - Usamos `Counter` para contar la frecuencia de palabras en los documentos.
from nltk.tokenize import word_tokenize  # Para dividir texto en palabras
from collections import Counter  # Para contar palabras

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LOS DOCUMENTOS Y LA CONSULTA
# ------------------------------------------------------------------------------------
# - Creamos una lista de documentos (cada documento es un texto).
# - Definimos una consulta que representa lo que el usuario desea buscar.
# - Los documentos y la consulta están en español.
documentos = [
    "El aprendizaje automático es una rama de la inteligencia artificial.",
    "La recuperación de datos es importante en el procesamiento de lenguaje natural.",
    "El procesamiento de texto incluye tareas como tokenización y análisis sintáctico."
]

consulta = "procesamiento de datos"  # Consulta del usuario

# ------------------------------------------------------------------------------------
# PASO 3: TOKENIZAR LOS DOCUMENTOS Y LA CONSULTA
# ------------------------------------------------------------------------------------
# - Dividimos los documentos y la consulta en palabras individuales (tokens).
# - Esto permite comparar palabras entre los documentos y la consulta.
# - Usamos `word_tokenize` para realizar la tokenización.
tokens_documentos = [word_tokenize(doc.lower()) for doc in documentos]  # Tokenizamos y convertimos a minúsculas
tokens_consulta = word_tokenize(consulta.lower())  # Tokenizamos la consulta y convertimos a minúsculas

# ------------------------------------------------------------------------------------
# PASO 4: CALCULAR LA RELEVANCIA DE LOS DOCUMENTOS
# ------------------------------------------------------------------------------------
# - Comparamos las palabras de la consulta con las palabras de cada documento.
# - Calculamos una puntuación de relevancia basada en la frecuencia de palabras comunes.
# - Usamos `Counter` para contar las palabras en cada documento.
relevancia = []
for tokens_doc in tokens_documentos:
    contador_doc = Counter(tokens_doc)  # Contamos las palabras en el documento
    puntuacion = sum(contador_doc[palabra] for palabra in tokens_consulta)  # Sumamos las frecuencias de palabras comunes
    relevancia.append(puntuacion)  # Guardamos la puntuación de relevancia

# ------------------------------------------------------------------------------------
# PASO 5: MOSTRAR LOS RESULTADOS ORDENADOS POR RELEVANCIA
# ------------------------------------------------------------------------------------
# - Ordenamos los documentos según su puntuación de relevancia (de mayor a menor).
# - Mostramos los documentos más relevantes primero.
resultados_ordenados = sorted(zip(relevancia, documentos), reverse=True, key=lambda x: x[0])

print("Resultados ordenados por relevancia:")
for puntuacion, doc in resultados_ordenados:
    print(f"Puntuación: {puntuacion} - Documento: {doc}")

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que la consulta es "inteligencia artificial".
# Podemos cambiar la variable `consulta` a "inteligencia artificial" y volver a ejecutar el código.
# Esto mostrará los documentos más relevantes para esa consulta específica.

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Tokenización**:
#    - Dividimos el texto en palabras individuales para facilitar la comparación.
#    - Esto es importante porque las búsquedas se realizan palabra por palabra.
# 2. **Cálculo de relevancia**:
#    - Comparamos las palabras de la consulta con las palabras de cada documento.
#    - La puntuación de relevancia se basa en cuántas palabras de la consulta aparecen en el documento.
# 3. **Ordenamiento**:
#    - Los documentos se ordenan según su relevancia, mostrando primero los más relevantes.
# 4. **Ventajas**:
#    - Es un enfoque simple y fácil de entender.
#    - Útil para conjuntos de datos pequeños y consultas básicas.
# 5. **Limitaciones**:
#    - No considera sinónimos ni el significado de las palabras.
#    - No es adecuado para grandes volúmenes de datos o búsquedas complejas.