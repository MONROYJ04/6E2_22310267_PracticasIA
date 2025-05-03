# Importamos las bibliotecas necesarias
import numpy as np  # Aunque no se usa en este ejemplo, se puede usar para cálculos más avanzados

# Definimos una función para calcular la probabilidad posterior usando el Teorema de Bayes
def calcular_probabilidad_posterior(probabilidad_hipotesis, probabilidad_evidencia_dado_hipotesis, probabilidad_evidencia):
    """
    Calcula la probabilidad posterior usando el Teorema de Bayes.
    
    Parametros:
    - probabilidad_hipotesis: Probabilidad inicial de la hipótesis (priori).
    - probabilidad_evidencia_dado_hipotesis: Probabilidad de la evidencia dado que la hipótesis es verdadera.
    - probabilidad_evidencia: Probabilidad total de la evidencia observada.
    
    Retorna:
    - Probabilidad posterior de la hipótesis dado la evidencia.
    """
    # Aplicamos la fórmula del Teorema de Bayes
    probabilidad_posterior = (probabilidad_evidencia_dado_hipotesis * probabilidad_hipotesis) / probabilidad_evidencia
    return probabilidad_posterior

# Ejemplo práctico: Diagnóstico médico
# Supongamos que queremos calcular la probabilidad de que una persona tenga una enfermedad (H),
# dado que obtuvo un resultado positivo en una prueba (E).

# Paso 1: Definir las probabilidades iniciales
probabilidad_hipotesis = 0.01  # Probabilidad de que una persona tenga la enfermedad (1%)
# Esto representa la probabilidad inicial (priori) basada en datos históricos o conocimiento previo.

probabilidad_evidencia_dado_hipotesis = 0.95  # Probabilidad de que la prueba sea positiva si la persona tiene la enfermedad (95%)
# Esto indica qué tan confiable es la prueba para detectar la enfermedad en personas que realmente la tienen.

probabilidad_evidencia_dado_no_hipotesis = 0.05  # Probabilidad de que la prueba sea positiva si la persona no tiene la enfermedad (5%)
# Esto representa la tasa de falsos positivos, es decir, cuando la prueba indica enfermedad en personas sanas.

probabilidad_no_hipotesis = 1 - probabilidad_hipotesis  # Probabilidad de que la persona no tenga la enfermedad (99%)
# Complemento de la probabilidad inicial, ya que una persona o tiene la enfermedad o no la tiene.

# Paso 2: Calcular la probabilidad total de la evidencia
# Esto se hace sumando las probabilidades ponderadas de que la evidencia ocurra en ambos casos (con y sin la hipótesis)
probabilidad_evidencia = (probabilidad_evidencia_dado_hipotesis * probabilidad_hipotesis) + \
                         (probabilidad_evidencia_dado_no_hipotesis * probabilidad_no_hipotesis)
# Aquí combinamos las probabilidades de obtener un resultado positivo tanto si la persona tiene la enfermedad
# como si no la tiene, ponderadas por las probabilidades iniciales.

# Paso 3: Calcular la probabilidad posterior
# Usamos la función definida anteriormente para calcular la probabilidad posterior
probabilidad_posterior = calcular_probabilidad_posterior(
    probabilidad_hipotesis,
    probabilidad_evidencia_dado_hipotesis,
    probabilidad_evidencia
)

# Imprimir resultados
print("Probabilidad inicial de tener la enfermedad (priori):", probabilidad_hipotesis)
# Mostramos la probabilidad inicial de que una persona tenga la enfermedad.

print("Probabilidad de la evidencia (resultado positivo):", probabilidad_evidencia)
# Mostramos la probabilidad total de obtener un resultado positivo en la prueba.

print("Probabilidad posterior de tener la enfermedad dado el resultado positivo:", probabilidad_posterior)
# Mostramos la probabilidad actualizada (posterior) de que la persona tenga la enfermedad,
# dado que obtuvo un resultado positivo en la prueba.

# Explicación del resultado:
# Aunque la prueba tiene una alta precisión (95%), la probabilidad posterior de tener la enfermedad
# sigue siendo baja debido a la baja probabilidad inicial (priori) de la enfermedad.