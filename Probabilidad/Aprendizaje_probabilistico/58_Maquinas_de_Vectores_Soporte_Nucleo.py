# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: MÁQUINAS DE VECTORES DE SOPORTE (SVM) CON NÚCLEO RBF
# ------------------------------------------------------------------------------------
# Este código implementa un modelo de Máquina de Vectores de Soporte (SVM) con un núcleo
# radial (RBF) para clasificar datos en dos categorías. Se generan datos de ejemplo,
# se entrena el modelo y se visualizan las regiones de decisión. Finalmente, se predice
# la categoría de un nuevo punto y se muestra en el gráfico.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos bibliotecas para trabajar con datos, entrenar el modelo y graficar.
# - `numpy`: Para operaciones matemáticas y manejo de arreglos.
# - `make_blobs`: Para generar datos de ejemplo distribuidos en grupos.
# - `SVC`: Para implementar el modelo SVM.
# - `matplotlib.pyplot`: Para graficar los datos y resultados.
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# PASO 2: GENERAR DATOS DE EJEMPLO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos de ejemplo con dos grupos (clusters).
# - `n_samples=100`: Genera 100 puntos de datos.
# - `centers=2`: Crea dos grupos o categorías.
# - `random_state=6`: Fija una semilla para reproducibilidad.
datos, etiquetas = make_blobs(n_samples=100, centers=2, random_state=6)

# ------------------------------------------------------------------------------------
# PASO 3: VISUALIZAR LOS DATOS GENERADOS
# ------------------------------------------------------------------------------------
# - Graficamos los puntos generados para observar su distribución.
# - `c=etiquetas`: Colorea los puntos según su categoría.
# - `cmap='coolwarm'`: Define el esquema de colores.
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, cmap='coolwarm')
plt.title("Datos de ejemplo")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# ------------------------------------------------------------------------------------
# PASO 4: CREAR EL MODELO SVM CON NÚCLEO RBF
# ------------------------------------------------------------------------------------
# - Creamos un modelo SVM con un núcleo radial (RBF).
# - `kernel='rbf'`: Permite separar datos no linealmente separables.
# - `C=1.0`: Controla la penalización por errores de clasificación.
# - `gamma=0.5`: Define la influencia de un solo punto de datos.
modelo_svm = SVC(kernel='rbf', C=1.0, gamma=0.5)

# ------------------------------------------------------------------------------------
# PASO 5: ENTRENAR EL MODELO
# ------------------------------------------------------------------------------------
# - Entrenamos el modelo con los datos generados y sus etiquetas.
# - `fit(datos, etiquetas)`: Ajusta el modelo a los datos.
modelo_svm.fit(datos, etiquetas)

# ------------------------------------------------------------------------------------
# PASO 6: CREAR UNA MALLA PARA VISUALIZAR LAS REGIONES DE DECISIÓN
# ------------------------------------------------------------------------------------
# - Creamos una malla de puntos para graficar las regiones de decisión del modelo.
# - `np.meshgrid`: Genera una cuadrícula de puntos en el espacio de datos.
# - `np.arange`: Define el rango y el paso entre puntos.
x_min, x_max = datos[:, 0].min() - 1, datos[:, 0].max() + 1
y_min, y_max = datos[:, 1].min() - 1, datos[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# ------------------------------------------------------------------------------------
# PASO 7: PREDECIR LAS ETIQUETAS PARA LA MALLA
# ------------------------------------------------------------------------------------
# - Predecimos la categoría de cada punto en la malla.
# - `np.c_[xx.ravel(), yy.ravel()]`: Combina las coordenadas de la malla.
# - `reshape`: Ajusta la forma de las predicciones para graficar.
Z = modelo_svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# ------------------------------------------------------------------------------------
# PASO 8: GRAFICAR LAS REGIONES DE DECISIÓN
# ------------------------------------------------------------------------------------
# - Graficamos las regiones de decisión del modelo.
# - `contourf`: Rellena las regiones con colores según la categoría.
# - `scatter`: Muestra los puntos originales con sus categorías.
plt.contourf(xx, yy, Z, alpha=0.8, cmap='coolwarm')
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, edgecolors='k', cmap='coolwarm')
plt.title("Regiones de decisión del modelo SVM")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# ------------------------------------------------------------------------------------
# PASO 9: EJEMPLO PRÁCTICO - PREDICCIÓN DE UN NUEVO PUNTO
# ------------------------------------------------------------------------------------
# - Creamos un nuevo punto para predecir su categoría.
# - `np.array([[0, 2]])`: Coordenadas del nuevo punto.
nuevo_punto = np.array([[0, 2]])
prediccion = modelo_svm.predict(nuevo_punto)  # Realizamos la predicción

# ------------------------------------------------------------------------------------
# PASO 10: MOSTRAR EL RESULTADO DE LA PREDICCIÓN
# ------------------------------------------------------------------------------------
# - Imprimimos la categoría predicha para el nuevo punto.
print(f"La etiqueta predicha para el punto {nuevo_punto} es: {prediccion[0]}")

# ------------------------------------------------------------------------------------
# PASO 11: VISUALIZAR EL NUEVO PUNTO EN EL GRÁFICO
# ------------------------------------------------------------------------------------
# - Graficamos nuevamente las regiones de decisión.
# - Añadimos el nuevo punto al gráfico para observar su posición.
plt.contourf(xx, yy, Z, alpha=0.8, cmap='coolwarm')
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, edgecolors='k', cmap='coolwarm')
plt.scatter(nuevo_punto[:, 0], nuevo_punto[:, 1], color='yellow', edgecolors='black', label='Nuevo punto')
plt.title("Predicción del nuevo punto")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Máquinas de Vectores de Soporte (SVM)**:
#    - Es un algoritmo de clasificación supervisada que encuentra un hiperplano óptimo
#      para separar datos en diferentes categorías.
# 2. **Núcleo RBF**:
#    - Permite manejar datos no linealmente separables al proyectarlos a un espacio
#      de mayor dimensión.
#    - Fórmula: `K(x, y) = exp(-gamma * ||x - y||^2)`, donde `gamma` controla la
#      influencia de los puntos.
# 3. **Ventajas**:
#    - Eficiente para problemas no lineales.
#    - Flexible con parámetros como `C` y `gamma`.
# 4. **Limitaciones**:
#    - Sensible a la selección de parámetros.
#    - Puede ser costoso computacionalmente para grandes conjuntos de datos.