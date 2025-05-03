# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: TRADUCCIÓN AUTOMÁTICA ESTADÍSTICA PARA ORACIONES
# ------------------------------------------------------------------------------------
# Este programa implementa un ejemplo básico de Traducción Automática Estadística.
# Utiliza un modelo probabilístico para traducir palabras de un idioma a otro.
# El objetivo es traducir una oración en español al inglés, seleccionando la traducción
# más probable para cada palabra según un diccionario predefinido.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINIR EL DICCIONARIO DE TRADUCCIÓN
# ------------------------------------------------------------------------------------
# - Este diccionario contiene las palabras en español como claves.
# - Cada clave tiene un valor que es otro diccionario con las posibles traducciones
#   al inglés y sus probabilidades asociadas.
# - Las probabilidades indican qué tan probable es cada traducción.
diccionario_traduccion = {
    "gato": {"cat": 0.8, "kitten": 0.2},  # "gato" puede traducirse como "cat" (80%) o "kitten" (20%).
    "perro": {"dog": 0.9, "puppy": 0.1},  # "perro" puede traducirse como "dog" (90%) o "puppy" (10%).
    "casa": {"house": 0.7, "home": 0.3},  # "casa" puede traducirse como "house" (70%) o "home" (30%).
    "comer": {"eat": 0.6, "dine": 0.4}    # "comer" puede traducirse como "eat" (60%) o "dine" (40%).
}

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PARA TRADUCIR UNA PALABRA
# ------------------------------------------------------------------------------------
# - Esta función toma una palabra en español como entrada.
# - Busca la palabra en el diccionario de traducción.
# - Si la palabra está en el diccionario, selecciona la traducción con la mayor probabilidad.
# - Si la palabra no está en el diccionario, devuelve un mensaje indicando que no hay traducción.
def traducir_palabra(palabra):
    """
    Traduce una palabra del idioma de origen al idioma de destino
    utilizando un modelo probabilístico.

    :param palabra: Palabra en el idioma de origen (string).
    :return: Traducción más probable (string).
    """
    # Verificar si la palabra existe en el diccionario
    if palabra in diccionario_traduccion:
        # Obtener las posibles traducciones y sus probabilidades
        traducciones = diccionario_traduccion[palabra]
        # Seleccionar la traducción con la mayor probabilidad
        traduccion_mas_probable = max(traducciones, key=traducciones.get)
        return traduccion_mas_probable
    else:
        # Si la palabra no está en el diccionario, devolver un mensaje de error
        return "Traducción no disponible"

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN PARA TRADUCIR UNA ORACIÓN COMPLETA
# ------------------------------------------------------------------------------------
# - Esta función toma una oración en español como entrada.
# - Divide la oración en palabras individuales.
# - Traduce cada palabra utilizando la función `traducir_palabra`.
# - Une las palabras traducidas para formar la oración traducida.
def traducir_oracion(oracion):
    """
    Traduce una oración palabra por palabra utilizando el modelo probabilístico.

    :param oracion: Oración en el idioma de origen (string).
    :return: Oración traducida (string).
    """
    # Dividir la oración en palabras
    palabras = oracion.split()
    # Traducir cada palabra y unirlas en una nueva oración
    oracion_traducida = [traducir_palabra(palabra) for palabra in palabras]
    return " ".join(oracion_traducida)

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, traducimos una oración en español al inglés.
# - La oración original es "gato perro casa comer".
# - El programa utiliza el modelo probabilístico para traducir cada palabra.
# - Finalmente, muestra la oración original y la traducida.

# Oración en español que queremos traducir
oracion_original = "gato perro casa comer"

# Traducir la oración
oracion_traducida = traducir_oracion(oracion_original)

# Mostrar los resultados
print("Oración original:", oracion_original)  # Muestra la oración en español.
print("Oración traducida:", oracion_traducida)  # Muestra la traducción al inglés.

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza un modelo probabilístico basado en un diccionario predefinido.
# 2. Cada palabra en español tiene una o más traducciones posibles al inglés, con probabilidades asociadas.
# 3. La función `traducir_palabra` selecciona la traducción con la mayor probabilidad.
# 4. La función `traducir_oracion` aplica esta lógica a cada palabra de una oración.
# 5. Suposiciones clave:
#    - Todas las palabras de la oración están separadas por espacios.
#    - Las palabras deben estar en el diccionario para ser traducidas.
# 6. Ventajas:
#    - Fácil de implementar y entender.
#    - Útil para traducciones simples con un vocabulario limitado.
# 7. Limitaciones:
#    - No maneja palabras fuera del diccionario.
#    - No considera el contexto de las palabras en la oración.

# ------------------------------------------------------------------------------------
# EJEMPLO DE SALIDA
# ------------------------------------------------------------------------------------
# Si ejecutamos este código, la salida será:
# Oración original: gato perro casa comer
# Oración traducida: cat dog house eat