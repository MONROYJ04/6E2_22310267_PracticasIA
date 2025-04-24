# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RED NEURONAL MULTICAPA PARA CLASIFICACIÓN BINARIA
# ------------------------------------------------------------------------------------
# Este código implementa una red neuronal multicapa desde cero utilizando Python y NumPy.
# El objetivo es entrenar la red para clasificar datos en dos clases (binarias) utilizando
# un conjunto de datos generado artificialmente.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos bibliotecas clave para cálculos matemáticos, generación de datos y evaluación.
# - `numpy`: Para realizar operaciones matemáticas y de álgebra lineal.
# - `sklearn`: Para generar datos de ejemplo y dividirlos en entrenamiento/prueba.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE RED NEURONAL MULTICAPA
# ------------------------------------------------------------------------------------
# - Creamos una clase que encapsula toda la funcionalidad de la red neuronal.
# - Incluye inicialización, funciones de activación, entrenamiento y predicción.
class RedNeuronalMulticapa:
    def __init__(self, capas):
        """
        Inicializa la red neuronal con las capas especificadas.
        :param capas: Lista que define el número de neuronas en cada capa.
        """
        # Guardamos la estructura de la red (número de neuronas por capa).
        self.capas = capas
        self.pesos = []  # Lista para almacenar los pesos de cada capa.
        self.sesgos = []  # Lista para almacenar los sesgos de cada capa.

        # ------------------------------------------------------------------------------------
        # PASO 2.1: INICIALIZACIÓN DE PESOS Y SESGOS
        # ------------------------------------------------------------------------------------
        # - Los pesos y sesgos se inicializan aleatoriamente para romper la simetría.
        # - `np.random.randn`: Genera valores aleatorios con distribución normal.
        for i in range(len(capas) - 1):
            self.pesos.append(np.random.randn(capas[i], capas[i + 1]))
            self.sesgos.append(np.random.randn(1, capas[i + 1]))

    def activacion_sigmoide(self, x):
        """
        Función de activación sigmoide.
        :param x: Entrada.
        :return: Salida transformada.
        """
        # ------------------------------------------------------------------------------------
        # PASO 2.2: FUNCIÓN DE ACTIVACIÓN
        # ------------------------------------------------------------------------------------
        # - La función sigmoide transforma los valores de entrada en un rango entre 0 y 1.
        # - Esto permite modelar probabilidades en la salida.
        return 1 / (1 + np.exp(-x))

    def derivada_sigmoide(self, x):
        """
        Derivada de la función sigmoide.
        :param x: Entrada.
        :return: Derivada de la salida.
        """
        # ------------------------------------------------------------------------------------
        # PASO 2.3: DERIVADA DE LA FUNCIÓN DE ACTIVACIÓN
        # ------------------------------------------------------------------------------------
        # - La derivada de la sigmoide se utiliza durante la retropropagación para calcular
        #   los gradientes necesarios para actualizar los pesos.
        return x * (1 - x)

    def entrenar(self, X, y, epocas, tasa_aprendizaje):
        """
        Entrena la red neuronal utilizando retropropagación.
        :param X: Datos de entrada.
        :param y: Etiquetas de salida.
        :param epocas: Número de iteraciones de entrenamiento.
        :param tasa_aprendizaje: Tasa de aprendizaje para ajustar los pesos.
        """
        # ------------------------------------------------------------------------------------
        # PASO 3: ENTRENAMIENTO DE LA RED NEURONAL
        # ------------------------------------------------------------------------------------
        # - El entrenamiento se realiza en varias épocas (iteraciones).
        # - Incluye dos pasos principales: propagación hacia adelante y retropropagación.
        for epoca in range(epocas):
            # ------------------------------------------------------------------------------------
            # PASO 3.1: PROPAGACIÓN HACIA ADELANTE
            # ------------------------------------------------------------------------------------
            # - Calculamos las salidas de cada capa aplicando los pesos, sesgos y la función
            #   de activación.
            activaciones = [X]
            for i in range(len(self.pesos)):
                z = np.dot(activaciones[-1], self.pesos[i]) + self.sesgos[i]
                activaciones.append(self.activacion_sigmoide(z))

            # ------------------------------------------------------------------------------------
            # PASO 3.2: RETROPROPAGACIÓN DEL ERROR
            # ------------------------------------------------------------------------------------
            # - Calculamos el error en la salida y lo propagamos hacia atrás para ajustar los pesos.
            error = y - activaciones[-1]
            deltas = [error * self.derivada_sigmoide(activaciones[-1])]

            for i in range(len(self.pesos) - 1, 0, -1):
                delta = deltas[-1].dot(self.pesos[i].T) * self.derivada_sigmoide(activaciones[i])
                deltas.append(delta)

            deltas.reverse()

            # ------------------------------------------------------------------------------------
            # PASO 3.3: ACTUALIZACIÓN DE PESOS Y SESGOS
            # ------------------------------------------------------------------------------------
            # - Ajustamos los pesos y sesgos utilizando los gradientes calculados.
            for i in range(len(self.pesos)):
                self.pesos[i] += activaciones[i].T.dot(deltas[i]) * tasa_aprendizaje
                self.sesgos[i] += np.sum(deltas[i], axis=0, keepdims=True) * tasa_aprendizaje

    def predecir(self, X):
        """
        Realiza predicciones con la red neuronal.
        :param X: Datos de entrada.
        :return: Predicciones.
        """
        # ------------------------------------------------------------------------------------
        # PASO 4: PREDICCIÓN
        # ------------------------------------------------------------------------------------
        # - Calculamos las salidas de la red para nuevos datos de entrada.
        # - La salida final se redondea a 0 o 1 para clasificaciones binarias.
        activacion = X
        for i in range(len(self.pesos)):
            z = np.dot(activacion, self.pesos[i]) + self.sesgos[i]
            activacion = self.activacion_sigmoide(z)
        return (activacion > 0.5).astype(int)

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Generamos un conjunto de datos de ejemplo con dos clases (forma de lunas).
# - Entrenamos la red neuronal para clasificar los datos.
if __name__ == "__main__":
    # Generamos un conjunto de datos de ejemplo
    X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
    y = y.reshape(-1, 1)  # Ajustamos la forma de las etiquetas

    # Dividimos los datos en entrenamiento y prueba
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creamos una red neuronal con 2 neuronas en la entrada, 5 en la capa oculta y 1 en la salida
    red = RedNeuronalMulticapa([2, 5, 1])

    # Entrenamos la red neuronal
    red.entrenar(X_entrenamiento, y_entrenamiento, epocas=10000, tasa_aprendizaje=0.01)

    # Realizamos predicciones
    y_pred = red.predecir(X_prueba)

    # Evaluamos el rendimiento
    print("Precisión:", accuracy_score(y_prueba, y_pred))

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. La red neuronal multicapa utiliza la propagación hacia adelante para calcular las salidas.
# 2. La retropropagación ajusta los pesos y sesgos para minimizar el error.
# 3. La función sigmoide permite modelar probabilidades y calcular gradientes fácilmente.
# Ventajas: Flexible y capaz de modelar relaciones no lineales.
# Limitaciones: Puede ser lento para entrenar y propenso a quedarse atrapado en mínimos locales.