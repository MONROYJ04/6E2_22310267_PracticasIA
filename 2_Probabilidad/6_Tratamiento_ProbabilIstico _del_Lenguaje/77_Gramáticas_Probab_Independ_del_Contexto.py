# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: GRAMÁTICAS PROBABILÍSTICAS INDEPENDIENTES DEL CONTEXTO (PCFG)
# ------------------------------------------------------------------------------------
# Este programa implementa una Gramática Probabilística Independiente del Contexto (PCFG).
# Una PCFG es una extensión de las gramáticas libres de contexto que asigna probabilidades
# a las reglas de producción, permitiendo modelar lenguajes con mayor precisión.
# Este algoritmo genera oraciones aleatorias basadas en una gramática definida.

import random  # Importamos la librería random para manejar probabilidades.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA GRAMÁTICA PROBABILÍSTICA
# ------------------------------------------------------------------------------------
# - Aquí definimos una gramática probabilística como un diccionario.
# - Las claves son los símbolos no terminales (como "S", "NP", "VP").
# - Los valores son listas de tuplas, donde cada tupla contiene:
#   1. Una producción (cadena de texto que define cómo expandir el símbolo).
#   2. Una probabilidad asociada (valor entre 0 y 1 que indica la frecuencia relativa).
# - Esta gramática modela un lenguaje simple con sustantivos, verbos y determinantes.

gramatica = {
    "S": [("NP VP", 0.9), ("VP", 0.1)],  # S -> NP VP (90%) o S -> VP (10%)
    "NP": [("Det N", 0.5), ("N", 0.5)],  # NP -> Det N (50%) o NP -> N (50%)
    "VP": [("V NP", 0.7), ("V", 0.3)],   # VP -> V NP (70%) o VP -> V (30%)
    "Det": [("el", 0.5), ("la", 0.5)],   # Det -> el (50%) o Det -> la (50%)
    "N": [("gato", 0.5), ("perro", 0.5)],# N -> gato (50%) o N -> perro (50%)
    "V": [("come", 0.5), ("duerme", 0.5)]# V -> come (50%) o V -> duerme (50%)
}

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PARA GENERAR ORACIONES
# ------------------------------------------------------------------------------------
# - Esta función genera una oración a partir de un símbolo no terminal inicial.
# - Utiliza la gramática probabilística para expandir los símbolos no terminales.
# - Si encuentra un símbolo terminal (como "gato" o "come"), lo devuelve directamente.
# - La generación es recursiva: cada símbolo no terminal se expande hasta que todos
#   los símbolos sean terminales.
# - Usa `random.choices` para seleccionar producciones basadas en sus probabilidades.

def generar_oracion(simbolo):
    """
    Genera una oración a partir de un símbolo no terminal utilizando la gramática probabilística.
    :param simbolo: El símbolo no terminal inicial (por ejemplo, "S").
    :return: Una oración generada como una cadena de texto.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: VERIFICAR SI EL SÍMBOLO ES TERMINAL
    # --------------------------------------------------------------------------------
    # - Si el símbolo no está en la gramática, asumimos que es un terminal.
    # - Los símbolos terminales son palabras finales como "gato" o "come".
    if simbolo not in gramatica:
        return simbolo  # Devolvemos el símbolo directamente.

    # --------------------------------------------------------------------------------
    # PASO 2.2: SELECCIONAR UNA PRODUCCIÓN BASADA EN PROBABILIDADES
    # --------------------------------------------------------------------------------
    # - Obtenemos las producciones y sus probabilidades asociadas.
    # - Usamos `random.choices` para elegir una producción al azar.
    producciones = gramatica[simbolo]
    produccion = random.choices(
        [p[0] for p in producciones],  # Lista de producciones (ej: "NP VP", "VP").
        [p[1] for p in producciones]  # Lista de probabilidades (ej: 0.9, 0.1).
    )[0]

    # --------------------------------------------------------------------------------
    # PASO 2.3: EXPANDIR RECURSIVAMENTE LOS SÍMBOLOS
    # --------------------------------------------------------------------------------
    # - Dividimos la producción seleccionada en símbolos individuales.
    # - Para cada símbolo, llamamos recursivamente a `generar_oracion`.
    resultado = []
    for s in produccion.split():  # Dividimos la producción en palabras/símbolos.
        resultado.append(generar_oracion(s))  # Generamos recursivamente.

    # --------------------------------------------------------------------------------
    # PASO 2.4: UNIR LOS RESULTADOS EN UNA ORACIÓN
    # --------------------------------------------------------------------------------
    # - Unimos los símbolos generados en una cadena de texto.
    # - Esto forma la oración final generada.
    return " ".join(resultado)

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este bloque, generamos 5 oraciones aleatorias utilizando la gramática definida.
# - Cada ejecución del programa puede generar oraciones diferentes debido a la
#   naturaleza probabilística del algoritmo.

if __name__ == "__main__":
    print("Ejemplo de oraciones generadas con la gramática probabilística:")
    for _ in range(5):  # Generamos 5 oraciones.
        print(generar_oracion("S"))  # Llamamos a la función con el símbolo inicial "S".

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Propósito del algoritmo**:
#    - Este algoritmo utiliza una gramática probabilística para generar oraciones.
#    - Las probabilidades asignadas a las reglas de producción determinan la frecuencia
#      relativa de las estructuras generadas.
#
# 2. **Cómo funciona**:
#    - La gramática se define como un conjunto de reglas con probabilidades.
#    - La generación comienza con un símbolo inicial (como "S").
#    - Cada símbolo no terminal se expande recursivamente hasta que todos los símbolos
#      sean terminales.
#
# 3. **Ventajas**:
#    - Permite modelar lenguajes con estructuras complejas.
#    - Es útil en aplicaciones como el procesamiento del lenguaje natural (NLP).
#
# 4. **Limitaciones**:
#    - La calidad de las oraciones generadas depende de la gramática definida.
#    - No maneja dependencias contextuales más allá de las probabilidades asignadas.

# ------------------------------------------------------------------------------------
# EJEMPLO DE SALIDA
# ------------------------------------------------------------------------------------
# Al ejecutar este programa, podrías obtener una salida como esta:
# Ejemplo de oraciones generadas con la gramática probabilística:
# el gato come
# la perro duerme
# gato duerme
# el perro come el gato
# la gato
#
# Cada ejecución generará oraciones diferentes debido a la naturaleza probabilística.