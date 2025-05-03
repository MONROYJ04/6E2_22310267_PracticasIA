# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MODELO PROBABILISTA RACIONAL PARA CALCULAR PROBABILIDADES
# ------------------------------------------------------------------------------------
# Este código implementa un modelo probabilista racional basado en el Teorema de Bayes.
# Su objetivo es calcular la probabilidad de que un evento ocurra (hipótesis) dado que
# se tiene información previa (probabilidad a priori) y nueva evidencia.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - En este caso, importamos la biblioteca `math` para realizar cálculos matemáticos.
# - Aunque no se utiliza explícitamente en este código, es una buena práctica incluirla
#   si se planea extender el algoritmo con operaciones matemáticas más complejas.
import math

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR FUNCIÓN PARA CALCULAR LA PROBABILIDAD POSTERIOR
# ------------------------------------------------------------------------------------
# - Esta función implementa el Teorema de Bayes para calcular la probabilidad posterior.
# - La probabilidad posterior es la probabilidad de que una hipótesis sea verdadera
#   después de observar nueva evidencia.
# - Parámetros:
#   - `probabilidad_a_priori`: Probabilidad inicial de la hipótesis.
#   - `probabilidad_evidencia_dado_hipotesis`: Probabilidad de observar la evidencia si la hipótesis es verdadera.
#   - `probabilidad_evidencia`: Probabilidad total de observar la evidencia.
def calcular_probabilidad_posterior(probabilidad_a_priori, probabilidad_evidencia_dado_hipotesis, probabilidad_evidencia):
    """
    Calcula la probabilidad posterior usando el Teorema de Bayes.

    Args:
        probabilidad_a_priori (float): Probabilidad inicial de la hipótesis.
        probabilidad_evidencia_dado_hipotesis (float): Probabilidad de la evidencia dada la hipótesis.
        probabilidad_evidencia (float): Probabilidad total de la evidencia.

    Returns:
        float: Probabilidad posterior de la hipótesis.
    """
    # Fórmula del Teorema de Bayes:
    # P(H|E) = (P(H) * P(E|H)) / P(E)
    probabilidad_posterior = (probabilidad_a_priori * probabilidad_evidencia_dado_hipotesis) / probabilidad_evidencia
    return probabilidad_posterior

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR FUNCIÓN PARA CALCULAR LA PROBABILIDAD TOTAL DE LA EVIDENCIA
# ------------------------------------------------------------------------------------
# - Esta función calcula la probabilidad total de observar la evidencia.
# - Es importante porque el Teorema de Bayes requiere este valor para normalizar
#   la probabilidad posterior.
# - Parámetros:
#   - `probabilidad_a_priori`: Probabilidad inicial de la hipótesis.
#   - `probabilidad_evidencia_dado_hipotesis`: Probabilidad de la evidencia si la hipótesis es verdadera.
#   - `probabilidad_a_priori_no`: Probabilidad inicial de que la hipótesis sea falsa.
#   - `probabilidad_evidencia_dado_no_hipotesis`: Probabilidad de la evidencia si la hipótesis es falsa.
def calcular_probabilidad_evidencia(probabilidad_a_priori, probabilidad_evidencia_dado_hipotesis, probabilidad_a_priori_no, probabilidad_evidencia_dado_no_hipotesis):
    """
    Calcula la probabilidad total de la evidencia.

    Args:
        probabilidad_a_priori (float): Probabilidad inicial de la hipótesis.
        probabilidad_evidencia_dado_hipotesis (float): Probabilidad de la evidencia dada la hipótesis.
        probabilidad_a_priori_no (float): Probabilidad inicial de la negación de la hipótesis.
        probabilidad_evidencia_dado_no_hipotesis (float): Probabilidad de la evidencia dada la negación de la hipótesis.

    Returns:
        float: Probabilidad total de la evidencia.
    """
    # Fórmula para calcular la probabilidad total de la evidencia:
    # P(E) = P(H) * P(E|H) + P(~H) * P(E|~H)
    probabilidad_evidencia = (probabilidad_a_priori * probabilidad_evidencia_dado_hipotesis) + \
                             (probabilidad_a_priori_no * probabilidad_evidencia_dado_no_hipotesis)
    return probabilidad_evidencia

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO - DIAGNÓSTICO MÉDICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, queremos calcular la probabilidad de que una persona tenga una
#   enfermedad (hipótesis) dado que obtuvo un resultado positivo en una prueba médica
#   (evidencia).
# - Este ejemplo es útil para entender cómo el Teorema de Bayes se aplica en la vida real.

# Probabilidad inicial de que una persona tenga la enfermedad (a priori)
probabilidad_a_priori = 0.01  # 1%

# Probabilidad de obtener un resultado positivo si la persona tiene la enfermedad
probabilidad_evidencia_dado_hipotesis = 0.95  # 95%

# Probabilidad de que una persona no tenga la enfermedad (complemento de la a priori)
probabilidad_a_priori_no = 1 - probabilidad_a_priori  # 99%

# Probabilidad de obtener un resultado positivo si la persona no tiene la enfermedad
probabilidad_evidencia_dado_no_hipotesis = 0.05  # 5%

# Calculamos la probabilidad total de la evidencia
probabilidad_evidencia = calcular_probabilidad_evidencia(
    probabilidad_a_priori,
    probabilidad_evidencia_dado_hipotesis,
    probabilidad_a_priori_no,
    probabilidad_evidencia_dado_no_hipotesis
)

# Calculamos la probabilidad posterior de que la persona tenga la enfermedad
probabilidad_posterior = calcular_probabilidad_posterior(
    probabilidad_a_priori,
    probabilidad_evidencia_dado_hipotesis,
    probabilidad_evidencia
)

# Mostramos el resultado
print("Probabilidad de que la persona tenga la enfermedad dado un resultado positivo:")
print(f"{probabilidad_posterior:.2%}")  # Formato en porcentaje

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza el Teorema de Bayes:
#    P(H|E) = (P(H) * P(E|H)) / P(E)
#    Donde:
#    - P(H|E): Probabilidad posterior (hipótesis dada la evidencia).
#    - P(H): Probabilidad a priori (hipótesis antes de la evidencia).
#    - P(E|H): Probabilidad de la evidencia dada la hipótesis.
#    - P(E): Probabilidad total de la evidencia.
# 2. Suposiciones clave:
#    - La evidencia es independiente de otras variables no consideradas.
# 3. Ventajas:
#    - Útil para actualizar probabilidades con nueva información.
#    - Aplicable en diagnóstico médico, sistemas de recomendación, etc.
# 4. Limitaciones:
#    - Requiere conocer las probabilidades a priori y condicionales.