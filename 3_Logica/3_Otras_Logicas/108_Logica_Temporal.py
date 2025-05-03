# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE LÓGICA TEMPORAL PARA COMPARAR EVENTOS EN EL TIEMPO
# ------------------------------------------------------------------------------------
# Este código permite comparar dos eventos definidos por fechas y horas para determinar 
# si uno ocurre antes, después o al mismo tiempo que el otro. Es útil para analizar 
# secuencias temporales en aplicaciones como calendarios, planificación de tareas, etc.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LA BIBLIOTECA NECESARIA
# ------------------------------------------------------------------------------------
# - Importamos `datetime` de la biblioteca estándar de Python.
# - `datetime` nos permite trabajar con fechas y horas de manera sencilla.
# - Es esencial para convertir cadenas de texto en objetos de tipo fecha/hora.
from datetime import datetime

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - La función `verificar_orden_eventos` compara dos eventos en el tiempo.
# - Recibe dos parámetros: `evento1` y `evento2`, que son cadenas de texto con formato 
#   'YYYY-MM-DD HH:MM:SS' (año-mes-día hora:minuto:segundo).
# - Devuelve un mensaje indicando si el primer evento ocurre antes, después o al mismo 
#   tiempo que el segundo.
def verificar_orden_eventos(evento1, evento2):
    """
    Esta función determina si un evento ocurre antes o después de otro.
    
    Parámetros:
    evento1 (str): Fecha y hora del primer evento en formato 'YYYY-MM-DD HH:MM:SS'.
    evento2 (str): Fecha y hora del segundo evento en formato 'YYYY-MM-DD HH:MM:SS'.
    
    Retorna:
    str: Mensaje indicando si el evento1 ocurre antes, después o al mismo tiempo que el evento2.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: CONVERTIR CADENAS EN OBJETOS DATETIME
    # --------------------------------------------------------------------------------
    # - Usamos `datetime.strptime` para convertir las cadenas de texto en objetos 
    #   `datetime`. Esto nos permite realizar comparaciones entre fechas y horas.
    # - `strptime` requiere que el formato de las cadenas coincida exactamente con 
    #   'YYYY-MM-DD HH:MM:SS'.
    tiempo_evento1 = datetime.strptime(evento1, '%Y-%m-%d %H:%M:%S')
    tiempo_evento2 = datetime.strptime(evento2, '%Y-%m-%d %H:%M:%S')
    
    # --------------------------------------------------------------------------------
    # PASO 2.2: COMPARAR LOS OBJETOS DATETIME
    # --------------------------------------------------------------------------------
    # - Comparamos los objetos `datetime` usando operadores relacionales:
    #   - `<` significa "antes".
    #   - `>` significa "después".
    #   - `==` significa "al mismo tiempo".
    # - Según el resultado, devolvemos un mensaje descriptivo.
    if tiempo_evento1 < tiempo_evento2:
        return "El evento1 ocurre antes que el evento2."
    elif tiempo_evento1 > tiempo_evento2:
        return "El evento1 ocurre después que el evento2."
    else:
        return "El evento1 y el evento2 ocurren al mismo tiempo."

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este bloque, probamos la función con dos eventos definidos por fechas y horas.
# - Mostramos el resultado en la consola para verificar el funcionamiento del algoritmo.
if __name__ == "__main__":
    # --------------------------------------------------------------------------------
    # PASO 3.1: DEFINIR LOS EVENTOS
    # --------------------------------------------------------------------------------
    # - Creamos dos eventos con fechas y horas específicas.
    # - Usamos el formato 'YYYY-MM-DD HH:MM:SS' para que sean compatibles con la función.
    evento1 = "2025-05-01 14:30:00"  # Evento 1: 1 de mayo de 2025 a las 14:30
    evento2 = "2025-05-03 10:00:00"  # Evento 2: 3 de mayo de 2025 a las 10:00
    
    # --------------------------------------------------------------------------------
    # PASO 3.2: LLAMAR A LA FUNCIÓN Y MOSTRAR EL RESULTADO
    # --------------------------------------------------------------------------------
    # - Llamamos a `verificar_orden_eventos` con los eventos definidos.
    # - Imprimimos el resultado para que el usuario lo vea.
    resultado = verificar_orden_eventos(evento1, evento2)
    print(resultado)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza la biblioteca `datetime` para convertir cadenas de texto en 
#    objetos de tipo fecha/hora. Esto permite realizar comparaciones precisas.
# 2. Supone que las fechas están en el formato 'YYYY-MM-DD HH:MM:SS'. Si el formato no 
#    coincide, se generará un error.
# 3. Ventajas:
#    - Fácil de usar y entender.
#    - Útil para aplicaciones que requieren análisis temporal.
# 4. Limitaciones:
#    - No maneja zonas horarias (los eventos deben estar en la misma zona horaria).
#    - No valida el formato de las cadenas (se espera que el usuario proporcione datos válidos).

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO ADICIONAL
# ------------------------------------------------------------------------------------
# Supongamos que queremos comparar dos eventos:
# - Evento A: "2025-12-25 18:00:00" (Navidad a las 6 PM).
# - Evento B: "2025-12-25 12:00:00" (Navidad al mediodía).
# Resultado esperado: "El evento1 ocurre después que el evento2."
evento_a = "2025-12-25 18:00:00"
evento_b = "2025-12-25 12:00:00"
print(verificar_orden_eventos(evento_a, evento_b))