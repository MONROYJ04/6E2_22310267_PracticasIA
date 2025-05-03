# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SEPARABILIDAD LINEAL CON PERCEPTRÓN
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo de separabilidad lineal utilizando un modelo
# de perceptrón. El objetivo es clasificar datos en dos clases diferentes si estos
# son linealmente separables, y visualizar la línea que los separa.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `numpy` para manejar datos numéricos y operaciones matemáticas.
# - Importamos `matplotlib.pyplot` para graficar los datos y la línea separadora.
# - Importamos `Perceptron` de `sklearn.linear_model` para crear el modelo.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Creamos una función llamada `separabilidad_lineal` que implementa el algoritmo.
# - Esta función genera datos, entrena un modelo de perceptrón y visualiza los resultados.
def separabilidad_lineal():
    """
    Este algoritmo demuestra el concepto de separabilidad lineal utilizando un perceptrón.
    Un perceptrón es un modelo de red neuronal simple que puede clasificar datos
    si estos son linealmente separables.
    """

    # --------------------------------------------------------------------------------
    # PASO 3: GENERAR DATOS DE EJEMPLO
    # --------------------------------------------------------------------------------
    # - Creamos dos grupos de puntos (Clase 1 y Clase 2) que son linealmente separables.
    # - `datos` contiene las coordenadas de los puntos.
    # - `etiquetas` contiene las clases correspondientes (0 o 1).
    datos = np.array([
        [2, 3], [1, 5], [3, 4],  # Clase 1
        [6, 8], [7, 9], [8, 7]   # Clase 2
    ])
    etiquetas = np.array([0, 0, 0, 1, 1, 1])  # Etiquetas de las clases

    # --------------------------------------------------------------------------------
    # PASO 4: CREAR Y ENTRENAR EL MODELO DE PERCEPTRÓN
    # --------------------------------------------------------------------------------
    # - Creamos un modelo de perceptrón utilizando la clase `Perceptron`.
    # - Entrenamos el modelo con los datos (`datos`) y las etiquetas (`etiquetas`).
    modelo = Perceptron()
    modelo.fit(datos, etiquetas)

    # --------------------------------------------------------------------------------
    # PASO 5: OBTENER LOS COEFICIENTES DE LA RECTA SEPARADORA
    # --------------------------------------------------------------------------------
    # - Extraemos los pesos (`w1`, `w2`) y el sesgo (`b`) del modelo entrenado.
    # - Estos valores definen la ecuación de la línea separadora: w1*x + w2*y + b = 0.
    w1, w2 = modelo.coef_[0]
    b = modelo.intercept_

    # --------------------------------------------------------------------------------
    # PASO 6: VISUALIZAR LOS DATOS Y LA RECTA SEPARADORA
    # --------------------------------------------------------------------------------
    # - Graficamos los puntos de Clase 1 y Clase 2 con colores diferentes.
    # - Dibujamos la línea separadora calculada a partir de los coeficientes.
    plt.scatter(datos[:3, 0], datos[:3, 1], color='blue', label='Clase 1')
    plt.scatter(datos[3:, 0], datos[3:, 1], color='red', label='Clase 2')

    # Dibujamos la recta separadora
    # La ecuación de la recta es: w1*x + w2*y + b = 0
    x = np.linspace(0, 10, 100)  # Valores de x para graficar la línea
    y = -(w1 / w2) * x - (b / w2)  # Calculamos los valores de y
    plt.plot(x, y, color='green', label='Recta separadora')

    # Configuramos el gráfico
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Separabilidad Lineal con Perceptrón')
    plt.legend()
    plt.grid()
    plt.show()

    # --------------------------------------------------------------------------------
    # PASO 7: CLASIFICAR UN NUEVO PUNTO
    # --------------------------------------------------------------------------------
    # - Creamos un nuevo punto con coordenadas `[4, 6]`.
    # - Utilizamos el modelo entrenado para predecir a qué clase pertenece.
    nuevo_punto = np.array([[4, 6]])  # Coordenadas del nuevo punto
    prediccion = modelo.predict(nuevo_punto)  # Clasificación del punto
    print(f"El nuevo punto {nuevo_punto} pertenece a la clase {prediccion[0]}.")

# ------------------------------------------------------------------------------------
# PASO 8: EJECUTAR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Llamamos a la función `separabilidad_lineal` para ejecutar el algoritmo.
if __name__ == "__main__":
    separabilidad_lineal()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El perceptrón es un modelo de red neuronal que clasifica datos linealmente separables.
#    Esto significa que los datos de diferentes clases pueden dividirse con una línea recta.
# 2. La ecuación de la línea separadora es: w1*x + w2*y + b = 0, donde:
#    - `w1` y `w2` son los pesos aprendidos por el modelo.
#    - `b` es el sesgo (intercepto).
# 3. Ventajas:
#    - Simple y eficiente para datos linealmente separables.
#    - Fácil de implementar y entender.
# 4. Limitaciones:
#    - No funciona con datos que no sean linealmente separables.
#    - No puede resolver problemas más complejos sin transformaciones adicionales.