# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA EXPERTO PARA DIAGNÓSTICO DE PROBLEMAS EN COMPUTADORAS
# ------------------------------------------------------------------------------------
# Este código implementa un sistema basado en reglas que utiliza conocimientos predefinidos
# para diagnosticar problemas comunes en una computadora. El usuario responde preguntas
# simples, y el sistema genera un diagnóstico basado en las respuestas.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - La función `diagnosticar_problema` evalúa las respuestas del usuario.
# - Utiliza un conjunto de reglas predefinidas para determinar el diagnóstico.
# - Recibe un diccionario `respuestas` con las respuestas del usuario como entrada.
# - Devuelve un mensaje con el diagnóstico basado en las reglas.

def diagnosticar_problema(respuestas):
    """
    Diagnostica problemas basados en las respuestas del usuario.
    
    :param respuestas: Diccionario con las respuestas del usuario a las preguntas.
    :return: Diagnostico basado en las reglas.
    """
    # --------------------------------------------------------------------------------
    # PASO 2: EVALUACIÓN DE LAS REGLAS DEL SISTEMA EXPERTO
    # --------------------------------------------------------------------------------
    # - Este bloque contiene las reglas del sistema experto.
    # - Cada regla evalúa una condición específica basada en las respuestas del usuario.
    # - Si se cumple una regla, se devuelve un diagnóstico correspondiente.
    # - Las reglas están organizadas en un árbol lógico para cubrir diferentes escenarios.

    if respuestas["enciende"] == "no":  # Si la computadora no enciende
        if respuestas["cable_conectado"] == "no":  # Si el cable no está conectado
            return "Conecta el cable de alimentacion."
        elif respuestas["bateria_cargada"] == "no":  # Si la batería no está cargada
            return "Carga la bateria o conecta el cargador."
        else:  # Si ninguna de las anteriores aplica
            return "El problema puede estar en el hardware interno. Lleva la computadora a un tecnico."
    elif respuestas["enciende"] == "si":  # Si la computadora enciende
        if respuestas["pantalla_muestra_algo"] == "no":  # Si la pantalla no muestra nada
            return "Revisa la conexion de la pantalla o el estado de la tarjeta grafica."
        elif respuestas["sistema_operativo_carga"] == "no":  # Si el sistema operativo no carga
            return "Reinstala el sistema operativo o revisa el disco duro."
        else:  # Si todo parece estar funcionando
            return "La computadora parece estar funcionando correctamente."
    else:  # Si las respuestas no son claras
        return "No se pudo determinar el problema. Proporciona mas informacion."

# ------------------------------------------------------------------------------------
# PASO 3: EJECUCIÓN DEL PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------------
# - Este bloque interactúa con el usuario para recopilar las respuestas.
# - Las respuestas se almacenan en un diccionario llamado `respuestas`.
# - Se llama a la función `diagnosticar_problema` con las respuestas del usuario.
# - Finalmente, se imprime el diagnóstico generado.

if __name__ == "__main__":
    # --------------------------------------------------------------------------------
    # PASO 4: RECOLECCIÓN DE RESPUESTAS DEL USUARIO
    # --------------------------------------------------------------------------------
    # - Se hacen preguntas al usuario sobre el estado de la computadora.
    # - Las respuestas se convierten a minúsculas y se eliminan espacios adicionales.
    # - Esto asegura que las respuestas sean consistentes para la evaluación.

    print("Responde las siguientes preguntas con 'si' o 'no':")
    respuestas = {}
    respuestas["enciende"] = input("¿La computadora enciende? ").strip().lower()
    respuestas["cable_conectado"] = input("¿El cable de alimentacion esta conectado? ").strip().lower()
    respuestas["bateria_cargada"] = input("¿La bateria esta cargada? ").strip().lower()
    respuestas["pantalla_muestra_algo"] = input("¿La pantalla muestra algo? ").strip().lower()
    respuestas["sistema_operativo_carga"] = input("¿El sistema operativo carga correctamente? ").strip().lower()

    # --------------------------------------------------------------------------------
    # PASO 5: GENERACIÓN DEL DIAGNÓSTICO
    # --------------------------------------------------------------------------------
    # - Se llama a la función `diagnosticar_problema` con las respuestas del usuario.
    # - El diagnóstico generado se imprime en pantalla.

    diagnostico = diagnosticar_problema(respuestas)
    print("\nDiagnostico:")
    print(diagnostico)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este sistema experto utiliza un enfoque basado en reglas para diagnosticar problemas.
# 2. Las reglas están organizadas en un árbol lógico, evaluando condiciones específicas.
# 3. Ventajas:
#    - Fácil de entender y modificar.
#    - Útil para problemas bien definidos.
# 4. Limitaciones:
#    - No puede manejar problemas fuera del alcance de las reglas predefinidas.
#    - Depende completamente de la calidad de las reglas implementadas.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que el usuario responde lo siguiente:
# - ¿La computadora enciende? no
# - ¿El cable de alimentación está conectado? no
# - ¿La batería está cargada? si
# - ¿La pantalla muestra algo? si
# - ¿El sistema operativo carga correctamente? si
#
# Resultado:
# Diagnóstico: "Conecta el cable de alimentacion."