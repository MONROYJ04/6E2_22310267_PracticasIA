# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MAPAS AUTOORGANIZADOS DE KOHONEN PARA CLASIFICACIÓN DE DATOS
# ------------------------------------------------------------------------------------
# Este código implementa un Mapa Autoorganizado de Kohonen (SOM), una red neuronal no supervisada
# que organiza datos en un mapa bidimensional, preservando la topología de los datos originales.
# Se utiliza para tareas como la clasificación, reducción de dimensionalidad y visualización.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `numpy` para realizar cálculos numéricos y manipulación de matrices.
# - Importamos `matplotlib.pyplot` para graficar el mapa resultante.
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA CLASE DEL MAPA AUTOORGANIZADO DE KOHONEN
# ------------------------------------------------------------------------------------
# - Esta clase implementa el algoritmo SOM.
# - Contiene métodos para inicializar el mapa, encontrar la neurona ganadora, actualizar pesos,
#   entrenar el mapa y graficar los resultados.
class MapaKohonen:
    def __init__(self, filas, columnas, dimensiones_entrada, tasa_aprendizaje=0.1, radio_inicial=1.0):
        """
        Inicializa el mapa de Kohonen.
        :param filas: Número de filas en el mapa (dimensión 1).
        :param columnas: Número de columnas en el mapa (dimensión 2).
        :param dimensiones_entrada: Dimensiones de los datos de entrada (ej: 3 para RGB).
        :param tasa_aprendizaje: Tasa inicial para ajustar los pesos.
        :param radio_inicial: Radio inicial de vecindad para actualizar pesos.
        """
        # Guardamos los parámetros iniciales
        self.filas = filas
        self.columnas = columnas
        self.dimensiones_entrada = dimensiones_entrada
        self.tasa_aprendizaje = tasa_aprendizaje
        self.radio_inicial = radio_inicial
        # Inicializamos los pesos del mapa con valores aleatorios entre 0 y 1
        self.pesos = np.random.random((filas, columnas, dimensiones_entrada))

    # ------------------------------------------------------------------------------------
    # PASO 3: ENCONTRAR LA NEURONA GANADORA
    # ------------------------------------------------------------------------------------
    # - Este método calcula cuál neurona del mapa tiene los pesos más cercanos al vector de entrada.
    # - Utiliza la distancia euclidiana para medir la similitud.
    def encontrar_ganador(self, entrada):
        """
        Encuentra la neurona ganadora (la más cercana a la entrada).
        :param entrada: Vector de entrada (ej: un color RGB).
        :return: Coordenadas de la neurona ganadora (fila, columna).
        """
        # Calculamos la distancia euclidiana entre la entrada y todos los pesos del mapa
        distancias = np.linalg.norm(self.pesos - entrada, axis=2)
        # Devolvemos las coordenadas de la neurona con la menor distancia
        return np.unravel_index(np.argmin(distancias), distancias.shape)

    # ------------------------------------------------------------------------------------
    # PASO 4: ACTUALIZAR LOS PESOS DEL MAPA
    # ------------------------------------------------------------------------------------
    # - Este método ajusta los pesos de las neuronas cercanas a la ganadora.
    # - La actualización depende de la distancia al ganador y de la iteración actual.
    def actualizar_pesos(self, entrada, ganador, iteracion, max_iteraciones):
        """
        Actualiza los pesos del mapa basándose en la entrada y la neurona ganadora.
        :param entrada: Vector de entrada.
        :param ganador: Coordenadas de la neurona ganadora.
        :param iteracion: Iteración actual del entrenamiento.
        :param max_iteraciones: Número máximo de iteraciones.
        """
        # Calculamos el radio de vecindad y la tasa de aprendizaje ajustados
        radio = self.radio_inicial * np.exp(-iteracion / max_iteraciones)
        tasa_aprendizaje = self.tasa_aprendizaje * np.exp(-iteracion / max_iteraciones)

        # Recorremos todas las neuronas del mapa
        for i in range(self.filas):
            for j in range(self.columnas):
                # Calculamos la distancia entre la neurona actual y la ganadora
                distancia = np.linalg.norm(np.array([i, j]) - np.array(ganador))
                if distancia <= radio:
                    # Calculamos la influencia de la neurona ganadora
                    influencia = np.exp(-distancia**2 / (2 * (radio**2)))
                    # Actualizamos los pesos de la neurona
                    self.pesos[i, j] += influencia * tasa_aprendizaje * (entrada - self.pesos[i, j])

    # ------------------------------------------------------------------------------------
    # PASO 5: ENTRENAR EL MAPA
    # ------------------------------------------------------------------------------------
    # - Este método entrena el mapa iterativamente con un conjunto de datos.
    # - En cada iteración, encuentra la neurona ganadora y actualiza los pesos.
    def entrenar(self, datos, iteraciones):
        """
        Entrena el mapa con los datos proporcionados.
        :param datos: Conjunto de datos de entrada (ej: colores RGB).
        :param iteraciones: Número de iteraciones de entrenamiento.
        """
        for iteracion in range(iteraciones):
            for entrada in datos:
                # Encontramos la neurona ganadora
                ganador = self.encontrar_ganador(entrada)
                # Actualizamos los pesos del mapa
                self.actualizar_pesos(entrada, ganador, iteracion, iteraciones)

    # ------------------------------------------------------------------------------------
    # PASO 6: GRAFICAR EL MAPA
    # ------------------------------------------------------------------------------------
    # - Este método grafica el mapa resultante después del entrenamiento.
    # - Muestra cómo se organizaron los datos en el espacio bidimensional.
    def graficar_mapa(self):
        """
        Grafica el mapa de Kohonen.
        """
        plt.imshow(self.pesos, interpolation='nearest')
        plt.title("Mapa Autoorganizado de Kohonen")
        plt.colorbar()
        plt.show()


# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO PRÁCTICO - CLASIFICACIÓN DE COLORES
# ------------------------------------------------------------------------------------
# - En este ejemplo, entrenamos el mapa con un conjunto de colores en formato RGB.
# - Después del entrenamiento, graficamos el mapa para visualizar cómo se organizaron los colores.
if __name__ == "__main__":
    # Creamos un conjunto de datos de colores (RGB)
    datos_colores = np.array([
        [1.0, 0.0, 0.0],  # Rojo
        [0.0, 1.0, 0.0],  # Verde
        [0.0, 0.0, 1.0],  # Azul
        [1.0, 1.0, 0.0],  # Amarillo
        [0.0, 1.0, 1.0],  # Cian
        [1.0, 0.0, 1.0],  # Magenta
        [0.5, 0.5, 0.5],  # Gris
        [0.0, 0.0, 0.0],  # Negro
        [1.0, 1.0, 1.0]   # Blanco
    ])

    # Creamos un mapa de Kohonen de 5x5 con 3 dimensiones de entrada (RGB)
    mapa = MapaKohonen(filas=5, columnas=5, dimensiones_entrada=3)

    # Entrenamos el mapa con los datos de colores
    mapa.entrenar(datos_colores, iteraciones=100)

    # Graficamos el mapa resultante
    mapa.graficar_mapa()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El SOM organiza datos en un espacio bidimensional preservando la topología.
# 2. Cada neurona tiene un vector de pesos que se ajusta durante el entrenamiento.
# 3. Ventajas: útil para visualización y reducción de dimensionalidad.
# 4. Limitaciones: requiere ajustar parámetros como la tasa de aprendizaje y el radio.