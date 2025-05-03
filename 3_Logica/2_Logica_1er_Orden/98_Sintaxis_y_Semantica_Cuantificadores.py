# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SINTAXIS Y SEMÁNTICA DE CUANTIFICADORES EN LÓGICA DE PRIMER ORDEN
# ------------------------------------------------------------------------------------
# Este programa tiene como objetivo explicar el uso de cuantificadores en lógica de primer orden.
# Los cuantificadores permiten expresar propiedades sobre conjuntos de elementos, como "para todo"
# o "existe al menos uno". Este código utiliza la librería `sympy` para construir expresiones lógicas.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `symbols` para definir variables simbólicas.
# - Importamos `ForAll` y `Exists` para trabajar con cuantificadores universales y existenciales.
# - También importamos operadores lógicos como `And`, `Or`, `Not`, `Implies` para construir expresiones.
from sympy import symbols, And, Or, Not, Implies, Exists, ForAll

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR VARIABLES SIMBÓLICAS
# ------------------------------------------------------------------------------------
# - Creamos variables simbólicas que representan elementos genéricos de un dominio.
# - Estas variables se usarán en las expresiones lógicas.
x = symbols('x')  # Variable simbólica genérica
y = symbols('y')  # Otra variable simbólica para ejemplos adicionales

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR UNA PROPIEDAD LÓGICA
# ------------------------------------------------------------------------------------
# - Creamos una función que representa una propiedad lógica.
# - En este caso, la propiedad es "x es mayor que 0".
# - Esta función será utilizada en los ejemplos con cuantificadores.
def propiedad(x):
    return x > 0  # Retorna True si x es mayor que 0

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO DE CUANTIFICADOR UNIVERSAL
# ------------------------------------------------------------------------------------
# - Construimos una expresión lógica que representa "Para todo x, x es mayor que 0".
# - Usamos el cuantificador universal `ForAll`.
# - Mostramos la expresión lógica resultante.
def ejemplo_cuantificador_universal():
    # Usamos el cuantificador universal (ForAll)
    expresion = ForAll(x, propiedad(x))
    # Mostramos la expresión lógica
    print("Cuantificador Universal:")
    print(expresion)
    # Nota: No evaluamos la verdad de la expresión, solo la construimos.

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO DE CUANTIFICADOR EXISTENCIAL
# ------------------------------------------------------------------------------------
# - Construimos una expresión lógica que representa "Existe al menos un x tal que x es mayor que 0".
# - Usamos el cuantificador existencial `Exists`.
# - Mostramos la expresión lógica resultante.
def ejemplo_cuantificador_existencial():
    # Usamos el cuantificador existencial (Exists)
    expresion = Exists(x, propiedad(x))
    # Mostramos la expresión lógica
    print("Cuantificador Existencial:")
    print(expresion)
    # Nota: Tampoco evaluamos la verdad de la expresión, solo la construimos.

# ------------------------------------------------------------------------------------
# PASO 6: LLAMAR A LOS EJEMPLOS DE CUANTIFICADORES
# ------------------------------------------------------------------------------------
# - Llamamos a las funciones que muestran cómo funcionan los cuantificadores.
# - Esto permite observar las expresiones lógicas construidas.
ejemplo_cuantificador_universal()
ejemplo_cuantificador_existencial()

# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO ADICIONAL CON CONDICIONALES
# ------------------------------------------------------------------------------------
# - Construimos una expresión lógica que representa:
#   "Para todo x, si x es mayor que 0, entonces x es positivo".
# - Usamos el operador lógico `Implies` para expresar la implicación.
# - Mostramos la expresión lógica resultante.
def ejemplo_condicional():
    # Construimos la expresión lógica
    expresion = ForAll(x, Implies(x > 0, x > -1))
    # Mostramos la expresión lógica
    print("Ejemplo con Condicional:")
    print(expresion)

# Llamamos al ejemplo adicional
ejemplo_condicional()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este programa utiliza cuantificadores para construir expresiones lógicas en lógica de primer orden.
# 2. Los cuantificadores universales (`ForAll`) expresan que una propiedad se cumple para todos los elementos.
# 3. Los cuantificadores existenciales (`Exists`) expresan que una propiedad se cumple para al menos un elemento.
# 4. Las expresiones lógicas no se evalúan directamente en este programa, solo se construyen y se muestran.
# 5. Este enfoque es útil para representar formalmente ideas matemáticas o lógicas.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que queremos representar la siguiente idea:
# "Para todo número entero x, si x es mayor que 0, entonces x es positivo".
# Este programa construye la expresión lógica correspondiente y la muestra en pantalla.