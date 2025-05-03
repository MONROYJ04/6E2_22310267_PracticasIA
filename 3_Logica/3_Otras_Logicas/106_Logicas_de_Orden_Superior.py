# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FUNCIONES DE ORDEN SUPERIOR PARA OPERACIONES EN LISTAS
# ------------------------------------------------------------------------------------
# Este código demuestra cómo usar funciones de orden superior en Python. Estas funciones
# permiten recibir otras funciones como argumentos para realizar operaciones genéricas
# sobre listas de datos. Se incluyen ejemplos prácticos para elevar números al cuadrado
# y verificar si son pares.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINIR UNA FUNCIÓN DE ORDEN SUPERIOR
# ------------------------------------------------------------------------------------
# - Aquí se define la función `aplicar_funcion`, que es una función de orden superior.
# - Esta función toma dos parámetros:
#   1. `funcion`: Una función que se aplicará a cada elemento de la lista.
#   2. `lista`: Una lista de elementos sobre los que se aplicará la función.
# - Devuelve una nueva lista con los resultados de aplicar la función a cada elemento.
# - Es importante porque permite abstraer operaciones repetitivas y reutilizar código.

def aplicar_funcion(funcion, lista):
    """
    Aplica una función dada a cada elemento de una lista y devuelve una nueva lista.
    
    :param funcion: Una función que se aplicará a cada elemento de la lista.
    :param lista: Una lista de elementos a los que se les aplicará la función.
    :return: Una nueva lista con los resultados de aplicar la función.
    """
    # Usamos una comprensión de lista para aplicar la función a cada elemento
    return [funcion(elemento) for elemento in lista]

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR FUNCIONES AUXILIARES
# ------------------------------------------------------------------------------------
# - Estas funciones son ejemplos de operaciones que se pueden aplicar a los elementos
#   de una lista usando la función de orden superior `aplicar_funcion`.

# Función auxiliar 1: Elevar un número al cuadrado
# - Toma un número como entrada y devuelve su cuadrado.
# - Es útil para realizar cálculos matemáticos simples.
def al_cuadrado(numero):
    """
    Calcula el cuadrado de un número.
    
    :param numero: Un número que se desea elevar al cuadrado.
    :return: El cuadrado del número.
    """
    return numero ** 2

# Función auxiliar 2: Verificar si un número es par
# - Toma un número como entrada y devuelve `True` si es par, o `False` si es impar.
# - Es útil para filtrar o clasificar números.
def es_par(numero):
    """
    Verifica si un número es par.
    
    :param numero: Un número que se desea verificar.
    :return: True si el número es par, False en caso contrario.
    """
    return numero % 2 == 0

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLOS PRÁCTICOS
# ------------------------------------------------------------------------------------
# - En esta sección, se demuestra cómo usar la función de orden superior `aplicar_funcion`
#   con las funciones auxiliares definidas anteriormente.
# - Se utiliza una lista de números como entrada para los ejemplos.

# Lista de números de ejemplo
# - Esta lista contiene números enteros del 1 al 6.
numeros = [1, 2, 3, 4, 5, 6]

# Aplicar la función `al_cuadrado` a cada número de la lista
# - Se calcula el cuadrado de cada número en la lista `numeros`.
resultado_cuadrados = aplicar_funcion(al_cuadrado, numeros)
print("Cuadrados de los números:", resultado_cuadrados)

# Aplicar la función `es_par` a cada número de la lista
# - Se verifica si cada número en la lista `numeros` es par.
resultado_pares = aplicar_funcion(es_par, numeros)
print("¿Son pares los números?:", resultado_pares)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza funciones de orden superior para aplicar operaciones genéricas
#    a listas de datos. La función `aplicar_funcion` abstrae el proceso de iterar sobre
#    una lista y aplicar una operación a cada elemento.
# 2. Suposiciones clave:
#    - La función pasada como argumento (`funcion`) debe aceptar un único parámetro.
#    - La lista de entrada (`lista`) debe ser iterable.
# 3. Ventajas:
#    - Reutilización de código: La lógica de iteración está centralizada en `aplicar_funcion`.
#    - Flexibilidad: Se pueden usar diferentes funciones para realizar diversas operaciones.
# 4. Limitaciones:
#    - Solo funciona con funciones que acepten un único argumento.
#    - No maneja errores si la lista contiene elementos incompatibles con la función.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO ADICIONAL
# ------------------------------------------------------------------------------------
# Supongamos que queremos calcular el triple de cada número en una lista.

# Definir una nueva función auxiliar para calcular el triple de un número
def al_triple(numero):
    """
    Calcula el triple de un número.
    
    :param numero: Un número que se desea triplicar.
    :return: El triple del número.
    """
    return numero * 3

# Aplicar la función `al_triple` a la lista de números
resultado_triples = aplicar_funcion(al_triple, numeros)
print("Triples de los números:", resultado_triples)

# ------------------------------------------------------------------------------------
# SALIDA ESPERADA
# ------------------------------------------------------------------------------------
# Cuadrados de los números: [1, 4, 9, 16, 25, 36]
# ¿Son pares los números?: [False, True, False, True, False, True]
# Triples de los números: [3, 6, 9, 12, 15, 18]