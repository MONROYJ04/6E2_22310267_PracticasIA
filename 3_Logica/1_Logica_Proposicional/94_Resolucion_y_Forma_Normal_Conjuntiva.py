# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RESOLUCIÓN Y FORMA NORMAL CONJUNTIVA (FNC) EN LÓGICA PROPOSICIONAL
# ------------------------------------------------------------------------------------
# Este programa implementa el método de Resolución y la conversión a Forma Normal Conjuntiva (FNC).
# La Resolución es una técnica utilizada en lógica proposicional para determinar si un conjunto de cláusulas es inconsistente.
# La FNC es una forma estándar en la que las fórmulas lógicas se expresan como una conjunción de disyunciones.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `itertools` para manejar combinaciones de cláusulas.
# - Esto es necesario para aplicar el método de resolución, que requiere comparar pares de cláusulas.
import itertools

# ------------------------------------------------------------------------------------
# PASO 2: CONVERTIR UNA FÓRMULA A FORMA NORMAL CONJUNTIVA (FNC)
# ------------------------------------------------------------------------------------
# - Esta función toma una fórmula lógica en forma de string y la convierte a FNC.
# - La FNC es una representación estándar que facilita la aplicación del método de resolución.
# - Separamos las conjunciones (`^`) y disyunciones (`v`) para estructurar las cláusulas.
def convertir_a_fnc(formula):
    """
    Convierte una fórmula lógica a Forma Normal Conjuntiva (FNC).
    :param formula: Una fórmula lógica en forma de string.
    :return: Una lista de conjuntos que representan las cláusulas en FNC.
    """
    # Eliminamos espacios en blanco para evitar errores de procesamiento.
    formula = formula.replace(" ", "")
    # Dividimos la fórmula en cláusulas separadas por conjunciones (`^`).
    clausulas = formula.split("^")
    # Dentro de cada cláusula, dividimos los literales por disyunciones (`v`) y los convertimos en conjuntos.
    fnc = [set(clausula.split("v")) for clausula in clausulas]
    return fnc

# ------------------------------------------------------------------------------------
# PASO 3: APLICAR EL MÉTODO DE RESOLUCIÓN
# ------------------------------------------------------------------------------------
# - Esta función aplica el método de resolución para determinar si un objetivo es deducible.
# - Se basa en la negación del objetivo y la generación de nuevas cláusulas resolventes.
# - Si se genera una cláusula vacía, significa que el objetivo es deducible.
def resolucion(fnc, objetivo):
    """
    Aplica el método de resolución para determinar si el objetivo es deducible.
    :param fnc: Una lista de conjuntos que representan las cláusulas en FNC.
    :param objetivo: Una proposición que queremos probar.
    :return: True si el objetivo es deducible, False en caso contrario.
    """
    # Negamos el objetivo y lo añadimos a las cláusulas existentes.
    objetivo_negado = {f"!{objetivo}"}
    fnc.append(objetivo_negado)

    # Bucle principal para aplicar resolución iterativa.
    while True:
        nuevas_clausulas = set()
        # Generamos todas las combinaciones posibles de pares de cláusulas.
        for (clausula1, clausula2) in itertools.combinations(fnc, 2):
            # Intentamos resolver el par de cláusulas.
            resolvente = resolver(clausula1, clausula2)
            if resolvente is not None:
                # Si la resolvente es vacía, hemos encontrado una contradicción.
                if not resolvente:
                    return True
                # Añadimos la nueva cláusula resolvente al conjunto de nuevas cláusulas.
                nuevas_clausulas.add(frozenset(resolvente))
        
        # Si no se generan nuevas cláusulas, terminamos el proceso.
        if nuevas_clausulas.issubset(map(frozenset, fnc)):
            return False
        
        # Añadimos las nuevas cláusulas a la FNC existente.
        fnc.extend(map(set, nuevas_clausulas))

# ------------------------------------------------------------------------------------
# PASO 4: RESOLVER DOS CLÁUSULAS
# ------------------------------------------------------------------------------------
# - Esta función intenta resolver dos cláusulas.
# - Busca literales opuestos (ejemplo: `A` y `!A`) y genera una nueva cláusula sin esos literales.
# - Si no es posible resolver, devuelve `None`.
def resolver(clausula1, clausula2):
    """
    Intenta resolver dos cláusulas.
    :param clausula1: Un conjunto que representa una cláusula.
    :param clausula2: Un conjunto que representa otra cláusula.
    :return: Una nueva cláusula si es posible resolver, None en caso contrario.
    """
    # Iteramos sobre los literales de la primera cláusula.
    for literal in clausula1:
        # Si encontramos el literal opuesto en la segunda cláusula, resolvemos.
        if f"!{literal}" in clausula2:
            # Creamos una nueva cláusula eliminando el literal y su opuesto.
            nueva_clausula = (clausula1 | clausula2) - {literal, f"!{literal}"}
            return nueva_clausula
    # Si no se puede resolver, devolvemos None.
    return None

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, probamos si la proposición `C` es deducible a partir de una fórmula lógica.
# - La fórmula inicial se convierte a FNC y se aplica el método de resolución.
if __name__ == "__main__":
    # Fórmula inicial en forma de string.
    formula = "(A v B) ^ (!A v C) ^ (!B v !C)"
    print("Fórmula original:", formula)

    # Convertimos la fórmula a FNC.
    fnc = convertir_a_fnc(formula)
    print("Forma Normal Conjuntiva (FNC):", fnc)

    # Objetivo a probar.
    objetivo = "C"
    print("Objetivo:", objetivo)

    # Aplicamos el método de resolución.
    es_deducible = resolucion(fnc, objetivo)
    if es_deducible:
        print(f"El objetivo '{objetivo}' es deducible a partir de las cláusulas.")
    else:
        print(f"El objetivo '{objetivo}' NO es deducible a partir de las cláusulas.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo convierte una fórmula lógica a FNC, una representación estándar que facilita la resolución.
# 2. Aplica el método de resolución, que busca contradicciones al combinar cláusulas.
# 3. Si se genera una cláusula vacía, el objetivo es deducible; de lo contrario, no lo es.
# 4. Ventajas: Es un método sistemático y completo para probar deducibilidad.
# 5. Limitaciones: Puede ser computacionalmente costoso para fórmulas grandes.