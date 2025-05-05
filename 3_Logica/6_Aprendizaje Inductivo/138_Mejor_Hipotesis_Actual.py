# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MEJOR HIPÓTESIS ACTUAL PARA APRENDIZAJE INDUCTIVO
# ------------------------------------------------------------------------------------
# Este código implementa el enfoque de "Mejor Hipótesis Actual" en aprendizaje inductivo.
# Su objetivo es encontrar una hipótesis general que sea consistente con un conjunto de 
# ejemplos positivos y negativos, utilizando atributos de los ejemplos positivos.

# ------------------------------------------------------------------------------------
# PASO 1: INICIALIZAR LA HIPÓTESIS MÁS GENERAL POSIBLE
# ------------------------------------------------------------------------------------
# - Aquí se define una función para crear la hipótesis inicial.
# - La hipótesis inicial es la más general posible, representada por una lista de '?'.
# - Esto es importante porque al inicio no tenemos información específica sobre los datos.
def inicializar_hipotesis(num_atributos):
    # Creamos una lista con '?' para cada atributo.
    return ['?'] * num_atributos

# ------------------------------------------------------------------------------------
# PASO 2: ACTUALIZAR LA HIPÓTESIS CON EJEMPLOS POSITIVOS
# ------------------------------------------------------------------------------------
# - Esta función actualiza la hipótesis actual basándose en un ejemplo positivo.
# - Si el valor del atributo en la hipótesis es '?', se reemplaza por el valor del ejemplo.
# - Si hay un conflicto entre la hipótesis y el ejemplo, el atributo se marca como '?'.
# - Esto asegura que la hipótesis sea consistente con todos los ejemplos positivos.
def actualizar_hipotesis(hipotesis, ejemplo):
    for i in range(len(hipotesis)):  # Iteramos sobre los atributos de la hipótesis y el ejemplo.
        if hipotesis[i] == '?':  # Si el atributo es general ('?'), lo actualizamos.
            hipotesis[i] = ejemplo[i]
        elif hipotesis[i] != ejemplo[i]:  # Si hay un conflicto, lo marcamos como general ('?').
            hipotesis[i] = '?'
    return hipotesis

# ------------------------------------------------------------------------------------
# PASO 3: ENCONTRAR LA MEJOR HIPÓTESIS ACTUAL
# ------------------------------------------------------------------------------------
# - Esta función principal encuentra la mejor hipótesis actual basada en los ejemplos.
# - Solo utiliza ejemplos positivos para actualizar la hipótesis.
# - Los ejemplos negativos no afectan la hipótesis, ya que no contribuyen a su generalización.
def mejor_hipotesis_actual(ejemplos, etiquetas):
    """
    ejemplos: Lista de ejemplos, donde cada ejemplo es una lista de atributos.
    etiquetas: Lista de etiquetas asociadas a los ejemplos (1 para positivo, 0 para negativo).
    """
    # Inicializamos la hipótesis más general posible.
    num_atributos = len(ejemplos[0])  # Número de atributos en los ejemplos.
    hipotesis = inicializar_hipotesis(num_atributos)

    # Iteramos sobre los ejemplos y sus etiquetas.
    for i in range(len(ejemplos)):
        if etiquetas[i] == 1:  # Solo actualizamos la hipótesis con ejemplos positivos.
            hipotesis = actualizar_hipotesis(hipotesis, ejemplos[i])

    return hipotesis

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Aquí se proporciona un ejemplo práctico para demostrar cómo funciona el algoritmo.
# - Los ejemplos tienen atributos como color, forma y tamaño.
# - Las etiquetas indican si un ejemplo es positivo (1) o negativo (0).
if __name__ == "__main__":
    # Conjunto de ejemplos (atributos: [color, forma, tamaño]).
    ejemplos = [
        ['rojo', 'redondo', 'grande'],  # Ejemplo positivo.
        ['rojo', 'ovalado', 'grande'],  # Ejemplo positivo.
        ['rojo', 'redondo', 'pequeño'],  # Ejemplo positivo.
        ['azul', 'redondo', 'grande']   # Ejemplo negativo.
    ]

    # Etiquetas asociadas a los ejemplos (1: positivo, 0: negativo).
    etiquetas = [1, 1, 1, 0]

    # Llamamos a la función para encontrar la mejor hipótesis actual.
    mejor_hipotesis = mejor_hipotesis_actual(ejemplos, etiquetas)

    # Mostramos la hipótesis resultante.
    print("La mejor hipótesis actual es:", mejor_hipotesis)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo comienza con la hipótesis más general posible: ['?', '?', '?'].
# 2. A medida que se procesan los ejemplos positivos, la hipótesis se ajusta para ser 
#    consistente con ellos. Esto se hace comparando cada atributo y actualizándolo.
# 3. Los ejemplos negativos no afectan la hipótesis, ya que no contribuyen a su generalización.
# 4. Al final, la hipótesis representa la generalización más específica que cubre todos 
#    los ejemplos positivos.

# SUPOSICIONES CLAVE:
# - Los ejemplos están correctamente etiquetados como positivos o negativos.
# - Los atributos son comparables y pueden ser generalizados con '?'.

# VENTAJAS:
# - Simple de implementar y entender.
# - Genera una hipótesis general consistente con los datos positivos.

# LIMITACIONES:
# - No maneja ruido en los datos (ejemplos mal etiquetados).
# - No considera relaciones complejas entre atributos.

# EJEMPLO PRÁCTICO:
# Entrada:
#   ejemplos = [['rojo', 'redondo', 'grande'], ['rojo', 'ovalado', 'grande'], ...]
#   etiquetas = [1, 1, 1, 0]
# Salida:
#   La mejor hipótesis actual es: ['rojo', '?', '?']