# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ÁRBOLES DE REGRESIÓN M5 PARA PREDICCIÓN NUMÉRICA
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de Árboles de Regresión M5, que se utiliza para 
# realizar predicciones numéricas dividiendo los datos en subconjuntos y ajustando 
# modelos simples en cada subconjunto. Es útil para problemas de regresión.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos las bibliotecas `numpy` y `pandas` para manejar datos numéricos y tabulares.
# - Usamos `train_test_split` para dividir los datos en entrenamiento y prueba.
# - `mean_squared_error` nos ayuda a evaluar el desempeño del modelo.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA CLASE DEL MODELO
# ------------------------------------------------------------------------------------
# - Creamos la clase `ArbolRegresionM5` para implementar el algoritmo.
# - Incluye métodos para ajustar el modelo (`ajustar`) y realizar predicciones (`predecir`).
class ArbolRegresionM5:
    def __init__(self, profundidad_maxima=5, min_datos_hoja=10):
        """
        Inicializa el árbol de regresión M5.
        :param profundidad_maxima: Profundidad máxima del árbol (controla la complejidad).
        :param min_datos_hoja: Número mínimo de datos en una hoja (evita sobreajuste).
        """
        self.profundidad_maxima = profundidad_maxima
        self.min_datos_hoja = min_datos_hoja
        self.modelo = None

    # ------------------------------------------------------------------------------------
    # PASO 3: AJUSTAR EL MODELO
    # ------------------------------------------------------------------------------------
    # - Este método construye el árbol de regresión a partir de los datos de entrenamiento.
    # - `X` es la matriz de características (variables independientes).
    # - `y` es el vector objetivo (variable dependiente).
    def ajustar(self, X, y):
        self.modelo = self._crear_arbol(X, y, profundidad=0)

    # ------------------------------------------------------------------------------------
    # PASO 4: REALIZAR PREDICCIONES
    # ------------------------------------------------------------------------------------
    # - Este método utiliza el árbol ajustado para predecir valores en nuevos datos.
    # - Devuelve un arreglo con las predicciones para cada fila de `X`.
    def predecir(self, X):
        return np.array([self._predecir_fila(fila, self.modelo) for fila in X])

    # ------------------------------------------------------------------------------------
    # PASO 5: CREAR EL ÁRBOL DE REGRESIÓN
    # ------------------------------------------------------------------------------------
    # - Este método construye el árbol recursivamente dividiendo los datos en nodos.
    # - Si se alcanza la profundidad máxima o hay pocos datos, se crea una hoja.
    def _crear_arbol(self, X, y, profundidad):
        if len(y) <= self.min_datos_hoja or profundidad >= self.profundidad_maxima:
            return {'tipo': 'hoja', 'valor': np.mean(y)}

        mejor_division = None
        mejor_error = float('inf')
        mejor_indice = None

        # Iteramos sobre cada característica para encontrar la mejor división
        for indice in range(X.shape[1]):
            valores_unicos = np.unique(X[:, indice])
            for valor in valores_unicos:
                izquierda = y[X[:, indice] <= valor]
                derecha = y[X[:, indice] > valor]

                if len(izquierda) == 0 or len(derecha) == 0:
                    continue

                # Calculamos el error de la división
                error = (len(izquierda) * np.var(izquierda) + len(derecha) * np.var(derecha)) / len(y)

                if error < mejor_error:
                    mejor_error = error
                    mejor_division = valor
                    mejor_indice = indice

        if mejor_division is None:
            return {'tipo': 'hoja', 'valor': np.mean(y)}

        izquierda_indices = X[:, mejor_indice] <= mejor_division
        derecha_indices = X[:, mejor_indice] > mejor_division

        nodo_izquierdo = self._crear_arbol(X[izquierda_indices], y[izquierda_indices], profundidad + 1)
        nodo_derecho = self._crear_arbol(X[derecha_indices], y[derecha_indices], profundidad + 1)

        return {
            'tipo': 'nodo',
            'indice': mejor_indice,
            'valor': mejor_division,
            'izquierda': nodo_izquierdo,
            'derecha': nodo_derecho
        }

    # ------------------------------------------------------------------------------------
    # PASO 6: PREDICCIÓN PARA UNA FILA
    # ------------------------------------------------------------------------------------
    # - Este método recorre el árbol para predecir el valor de una fila específica.
    # - Si el nodo es una hoja, devuelve el valor promedio almacenado.
    def _predecir_fila(self, fila, nodo):
        if nodo['tipo'] == 'hoja':
            return nodo['valor']

        if fila[nodo['indice']] <= nodo['valor']:
            return self._predecir_fila(fila, nodo['izquierda'])
        else:
            return self._predecir_fila(fila, nodo['derecha'])


# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos de ejemplo con dos características (`x1`, `x2`) y un objetivo (`y`).
# - Dividimos los datos en entrenamiento y prueba.
# - Ajustamos el modelo y realizamos predicciones.
if __name__ == "__main__":
    datos = pd.DataFrame({
        'x1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'x2': [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
        'y': [10, 9, 8, 7, 6, 5, 6, 7, 8, 9]
    })

    # Dividimos los datos en entrenamiento (80%) y prueba (20%)
    X = datos[['x1', 'x2']].values
    y = datos['y'].values
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creamos y ajustamos el modelo
    modelo = ArbolRegresionM5(profundidad_maxima=3, min_datos_hoja=2)
    modelo.ajustar(X_entrenamiento, y_entrenamiento)

    # Realizamos predicciones en los datos de prueba
    predicciones = modelo.predecir(X_prueba)

    # Mostramos los resultados
    print("Predicciones:", predicciones)
    print("Error cuadrático medio:", mean_squared_error(y_prueba, predicciones))

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El Árbol de Regresión M5 divide los datos en subconjuntos basados en reglas de decisión.
# 2. En cada nodo, se calcula el mejor punto de división minimizando la varianza.
# 3. Las hojas contienen valores promedio de los datos en ese subconjunto.
# 4. Ventajas: Maneja datos no lineales y es interpretable. Limitaciones: Puede sobreajustarse.