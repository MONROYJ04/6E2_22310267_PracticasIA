# Este algoritmo calcula el Valor de la Información (VOI) en un contexto de toma de decisiones.
# El VOI mide cuánto vale obtener información adicional antes de tomar una decisión.
# Se utiliza en situaciones donde hay incertidumbre y se busca maximizar la utilidad esperada.

# Importamos la biblioteca necesaria para realizar cálculos matemáticos
import numpy as np

# Función para calcular la utilidad esperada sin información adicional
def utilidad_esperada_sin_informacion(probabilidades, utilidades):
    """
    Calcula la utilidad esperada sin información adicional.
    
    :param probabilidades: Lista de probabilidades de los estados del mundo.
    :param utilidades: Lista de utilidades asociadas a cada estado del mundo.
    :return: Utilidad esperada sin información.
    """
    # Multiplicamos las probabilidades por las utilidades y sumamos los resultados
    return np.dot(probabilidades, utilidades)

# Función para calcular la utilidad esperada con información adicional
def utilidad_esperada_con_informacion(probabilidades_condicionales, utilidades):
    """
    Calcula la utilidad esperada con información adicional.
    
    :param probabilidades_condicionales: Matriz de probabilidades condicionales dado cada estado del mundo.
    :param utilidades: Lista de utilidades asociadas a cada estado del mundo.
    :return: Utilidad esperada con información.
    """
    utilidad_total = 0
    # Iteramos sobre cada estado del mundo
    for i in range(len(probabilidades_condicionales)):
        # Calculamos la utilidad esperada para cada estado y la sumamos
        utilidad_total += max(np.dot(probabilidades_condicionales[i], utilidades))
    return utilidad_total

# Función principal para calcular el Valor de la Información (VOI)
def valor_de_la_informacion(probabilidades, probabilidades_condicionales, utilidades):
    """
    Calcula el Valor de la Información (VOI).
    
    :param probabilidades: Lista de probabilidades de los estados del mundo.
    :param probabilidades_condicionales: Matriz de probabilidades condicionales dado cada estado del mundo.
    :param utilidades: Lista de utilidades asociadas a cada estado del mundo.
    :return: Valor de la Información.
    """
    # Calculamos la utilidad esperada sin información
    utilidad_sin_info = utilidad_esperada_sin_informacion(probabilidades, utilidades)
    # Calculamos la utilidad esperada con información
    utilidad_con_info = utilidad_esperada_con_informacion(probabilidades_condicionales, utilidades)
    # El VOI es la diferencia entre ambas utilidades
    return utilidad_con_info - utilidad_sin_info

# Ejemplo práctico
if __name__ == "__main__":
    # Probabilidades de los estados del mundo (sin información adicional)
    probabilidades = [0.6, 0.4]  # Ejemplo: 60% de probabilidad de buen clima, 40% de mal clima

    # Utilidades asociadas a cada estado del mundo
    utilidades = [100, 20]  # Ejemplo: Ganancia de 100 si hay buen clima, 20 si hay mal clima

    # Probabilidades condicionales dado que se obtiene información adicional
    probabilidades_condicionales = [
        [0.8, 0.2],  # Probabilidades ajustadas si se recibe un reporte favorable
        [0.3, 0.7]   # Probabilidades ajustadas si se recibe un reporte desfavorable
    ]

    # Calculamos el Valor de la Información
    voi = valor_de_la_informacion(probabilidades, probabilidades_condicionales, utilidades)

    # Mostramos el resultado
    print(f"El Valor de la Información es: {voi}")