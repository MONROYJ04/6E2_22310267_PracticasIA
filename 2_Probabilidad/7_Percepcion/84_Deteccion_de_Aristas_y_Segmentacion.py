# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: DETECCIÓN DE BORDES Y SEGMENTACIÓN DE IMÁGENES
# ------------------------------------------------------------------------------------
# Este código procesa una imagen para detectar sus bordes y realizar una segmentación básica.
# Utiliza técnicas de procesamiento de imágenes como la conversión a escala de grises, 
# desenfoque gaussiano, detección de bordes con el algoritmo de Canny y umbralización binaria.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - `cv2`: Librería OpenCV para procesamiento de imágenes.
# - `numpy`: Librería para operaciones matemáticas y manejo de matrices.
import cv2  # Librería para procesamiento de imágenes
import numpy as np  # Librería para operaciones matemáticas y matrices

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada la ruta de una imagen.
# - Realiza los pasos necesarios para detectar bordes y segmentar la imagen.
def detectar_bordes_y_segmentar(ruta_imagen):
    """
    Esta función toma la ruta de una imagen, detecta los bordes en ella y realiza una segmentación básica.
    :param ruta_imagen: Ruta de la imagen que se desea procesar.
    :return: Imagen con bordes detectados y segmentación aplicada.
    """

    # --------------------------------------------------------------------------------
    # PASO 3: CARGAR LA IMAGEN DESDE LA RUTA ESPECIFICADA
    # --------------------------------------------------------------------------------
    # - `cv2.imread`: Carga la imagen desde la ruta proporcionada.
    # - Si la imagen no se carga correctamente, se muestra un mensaje de error.
    imagen_original = cv2.imread(ruta_imagen)

    # Verificamos si la imagen se cargó correctamente
    if imagen_original is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return

    # --------------------------------------------------------------------------------
    # PASO 4: CONVERTIR LA IMAGEN A ESCALA DE GRISES
    # --------------------------------------------------------------------------------
    # - `cv2.cvtColor`: Convierte la imagen de color (RGB) a escala de grises.
    # - Esto simplifica el procesamiento al reducir la cantidad de información.
    imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

    # --------------------------------------------------------------------------------
    # PASO 5: APLICAR DESENFOQUE GAUSSIANO
    # --------------------------------------------------------------------------------
    # - `cv2.GaussianBlur`: Aplica un filtro gaussiano para reducir el ruido.
    # - Parámetros:
    #   - `(5, 5)`: Tamaño del kernel (ventana de desenfoque).
    #   - `0`: Desviación estándar calculada automáticamente.
    imagen_desenfocada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

    # --------------------------------------------------------------------------------
    # PASO 6: DETECTAR BORDES CON EL ALGORITMO DE CANNY
    # --------------------------------------------------------------------------------
    # - `cv2.Canny`: Detecta bordes en la imagen.
    # - Parámetros:
    #   - `50`: Umbral inferior para la detección de bordes.
    #   - `150`: Umbral superior para la detección de bordes.
    bordes = cv2.Canny(imagen_desenfocada, 50, 150)

    # --------------------------------------------------------------------------------
    # PASO 7: APLICAR UMBRALIZACIÓN BINARIA PARA SEGMENTACIÓN
    # --------------------------------------------------------------------------------
    # - `cv2.threshold`: Convierte la imagen en una máscara binaria.
    # - Parámetros:
    #   - `127`: Valor del umbral.
    #   - `255`: Valor máximo para los píxeles que superan el umbral.
    #   - `cv2.THRESH_BINARY`: Tipo de umbralización (binaria).
    _, segmentacion = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)

    # --------------------------------------------------------------------------------
    # PASO 8: MOSTRAR LOS RESULTADOS
    # --------------------------------------------------------------------------------
    # - `cv2.imshow`: Muestra las imágenes procesadas en ventanas separadas.
    # - `cv2.waitKey(0)`: Espera a que el usuario presione una tecla para cerrar las ventanas.
    cv2.imshow("Imagen Original", imagen_original)
    cv2.imshow("Bordes Detectados", bordes)
    cv2.imshow("Segmentacion", segmentacion)

    # Esperamos a que el usuario presione una tecla para cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------
# PASO 9: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Ruta de la imagen de ejemplo (asegúrate de cambiarla por una imagen válida en tu sistema).
# - Llamamos a la función con la ruta de la imagen.
ruta_imagen_ejemplo = "ejemplo.jpg"
detectar_bordes_y_segmentar(ruta_imagen_ejemplo)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Conversión a escala de grises**:
#    - Reduce la complejidad del procesamiento al trabajar con una sola canal de color.
# 2. **Desenfoque gaussiano**:
#    - Suaviza la imagen para eliminar ruido y evitar detecciones falsas de bordes.
# 3. **Detección de bordes (Canny)**:
#    - Identifica bordes significativos en la imagen basándose en gradientes de intensidad.
# 4. **Segmentación (umbralización binaria)**:
#    - Divide la imagen en regiones claras y oscuras para resaltar áreas de interés.
# 5. **Ventajas**:
#    - Rápido y eficiente para imágenes simples.
# 6. **Limitaciones**:
#    - No funciona bien con imágenes complejas o con mucho ruido.