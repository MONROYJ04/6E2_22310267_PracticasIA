# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SUBIDA DE COLINA PARA OPTIMIZACIÓN DE FUNCIONES
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de Subida de Colina (Hill Climbing), que es un 
# método de búsqueda local utilizado para encontrar el máximo (o mínimo) de una función 
# objetivo. El algoritmo explora soluciones vecinas y se mueve hacia la mejor solución 
# encontrada hasta que no haya mejoras posibles.

import random

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DEL ALGORITMO DE SUBIDA DE COLINA
# ------------------------------------------------------------------------------------
# - Este bloque define el algoritmo principal de Subida de Colina.
# - El algoritmo comienza desde un estado inicial y evalúa su calidad usando una 
#   función objetivo. Luego, genera estados vecinos y se mueve hacia el vecino que 
#   mejora la solución actual. Si no hay mejoras, el algoritmo termina.
# - Parámetros clave:
#   - `funcion_objetivo`: Evalúa la calidad de un estado.
#   - `generar_vecino`: Genera un estado vecino al actual.
#   - `estado_inicial`: El estado desde donde comienza la búsqueda.

def subida_colina(funcion_objetivo, generar_vecino, estado_inicial):
    """
    Algoritmo de Subida de Colina para encontrar una solucion optima.
    
    Parametros:
    - funcion_objetivo: Una funcion que evalua la calidad de un estado.
    - generar_vecino: Una funcion que genera un estado vecino al actual.
    - estado_inicial: El estado inicial desde donde comienza la busqueda.
    
    Retorna:
    - El mejor estado encontrado.
    """
    # Inicializamos el estado actual como el estado inicial
    estado_actual = estado_inicial
    # Evaluamos la calidad del estado actual
    valor_actual = funcion_objetivo(estado_actual)
    
    while True:
        # Generamos un estado vecino
        vecino = generar_vecino(estado_actual)
        # Evaluamos la calidad del estado vecino
        valor_vecino = funcion_objetivo(vecino)
        
        # Si el vecino es mejor que el estado actual, nos movemos al vecino
        if valor_vecino > valor_actual:
            estado_actual = vecino
            valor_actual = valor_vecino
        else:
            # Si no hay mejora, terminamos la busqueda
            break
    
    # Retornamos el mejor estado encontrado
    return estado_actual

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA FUNCIÓN OBJETIVO
# ------------------------------------------------------------------------------------
# - Este bloque define la función objetivo que queremos maximizar.
# - En este caso, la función es una parábola: f(x) = -(x^2) + 4x + 6.
# - La función devuelve un valor que representa la calidad de un estado dado.

def funcion_objetivo(x):
    """
    Funcion objetivo que queremos maximizar.
    En este caso, es una parabola: f(x) = -(x^2) + 4x + 6
    """
    return -(x**2) + 4*x + 6

# ------------------------------------------------------------------------------------
# PASO 3: GENERACIÓN DE ESTADOS VECINOS
# ------------------------------------------------------------------------------------
# - Este bloque define cómo se generan los estados vecinos.
# - En este caso, un vecino se genera sumando o restando un valor aleatorio pequeño 
#   (en este caso, ±1) al estado actual.
# - Esto permite explorar soluciones cercanas al estado actual.

def generar_vecino(x):
    """
    Genera un vecino cercano al estado actual.
    En este caso, sumamos o restamos un valor aleatorio pequeño.
    """
    return x + random.choice([-1, 1])

# ------------------------------------------------------------------------------------
# PASO 4: EJECUCIÓN DEL ALGORITMO
# ------------------------------------------------------------------------------------
# - Este bloque inicializa el estado inicial y ejecuta el algoritmo de Subida de Colina.
# - El estado inicial se elige aleatoriamente dentro de un rango (en este caso, -10 a 10).
# - El algoritmo busca el mejor estado posible y muestra los resultados.

# Estado inicial
estado_inicial = random.randint(-10, 10)

# Ejecutamos el algoritmo de Subida de Colina
mejor_estado = subida_colina(funcion_objetivo, generar_vecino, estado_inicial)

# Mostramos los resultados
print("Estado inicial:", estado_inicial)
print("Mejor estado encontrado:", mejor_estado)
print("Valor de la funcion objetivo en el mejor estado:", funcion_objetivo(mejor_estado))

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo de Subida de Colina es un método de búsqueda local que explora 
#    soluciones vecinas para encontrar el máximo (o mínimo) de una función objetivo.
# 2. Suposiciones clave:
#    - La función objetivo es continua y tiene un máximo local alcanzable.
#    - Los estados vecinos son accesibles desde el estado actual.
# 3. Ventajas:
#    - Es simple de implementar y eficiente para problemas pequeños.
# 4. Limitaciones:
#    - Puede quedarse atrapado en máximos locales si no hay un mecanismo para escapar.
#    - No garantiza encontrar el máximo global.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que queremos encontrar el máximo de la función f(x) = -(x^2) + 4x + 6.
# El algoritmo comienza desde un estado inicial aleatorio (por ejemplo, x = -3) y 
# explora estados vecinos (por ejemplo, x = -2, x = -4, etc.) hasta encontrar el 
# máximo local. En este caso, el máximo global es x = 2, donde f(x) = 10.