# Este archivo contiene una implementación del algoritmo de Inferencia por Enumeración.
# Este algoritmo se utiliza en redes bayesianas para calcular la probabilidad de una variable
# de interés dado un conjunto de evidencias. A continuación, se explica cada parte del código.

# Importamos la biblioteca necesaria para manejar combinaciones de valores
from itertools import product

# Definimos una función principal para calcular la probabilidad de una variable de consulta
# dado un conjunto de evidencias. Esta función utiliza el método de enumeración.
def probabilidad_por_enumeracion(consulta, evidencia, red_bayesiana):
    """
    Calcula la probabilidad de una variable de consulta dado un conjunto de evidencias
    utilizando el método de enumeración.

    :param consulta: Diccionario con la variable de consulta y su valor {variable: valor}
                     Ejemplo: {'Riego': True}
    :param evidencia: Diccionario con las variables de evidencia y sus valores {variable: valor}
                      Ejemplo: {'Lluvia': False}
    :param red_bayesiana: Diccionario que representa la red bayesiana.
                          Contiene las variables, sus valores posibles y sus tablas de probabilidad condicional (CPT).
    :return: Diccionario con las probabilidades normalizadas de la consulta.
             Ejemplo: {True: 0.8, False: 0.2}
    """
    # Obtenemos todas las variables de la red bayesiana
    variables = list(red_bayesiana.keys())

    # Definimos una función recursiva para enumerar todas las probabilidades posibles
    def enumerar_todas(variables, evidencia):
        """
        Función recursiva que calcula la probabilidad total considerando todas las combinaciones
        posibles de valores para las variables no observadas.

        :param variables: Lista de variables que quedan por procesar.
        :param evidencia: Diccionario con las variables observadas y sus valores.
        :return: Probabilidad total calculada.
        """
        # Caso base: Si no quedan variables por procesar, devolvemos 1.0
        if not variables:
            return 1.0

        # Tomamos la primera variable de la lista
        primera = variables[0]
        resto = variables[1:]

        # Si la variable ya está en la evidencia (es conocida)
        if primera in evidencia:
            # Calculamos la probabilidad condicional de la variable dada la evidencia
            probabilidad = calcular_probabilidad(primera, evidencia, red_bayesiana)
            # Multiplicamos esta probabilidad por la enumeración del resto de variables
            return probabilidad * enumerar_todas(resto, evidencia)
        else:
            # Si la variable no está en la evidencia, sumamos sobre todos sus valores posibles
            suma = 0
            for valor in red_bayesiana[primera]['valores']:
                # Creamos una nueva evidencia temporal que incluye el valor actual de la variable
                nueva_evidencia = evidencia.copy()
                nueva_evidencia[primera] = valor
                # Calculamos la probabilidad condicional y continuamos con la recursión
                probabilidad = calcular_probabilidad(primera, nueva_evidencia, red_bayesiana)
                suma += probabilidad * enumerar_todas(resto, nueva_evidencia)
            return suma

    # Calculamos las probabilidades para cada valor posible de la variable de consulta
    resultado = {}
    for valor in red_bayesiana[list(consulta.keys())[0]]['valores']:
        # Actualizamos la evidencia con el valor actual de la consulta
        nueva_evidencia = evidencia.copy()
        nueva_evidencia.update({list(consulta.keys())[0]: valor})
        # Llamamos a la función recursiva para calcular la probabilidad
        resultado[valor] = enumerar_todas(variables, nueva_evidencia)

    # Normalizamos las probabilidades para que sumen 1
    total = sum(resultado.values())
    for clave in resultado:
        resultado[clave] /= total

    # Devolvemos las probabilidades normalizadas
    return resultado

# Definimos una función auxiliar para calcular la probabilidad condicional de una variable
def calcular_probabilidad(variable, evidencia, red_bayesiana):
    """
    Calcula la probabilidad condicional de una variable dada la evidencia.

    :param variable: Variable de interés (por ejemplo, 'Lluvia').
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
    :return: Probabilidad condicional de la variable.
    """
    # Obtenemos la tabla de probabilidad condicional (CPT) de la variable
    cpt = red_bayesiana[variable]['cpt']

    # Buscamos en la CPT la fila que coincide con la evidencia actual
    for condicion, probabilidad in cpt.items():
        # Verificamos si todas las condiciones coinciden con la evidencia
        if all(evidencia.get(var) == val for var, val in condicion.items()):
            return probabilidad

    # Si no se encuentra una coincidencia, devolvemos 0 (esto no debería ocurrir si la CPT está bien definida)
    return 0.0

# Ejemplo práctico: Red bayesiana simple
# Definimos una red bayesiana con dos variables: Lluvia y Riego
red_bayesiana = {
    'Lluvia': {
        'valores': [True, False],  # Valores posibles: True (llueve) o False (no llueve)
        'cpt': {
            (): 0.2  # Probabilidad de que llueva (sin condiciones)
        }
    },
    'Riego': {
        'valores': [True, False],  # Valores posibles: True (hay riego) o False (no hay riego)
        'cpt': {
            ('Lluvia', True): 0.01,  # Probabilidad de que haya riego si llueve
            ('Lluvia', False): 0.4  # Probabilidad de que haya riego si no llueve
        }
    }
}

# Consulta: ¿Cuál es la probabilidad de que haya riego dado que no llueve?
consulta = {'Riego': True}  # Queremos saber la probabilidad de que haya riego
evidencia = {'Lluvia': False}  # Sabemos que no está lloviendo

# Calculamos la probabilidad utilizando el algoritmo de enumeración
resultado = probabilidad_por_enumeracion(consulta, evidencia, red_bayesiana)

# Imprimimos el resultado
print("Probabilidad de que haya riego dado que no llueve:")
for valor, probabilidad in resultado.items():
    print(f"{valor}: {probabilidad:.4f}")