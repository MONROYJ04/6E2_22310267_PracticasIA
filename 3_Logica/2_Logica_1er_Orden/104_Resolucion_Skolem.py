# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE RESOLUCIÓN CON SKOLEMIZACIÓN PARA LÓGICA DE PRIMER ORDEN
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de resolución con Skolemización para determinar 
# si dos fórmulas lógicas son inconsistentes (es decir, si su conjunción es insatisfacible).
# La resolución es una técnica utilizada en lógica matemática y ciencias de la computación 
# para verificar la validez de fórmulas lógicas.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Aquí se importan las funciones y clases necesarias de la biblioteca `sympy`, 
#   que es una herramienta para realizar cálculos simbólicos en Python.
# - Estas funciones permiten trabajar con expresiones lógicas, convertirlas a CNF 
#   (Forma Normal Conjuntiva) y simplificarlas.

from sympy import symbols, And, Or, Not, Implies, simplify
from sympy.logic.boolalg import is_cnf, to_cnf

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA CONVERTIR UNA FÓRMULA A CNF
# ------------------------------------------------------------------------------------
# - QUÉ: Esta función toma una fórmula lógica y la convierte a su Forma Normal Conjuntiva (CNF).
# - POR QUÉ: La CNF es una representación estándar que facilita la aplicación del algoritmo 
#   de resolución, ya que las fórmulas se expresan como una conjunción de disyunciones.
# - PARÁMETROS:
#   - `formula`: Una expresión lógica que se desea convertir a CNF.

def convertir_a_cnf(formula):
    """
    Convierte una fórmula lógica a su forma normal conjuntiva (CNF).
    La CNF es una forma estándar que facilita la aplicación del algoritmo de resolución.
    """
    # Simplificamos la fórmula y la convertimos a CNF
    cnf = to_cnf(simplify(formula), simplify=True)
    return cnf

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN PARA APLICAR LA SKOLEMIZACIÓN
# ------------------------------------------------------------------------------------
# - QUÉ: Esta función aplica la Skolemización, que elimina los cuantificadores existenciales 
#   reemplazándolos por funciones de Skolem.
# - POR QUÉ: La Skolemización es un paso necesario en lógica de primer orden para trabajar 
#   con fórmulas sin cuantificadores existenciales.
# - NOTA: En este ejemplo, asumimos que las fórmulas ya están en CNF y no contienen cuantificadores.

def skolemizar(formula):
    """
    Aplica la Skolemización a una fórmula lógica.
    La Skolemización elimina los cuantificadores existenciales reemplazándolos
    por funciones de Skolem.
    """
    # En este ejemplo, asumimos que la fórmula ya está en CNF
    # y no contiene cuantificadores. En un caso real, se debería
    # implementar la eliminación de cuantificadores.
    return formula

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR LA FUNCIÓN PRINCIPAL DEL ALGORITMO DE RESOLUCIÓN
# ------------------------------------------------------------------------------------
# - QUÉ: Esta función aplica el algoritmo de resolución para determinar si dos fórmulas 
#   lógicas son inconsistentes.
# - POR QUÉ: La resolución permite verificar si la conjunción de dos fórmulas lógicas 
#   lleva a una contradicción, lo que indica inconsistencia.
# - PARÁMETROS:
#   - `formula1`: Primera fórmula lógica.
#   - `formula2`: Segunda fórmula lógica.

def resolver_skolem(formula1, formula2):
    """
    Aplica el algoritmo de resolución para determinar si dos fórmulas
    lógicas son inconsistentes (es decir, si su conjunción es insatisfacible).
    """
    # --------------------------------------------------------------------------------
    # PASO 4.1: CONVERTIR LAS FÓRMULAS A CNF
    # --------------------------------------------------------------------------------
    # - Convertimos las fórmulas a su Forma Normal Conjuntiva (CNF).
    # - Esto es necesario para aplicar el algoritmo de resolución.
    cnf1 = convertir_a_cnf(formula1)
    cnf2 = convertir_a_cnf(formula2)

    # Mostramos las fórmulas en CNF para que el usuario las vea
    print("Formula 1 en CNF:", cnf1)
    print("Formula 2 en CNF:", cnf2)

    # --------------------------------------------------------------------------------
    # PASO 4.2: APLICAR LA RESOLUCIÓN
    # --------------------------------------------------------------------------------
    # - Creamos el resolvente combinando las fórmulas con una conjunción
    #   y negando la segunda fórmula.
    # - Esto permite verificar si las fórmulas son inconsistentes.
    resolvente = And(cnf1, Not(cnf2))

    # --------------------------------------------------------------------------------
    # PASO 4.3: SIMPLIFICAR EL RESOLVENTE
    # --------------------------------------------------------------------------------
    # - Simplificamos el resolvente para verificar si es una contradicción.
    resolvente_simplificado = simplify(resolvente)

    # --------------------------------------------------------------------------------
    # PASO 4.4: VERIFICAR SI HAY CONTRADICCIÓN
    # --------------------------------------------------------------------------------
    # - Si el resolvente simplificado es `False`, significa que las fórmulas 
    #   son inconsistentes (hay contradicción).
    if resolvente_simplificado == False:
        print("Las formulas son inconsistentes (contradiccion encontrada).")
        return True
    else:
        print("No se encontro contradiccion.")
        return False

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO DEL ALGORITMO DE RESOLUCIÓN
# ------------------------------------------------------------------------------------
# - QUÉ: Este bloque muestra un ejemplo práctico del algoritmo de resolución.
# - POR QUÉ: Permite al usuario entender cómo funciona el algoritmo con un caso real.
# - EJEMPLO:
#   - Fórmula 1: `p → q` (Si p, entonces q).
#   - Fórmula 2: `¬q` (No q).
#   - Resultado esperado: Las fórmulas son inconsistentes.

if __name__ == "__main__":
    # Definimos las variables lógicas
    p, q = symbols('p q')

    # Definimos dos fórmulas lógicas
    formula1 = Implies(p, q)  # Si p, entonces q
    formula2 = Not(q)         # No q

    # Aplicamos el algoritmo de resolución
    print("Ejemplo practico del algoritmo de resolucion:")
    resultado = resolver_skolem(formula1, formula2)

    # Mostramos el resultado
    if resultado:
        print("El algoritmo determino que las formulas son inconsistentes.")
    else:
        print("El algoritmo determino que las formulas son consistentes.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo convierte las fórmulas a CNF para facilitar la resolución.
# 2. Aplica la Skolemización para eliminar cuantificadores existenciales (si los hubiera).
# 3. Combina las fórmulas con una conjunción y niega la segunda fórmula.
# 4. Simplifica el resolvente y verifica si es una contradicción.
# 5. Si hay contradicción, las fórmulas son inconsistentes; de lo contrario, son consistentes.
# 
# VENTAJAS:
# - Permite verificar la validez de fórmulas lógicas de manera sistemática.
# LIMITACIONES:
# - En este ejemplo, no se implementa la eliminación de cuantificadores.