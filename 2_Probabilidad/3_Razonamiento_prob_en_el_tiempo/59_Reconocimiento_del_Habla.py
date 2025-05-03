# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RECONOCIMIENTO DEL HABLA PARA CONVERTIR AUDIO EN TEXTO
# ------------------------------------------------------------------------------------
# Este programa utiliza la biblioteca `speech_recognition` para capturar audio desde
# el micrófono y convertirlo en texto utilizando el servicio de reconocimiento de voz
# de Google. Es útil para aplicaciones como asistentes virtuales o transcripción.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LA BIBLIOTECA NECESARIA
# ------------------------------------------------------------------------------------
# - Importamos la biblioteca `speech_recognition` como `sr`.
# - Esta biblioteca proporciona herramientas para capturar y procesar audio.
import speech_recognition as sr

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Creamos una función llamada `reconocimiento_habla`.
# - Esta función captura el audio del micrófono y lo convierte en texto.
# - Incluye manejo de errores para casos en los que no se entienda el audio o haya
#   problemas con el servicio de reconocimiento.
def reconocimiento_habla():
    """
    Esta función utiliza la biblioteca speech_recognition para convertir
    el audio capturado por el micrófono en texto.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: CREAR EL OBJETO RECONOCEDOR
    # --------------------------------------------------------------------------------
    # - Creamos un objeto de la clase `Recognizer` llamado `reconocedor`.
    # - Este objeto es el encargado de procesar el audio y convertirlo en texto.
    reconocedor = sr.Recognizer()

    # --------------------------------------------------------------------------------
    # PASO 2.2: CONFIGURAR EL MICRÓFONO COMO FUENTE DE AUDIO
    # --------------------------------------------------------------------------------
    # - Usamos el micrófono como fuente de entrada de audio.
    # - El bloque `with` asegura que los recursos del micrófono se liberen al terminar.
    with sr.Microphone() as fuente_audio:
        print("Por favor, hable claramente para que el sistema lo reconozca...")
        
        # ---------------------------------------------------------------------------
        # PASO 2.3: AJUSTAR EL RUIDO AMBIENTAL
        # ---------------------------------------------------------------------------
        # - Ajustamos el nivel de ruido ambiental para mejorar la calidad del audio.
        # - Esto es útil en entornos ruidosos, ya que filtra sonidos de fondo.
        reconocedor.adjust_for_ambient_noise(fuente_audio)
        
        try:
            # -----------------------------------------------------------------------
            # PASO 2.4: ESCUCHAR EL AUDIO DEL USUARIO
            # -----------------------------------------------------------------------
            # - Capturamos el audio del usuario utilizando el método `listen`.
            # - Este método graba el audio desde el micrófono.
            audio = reconocedor.listen(fuente_audio)
            
            # -----------------------------------------------------------------------
            # PASO 2.5: CONVERTIR EL AUDIO EN TEXTO
            # -----------------------------------------------------------------------
            # - Usamos el método `recognize_google` para convertir el audio en texto.
            # - Especificamos el idioma como español ("es-ES").
            texto = reconocedor.recognize_google(audio, language="es-ES")
            
            # -----------------------------------------------------------------------
            # PASO 2.6: MOSTRAR EL TEXTO RECONOCIDO
            # -----------------------------------------------------------------------
            # - Imprimimos el texto reconocido en la consola.
            print("Usted dijo: ", texto)
        
        except sr.UnknownValueError:
            # -----------------------------------------------------------------------
            # PASO 2.7: MANEJO DE ERRORES - AUDIO NO ENTENDIDO
            # -----------------------------------------------------------------------
            # - Este error ocurre si el sistema no puede entender el audio.
            # - Mostramos un mensaje indicando que no se pudo reconocer el audio.
            print("No se pudo entender el audio. Por favor, intente de nuevo.")
        
        except sr.RequestError as e:
            # -----------------------------------------------------------------------
            # PASO 2.8: MANEJO DE ERRORES - PROBLEMAS CON EL SERVICIO
            # -----------------------------------------------------------------------
            # - Este error ocurre si hay un problema con el servicio de Google.
            # - Mostramos un mensaje indicando el error específico.
            print("Error con el servicio de reconocimiento: ", e)

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque se ejecuta solo si el archivo se ejecuta directamente.
# - Llama a la función `reconocimiento_habla` para que el usuario pueda probar el
#   sistema de reconocimiento del habla.
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo si el archivo se ejecuta directamente.
    Llama a la función de reconocimiento del habla para que el usuario
    pueda probar el sistema.
    """
    reconocimiento_habla()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza la biblioteca `speech_recognition` para capturar audio desde
#    el micrófono y convertirlo en texto utilizando el servicio de Google.
# 2. Suposiciones clave:
#    - El micrófono está configurado correctamente y funciona.
#    - El usuario habla claramente en español.
# 3. Ventajas:
#    - Fácil de implementar y usar.
#    - Compatible con múltiples idiomas.
# 4. Limitaciones:
#    - Requiere conexión a Internet para usar el servicio de Google.
#    - Puede fallar en entornos muy ruidosos o si el usuario no habla claramente.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Cuando ejecutes este código, el sistema te pedirá que hables por el micrófono.
# - Si dices algo como "Hola, ¿cómo estás?", el programa debería mostrar:
#   `Usted dijo: Hola, ¿cómo estás?`