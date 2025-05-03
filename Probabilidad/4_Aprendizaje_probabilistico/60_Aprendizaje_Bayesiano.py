# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: TEOREMA DE BAYES PARA DIAGNÓSTICO MÉDICO
# ------------------------------------------------------------------------------------
# Este código utiliza el Teorema de Bayes para calcular la probabilidad posterior de que 
# una persona tenga una enfermedad, dado que obtuvo un resultado positivo en una prueba médica.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - En este caso, se importa `numpy` para cálculos avanzados si fueran necesarios.
# - Aunque no se utiliza directamente en este ejemplo, es útil para extender el análisis.
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA EL CÁLCULO DE LA PROBABILIDAD POSTERIOR
# ------------------------------------------------------------------------------------
# - Esta función implementa el Teorema de Bayes.
# - Recibe como parámetros:
#   - `probabilidad_hipotesis`: Probabilidad inicial de la hipótesis (priori).
#   - `probabilidad_evidencia_dado_hipotesis`: Probabilidad de observar la evidencia si la hipótesis es verdadera.
#   - `probabilidad_evidencia`: Probabilidad total de la evidencia observada.
# - Retorna la probabilidad posterior de la hipótesis dado que se observa la evidencia.
def calcular_probabilidad_posterior(probabilidad_hipotesis, probabilidad_evidencia_dado_hipotesis, probabilidad_evidencia):
    """
    Calcula la probabilidad posterior usando el Teorema de Bayes.
    
    Fórmula:
    P(H|E) = (P(E|H) * P(H)) / P(E)
    
    Donde:
    - P(H|E): Probabilidad posterior de la hipótesis dado la evidencia.
    - P(E|H): Probabilidad de la evidencia dado que la hipótesis es verdadera.
    - P(H): Probabilidad inicial de la hipótesis (priori).
    - P(E): Probabilidad total de la evidencia observada.
    """
    probabilidad_posterior = (probabilidad_evidencia_dado_hipotesis * probabilidad_hipotesis) / probabilidad_evidencia
    return probabilidad_posterior

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LAS PROBABILIDADES INICIALES
# ------------------------------------------------------------------------------------
# - Aquí se establecen las probabilidades iniciales necesarias para el cálculo.
# - Estas probabilidades se basan en datos históricos o conocimiento previo.

# Probabilidad inicial de que una persona tenga la enfermedad (priori).
probabilidad_hipotesis = 0.01  # 1%

# Probabilidad de que la prueba sea positiva si la persona tiene la enfermedad.
probabilidad_evidencia_dado_hipotesis = 0.95  # 95%

# Probabilidad de que la prueba sea positiva si la persona NO tiene la enfermedad (falsos positivos).
probabilidad_evidencia_dado_no_hipotesis = 0.05  # 5%

# Probabilidad de que la persona NO tenga la enfermedad (complemento de la probabilidad inicial).
probabilidad_no_hipotesis = 1 - probabilidad_hipotesis  # 99%

# ------------------------------------------------------------------------------------
# PASO 4: CALCULAR LA PROBABILIDAD TOTAL DE LA EVIDENCIA
# ------------------------------------------------------------------------------------
# - Este paso combina las probabilidades de obtener un resultado positivo en ambos casos:
#   - Si la persona tiene la enfermedad.
#   - Si la persona no tiene la enfermedad.
# - La fórmula es:
#   P(E) = P(E|H) * P(H) + P(E|¬H) * P(¬H)
# - Esto es importante porque normaliza las probabilidades para que sumen 1.
probabilidad_evidencia = (probabilidad_evidencia_dado_hipotesis * probabilidad_hipotesis) + \
                         (probabilidad_evidencia_dado_no_hipotesis * probabilidad_no_hipotesis)

# ------------------------------------------------------------------------------------
# PASO 5: CALCULAR LA PROBABILIDAD POSTERIOR
# ------------------------------------------------------------------------------------
# - Usamos la función definida anteriormente para calcular la probabilidad posterior.
# - Esto nos da la probabilidad actualizada de que la persona tenga la enfermedad,
#   dado que obtuvo un resultado positivo en la prueba.
probabilidad_posterior = calcular_probabilidad_posterior(
    probabilidad_hipotesis,
    probabilidad_evidencia_dado_hipotesis,
    probabilidad_evidencia
)

# ------------------------------------------------------------------------------------
# PASO 6: IMPRIMIR LOS RESULTADOS
# ------------------------------------------------------------------------------------
# - Aquí mostramos los resultados intermedios y finales para entender el proceso.
print("Probabilidad inicial de tener la enfermedad (priori):", probabilidad_hipotesis)
print("Probabilidad de la evidencia (resultado positivo):", probabilidad_evidencia)
print("Probabilidad posterior de tener la enfermedad dado el resultado positivo:", probabilidad_posterior)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El Teorema de Bayes permite actualizar la probabilidad de una hipótesis (tener la enfermedad)
#    en función de nueva evidencia (resultado positivo en la prueba).
# 2. Suposiciones clave:
#    - La prueba tiene una tasa de falsos positivos y falsos negativos conocida.
#    - La probabilidad inicial (priori) es baja porque la enfermedad es rara.
# 3. Ventajas:
#    - Permite combinar datos históricos con nueva evidencia.
#    - Es útil en diagnósticos médicos y otros problemas probabilísticos.
# 4. Limitaciones:
#    - Depende de estimaciones precisas de las probabilidades iniciales y condicionales.
#    - Puede ser sensible a errores en estas estimaciones.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: NUEVA PREDICCIÓN
# ------------------------------------------------------------------------------------
# Supongamos que queremos calcular la probabilidad para otra persona con las mismas condiciones.
# Podemos reutilizar el mismo código y ajustar las probabilidades iniciales si es necesario.