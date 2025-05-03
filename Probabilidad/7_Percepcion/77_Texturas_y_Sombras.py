# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: GRÁFICO DE BARRAS CON TEXTURAS Y SOMBRAS PARA MEJORAR PERCEPCIÓN
# ------------------------------------------------------------------------------------
# Este código genera un gráfico de barras que utiliza texturas y sombras para mejorar
# la percepción visual de los datos. Es útil para representar información categórica
# de manera clara y atractiva.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `matplotlib.pyplot` para crear gráficos.
# - Importamos `numpy` para manejar arreglos numéricos y calcular posiciones.
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Creamos una función llamada `graficar_texturas_y_sombras` que encapsula todo el
#   proceso de creación del gráfico.
# - Esta función no recibe parámetros, pero utiliza datos de ejemplo definidos dentro.
def graficar_texturas_y_sombras():
    """
    Esta función genera un gráfico de barras con texturas y sombras.
    El objetivo es mostrar cómo se pueden aplicar patrones visuales (texturas)
    y efectos de sombra para mejorar la percepción de los datos.
    """

    # --------------------------------------------------------------------------------
    # PASO 3: DEFINIR LOS DATOS DE EJEMPLO
    # --------------------------------------------------------------------------------
    # - Creamos una lista de categorías (`categorias`) que representan los nombres
    #   de cada barra en el gráfico.
    # - Creamos una lista de valores (`valores`) que representan la altura de cada
    #   barra en el gráfico.
    categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
    valores = [10, 15, 7, 12]

    # --------------------------------------------------------------------------------
    # PASO 4: CREAR LA FIGURA Y EL EJE
    # --------------------------------------------------------------------------------
    # - Usamos `plt.subplots()` para crear una figura (`fig`) y un eje (`ax`).
    # - La figura es el contenedor general del gráfico, y el eje es donde se dibujan
    #   los elementos del gráfico.
    fig, ax = plt.subplots()

    # --------------------------------------------------------------------------------
    # PASO 5: GENERAR LAS POSICIONES DE LAS BARRAS
    # --------------------------------------------------------------------------------
    # - Usamos `np.arange()` para generar un arreglo con las posiciones de las barras
    #   en el eje X. Esto asegura que las barras estén espaciadas uniformemente.
    posiciones = np.arange(len(categorias))

    # --------------------------------------------------------------------------------
    # PASO 6: DIBUJAR LAS BARRAS CON TEXTURAS
    # --------------------------------------------------------------------------------
    # - Usamos `ax.bar()` para dibujar las barras.
    # - Parámetros clave:
    #   - `posiciones`: posiciones en el eje X.
    #   - `valores`: altura de cada barra.
    #   - `color='skyblue'`: color de las barras.
    #   - `edgecolor='black'`: color del borde de las barras.
    #   - `hatch='//'`: patrón de textura aplicado a las barras.
    barras = ax.bar(posiciones, valores, color='skyblue', edgecolor='black', hatch='//')

    # --------------------------------------------------------------------------------
    # PASO 7: AGREGAR SOMBRAS DETRÁS DE LAS BARRAS
    # --------------------------------------------------------------------------------
    # - Iteramos sobre cada barra para calcular su posición y dimensiones.
    # - Usamos `ax.add_patch()` para dibujar un rectángulo detrás de cada barra,
    #   simulando una sombra.
    # - Parámetros clave:
    #   - `x + 0.02`: desplazamiento horizontal de la sombra.
    #   - `y - 0.5`: desplazamiento vertical de la sombra.
    #   - `color='gray'`: color de la sombra.
    #   - `alpha=0.3`: transparencia de la sombra.
    #   - `zorder=0`: asegura que la sombra esté detrás de las barras.
    for barra in barras:
        x = barra.get_x()
        y = barra.get_y()
        ancho = barra.get_width()
        alto = barra.get_height()
        ax.add_patch(plt.Rectangle((x + 0.02, y - 0.5), ancho, alto, 
                                    color='gray', alpha=0.3, zorder=0))

    # --------------------------------------------------------------------------------
    # PASO 8: CONFIGURAR LAS ETIQUETAS Y TÍTULOS
    # --------------------------------------------------------------------------------
    # - Configuramos las etiquetas del eje X con `ax.set_xticks()` y `ax.set_xticklabels()`.
    # - Agregamos un título al gráfico y etiquetas a los ejes X e Y.
    ax.set_xticks(posiciones)
    ax.set_xticklabels(categorias)
    ax.set_title('Ejemplo de Texturas y Sombras en un Gráfico de Barras')
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')

    # --------------------------------------------------------------------------------
    # PASO 9: MOSTRAR EL GRÁFICO
    # --------------------------------------------------------------------------------
    # - Usamos `plt.show()` para mostrar el gráfico en pantalla.
    plt.show()

# ------------------------------------------------------------------------------------
# PASO 10: LLAMAR A LA FUNCIÓN PARA GENERAR EL GRÁFICO
# ------------------------------------------------------------------------------------
# - Llamamos a la función `graficar_texturas_y_sombras` para ejecutar todo el proceso
#   y generar el gráfico.
graficar_texturas_y_sombras()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza un gráfico de barras para representar datos categóricos.
# 2. Las texturas (`hatch`) y sombras mejoran la percepción visual, haciendo que las
#    barras sean más fáciles de distinguir.
# 3. Ventajas:
#    - Mejora la estética del gráfico.
#    - Facilita la interpretación de los datos.
# 4. Limitaciones:
#    - Puede ser menos efectivo con demasiadas categorías o valores muy pequeños.