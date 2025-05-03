# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA DE REGLAS PARA DIAGNÓSTICO Y CAUSAS
# ------------------------------------------------------------------------------------
# Este programa implementa un sistema basado en reglas simples para determinar posibles
# diagnósticos y sus causas a partir de síntomas proporcionados por el usuario.
# Utiliza diccionarios para mapear síntomas a diagnósticos y diagnósticos a causas.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LAS REGLAS DE DIAGNÓSTICO
# ------------------------------------------------------------------------------------
# - Aquí se define un diccionario llamado `reglas_diagnostico`.
# - Cada clave representa un síntoma (por ejemplo, "fiebre").
# - Cada valor asociado es el diagnóstico correspondiente (por ejemplo, "infección").
# - Esto permite mapear síntomas a diagnósticos de manera directa.
reglas_diagnostico = {
    "fiebre": "infeccion",
    "dolor_garganta": "faringitis",
    "tos": "resfriado",
    "dolor_cabeza": "migraña",
    "nauseas": "intoxicacion_alimentaria"
}

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LAS REGLAS CAUSALES
# ------------------------------------------------------------------------------------
# - Aquí se define un diccionario llamado `reglas_causales`.
# - Cada clave representa un diagnóstico (por ejemplo, "infección").
# - Cada valor asociado es la posible causa del diagnóstico (por ejemplo, "bacteria o virus").
# - Esto permite mapear diagnósticos a causas de manera directa.
reglas_causales = {
    "infeccion": "bacteria_o_virus",
    "faringitis": "infeccion_bacteriana",
    "resfriado": "virus_comun",
    "migraña": "estres_o_fatiga",
    "intoxicacion_alimentaria": "comida_contaminada"
}

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN PARA REALIZAR EL DIAGNÓSTICO
# ------------------------------------------------------------------------------------
# - Esta función toma una lista de síntomas como entrada.
# - Itera sobre cada síntoma y verifica si está en las `reglas_diagnostico`.
# - Si el síntoma está presente, agrega el diagnóstico correspondiente a una lista.
# - Devuelve una lista con todos los diagnósticos encontrados.
def realizar_diagnostico(lista_sintomas):
    # Lista para almacenar los diagnósticos encontrados.
    diagnosticos = []
    # Iteramos sobre los síntomas proporcionados.
    for sintoma in lista_sintomas:
        # Verificamos si el síntoma está en las reglas de diagnóstico.
        if sintoma in reglas_diagnostico:
            # Agregamos el diagnóstico correspondiente a la lista.
            diagnosticos.append(reglas_diagnostico[sintoma])
    return diagnosticos

# ------------------------------------------------------------------------------------
# PASO 4: FUNCIÓN PARA DETERMINAR LAS POSIBLES CAUSAS
# ------------------------------------------------------------------------------------
# - Esta función toma una lista de diagnósticos como entrada.
# - Itera sobre cada diagnóstico y verifica si está en las `reglas_causales`.
# - Si el diagnóstico está presente, agrega la causa correspondiente a una lista.
# - Devuelve una lista con todas las causas encontradas.
def determinar_causas(lista_diagnosticos):
    # Lista para almacenar las causas encontradas.
    causas = []
    # Iteramos sobre los diagnósticos proporcionados.
    for diagnostico in lista_diagnosticos:
        # Verificamos si el diagnóstico está en las reglas causales.
        if diagnostico in reglas_causales:
            # Agregamos la causa correspondiente a la lista.
            causas.append(reglas_causales[diagnostico])
    return causas

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Aquí se simula un caso práctico donde un usuario reporta síntomas.
# - Se utiliza la función `realizar_diagnostico` para obtener los diagnósticos.
# - Luego, se utiliza la función `determinar_causas` para obtener las causas.
# - Finalmente, se imprimen los resultados para que el usuario los vea.

# Supongamos que un usuario reporta los siguientes síntomas.
sintomas_usuario = ["fiebre", "tos", "dolor_cabeza"]

# Realizamos el diagnóstico basado en los síntomas.
diagnosticos_usuario = realizar_diagnostico(sintomas_usuario)

# Determinamos las posibles causas basadas en los diagnósticos.
causas_usuario = determinar_causas(diagnosticos_usuario)

# Mostramos los resultados al usuario.
print("Sintomas reportados:", sintomas_usuario)
print("Diagnosticos posibles:", diagnosticos_usuario)
print("Causas posibles:", causas_usuario)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza dos diccionarios (`reglas_diagnostico` y `reglas_causales`) 
#    para mapear síntomas a diagnósticos y diagnósticos a causas, respectivamente.
# 2. La función `realizar_diagnostico` busca coincidencias entre los síntomas reportados
#    y las claves del diccionario `reglas_diagnostico`.
# 3. La función `determinar_causas` busca coincidencias entre los diagnósticos obtenidos
#    y las claves del diccionario `reglas_causales`.
# 4. Este enfoque es simple pero efectivo para sistemas de diagnóstico básicos.
# 5. Limitaciones: No considera múltiples causas para un diagnóstico ni relaciones complejas.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO ADICIONAL
# ------------------------------------------------------------------------------------
# Supongamos que un nuevo usuario reporta los síntomas: "nauseas" y "dolor_garganta".
nuevos_sintomas = ["nauseas", "dolor_garganta"]

# Realizamos el diagnóstico para los nuevos síntomas.
nuevos_diagnosticos = realizar_diagnostico(nuevos_sintomas)

# Determinamos las posibles causas para los nuevos diagnósticos.
nuevas_causas = determinar_causas(nuevos_diagnosticos)

# Mostramos los resultados al usuario.
print("Sintomas reportados (nuevo caso):", nuevos_sintomas)
print("Diagnosticos posibles (nuevo caso):", nuevos_diagnosticos)
print("Causas posibles (nuevo caso):", nuevas_causas)