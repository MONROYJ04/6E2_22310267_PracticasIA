# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE UNIFICACIÓN PARA INFERENCIA LÓGICA
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de unificación que busca encontrar una sustitución
# que haga que dos expresiones lógicas sean equivalentes. Es una técnica fundamental en
# sistemas de inferencia lógica y programación lógica, como Prolog.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL DE UNIFICACIÓN
# ------------------------------------------------------------------------------------
# - La función `unificar` es el núcleo del algoritmo. Intenta unificar dos expresiones
#   lógicas (pueden ser constantes, variables o listas).
# - Si las expresiones son unificables, devuelve un diccionario con las sustituciones
#   necesarias. Si no, devuelve `None`.
# - Parámetros clave:
#   - `expresion1` y `expresion2`: Las expresiones lógicas a unificar.
#   - `sustituciones`: Diccionario que almacena las sustituciones realizadas hasta el momento.

def unificar(expresion1, expresion2, sustituciones=None):
    """
    Funcion que intenta unificar dos expresiones logicas.
    
    Parametros:
    - expresion1: La primera expresion logica (puede ser una constante, variable o lista).
    - expresion2: La segunda expresion logica (puede ser una constante, variable o lista).
    - sustituciones: Un diccionario que almacena las sustituciones realizadas.

    Retorna:
    - Un diccionario con las sustituciones necesarias para unificar las expresiones,
      o None si no es posible unificarlas.
    """
    # ------------------------------------------------------------------------------------
    # PASO 2: INICIALIZACIÓN DE LAS SUSTITUCIONES
    # ------------------------------------------------------------------------------------
    # - Si no se proporciona un diccionario de sustituciones, se inicializa como vacío.
    # - Esto asegura que siempre tengamos un lugar donde almacenar las sustituciones.
    if sustituciones is None:
        sustituciones = {}

    # ------------------------------------------------------------------------------------
    # PASO 3: CASO BASE - LAS EXPRESIONES SON IGUALES
    # ------------------------------------------------------------------------------------
    # - Si las expresiones son idénticas, no se necesita ninguna sustitución.
    # - Este es el caso más simple y sirve como base para el algoritmo.
    if expresion1 == expresion2:
        return sustituciones

    # ------------------------------------------------------------------------------------
    # PASO 4: CASO - LA PRIMERA EXPRESIÓN ES UNA VARIABLE
    # ------------------------------------------------------------------------------------
    # - Si `expresion1` es una variable, intentamos unificarla con `expresion2`.
    # - Esto se delega a la función `unificar_variable`.
    if es_variable(expresion1):
        return unificar_variable(expresion1, expresion2, sustituciones)

    # ------------------------------------------------------------------------------------
    # PASO 5: CASO - LA SEGUNDA EXPRESIÓN ES UNA VARIABLE
    # ------------------------------------------------------------------------------------
    # - Similar al caso anterior, pero ahora la variable es `expresion2`.
    if es_variable(expresion2):
        return unificar_variable(expresion2, expresion1, sustituciones)

    # ------------------------------------------------------------------------------------
    # PASO 6: CASO - AMBAS EXPRESIONES SON LISTAS
    # ------------------------------------------------------------------------------------
    # - Si ambas expresiones son listas (por ejemplo, funciones o predicados),
    #   intentamos unificar cada elemento de las listas.
    # - Primero verificamos que las listas tengan la misma longitud.
    # - Luego, unificamos elemento por elemento usando recursión.
    if isinstance(expresion1, list) and isinstance(expresion2, list):
        if len(expresion1) != len(expresion2):
            return None
        for sub1, sub2 in zip(expresion1, expresion2):
            sustituciones = unificar(sub1, sub2, sustituciones)
            if sustituciones is None:
                return None
        return sustituciones

    # ------------------------------------------------------------------------------------
    # PASO 7: CASO - NO SE PUEDEN UNIFICAR
    # ------------------------------------------------------------------------------------
    # - Si no se cumple ninguno de los casos anteriores, las expresiones no son unificables.
    return None

# ------------------------------------------------------------------------------------
# PASO 8: FUNCIÓN AUXILIAR - VERIFICAR SI UNA EXPRESIÓN ES UNA VARIABLE
# ------------------------------------------------------------------------------------
# - Una variable se define como un string que comienza con una letra minúscula.
# - Esto es una convención común en lógica de primer orden.
def es_variable(expresion):
    """
    Verifica si una expresion es una variable.
    En este caso, consideramos que una variable es un string que comienza con una letra minuscula.
    """
    return isinstance(expresion, str) and expresion[0].islower()

# ------------------------------------------------------------------------------------
# PASO 9: FUNCIÓN AUXILIAR - UNIFICAR UNA VARIABLE CON UN VALOR
# ------------------------------------------------------------------------------------
# - Esta función intenta unificar una variable con un valor.
# - Si la variable ya tiene una sustitución, intenta unificar con ese valor.
# - Si el valor ya tiene una sustitución, intenta unificar con ese valor.
# - Si la variable ocurre dentro del valor, no se puede unificar (para evitar ciclos).
def unificar_variable(variable, valor, sustituciones):
    """
    Intenta unificar una variable con un valor.
    
    Parametros:
    - variable: La variable a unificar.
    - valor: El valor con el que se intenta unificar la variable.
    - sustituciones: El diccionario de sustituciones.

    Retorna:
    - Un diccionario actualizado con las nuevas sustituciones, o None si no es posible unificar.
    """
    if variable in sustituciones:
        return unificar(sustituciones[variable], valor, sustituciones)
    elif valor in sustituciones:
        return unificar(variable, sustituciones[valor], sustituciones)
    elif ocurre(variable, valor):
        return None
    else:
        sustituciones[variable] = valor
        return sustituciones

# ------------------------------------------------------------------------------------
# PASO 10: FUNCIÓN AUXILIAR - VERIFICAR SI UNA VARIABLE OCURRE EN UN VALOR
# ------------------------------------------------------------------------------------
# - Esta función verifica si una variable ocurre dentro de un valor.
# - Es importante para evitar ciclos en las sustituciones.
def ocurre(variable, valor):
    """
    Verifica si una variable ocurre dentro de un valor.
    Esto es necesario para evitar ciclos en las sustituciones.
    """
    if variable == valor:
        return True
    elif isinstance(valor, list):
        return any(ocurre(variable, subvalor) for subvalor in valor)
    return False

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, intentamos unificar dos expresiones lógicas:
#   - `expresion1 = ["f", "x", ["g", "y"]]`
#   - `expresion2 = ["f", "a", ["g", "b"]]`
# - El objetivo es encontrar las sustituciones necesarias para que ambas expresiones sean iguales.

if __name__ == "__main__":
    expresion1 = ["f", "x", ["g", "y"]]
    expresion2 = ["f", "a", ["g", "b"]]

    # Intentamos unificar las expresiones
    resultado = unificar(expresion1, expresion2)

    # Mostramos el resultado
    if resultado is not None:
        print("Las expresiones se pueden unificar.")
        print("Sustituciones:", resultado)
    else:
        print("Las expresiones no se pueden unificar.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza recursión para descomponer las expresiones lógicas en sus partes.
# 2. Las variables se manejan mediante un diccionario de sustituciones.
# 3. Se evita la creación de ciclos mediante la función `ocurre`.
# 4. Ventajas: Es un enfoque general para unificación en lógica de primer orden.
# 5. Limitaciones: No maneja casos más complejos como lógica de orden superior.