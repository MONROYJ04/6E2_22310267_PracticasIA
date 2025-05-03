# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SIMULACIÓN DE PROGRAMACIÓN LÓGICA EN PYTHON
# ------------------------------------------------------------------------------------
# Este programa simula el razonamiento lógico de sistemas como Prolog y CLIPS.
# Utiliza un conjunto de hechos y reglas para inferir nuevos conocimientos.
# Los hechos representan información conocida, y las reglas definen cómo generar
# nuevos hechos a partir de los existentes.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LOS HECHOS INICIALES
# ------------------------------------------------------------------------------------
# - Aquí se define una lista de hechos iniciales que representan el conocimiento base.
# - Cada hecho está representado como una cadena de texto en formato lógico.
# - Estos hechos serán utilizados por el motor de inferencia para generar nuevos hechos.
hechos = [
    "es_mamifero(perro)",  # El perro es un mamífero.
    "es_mamifero(gato)",   # El gato es un mamífero.
    "es_ave(aguila)",      # El águila es un ave.
    "tiene_plumas(aguila)",# El águila tiene plumas.
    "tiene_pelo(perro)",   # El perro tiene pelo.
    "tiene_pelo(gato)"     # El gato tiene pelo.
]

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LAS REGLAS
# ------------------------------------------------------------------------------------
# - Las reglas son funciones que determinan cómo generar nuevos hechos.
# - Cada regla toma un parámetro (el animal) y verifica si se cumple una condición
#   en la lista de hechos. Si la condición se cumple, devuelve un nuevo hecho.

def regla_es_mamifero_con_pelo(animal):
    """
    Regla: Si un animal tiene pelo, entonces es un mamífero.
    - Parámetro: `animal` (nombre del animal a evaluar).
    - Retorna: Un nuevo hecho en formato lógico si se cumple la regla, o None.
    """
    if f"tiene_pelo({animal})" in hechos:  # Verifica si el animal tiene pelo.
        return f"es_mamifero({animal})"    # Genera el hecho "es_mamifero".
    return None                            # Si no se cumple, no genera nada.

def regla_es_ave_con_plumas(animal):
    """
    Regla: Si un animal tiene plumas, entonces es un ave.
    - Parámetro: `animal` (nombre del animal a evaluar).
    - Retorna: Un nuevo hecho en formato lógico si se cumple la regla, o None.
    """
    if f"tiene_plumas({animal})" in hechos:  # Verifica si el animal tiene plumas.
        return f"es_ave({animal})"           # Genera el hecho "es_ave".
    return None                              # Si no se cumple, no genera nada.

# ------------------------------------------------------------------------------------
# PASO 3: MOTOR DE INFERENCIA
# ------------------------------------------------------------------------------------
# - Este bloque aplica las reglas a los hechos conocidos para generar nuevos hechos.
# - Recorre cada hecho en la lista y evalúa si alguna regla puede generar un nuevo hecho.
# - Los nuevos hechos se agregan a la lista de hechos existentes.

def motor_inferencia():
    """
    Motor de inferencia:
    - Aplica las reglas a los hechos conocidos para inferir nuevos hechos.
    - Retorna: Una lista de nuevos hechos generados.
    """
    nuevos_hechos = []  # Lista para almacenar los nuevos hechos generados.

    for hecho in hechos:  # Recorre cada hecho conocido.
        # Si el hecho indica que un animal tiene pelo, aplica la regla correspondiente.
        if "tiene_pelo" in hecho:
            animal = hecho.split("(")[1].split(")")[0]  # Extrae el nombre del animal.
            nuevo_hecho = regla_es_mamifero_con_pelo(animal)  # Aplica la regla.
            if nuevo_hecho and nuevo_hecho not in hechos:  # Si el nuevo hecho no existe aún:
                nuevos_hechos.append(nuevo_hecho)  # Lo agrega a la lista de nuevos hechos.
        # Si el hecho indica que un animal tiene plumas, aplica la regla correspondiente.
        elif "tiene_plumas" in hecho:
            animal = hecho.split("(")[1].split(")")[0]  # Extrae el nombre del animal.
            nuevo_hecho = regla_es_ave_con_plumas(animal)  # Aplica la regla.
            if nuevo_hecho and nuevo_hecho not in hechos:  # Si el nuevo hecho no existe aún:
                nuevos_hechos.append(nuevo_hecho)  # Lo agrega a la lista de nuevos hechos.
    
    # Agrega los nuevos hechos generados a la lista de hechos existentes.
    hechos.extend(nuevos_hechos)
    return nuevos_hechos  # Retorna la lista de nuevos hechos.

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo funciona el motor de inferencia con los hechos iniciales.
# - Se imprimen los hechos iniciales, los nuevos hechos inferidos y los hechos finales.

print("Hechos iniciales:")  # Muestra los hechos iniciales.
print(hechos)

# Ejecuta el motor de inferencia para generar nuevos hechos.
nuevos = motor_inferencia()

print("\nNuevos hechos inferidos:")  # Muestra los nuevos hechos generados.
print(nuevos)

print("\nHechos finales:")  # Muestra la lista completa de hechos después de la inferencia.
print(hechos)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza un enfoque basado en reglas para simular el razonamiento lógico.
# 2. Los hechos iniciales representan el conocimiento base del sistema.
# 3. Las reglas definen cómo generar nuevos hechos a partir de los existentes.
# 4. El motor de inferencia aplica las reglas a los hechos conocidos y actualiza la lista de hechos.
# 5. Ventajas: Es fácil de entender y extender añadiendo nuevas reglas o hechos.
# 6. Limitaciones: No maneja incertidumbre ni conflictos entre reglas.