# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: BOOSTING PARA CLASIFICACIÓN BINARIA
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de Boosting desde cero utilizando árboles de decisión
# como modelos débiles. El objetivo es combinar varios modelos débiles para crear un modelo
# fuerte que clasifique correctamente los datos de entrada.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos las bibliotecas necesarias para manejar datos, crear modelos y evaluar resultados.
# - `numpy` se utiliza para operaciones matemáticas y manejo de matrices.
# - `DecisionTreeClassifier` es el modelo débil utilizado en Boosting.
# - `accuracy_score` mide la precisión del modelo.
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE BOOSTING
# ------------------------------------------------------------------------------------
# - Esta clase implementa el algoritmo de Boosting desde cero.
# - Combina varios modelos débiles (árboles de decisión) para mejorar la precisión.
# - Contiene métodos para entrenar (`ajustar`) y predecir (`predecir`) con el modelo.
class Boosting:
    def __init__(self, num_modelos):
        """
        Inicializa el algoritmo de Boosting.
        :param num_modelos: Número de modelos débiles que se combinarán.
        """
        self.num_modelos = num_modelos  # Número de modelos débiles
        self.modelos = []  # Lista para almacenar los modelos débiles
        self.pesos_modelos = []  # Lista para almacenar los pesos de cada modelo

    # ------------------------------------------------------------------------------------
    # PASO 3: ENTRENAMIENTO DEL MODELO (MÉTODO `ajustar`)
    # ------------------------------------------------------------------------------------
    # - Este método entrena el modelo de Boosting utilizando los datos de entrada.
    # - Ajusta los pesos de las muestras para enfocarse en los errores de clasificación.
    def ajustar(self, X, y):
        """
        Ajusta el modelo de Boosting a los datos de entrenamiento.
        :param X: Matriz de características (datos de entrada).
        :param y: Vector de etiquetas (clases).
        """
        # Inicializamos los pesos de las muestras de manera uniforme
        n_muestras = X.shape[0]
        pesos_muestras = np.ones(n_muestras) / n_muestras

        for _ in range(self.num_modelos):
            # Entrenamos un modelo débil (árbol de decisión con profundidad 1)
            modelo = DecisionTreeClassifier(max_depth=1)
            modelo.fit(X, y, sample_weight=pesos_muestras)

            # Predecimos las etiquetas con el modelo entrenado
            predicciones = modelo.predict(X)

            # Calculamos el error ponderado del modelo
            error = np.sum(pesos_muestras * (predicciones != y)) / np.sum(pesos_muestras)

            # Si el error es mayor o igual al 50%, detenemos el entrenamiento
            if error >= 0.5:
                break

            # Calculamos el peso del modelo basado en su error
            peso_modelo = 0.5 * np.log((1 - error) / error)

            # Actualizamos los pesos de las muestras
            pesos_muestras *= np.exp(-peso_modelo * y * predicciones)
            pesos_muestras /= np.sum(pesos_muestras)  # Normalizamos los pesos

            # Guardamos el modelo y su peso
            self.modelos.append(modelo)
            self.pesos_modelos.append(peso_modelo)

    # ------------------------------------------------------------------------------------
    # PASO 4: PREDICCIÓN CON EL MODELO (MÉTODO `predecir`)
    # ------------------------------------------------------------------------------------
    # - Este método combina las predicciones de los modelos débiles utilizando sus pesos.
    # - Devuelve la clase final (+1 o -1) basada en el signo de la predicción combinada.
    def predecir(self, X):
        """
        Realiza predicciones combinando los modelos débiles.
        :param X: Matriz de características (datos de entrada).
        :return: Vector de predicciones.
        """
        # Combinamos las predicciones de los modelos débiles usando sus pesos
        predicciones = np.zeros(X.shape[0])
        for modelo, peso in zip(self.modelos, self.pesos_modelos):
            predicciones += peso * modelo.predict(X)
        return np.sign(predicciones)  # Devolvemos la clase final (+1 o -1)


# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos sintético para probar el algoritmo.
# - Entrenamos el modelo de Boosting y evaluamos su precisión.
# - Visualizamos las predicciones en un gráfico.
if __name__ == "__main__":
    # Creamos un conjunto de datos simple
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)
    y = np.where(y == 0, -1, 1)  # Convertimos las etiquetas a -1 y 1 para Boosting

    # Dividimos los datos en entrenamiento y prueba
    from sklearn.model_selection import train_test_split
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

    # Entrenamos el modelo de Boosting
    modelo_boosting = Boosting(num_modelos=10)
    modelo_boosting.ajustar(X_entrenamiento, y_entrenamiento)

    # Realizamos predicciones
    predicciones = modelo_boosting.predecir(X_prueba)

    # Calculamos la precisión del modelo
    precision = accuracy_score(y_prueba, predicciones)
    print(f"Precisión del modelo de Boosting: {precision:.2f}")

    # Visualizamos los datos y las predicciones
    import matplotlib.pyplot as plt
    plt.scatter(X_prueba[:, 0], X_prueba[:, 1], c=predicciones, cmap='coolwarm', edgecolor='k')
    plt.title("Predicciones del modelo de Boosting")
    plt.show()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Boosting combina varios modelos débiles (árboles de decisión) para crear un modelo fuerte.
# 2. Cada modelo débil se entrena con un conjunto de datos ponderado, donde las muestras mal clasificadas
#    reciben mayor peso en iteraciones posteriores.
# 3. Las predicciones finales se obtienen combinando las predicciones de los modelos débiles según sus pesos.
# 4. Ventajas:
#    - Mejora la precisión en comparación con un solo modelo débil.
#    - Es robusto frente a sobreajuste si se configura correctamente.
# 5. Limitaciones:
#    - Puede ser sensible a ruido en los datos.
#    - Requiere más tiempo de entrenamiento debido a la naturaleza iterativa del algoritmo.