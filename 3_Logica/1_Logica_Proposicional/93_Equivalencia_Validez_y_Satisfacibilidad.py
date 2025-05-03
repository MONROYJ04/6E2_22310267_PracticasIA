# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO PARA EXPLICAR EQUIVALENCIA, VALIDEZ Y SATISFACIBILIDAD
# ------------------------------------------------------------------------------------
# Este código utiliza lógica proposicional para explicar tres conceptos fundamentales:
# equivalencia lógica, validez lógica y satisfacibilidad lógica. Se emplean ejemplos
# prácticos para ilustrar cada concepto y se utiliza la biblioteca `sympy` para realizar
# las operaciones lógicas.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE LA BIBLIOTECA NECESARIA
# ------------------------------------------------------------------------------------
# - Importamos `sympy`, una biblioteca que permite trabajar con lógica proposicional.
# - Incluye funciones como `And`, `Or`, `Not`, `Equivalent` y `satisfiable` para
#   realizar operaciones lógicas y verificar propiedades.
from sympy import symbols, Or, And, Not, Implies, Equivalent, satisfiable

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DEL ALGORITMO PRINCIPAL
# ------------------------------------------------------------------------------------
# - Creamos una función llamada `explicar_logica_proposicional` que contiene los pasos
#   para explicar los conceptos de equivalencia, validez y satisfacibilidad.
# - Cada concepto se explica con un ejemplo práctico.

def explicar_logica_proposicional():
    """
    Este algoritmo explica los conceptos de equivalencia, validez y satisfacibilidad
    en lógica proposicional utilizando ejemplos prácticos.
    """

    # --------------------------------------------------------------------------------
    # PASO 3: DEFINICIÓN DE VARIABLES PROPOSICIONALES
    # --------------------------------------------------------------------------------
    # - Definimos las variables `p` y `q` como símbolos proposicionales.
    # - Estas variables representan proposiciones lógicas que pueden ser verdaderas o falsas.
    p = symbols('p')  # Representa una proposición cualquiera
    q = symbols('q')  # Representa otra proposición

    # --------------------------------------------------------------------------------
    # PASO 4: EJEMPLO DE EQUIVALENCIA LÓGICA
    # --------------------------------------------------------------------------------
    # - Dos proposiciones son equivalentes si tienen el mismo valor de verdad en todos
    #   los casos posibles.
    # - Aquí comparamos `p ∧ q` con `¬(¬p ∨ ¬q)` para verificar si son equivalentes.
    proposicion1 = And(p, q)  # p ∧ q
    proposicion2 = Not(Or(Not(p), Not(q)))  # ¬(¬p ∨ ¬q)
    equivalencia = Equivalent(proposicion1, proposicion2)  # Verificamos si son equivalentes
    print("Equivalencia lógica:")
    print(f"¿Son equivalentes p ∧ q y ¬(¬p ∨ ¬q)? {equivalencia}")

    # --------------------------------------------------------------------------------
    # PASO 5: EJEMPLO DE VALIDEZ LÓGICA
    # --------------------------------------------------------------------------------
    # - Una proposición es válida si es verdadera en todos los casos posibles.
    # - Aquí verificamos si `p ∨ ¬p` (la Ley del Tercero Excluido) es válida.
    proposicion_valida = Or(p, Not(p))  # p ∨ ¬p
    print("\nValidez lógica:")
    print(f"¿Es válida la proposición p ∨ ¬p? {proposicion_valida}")

    # --------------------------------------------------------------------------------
    # PASO 6: EJEMPLO DE SATISFACIBILIDAD LÓGICA
    # --------------------------------------------------------------------------------
    # - Una proposición es satisfacible si existe al menos un caso en el que sea verdadera.
    # - Aquí verificamos si `p ∧ ¬q` es satisfacible y buscamos un modelo que lo cumpla.
    proposicion_satisfacible = And(p, Not(q))  # p ∧ ¬q
    modelo = satisfiable(proposicion_satisfacible)  # Buscamos un modelo que satisfaga la proposición
    print("\nSatisfacibilidad lógica:")
    print(f"¿Es satisfacible la proposición p ∧ ¬q? {modelo}")

# ------------------------------------------------------------------------------------
# PASO 7: LLAMADA AL ALGORITMO
# ------------------------------------------------------------------------------------
# - Llamamos a la función `explicar_logica_proposicional` para ejecutar el algoritmo
#   y mostrar los resultados de los ejemplos prácticos.
explicar_logica_proposicional()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Equivalencia lógica**:
#    - Dos proposiciones son equivalentes si tienen el mismo valor de verdad en todos
#      los casos posibles.
#    - Ejemplo: `p ∧ q` es equivalente a `¬(¬p ∨ ¬q)` porque ambas expresiones tienen
#      el mismo resultado en cualquier combinación de valores de verdad para `p` y `q`.
#
# 2. **Validez lógica**:
#    - Una proposición es válida si es verdadera en todos los casos posibles.
#    - Ejemplo: `p ∨ ¬p` (Ley del Tercero Excluido) es válida porque siempre es verdadera,
#      independientemente del valor de `p`.
#
# 3. **Satisfacibilidad lógica**:
#    - Una proposición es satisfacible si existe al menos un caso en el que sea verdadera.
#    - Ejemplo: `p ∧ ¬q` es satisfacible cuando `p` es verdadero y `q` es falso.
#
# **Ventajas del algoritmo**:
# - Permite entender conceptos fundamentales de lógica proposicional de manera práctica.
# - Utiliza ejemplos simples y claros para ilustrar cada concepto.
#
# **Limitaciones**:
# - Solo cubre ejemplos básicos; no incluye proposiciones más complejas o múltiples variables.