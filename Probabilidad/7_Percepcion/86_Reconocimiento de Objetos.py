# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RECONOCIMIENTO DE OBJETOS EN IMÁGENES
# ------------------------------------------------------------------------------------
# Este código utiliza técnicas de procesamiento de imágenes para detectar y resaltar
# los contornos de objetos presentes en una imagen. Se apoya en la biblioteca OpenCV
# para realizar operaciones como conversión de color, detección de bordes y contornos.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS
# ------------------------------------------------------------------------------------
# - Importamos las bibliotecas necesarias para el procesamiento de imágenes y cálculos.
# - OpenCV (`cv2`) se utiliza para manipular imágenes y realizar operaciones avanzadas.
# - NumPy (`np`) es útil para manejar datos en forma de matrices (aunque no se usa aquí).
import cv2  # Biblioteca para procesamiento de imágenes
import numpy as np  # Biblioteca para operaciones matemáticas

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Creamos una función llamada `reconocer_objetos` que realiza el reconocimiento de
#   objetos en una imagen.
# - La función toma como entrada la ruta de la imagen (`ruta_imagen`) y no retorna nada.
def reconocer_objetos(ruta_imagen):
    """
    Esta función realiza el reconocimiento de objetos en una imagen.
    Utiliza técnicas de procesamiento de imágenes para detectar contornos.
    
    Parámetros:
    ruta_imagen (str): Ruta de la imagen que se desea analizar.
    
    Retorna:
    None
    """
    # --------------------------------------------------------------------------------
    # PASO 3: CARGA DE LA IMAGEN
    # --------------------------------------------------------------------------------
    # - Cargamos la imagen desde la ruta proporcionada utilizando `cv2.imread`.
    # - Si la imagen no se carga correctamente (por ejemplo, si la ruta es incorrecta),
    #   mostramos un mensaje de error y terminamos la ejecución de la función.
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return

    # --------------------------------------------------------------------------------
    # PASO 4: CONVERSIÓN A ESCALA DE GRISES
    # --------------------------------------------------------------------------------
    # - Convertimos la imagen a escala de grises usando `cv2.cvtColor`.
    # - Esto simplifica el procesamiento, ya que reduce la cantidad de información
    #   (de color) que debe analizarse.
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # --------------------------------------------------------------------------------
    # PASO 5: REDUCCIÓN DE RUIDO
    # --------------------------------------------------------------------------------
    # - Aplicamos un desenfoque gaussiano con `cv2.GaussianBlur` para suavizar la imagen.
    # - Esto ayuda a reducir el ruido y mejora la detección de bordes en el siguiente paso.
    # - Parámetros clave:
    #   - `(5, 5)`: Tamaño del kernel (ventana de desenfoque).
    #   - `0`: Desviación estándar del desenfoque (calculada automáticamente).
    imagen_desenfocada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

    # --------------------------------------------------------------------------------
    # PASO 6: DETECCIÓN DE BORDES
    # --------------------------------------------------------------------------------
    # - Usamos el algoritmo de Canny (`cv2.Canny`) para detectar bordes en la imagen.
    # - Este algoritmo identifica cambios bruscos en la intensidad de los píxeles.
    # - Parámetros clave:
    #   - `50`: Umbral inferior para la detección de bordes.
    #   - `150`: Umbral superior para la detección de bordes.
    bordes = cv2.Canny(imagen_desenfocada, 50, 150)

    # --------------------------------------------------------------------------------
    # PASO 7: DETECCIÓN DE CONTORNOS
    # --------------------------------------------------------------------------------
    # - Encontramos los contornos en la imagen usando `cv2.findContours`.
    # - Los contornos son líneas cerradas que delimitan los bordes detectados.
    # - Parámetros clave:
    #   - `cv2.RETR_EXTERNAL`: Recupera solo los contornos externos.
    #   - `cv2.CHAIN_APPROX_SIMPLE`: Reduce los puntos redundantes en los contornos.
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # --------------------------------------------------------------------------------
    # PASO 8: DIBUJAR LOS CONTORNOS
    # --------------------------------------------------------------------------------
    # - Dibujamos los contornos detectados sobre la imagen original usando `cv2.drawContours`.
    # - Parámetros clave:
    #   - `imagen.copy()`: Creamos una copia de la imagen original para no modificarla.
    #   - `contornos`: Lista de contornos detectados.
    #   - `-1`: Dibuja todos los contornos.
    #   - `(0, 255, 0)`: Color verde para los contornos.
    #   - `2`: Grosor de las líneas de los contornos.
    imagen_contornos = imagen.copy()
    cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

    # --------------------------------------------------------------------------------
    # PASO 9: MOSTRAR RESULTADOS
    # --------------------------------------------------------------------------------
    # - Mostramos la imagen original y la imagen con los contornos detectados.
    # - Usamos `cv2.imshow` para abrir ventanas con las imágenes.
    # - Esperamos a que el usuario presione una tecla para cerrar las ventanas.
    cv2.imshow("Imagen Original", imagen)
    cv2.imshow("Contornos Detectados", imagen_contornos)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------
# PASO 10: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Definimos la ruta de una imagen de ejemplo (asegúrate de que sea válida en tu sistema).
# - Llamamos a la función `reconocer_objetos` para analizar la imagen.
ruta_ejemplo = "d:/Documentos/GitHub/6E2_22310267_PracticasIA/Probabilidad/Percepcion/ejemplo.jpg"
reconocer_objetos(ruta_ejemplo)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza técnicas de procesamiento de imágenes para detectar bordes
#    y contornos en una imagen. Esto se logra mediante:
#    - Conversión a escala de grises para simplificar la información.
#    - Reducción de ruido para mejorar la precisión de los bordes detectados.
#    - Detección de bordes con el algoritmo de Canny.
#    - Detección de contornos basados en los bordes.
# 2. Suposiciones clave:
#    - La imagen tiene suficiente contraste para que los bordes sean detectables.
#    - Los parámetros de Canny y desenfoque están ajustados adecuadamente.
# 3. Ventajas/limitaciones:
#    - Ventaja: Es rápido y eficiente para imágenes con buen contraste.
#    - Limitación: Puede fallar en imágenes con bajo contraste o mucho ruido.