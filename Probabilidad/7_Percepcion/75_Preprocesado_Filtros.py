# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FILTRO DE DESENFOQUE PARA REDUCCIÓN DE RUIDO EN IMÁGENES
# ------------------------------------------------------------------------------------
# Este código aplica un filtro de desenfoque gaussiano a una imagen para reducir el ruido.
# El desenfoque es útil en preprocesamiento de imágenes, especialmente antes de realizar
# tareas como detección de bordes o segmentación.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `cv2` para trabajar con imágenes (cargar, procesar y mostrar).
# - Importamos `numpy` para realizar operaciones matemáticas con matrices.
import cv2  # Biblioteca para procesamiento de imágenes
import numpy as np  # Biblioteca para operaciones matemáticas con matrices

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA APLICAR EL FILTRO DE DESENFOQUE
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada la ruta de una imagen y el tamaño del kernel.
# - El kernel es una matriz cuadrada que define la intensidad del desenfoque.
# - Devuelve la imagen procesada con el filtro aplicado.
def aplicar_filtro_desfoque(ruta_imagen, tamano_kernel):
    """
    Aplica un filtro de desenfoque a una imagen.

    Parametros:
    ruta_imagen (str): Ruta de la imagen que se desea procesar.
    tamano_kernel (int): Tamaño del kernel (matriz) para el filtro de desenfoque. Debe ser un número impar.

    Retorna:
    imagen_filtrada (numpy.ndarray): Imagen procesada con el filtro de desenfoque.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: CARGAR LA IMAGEN DESDE LA RUTA ESPECIFICADA
    # --------------------------------------------------------------------------------
    # - Usamos `cv2.imread` para cargar la imagen desde el disco.
    # - Si la imagen no se encuentra o no se puede cargar, devolvemos un mensaje de error.
    imagen = cv2.imread(ruta_imagen)

    # Verificamos si la imagen se cargó correctamente
    if imagen is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return None

    # --------------------------------------------------------------------------------
    # PASO 2.2: APLICAR EL FILTRO DE DESENFOQUE
    # --------------------------------------------------------------------------------
    # - Usamos `cv2.GaussianBlur` para aplicar un filtro gaussiano.
    # - El tamaño del kernel debe ser impar (ej: 3, 5, 7).
    # - El tercer parámetro (sigmaX) controla la desviación estándar del filtro.
    imagen_filtrada = cv2.GaussianBlur(imagen, (tamano_kernel, tamano_kernel), 0)

    # --------------------------------------------------------------------------------
    # PASO 2.3: RETORNAR LA IMAGEN FILTRADA
    # --------------------------------------------------------------------------------
    # - Devolvemos la imagen procesada para que pueda ser utilizada o mostrada.
    return imagen_filtrada

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque ejecuta el código si el archivo se ejecuta directamente.
# - Carga una imagen, aplica el filtro y muestra los resultados.
if __name__ == "__main__":
    # --------------------------------------------------------------------------------
    # PASO 3.1: DEFINIR LA RUTA DE LA IMAGEN Y EL TAMAÑO DEL KERNEL
    # --------------------------------------------------------------------------------
    # - `ruta_imagen` debe ser la ruta de una imagen válida en tu sistema.
    # - `tamano_kernel` define la intensidad del desenfoque (debe ser impar).
    ruta_imagen = "ejemplo.jpg"  # Cambia esto por la ruta de tu imagen
    tamano_kernel = 5  # Tamaño del kernel (ej: 3, 5, 7)

    # --------------------------------------------------------------------------------
    # PASO 3.2: APLICAR EL FILTRO DE DESENFOQUE
    # --------------------------------------------------------------------------------
    # - Llamamos a la función `aplicar_filtro_desfoque` con los parámetros definidos.
    # - Guardamos el resultado en la variable `imagen_procesada`.
    imagen_procesada = aplicar_filtro_desfoque(ruta_imagen, tamano_kernel)

    # --------------------------------------------------------------------------------
    # PASO 3.3: MOSTRAR LOS RESULTADOS
    # --------------------------------------------------------------------------------
    # - Si la imagen fue procesada correctamente, mostramos la original y la filtrada.
    # - Usamos `cv2.imshow` para abrir ventanas con las imágenes.
    if imagen_procesada is not None:
        # Mostramos la imagen original y la imagen procesada
        cv2.imshow("Imagen Original", cv2.imread(ruta_imagen))
        cv2.imshow("Imagen Filtrada (Desenfoque)", imagen_procesada)

        # Esperamos a que el usuario presione una tecla para cerrar las ventanas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El filtro de desenfoque gaussiano utiliza una matriz (kernel) para suavizar la imagen.
#    La fórmula del filtro gaussiano es:
#        G(x, y) = (1 / (2 * π * σ^2)) * e^(-(x^2 + y^2) / (2 * σ^2))
#    Donde `σ` es la desviación estándar y controla la intensidad del desenfoque.
# 2. Este filtro es útil para reducir el ruido en imágenes antes de aplicar otros
#    algoritmos como detección de bordes o segmentación.
# 3. Ventajas:
#    - Suaviza la imagen de manera uniforme.
#    - Reduce el ruido sin eliminar detalles importantes.
# 4. Limitaciones:
#    - Puede perder detalles finos si el kernel es demasiado grande.
#    - No es adecuado para imágenes donde se requiere alta precisión en bordes.