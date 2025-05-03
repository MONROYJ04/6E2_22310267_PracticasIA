# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: GENERACIÓN DE TABLAS DE VERDAD PARA PROPOSICIONES LÓGICAS
# ------------------------------------------------------------------------------------
# Este programa genera una tabla de verdad para una proposición lógica.
# Una tabla de verdad muestra todas las combinaciones posibles de valores de verdad 
# (True o False) para las variables de una proposición lógica y evalúa el resultado 
# de la proposición para cada combinación.

from itertools import product  # Importamos product para generar combinaciones de valores True y False.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PARA GENERAR LA TABLA DE VERDAD
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada una lista de variables proposicionales y una 
#   expresión lógica en forma de cadena.
# - Genera todas las combinaciones posibles de valores de verdad para las variables 
#   y evalúa la expresión lógica para cada combinación.
# - Finalmente, imprime la tabla de verdad con los resultados.

def generar_tabla_verdad(variables, expresion):
    """
    Genera una tabla de verdad para una expresion logica.

    :param variables: Lista de variables proposicionales (ejemplo: ['p', 'q']).
    :param expresion: Expresion logica como cadena (ejemplo: '(p and q) or not p').
    :return: Imprime la tabla de verdad en consola.
    """
    # --------------------------------------------------------------------------------
    # PASO 2: GENERACIÓN DE TODAS LAS COMBINACIONES POSIBLES
    # --------------------------------------------------------------------------------
    # - Usamos la función `product` del módulo `itertools` para generar todas las 
    #   combinaciones posibles de valores True y False para las variables.
    # - Si hay 2 variables, se generan 2^2 = 4 combinaciones: 
    #   (False, False), (False, True), (True, False), (True, True).
    combinaciones = list(product([False, True], repeat=len(variables)))

    # --------------------------------------------------------------------------------
    # PASO 3: IMPRESIÓN DE LOS ENCABEZADOS DE LA TABLA
    # --------------------------------------------------------------------------------
    # - Imprimimos los nombres de las variables como encabezados de la tabla.
    # - Añadimos una columna adicional llamada "Resultado" para mostrar el resultado 
    #   de evaluar la expresión lógica.
    print("Tabla de Verdad")
    print(" | ".join(variables) + " | Resultado")
    print("-" * (len(variables) * 4 + 12))

    # --------------------------------------------------------------------------------
    # PASO 4: EVALUACIÓN DE LA EXPRESIÓN LÓGICA PARA CADA COMBINACIÓN
    # --------------------------------------------------------------------------------
    # - Iteramos sobre cada combinación de valores de verdad.
    # - Creamos un diccionario que asigna cada variable a su valor correspondiente 
    #   en la combinación actual.
    # - Usamos la función `eval` para evaluar la expresión lógica con los valores 
    #   actuales de las variables.
    # - Imprimimos los valores de las variables y el resultado de la evaluación.
    for combinacion in combinaciones:
        # Creamos un diccionario que asigna valores a las variables.
        valores = dict(zip(variables, combinacion))

        # Evaluamos la expresion usando los valores actuales.
        # Usamos eval para evaluar la expresion como codigo Python.
        resultado = eval(expresion, {}, valores)

        # Imprimimos la fila de la tabla con los valores y el resultado.
        valores_str = " | ".join(str(valores[var]) for var in variables)
        print(f"{valores_str} | {resultado}")

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, definimos dos variables proposicionales: `p` y `q`.
# - La expresión lógica es "(p and q) or not p", que significa "(p Y q) O NO p".
# - El programa generará una tabla de verdad para esta expresión lógica.
if __name__ == "__main__":
    # Definimos las variables proposicionales.
    variables = ['p', 'q']

    # Definimos la expresion logica.
    # Ejemplo: "(p and q) or not p" significa "(p Y q) O NO p".
    expresion = "(p and q) or not p"

    # Llamamos a la función para generar la tabla de verdad.
    generar_tabla_verdad(variables, expresion)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza combinaciones de valores de verdad (True y False) para 
#    evaluar una expresión lógica en todas las posibilidades.
# 2. La función `product` genera las combinaciones de valores de verdad, mientras que 
#    `eval` evalúa la expresión lógica como si fuera código Python.
# 3. Ventajas:
#    - Permite evaluar cualquier expresión lógica válida en Python.
#    - Es flexible y puede manejar cualquier número de variables proposicionales.
# 4. Limitaciones:
#    - Usar `eval` puede ser peligroso si se evalúan expresiones no controladas.
#    - El número de combinaciones crece exponencialmente con el número de variables 
#      (2^n combinaciones para n variables).