# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: LÓGICA NO MONOTÓNICA PARA EVALUAR SI UN OBJETO PUEDE VOLAR
# ------------------------------------------------------------------------------------
# Este algoritmo implementa un sistema básico de Lógica No Monotónica. 
# La Lógica No Monotónica permite que las conclusiones puedan cambiar si se introduce nueva información, 
# a diferencia de la lógica clásica donde las conclusiones son inmutables.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINIR LA BASE DE CONOCIMIENTO INICIAL
# ------------------------------------------------------------------------------------
# - Aquí se define un conjunto inicial de hechos que representan lo que "sabemos" sobre el mundo.
# - En este caso, asumimos que el objeto es un pájaro y que los pájaros vuelan.
# - Esta base de conocimiento se usará para evaluar si el objeto puede volar.

base_conocimiento = {
    "es_pajaro": True,  # Suponemos que algo es un pájaro
    "vuela": True       # Suponemos que los pájaros vuelan
}

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN `puede_volar`
# ------------------------------------------------------------------------------------
# - Esta función evalúa si un objeto puede volar basado en la base de conocimiento.
# - Si el objeto es un pájaro y no hay evidencia de que no vuele, se asume que vuela.
# - La función utiliza las claves de la base de conocimiento para tomar decisiones.

def puede_volar(base_conocimiento):
    """
    Evalúa si un objeto puede volar basado en la base de conocimiento.
    Si el objeto es un pájaro y no hay evidencia de que no vuele, se asume que vuela.
    """
    # Si el objeto es un pájaro y no está explícitamente indicado que no vuela
    if base_conocimiento.get("es_pajaro", False) and not base_conocimiento.get("no_vuela", False):
        return True  # El objeto puede volar
    else:
        return False  # El objeto no puede volar

# ------------------------------------------------------------------------------------
# PASO 3: EVALUAR EL CASO INICIAL
# ------------------------------------------------------------------------------------
# - En este paso, evaluamos si el objeto puede volar con la información inicial.
# - Dado que asumimos que el objeto es un pájaro y no hay evidencia de que no vuele, 
#   la función debería devolver `True`.

print("Caso inicial:")
print("¿Puede volar?", puede_volar(base_conocimiento))  # Debería devolver True

# ------------------------------------------------------------------------------------
# PASO 4: INTRODUCIR NUEVA INFORMACIÓN
# ------------------------------------------------------------------------------------
# - Ahora agregamos nueva información a la base de conocimiento.
# - Indicamos que el objeto es un pingüino. Los pingüinos son pájaros, pero no vuelan.
# - Esto demuestra cómo la Lógica No Monotónica permite que las conclusiones cambien.

base_conocimiento["es_pinguino"] = True  # Nueva información: el objeto es un pingüino
base_conocimiento["no_vuela"] = True    # Nueva información: los pingüinos no vuelan

# ------------------------------------------------------------------------------------
# PASO 5: EVALUAR CON LA NUEVA INFORMACIÓN
# ------------------------------------------------------------------------------------
# - Evaluamos nuevamente si el objeto puede volar, pero ahora con la nueva información.
# - Dado que sabemos que el objeto no vuela, la función debería devolver `False`.

print("\nDespués de agregar nueva información:")
print("¿Puede volar?", puede_volar(base_conocimiento))  # Debería devolver False

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una base de conocimiento para tomar decisiones sobre si un objeto puede volar.
# 2. La Lógica No Monotónica permite que las conclusiones cambien cuando se introduce nueva información.
# 3. Suposiciones clave:
#    - Si no hay evidencia que contradiga que un pájaro vuela, se asume que vuela.
#    - La base de conocimiento puede expandirse dinámicamente con nueva información.
# 4. Ventajas:
#    - Flexible y adaptable a nueva información.
# 5. Limitaciones:
#    - Depende completamente de la calidad y precisión de la base de conocimiento.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Caso inicial:
# - El objeto es un pájaro y vuela. Resultado: True.
# Nueva información:
# - El objeto es un pingüino (un pájaro que no vuela). Resultado: False.

# Ejecución esperada:
# Caso inicial:
# ¿Puede volar? True
# Después de agregar nueva información:
# ¿Puede volar? False