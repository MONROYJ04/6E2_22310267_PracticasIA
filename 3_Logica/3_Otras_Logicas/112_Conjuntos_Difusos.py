# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: CONJUNTOS DIFUSOS PARA EVALUAR ALTURAS
# ------------------------------------------------------------------------------------
# Este programa implementa un algoritmo básico de conjuntos difusos para evaluar el grado
# de pertenencia de un valor (en este caso, la altura de una persona) a un conjunto difuso.
# Los conjuntos difusos permiten representar conceptos que no son estrictamente verdaderos
# o falsos, sino que tienen grados de pertenencia (por ejemplo, "ser alto").

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PARA CALCULAR EL GRADO DE PERTENENCIA
# ------------------------------------------------------------------------------------
# - Esta función calcula el grado de pertenencia de un valor a un conjunto difuso.
# - Si el valor está fuera de los límites definidos, el grado de pertenencia será 0.
# - Si el valor está dentro de los límites, se calcula el grado de pertenencia como
#   una proporción lineal entre el límite inferior y el límite superior.
# - Parámetros clave:
#   - `valor`: El valor que queremos evaluar.
#   - `limite_inferior`: El límite inferior del conjunto difuso.
#   - `limite_superior`: El límite superior del conjunto difuso.
def calcular_grado_pertenencia(valor, limite_inferior, limite_superior):
    """
    Calcula el grado de pertenencia de un valor a un conjunto difuso.
    
    :param valor: El valor que queremos evaluar.
    :param limite_inferior: El límite inferior del conjunto difuso.
    :param limite_superior: El límite superior del conjunto difuso.
    :return: El grado de pertenencia (entre 0 y 1).
    """
    # Si el valor está fuera de los límites, el grado de pertenencia es 0.
    if valor < limite_inferior or valor > limite_superior:
        return 0.0
    # Si el valor está dentro de los límites, calculamos el grado de pertenencia.
    return (valor - limite_inferior) / (limite_superior - limite_inferior)

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DEL CONJUNTO DIFUSO "ALTO"
# ------------------------------------------------------------------------------------
# - Aquí definimos los límites del conjunto difuso "alto".
# - El límite inferior es la altura mínima para empezar a ser considerado "alto".
# - El límite superior es la altura máxima para ser considerado "alto".
# - Estos límites son arbitrarios y pueden ajustarse según el contexto.
limite_inferior_alto = 1.70  # Altura mínima para empezar a ser considerado "alto" (en metros).
limite_superior_alto = 2.00  # Altura máxima para ser considerado "alto" (en metros).

# ------------------------------------------------------------------------------------
# PASO 3: LISTA DE ALTURAS A EVALUAR
# ------------------------------------------------------------------------------------
# - Creamos una lista con las alturas de diferentes personas (en metros).
# - Estas alturas serán evaluadas para determinar su grado de pertenencia al conjunto "alto".
alturas = [1.60, 1.75, 1.80, 1.90, 2.10]

# ------------------------------------------------------------------------------------
# PASO 4: EVALUACIÓN DEL GRADO DE PERTENENCIA
# ------------------------------------------------------------------------------------
# - Iteramos sobre la lista de alturas y calculamos el grado de pertenencia de cada altura
#   al conjunto difuso "alto" utilizando la función `calcular_grado_pertenencia`.
# - Imprimimos los resultados para cada altura.
print("Evaluación del grado de pertenencia al conjunto 'alto':")
for altura in alturas:
    grado = calcular_grado_pertenencia(altura, limite_inferior_alto, limite_superior_alto)
    print(f"Altura: {altura} m -> Grado de pertenencia: {grado:.2f}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una función lineal para calcular el grado de pertenencia
#    de un valor a un conjunto difuso. La fórmula utilizada es:
#       grado_pertenencia = (valor - limite_inferior) / (limite_superior - limite_inferior)
# 2. Suposiciones clave:
#    - Los valores fuera del rango definido tienen un grado de pertenencia de 0.
#    - Los valores dentro del rango tienen un grado de pertenencia proporcional a su posición.
# 3. Ventajas:
#    - Es simple y fácil de implementar.
#    - Permite representar conceptos vagos como "ser alto" de manera cuantitativa.
# 4. Limitaciones:
#    - Solo funciona con conjuntos difusos lineales. Para conjuntos más complejos,
#      se necesitarían funciones de pertenencia más avanzadas (como funciones gaussianas).

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: PREDICCIÓN PARA UNA NUEVA PERSONA
# ------------------------------------------------------------------------------------
# - Supongamos que queremos evaluar si una persona con una altura de 1.85 m es "alta".
# - Utilizamos la función `calcular_grado_pertenencia` para obtener el grado de pertenencia.
nueva_altura = 1.85
grado_nueva_altura = calcular_grado_pertenencia(nueva_altura, limite_inferior_alto, limite_superior_alto)
print(f"\nAltura de la nueva persona: {nueva_altura} m -> Grado de pertenencia: {grado_nueva_altura:.2f}")

# ------------------------------------------------------------------------------------
# RESULTADOS:
# ------------------------------------------------------------------------------------
# - Si el grado de pertenencia es cercano a 0, significa que la persona no es considerada "alta".
# - Si el grado de pertenencia es cercano a 1, significa que la persona es considerada "muy alta".
# - Valores intermedios indican que la persona es "algo alta".