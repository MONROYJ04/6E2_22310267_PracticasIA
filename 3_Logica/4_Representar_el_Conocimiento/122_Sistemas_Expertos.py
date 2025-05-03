# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA EXPERTO PARA DIAGNÓSTICO MÉDICO
# ------------------------------------------------------------------------------------
# Este código implementa un sistema experto básico que diagnostica enfermedades
# basándose en los síntomas proporcionados por el usuario. Utiliza una base de 
# conocimiento predefinida con reglas simples para realizar el diagnóstico.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Aquí se define la función `diagnosticar_enfermedad`, que toma como entrada una 
#   lista de síntomas proporcionados por el usuario.
# - La función compara los síntomas del usuario con una base de conocimiento que 
#   relaciona síntomas con enfermedades.
# - Devuelve un diagnóstico basado en la coincidencia de los síntomas.

def diagnosticar_enfermedad(sintomas_usuario):
    """
    Esta función toma una lista de síntomas proporcionados por el usuario
    y devuelve un diagnóstico basado en reglas predefinidas.
    """
    # --------------------------------------------------------------------------------
    # PASO 2: DEFINICIÓN DE LA BASE DE CONOCIMIENTO
    # --------------------------------------------------------------------------------
    # - La base de conocimiento es un diccionario que asocia enfermedades con sus 
    #   síntomas característicos.
    # - Cada clave del diccionario es el nombre de una enfermedad, y su valor es 
    #   una lista de síntomas asociados.
    # - Esto permite que el sistema experto realice comparaciones simples.
    base_conocimiento = {
        "gripe": ["fiebre", "tos", "dolor_garganta", "congestion_nasal"],
        "resfriado": ["tos", "congestion_nasal", "estornudos"],
        "alergia": ["estornudos", "picazon_ojos", "congestion_nasal"],
        "covid": ["fiebre", "tos", "dificultad_respirar", "perdida_olfato"]
    }

    # --------------------------------------------------------------------------------
    # PASO 3: INICIALIZACIÓN DEL DIAGNÓSTICO
    # --------------------------------------------------------------------------------
    # - Se inicializa la variable `diagnostico` con un mensaje predeterminado.
    # - Este mensaje se utiliza si no se encuentra una coincidencia en la base de 
    #   conocimiento.
    diagnostico = "No se pudo determinar la enfermedad con los síntomas proporcionados."

    # --------------------------------------------------------------------------------
    # PASO 4: COMPARACIÓN DE SÍNTOMAS
    # --------------------------------------------------------------------------------
    # - Se recorre la base de conocimiento para comparar los síntomas del usuario 
    #   con los síntomas de cada enfermedad.
    # - Si todos los síntomas de una enfermedad están presentes en los síntomas 
    #   proporcionados por el usuario, se asigna el diagnóstico correspondiente.
    for enfermedad, sintomas in base_conocimiento.items():
        # `all()` verifica si todos los síntomas de la enfermedad están en la lista 
        # de síntomas del usuario.
        if all(sintoma in sintomas_usuario for sintoma in sintomas):
            diagnostico = f"El diagnóstico probable es: {enfermedad.capitalize()}."
            break

    # --------------------------------------------------------------------------------
    # PASO 5: RETORNO DEL DIAGNÓSTICO
    # --------------------------------------------------------------------------------
    # - La función devuelve el diagnóstico final, ya sea una enfermedad específica 
    #   o el mensaje predeterminado.
    return diagnostico


# ------------------------------------------------------------------------------------
# PASO 6: INTERACCIÓN CON EL USUARIO
# ------------------------------------------------------------------------------------
# - Este bloque permite que el usuario interactúe con el sistema experto.
# - Se solicita al usuario que ingrese sus síntomas como texto, separados por comas.
# - Los síntomas se procesan y se pasan a la función `diagnosticar_enfermedad`.

if __name__ == "__main__":
    # Mensaje de bienvenida
    print("Bienvenido al sistema experto de diagnóstico médico.")
    print("Por favor, ingrese sus síntomas separados por comas (por ejemplo: fiebre, tos, dolor_garganta):")
    
    # Entrada del usuario
    entrada_usuario = input()

    # --------------------------------------------------------------------------------
    # PASO 7: PROCESAMIENTO DE LA ENTRADA
    # --------------------------------------------------------------------------------
    # - La entrada del usuario se convierte en una lista de síntomas.
    # - Se eliminan espacios en blanco y se convierten a minúsculas para evitar 
    #   problemas de formato.
    sintomas_usuario = [sintoma.strip().lower() for sintoma in entrada_usuario.split(",")]

    # --------------------------------------------------------------------------------
    # PASO 8: OBTENCIÓN DEL DIAGNÓSTICO
    # --------------------------------------------------------------------------------
    # - Se llama a la función `diagnosticar_enfermedad` con los síntomas procesados.
    # - El resultado se almacena en la variable `resultado`.
    resultado = diagnosticar_enfermedad(sintomas_usuario)

    # --------------------------------------------------------------------------------
    # PASO 9: MOSTRAR EL RESULTADO
    # --------------------------------------------------------------------------------
    # - Se muestra el diagnóstico al usuario.
    print(resultado)


# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este sistema experto utiliza una base de conocimiento simple (diccionario) para 
#    relacionar síntomas con enfermedades.
# 2. La función `all()` verifica si todos los síntomas de una enfermedad están 
#    presentes en los síntomas proporcionados por el usuario.
# 3. Ventajas:
#    - Fácil de entender y modificar.
#    - Útil para problemas simples con reglas claras.
# 4. Limitaciones:
#    - No maneja incertidumbre (ejemplo: síntomas parciales o probabilidad).
#    - No escala bien para bases de conocimiento grandes.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Entrada del usuario: "fiebre, tos, dolor_garganta"
# Procesamiento:
# - Lista de síntomas: ["fiebre", "tos", "dolor_garganta"]
# Diagnóstico:
# - Coincidencia con "gripe" en la base de conocimiento.
# Resultado:
# - "El diagnóstico probable es: Gripe."