# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: INFERENCIA LÓGICA PROPOSICIONAL PARA DEDUCIR NUEVOS HECHOS
# ------------------------------------------------------------------------------------
# Este código implementa un sistema básico de inferencia lógica proposicional.
# Su objetivo es deducir nuevas proposiciones (hechos) a partir de un conjunto inicial 
# de hechos conocidos y un conjunto de reglas lógicas.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINIR UNA FUNCIÓN PARA VERIFICAR SI UNA PROPOSICIÓN ES VERDADERA
# ------------------------------------------------------------------------------------
# - Esta función verifica si una proposición específica está presente en el conjunto 
#   de hechos conocidos.
# - Es importante porque permite comprobar si las condiciones de una regla lógica 
#   se cumplen.
# - Parámetros clave:
#   - `proposicion`: La proposición que queremos verificar.
#   - `hechos`: Un conjunto de proposiciones que sabemos que son verdaderas.

def es_verdadero(proposicion, hechos):
    """
    Verifica si una proposición es verdadera basándose en los hechos conocidos.
    
    :param proposicion: La proposición que queremos verificar.
    :param hechos: Un conjunto de hechos conocidos (proposiciones verdaderas).
    :return: True si la proposición es verdadera, False en caso contrario.
    """
    return proposicion in hechos

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR UNA FUNCIÓN PARA REALIZAR LA INFERENCIA LÓGICA
# ------------------------------------------------------------------------------------
# - Esta función aplica las reglas lógicas al conjunto de hechos conocidos para 
#   deducir nuevas proposiciones.
# - Es importante porque permite expandir el conocimiento inicial con base en las 
#   reglas definidas.
# - Parámetros clave:
#   - `reglas`: Una lista de reglas, donde cada regla es una tupla (condiciones, conclusión).
#     - `condiciones`: Lista de proposiciones que deben ser verdaderas para aplicar la regla.
#     - `conclusion`: Proposición que se deduce si las condiciones son verdaderas.
#   - `hechos`: Un conjunto de proposiciones conocidas como verdaderas.

def inferencia_logica(reglas, hechos):
    """
    Realiza inferencia lógica a partir de un conjunto de reglas y hechos conocidos.
    
    :param reglas: Una lista de reglas, donde cada regla es una tupla (condiciones, conclusion).
                   - condiciones: Una lista de proposiciones que deben ser verdaderas.
                   - conclusion: La proposición que se deduce si las condiciones son verdaderas.
    :param hechos: Un conjunto de hechos conocidos (proposiciones verdaderas).
    :return: Un conjunto actualizado de hechos con las nuevas conclusiones deducidas.
    """
    nuevos_hechos = set(hechos)  # Copiamos los hechos iniciales

    # --------------------------------------------------------------------------------
    # PASO 3: ITERAR SOBRE LAS REGLAS PARA VERIFICAR SI SE PUEDEN APLICAR
    # --------------------------------------------------------------------------------
    # - Este bloque recorre todas las reglas definidas y verifica si las condiciones 
    #   de cada regla son verdaderas.
    # - Si las condiciones son verdaderas, se añade la conclusión de la regla al 
    #   conjunto de hechos.
    # - Es importante porque permite deducir nuevos hechos basados en las reglas.
    for condiciones, conclusion in reglas:
        # Verificamos si todas las condiciones de la regla son verdaderas
        if all(es_verdadero(condicion, nuevos_hechos) for condicion in condiciones):
            # Si todas las condiciones son verdaderas, añadimos la conclusión a los hechos
            nuevos_hechos.add(conclusion)
    
    return nuevos_hechos

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO DE INFERENCIA LÓGICA
# ------------------------------------------------------------------------------------
# - En este ejemplo, partimos de un conjunto inicial de hechos y aplicamos reglas 
#   lógicas para deducir nuevos hechos.
# - Hechos iniciales:
#   - Sabemos que "A" y "B" son verdaderos.
# - Reglas:
#   - Si "A" y "B" son verdaderos, entonces "C" es verdadero.
#   - Si "C" es verdadero, entonces "D" es verdadero.

# Hechos iniciales: Sabemos que "A" y "B" son verdaderos.
hechos_iniciales = {"A", "B"}

# Reglas: Si "A" y "B" son verdaderos, entonces "C" es verdadero.
#         Si "C" es verdadero, entonces "D" es verdadero.
reglas = [
    (["A", "B"], "C"),  # Si A y B, entonces C
    (["C"], "D")        # Si C, entonces D
]

# Realizamos la inferencia lógica
hechos_deducidos = inferencia_logica(reglas, hechos_iniciales)

# Mostramos los resultados
print("Hechos iniciales:", hechos_iniciales)
print("Hechos deducidos:", hechos_deducidos)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza un enfoque basado en reglas para deducir nuevos hechos.
# 2. Suposiciones clave:
#    - Los hechos iniciales son correctos.
#    - Las reglas están bien definidas y no contienen contradicciones.
# 3. Ventajas:
#    - Es simple y fácil de implementar.
#    - Permite deducir conclusiones de manera lógica y estructurada.
# 4. Limitaciones:
#    - No maneja incertidumbre (todas las proposiciones son verdaderas o falsas).
#    - No detecta conflictos entre reglas.

# ------------------------------------------------------------------------------------
# RESULTADO DEL EJEMPLO
# ------------------------------------------------------------------------------------
# Hechos iniciales: {"A", "B"}
# Hechos deducidos: {"A", "B", "C", "D"}
# Explicación:
# - Sabemos que "A" y "B" son verdaderos.
# - Según la primera regla, si "A" y "B" son verdaderos, entonces "C" es verdadero.
# - Según la segunda regla, si "C" es verdadero, entonces "D" es verdadero.
# - Por lo tanto, deducimos que "C" y "D" también son verdaderos.