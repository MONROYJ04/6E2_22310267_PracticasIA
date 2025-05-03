# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: EXTRACCIÓN DE INFORMACIÓN PARA CORREOS Y TELÉFONOS
# ------------------------------------------------------------------------------------
# Este código tiene como objetivo extraer información específica (correos electrónicos y números
# de teléfono) de un texto dado utilizando expresiones regulares. Es útil para procesar datos
# no estructurados y obtener información clave de manera automatizada.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LA LIBRERÍA NECESARIA
# ------------------------------------------------------------------------------------
# - Importamos la librería `re`, que permite trabajar con expresiones regulares en Python.
# - Las expresiones regulares son patrones que permiten buscar coincidencias en cadenas de texto.
import re

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA EXTRAER CORREOS ELECTRÓNICOS
# ------------------------------------------------------------------------------------
# - Esta función busca y extrae todas las direcciones de correo electrónico presentes en un texto.
# - Utiliza una expresión regular que identifica el formato estándar de los correos electrónicos.
# - Devuelve una lista con todos los correos encontrados.
def extraer_correos(texto):
    """
    Esta función busca y extrae todas las direcciones de correo electrónico en un texto dado.
    :param texto: Cadena de texto donde se buscarán los correos.
    :return: Lista de correos electrónicos encontrados.
    """
    # Expresión regular para encontrar correos electrónicos:
    # - `[a-zA-Z0-9._%+-]+`: Busca caracteres válidos antes del símbolo `@`.
    # - `@[a-zA-Z0-9.-]+`: Busca el dominio después del `@`.
    # - `\.[a-zA-Z]{2,}`: Busca la extensión del dominio (ej: `.com`, `.org`).
    patron_correos = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Usamos `re.findall` para encontrar todas las coincidencias en el texto.
    correos = re.findall(patron_correos, texto)
    return correos

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN PARA EXTRAER NÚMEROS DE TELÉFONO
# ------------------------------------------------------------------------------------
# - Esta función busca y extrae todos los números de teléfono presentes en un texto.
# - Utiliza una expresión regular que identifica números de exactamente 10 dígitos.
# - Devuelve una lista con todos los números encontrados.
def extraer_telefonos(texto):
    """
    Esta función busca y extrae todos los números de teléfono en un texto dado.
    :param texto: Cadena de texto donde se buscarán los números de teléfono.
    :return: Lista de números de teléfono encontrados.
    """
    # Expresión regular para encontrar números de teléfono:
    # - `\b`: Asegura que el número esté delimitado por espacios o inicio/fin de línea.
    # - `\d{10}`: Busca exactamente 10 dígitos consecutivos.
    # - `\b`: Asegura que el número esté delimitado al final.
    patron_telefonos = r'\b\d{10}\b'
    
    # Usamos `re.findall` para encontrar todas las coincidencias en el texto.
    telefonos = re.findall(patron_telefonos, texto)
    return telefonos

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este bloque se utiliza un texto de ejemplo que contiene correos electrónicos y números
#   de teléfono.
# - Se llaman las funciones `extraer_correos` y `extraer_telefonos` para extraer la información.
# - Los resultados se imprimen en la consola para verificar el funcionamiento del algoritmo.
if __name__ == "__main__":
    # Texto de ejemplo que contiene correos y números de teléfono.
    texto_ejemplo = """
    Hola, mi nombre es Juan Perez. Puedes contactarme en juan.perez@example.com o en mi telefono 1234567890.
    Tambien puedes escribir a mi correo alternativo juanito123@correo.com o llamarme al 0987654321.
    """

    # Extraemos los correos del texto.
    correos_encontrados = extraer_correos(texto_ejemplo)
    print("Correos encontrados:", correos_encontrados)

    # Extraemos los números de teléfono del texto.
    telefonos_encontrados = extraer_telefonos(texto_ejemplo)
    print("Teléfonos encontrados:", telefonos_encontrados)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza expresiones regulares para buscar patrones específicos en un texto.
#    - Correos electrónicos: Se basan en el formato estándar `usuario@dominio.ext`.
#    - Números de teléfono: Se asume que tienen exactamente 10 dígitos.
# 2. Suposiciones clave:
#    - Los correos electrónicos y números de teléfono están correctamente formateados.
#    - Los números de teléfono no contienen espacios ni caracteres adicionales.
# 3. Ventajas:
#    - Es rápido y eficiente para procesar grandes cantidades de texto.
#    - Fácil de adaptar a otros patrones de búsqueda.
# 4. Limitaciones:
#    - No detecta formatos de números de teléfono internacionales o con separadores (ej: `123-456-7890`).
#    - No valida si los correos electrónicos o números de teléfono son reales.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Entrada:
# """
# Hola, mi nombre es Juan Perez. Puedes contactarme en juan.perez@example.com o en mi telefono 1234567890.
# Tambien puedes escribir a mi correo alternativo juanito123@correo.com o llamarme al 0987654321.
# """
# Salida esperada:
# Correos encontrados: ['juan.perez@example.com', 'juanito123@correo.com']
# Teléfonos encontrados: ['1234567890', '0987654321']