# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FACTORES DE CERTEZA PARA MANEJO DE INCERTIDUMBRE
# ------------------------------------------------------------------------------------
# Este algoritmo implementa el concepto de factores de certeza (FC), que son valores
# que representan el grado de confianza en una afirmación o hipótesis. Se utiliza
# para manejar información incierta en sistemas expertos.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PARA CALCULAR EL FACTOR DE CERTEZA
# ------------------------------------------------------------------------------------
# - Esta función toma dos parámetros: evidencia a favor y evidencia en contra.
# - Calcula el Factor de Certeza (FC) como la diferencia entre ambas evidencias.
# - Valida que los valores de entrada estén en el rango permitido (0 a 1).
# - Retorna un valor entre -1 y 1, donde:
#   - FC > 0 indica mayor confianza en la hipótesis.
#   - FC < 0 indica mayor confianza en la negación de la hipótesis.
#   - FC = 0 indica que no hay suficiente evidencia para decidir.

def calcular_factor_certeza(evidencia_a_favor, evidencia_en_contra):
    """
    Calcula el Factor de Certeza (FC) basado en la evidencia a favor y en contra.

    :param evidencia_a_favor: Grado de confianza en la evidencia a favor (valor entre 0 y 1).
    :param evidencia_en_contra: Grado de confianza en la evidencia en contra (valor entre 0 y 1).
    :return: El Factor de Certeza (valor entre -1 y 1).
    """
    # Validamos que los valores estén en el rango permitido (0 a 1).
    if not (0 <= evidencia_a_favor <= 1 and 0 <= evidencia_en_contra <= 1):
        raise ValueError("Los valores de evidencia deben estar entre 0 y 1.")

    # Calculamos el Factor de Certeza (FC) usando la fórmula:
    # FC = evidencia_a_favor - evidencia_en_contra
    factor_certeza = evidencia_a_favor - evidencia_en_contra

    # Retornamos el resultado.
    return factor_certeza

# ------------------------------------------------------------------------------------
# PASO 2: EJEMPLO PRÁCTICO PARA ENTENDER EL ALGORITMO
# ------------------------------------------------------------------------------------
# - En este ejemplo, evaluamos si una persona tiene fiebre.
# - Evidencia a favor: La persona tiene una temperatura alta (confianza de 0.8).
# - Evidencia en contra: La persona no tiene otros síntomas relacionados (confianza de 0.3).
# - Calculamos el Factor de Certeza (FC) y lo interpretamos.

# Definimos las variables para la evidencia.
evidencia_favor = 0.8  # Confianza en la evidencia a favor.
evidencia_contra = 0.3  # Confianza en la evidencia en contra.

# Calculamos el Factor de Certeza (FC) para esta situación.
fc_resultado = calcular_factor_certeza(evidencia_favor, evidencia_contra)

# Mostramos el resultado con una explicación.
print("Ejemplo práctico:")
print(f"Evidencia a favor: {evidencia_favor}")
print(f"Evidencia en contra: {evidencia_contra}")
print(f"El Factor de Certeza (FC) es: {fc_resultado}")

# ------------------------------------------------------------------------------------
# PASO 3: INTERPRETACIÓN DEL RESULTADO
# ------------------------------------------------------------------------------------
# - Interpretamos el valor del Factor de Certeza (FC) para tomar una decisión.
# - Las posibles conclusiones son:
#   - Si FC > 0: Es probable que la hipótesis sea verdadera (la persona tiene fiebre).
#   - Si FC < 0: Es poco probable que la hipótesis sea verdadera.
#   - Si FC = 0: No hay suficiente evidencia para decidir.

if fc_resultado > 0:
    print("Conclusión: Es probable que la persona tenga fiebre.")
elif fc_resultado < 0:
    print("Conclusión: Es poco probable que la persona tenga fiebre.")
else:
    print("Conclusión: No hay suficiente evidencia para determinar si la persona tiene fiebre.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza una fórmula simple para calcular el Factor de Certeza (FC):
#    FC = evidencia_a_favor - evidencia_en_contra
#    - Esto significa que si la evidencia a favor es mayor que la evidencia en contra,
#      el FC será positivo, indicando confianza en la hipótesis.
#    - Si la evidencia en contra es mayor, el FC será negativo, indicando confianza
#      en la negación de la hipótesis.
#    - Si ambas evidencias son iguales, el FC será 0, indicando incertidumbre.
#
# 2. Suposiciones clave:
#    - Los valores de evidencia deben estar en el rango [0, 1].
#    - La evidencia a favor y en contra son independientes entre sí.
#
# 3. Ventajas y limitaciones:
#    - Ventaja: Es fácil de implementar y entender.
#    - Limitación: No considera interacciones complejas entre evidencias.