# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: PROCESOS ESTACIONARIOS PARA SERIES DE TIEMPO
# ------------------------------------------------------------------------------------
# Este código genera y grafica una serie de tiempo estacionaria. Una serie estacionaria
# es aquella cuyos parámetros estadísticos (como la media y la varianza) permanecen 
# constantes a lo largo del tiempo. Esto es útil en análisis de datos y modelado 
# estadístico, ya que permite trabajar con datos más predecibles y estables.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - `numpy` se utiliza para realizar cálculos matemáticos y generar números aleatorios.
# - `matplotlib.pyplot` se usa para graficar la serie de tiempo y visualizar su comportamiento.
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR UNA FUNCIÓN PARA GENERAR UNA SERIE ESTACIONARIA
# ------------------------------------------------------------------------------------
# - Esta función genera una serie de tiempo basada en una distribución normal.
# - La distribución normal asegura que los valores se distribuyan alrededor de una media
#   con una desviación estándar específica, lo que garantiza la estacionariedad.
# - Parámetros:
#   - `tamanio`: Número de puntos en la serie de tiempo.
#   - `media`: Valor promedio de la serie.
#   - `desviacion`: Desviación estándar de la serie.
def generar_serie_estacionaria(tamanio, media, desviacion):
    """
    Genera una serie de tiempo estacionaria basada en una distribucion normal.

    Parametros:
    tamanio (int): Numero de puntos en la serie de tiempo.
    media (float): Valor promedio de la serie.
    desviacion (float): Desviacion estandar de la serie.

    Retorna:
    np.array: Serie de tiempo estacionaria.
    """
    # Generamos valores aleatorios con distribución normal.
    # `loc=media` define la media de la distribución.
    # `scale=desviacion` define la desviación estándar.
    # `size=tamanio` define el número de puntos generados.
    serie = np.random.normal(loc=media, scale=desviacion, size=tamanio)
    return serie

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR UNA FUNCIÓN PARA GRAFICAR LA SERIE DE TIEMPO
# ------------------------------------------------------------------------------------
# - Esta función grafica la serie de tiempo generada para visualizar su comportamiento.
# - Se incluye una línea horizontal que representa la media de la serie.
# - Parámetros:
#   - `serie`: La serie de tiempo a graficar.
#   - `titulo`: El título del gráfico.
def graficar_serie(serie, titulo):
    """
    Grafica una serie de tiempo.

    Parametros:
    serie (np.array): Serie de tiempo a graficar.
    titulo (str): Titulo del grafico.
    """
    # Configuramos el tamaño de la figura para que sea más legible.
    plt.figure(figsize=(10, 5))
    
    # Graficamos la serie de tiempo.
    plt.plot(serie, label="Serie de tiempo")
    
    # Agregamos una línea horizontal que indica la media de la serie.
    plt.axhline(y=np.mean(serie), color='r', linestyle='--', label="Media")
    
    # Configuramos el título y las etiquetas de los ejes.
    plt.title(titulo)
    plt.xlabel("Tiempo")
    plt.ylabel("Valor")
    
    # Mostramos la leyenda para identificar los elementos del gráfico.
    plt.legend()
    
    # Mostramos el gráfico.
    plt.show()

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este bloque se genera una serie de tiempo estacionaria con parámetros definidos.
# - Se imprime la serie generada y se grafica para observar su comportamiento.
if __name__ == "__main__":
    # Definimos los parámetros de la serie estacionaria:
    # - `tamanio`: Número de puntos en la serie (100 puntos).
    # - `media`: Media de la serie (0).
    # - `desviacion`: Desviación estándar de la serie (1).
    tamanio = 100
    media = 0
    desviacion = 1

    # Generamos la serie estacionaria utilizando la función definida anteriormente.
    serie_estacionaria = generar_serie_estacionaria(tamanio, media, desviacion)

    # Mostramos la serie generada en la consola.
    print("Serie estacionaria generada:")
    print(serie_estacionaria)

    # Graficamos la serie para visualizar su comportamiento.
    graficar_serie(serie_estacionaria, "Serie de Tiempo Estacionaria")

    # --------------------------------------------------------------------------------
    # EXPLICACIÓN DETALLADA DEL ALGORITMO
    # --------------------------------------------------------------------------------
    # 1. Este algoritmo genera una serie de tiempo estacionaria utilizando una 
    #    distribución normal. Esto significa que los valores de la serie se distribuyen
    #    alrededor de una media constante con una dispersión controlada por la desviación
    #    estándar.
    # 2. Suposiciones clave:
    #    - La media y la desviación estándar no cambian con el tiempo.
    #    - Los valores son independientes entre sí.
    # 3. Ventajas:
    #    - Las series estacionarias son más fáciles de analizar y modelar.
    #    - Son útiles en aplicaciones como predicción y análisis de tendencias.
    # 4. Limitaciones:
    #    - Este modelo no captura patrones complejos como tendencias o estacionalidad.
    #    - Es una simplificación que puede no ser adecuada para todos los datos reales.