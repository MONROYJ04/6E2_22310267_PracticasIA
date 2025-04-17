import random
import math

# Muestreo Directo
# Este método genera muestras directamente de una distribución conocida.
# En este caso, generaremos muestras de una distribución uniforme.

def muestreo_directo(cantidad_muestras):
    """
    Genera muestras de una distribución uniforme entre 0 y 1.

    Args:
        cantidad_muestras (int): Número de muestras a generar.

    Returns:
        list: Lista de muestras generadas.
    """
    muestras = []
    for _ in range(cantidad_muestras):
        muestra = random.uniform(0, 1)  # Genera un número aleatorio entre 0 y 1
        muestras.append(muestra)
    return muestras

# Muestreo por Rechazo
# Este método genera muestras de una distribución objetivo utilizando una función propuesta.
# Las muestras se aceptan o rechazan en función de una probabilidad.

def muestreo_por_rechazo(cantidad_muestras, funcion_objetivo, funcion_propuesta, constante_c):
    """
    Genera muestras utilizando el método de muestreo por rechazo.

    Args:
        cantidad_muestras (int): Número de muestras a generar.
        funcion_objetivo (function): Función de la distribución objetivo.
        funcion_propuesta (function): Función de la distribución propuesta.
        constante_c (float): Constante que satisface f(x) <= c * g(x).

    Returns:
        list: Lista de muestras aceptadas.
    """
    muestras = []
    while len(muestras) < cantidad_muestras:
        # Genera una muestra de la distribución propuesta
        x = funcion_propuesta()
        # Genera un número aleatorio entre 0 y c * g(x)
        u = random.uniform(0, constante_c * funcion_propuesta(x))
        # Acepta la muestra si u <= f(x)
        if u <= funcion_objetivo(x):
            muestras.append(x)
    return muestras

# Ejemplo práctico
# Queremos generar muestras de una distribución objetivo f(x) = 2x en el intervalo [0, 1].
# Usaremos una distribución uniforme g(x) = 1 como función propuesta.

def funcion_objetivo(x):
    """
    Función objetivo f(x) = 2x en el intervalo [0, 1].
    """
    if 0 <= x <= 1:
        return 2 * x
    return 0

def funcion_propuesta(x=None):
    """
    Función propuesta g(x) = 1 en el intervalo [0, 1].
    Si no se pasa un valor, genera una muestra uniforme entre 0 y 1.
    """
    if x is None:
        return random.uniform(0, 1)
    return 1  # g(x) = 1 para cualquier x en [0, 1]

# Constante c que satisface f(x) <= c * g(x)
constante_c = 2  # En este caso, c = 2 porque f(x) <= 2 * g(x)

# Generamos muestras utilizando ambos métodos
cantidad_muestras = 1000

# Muestreo directo
muestras_directas = muestreo_directo(cantidad_muestras)
print("Muestras generadas por Muestreo Directo:", muestras_directas[:10])  # Mostramos las primeras 10 muestras

# Muestreo por rechazo
muestras_rechazo = muestreo_por_rechazo(cantidad_muestras, funcion_objetivo, funcion_propuesta, constante_c)
print("Muestras generadas por Muestreo por Rechazo:", muestras_rechazo[:10])  # Mostramos las primeras 10 muestras