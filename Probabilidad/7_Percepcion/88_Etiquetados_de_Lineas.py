# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ETIQUETADO DE LÍNEAS PARA IDENTIFICAR REGIONES CONECTADAS
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo para etiquetar regiones conectadas en una imagen binaria.
# Una imagen binaria está compuesta por valores 0 y 1, donde los valores 1 representan las regiones
# de interés. El objetivo es asignar un número único a cada región conectada.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `numpy` para manejar matrices y operaciones numéricas.
# - Importamos `matplotlib.pyplot` para visualizar las imágenes y los resultados.
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL PARA EL ETIQUETADO
# ------------------------------------------------------------------------------------
# - Esta función recorre la imagen binaria y etiqueta cada región conectada.
# - Utiliza una matriz de etiquetas para almacenar los números asignados a cada región.
# - Llama a una función auxiliar para realizar el etiquetado de cada región conectada.
def etiquetado_lineas(imagen_binaria):
    """
    Realiza el etiquetado de regiones conectadas en una imagen binaria.
    
    Parámetros:
    imagen_binaria (numpy.ndarray): Matriz binaria (0 y 1) que representa la imagen.

    Retorna:
    numpy.ndarray: Matriz con las regiones etiquetadas.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: INICIALIZAR MATRIZ DE ETIQUETAS Y CONTADOR
    # --------------------------------------------------------------------------------
    # - Creamos una matriz del mismo tamaño que la imagen binaria para almacenar las etiquetas.
    # - Inicializamos el contador de etiquetas en 1 (cada región tendrá un número único).
    etiquetas = np.zeros_like(imagen_binaria, dtype=int)
    contador_etiquetas = 1

    # --------------------------------------------------------------------------------
    # PASO 2.2: RECORRER LA IMAGEN BINARIA
    # --------------------------------------------------------------------------------
    # - Recorremos cada píxel de la imagen binaria.
    # - Si encontramos un píxel con valor 1 que no ha sido etiquetado, iniciamos el proceso
    #   de etiquetado para esa región conectada.
    filas, columnas = imagen_binaria.shape
    for i in range(filas):
        for j in range(columnas):
            if imagen_binaria[i, j] == 1 and etiquetas[i, j] == 0:
                # Llamamos a la función auxiliar para etiquetar la región conectada.
                etiquetar_region(imagen_binaria, etiquetas, i, j, contador_etiquetas)
                # Incrementamos el contador de etiquetas para la próxima región.
                contador_etiquetas += 1

    # Retornamos la matriz con las regiones etiquetadas.
    return etiquetas

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN AUXILIAR PARA ETIQUETAR REGIONES CONECTADAS
# ------------------------------------------------------------------------------------
# - Esta función utiliza una búsqueda en profundidad (DFS) para etiquetar todos los píxeles
#   conectados que pertenecen a la misma región.
# - Se utiliza una pila para explorar los píxeles vecinos.
def etiquetar_region(imagen_binaria, etiquetas, fila, columna, etiqueta):
    """
    Etiqueta una región conectada en la imagen binaria.

    Parámetros:
    imagen_binaria (numpy.ndarray): Matriz binaria (0 y 1) que representa la imagen.
    etiquetas (numpy.ndarray): Matriz donde se almacenan las etiquetas.
    fila (int): Fila actual.
    columna (int): Columna actual.
    etiqueta (int): Etiqueta asignada a la región.
    """
    # --------------------------------------------------------------------------------
    # PASO 3.1: INICIALIZAR LA PILA PARA LA BÚSQUEDA EN PROFUNDIDAD
    # --------------------------------------------------------------------------------
    # - La pila almacena las coordenadas de los píxeles que deben ser explorados.
    # - Comenzamos con el píxel inicial (fila, columna).
    filas, columnas = imagen_binaria.shape
    pila = [(fila, columna)]

    # --------------------------------------------------------------------------------
    # PASO 3.2: REALIZAR LA BÚSQUEDA EN PROFUNDIDAD
    # --------------------------------------------------------------------------------
    # - Mientras haya píxeles en la pila, seguimos explorando.
    # - Para cada píxel, verificamos si pertenece a la región y si no ha sido etiquetado.
    while pila:
        f, c = pila.pop()
        if 0 <= f < filas and 0 <= c < columnas:
            if imagen_binaria[f, c] == 1 and etiquetas[f, c] == 0:
                # Asignamos la etiqueta al píxel actual.
                etiquetas[f, c] = etiqueta
                # Agregamos los píxeles vecinos (arriba, abajo, izquierda, derecha) a la pila.
                pila.append((f-1, c))  # Vecino superior
                pila.append((f+1, c))  # Vecino inferior
                pila.append((f, c-1))  # Vecino izquierdo
                pila.append((f, c+1))  # Vecino derecho

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos una imagen binaria de ejemplo con varias regiones conectadas.
# - Aplicamos el algoritmo de etiquetado de líneas para identificar y etiquetar las regiones.
# - Mostramos los resultados en la consola y visualizamos las imágenes con `matplotlib`.
if __name__ == "__main__":
    # Creamos una imagen binaria de ejemplo.
    imagen_binaria = np.array([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ])
    
    # Mostramos la imagen binaria original.
    print("Imagen binaria original:")
    print(imagen_binaria)
    
    # Aplicamos el algoritmo de etiquetado de líneas.
    etiquetas = etiquetado_lineas(imagen_binaria)
    
    # Mostramos la imagen con las regiones etiquetadas.
    print("\nImagen con regiones etiquetadas:")
    print(etiquetas)
    
    # Visualizamos las imágenes usando matplotlib.
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Imagen Binaria Original")
    plt.imshow(imagen_binaria, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("Regiones Etiquetadas")
    plt.imshow(etiquetas, cmap="nipy_spectral")
    plt.show()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza una búsqueda en profundidad (DFS) para explorar píxeles conectados.
# 2. Una región conectada se define como un conjunto de píxeles con valor 1 que están
#    adyacentes (arriba, abajo, izquierda, derecha).
# 3. Ventajas:
#    - Es simple de implementar y eficiente para imágenes pequeñas.
# 4. Limitaciones:
#    - Puede ser lento para imágenes grandes debido al uso de la pila.