# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: TIPOS DE RAZONAMIENTO Y APRENDIZAJE
# ------------------------------------------------------------------------------------
# Este programa tiene como objetivo explicar dos tipos principales de razonamiento:
# 1. Razonamiento inductivo: Generaliza patrones a partir de observaciones.
# 2. Razonamiento deductivo: Aplica reglas generales a casos específicos.
# Incluye ejemplos prácticos para ilustrar ambos conceptos.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PARA RAZONAMIENTO INDUCTIVO
# ------------------------------------------------------------------------------------
# - Esta función toma una lista de observaciones y genera una conclusión general.
# - Es útil para identificar patrones comunes en los datos.
# - Parámetro clave: `observaciones` (lista de elementos observados).
def razonamiento_inductivo(observaciones):
    """
    Esta funcion toma una lista de observaciones y genera una conclusion general.
    El razonamiento inductivo se basa en observar patrones y generalizarlos.
    """
    # Si todas las observaciones son iguales, asumimos que el patrón es válido.
    if all(observacion == observaciones[0] for observacion in observaciones):
        conclusion = f"Todas las observaciones indican que '{observaciones[0]}' es una regla general."
    else:
        conclusion = "No se puede determinar una regla general con las observaciones dadas."
    return conclusion

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA FUNCIÓN PARA RAZONAMIENTO DEDUCTIVO
# ------------------------------------------------------------------------------------
# - Esta función toma una premisa general y un caso específico para llegar a una conclusión.
# - Es útil para verificar si un caso cumple con una regla general.
# - Parámetros clave:
#   - `premisa_general`: Lista que representa la regla general.
#   - `caso_especifico`: Elemento que se desea verificar contra la regla.
def razonamiento_deductivo(premisa_general, caso_especifico):
    """
    Esta funcion toma una premisa general y un caso especifico para llegar a una conclusion.
    El razonamiento deductivo aplica reglas generales a casos particulares.
    """
    # Verificamos si el caso específico está contenido en la premisa general.
    if caso_especifico in premisa_general:
        conclusion = f"El caso especifico '{caso_especifico}' cumple con la premisa general."
    else:
        conclusion = f"El caso especifico '{caso_especifico}' no cumple con la premisa general."
    return conclusion

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLOS PRÁCTICOS DE LOS TIPOS DE RAZONAMIENTO
# ------------------------------------------------------------------------------------
# - Aquí se muestran ejemplos prácticos para ilustrar el razonamiento inductivo y deductivo.
# - Se utilizan listas de observaciones y premisas generales para demostrar los conceptos.
if __name__ == "__main__":
    # Ejemplo de razonamiento inductivo:
    # Observaciones: Todas las manzanas que hemos visto son rojas.
    observaciones = ["roja", "roja", "roja", "roja"]
    print("Razonamiento Inductivo:")
    print(razonamiento_inductivo(observaciones))
    
    # Ejemplo de razonamiento deductivo:
    # Premisa general: Todos los gatos son mamíferos.
    premisa_general = ["mamifero"]
    caso_especifico = "mamifero"
    print("\nRazonamiento Deductivo:")
    print(razonamiento_deductivo(premisa_general, caso_especifico))

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Razonamiento inductivo**:
#    - Observa patrones en un conjunto de datos y generaliza una regla.
#    - Ejemplo: Si todas las manzanas observadas son rojas, concluimos que "todas las manzanas son rojas".
#    - Limitación: No garantiza que la regla sea siempre verdadera.
#
# 2. **Razonamiento deductivo**:
#    - Parte de una regla general y la aplica a un caso específico.
#    - Ejemplo: Si sabemos que "todos los gatos son mamíferos", podemos deducir que un gato es un mamífero.
#    - Ventaja: Es más confiable si la premisa general es verdadera.
#
# 3. **Ventajas y limitaciones**:
#    - Inductivo: Útil para generar hipótesis, pero no asegura precisión.
#    - Deductivo: Preciso si las premisas son correctas, pero no genera nuevas ideas.