# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: k-NN, k-Medias y Clustering PARA CLASIFICACIÓN Y AGRUPAMIENTO
# ------------------------------------------------------------------------------------
# Este código implementa tres algoritmos de aprendizaje automático: k-NN (k-Nearest Neighbors),
# k-Medias (k-Means) y Clustering. El objetivo es clasificar datos y agruparlos en grupos
# similares, utilizando ejemplos prácticos para entender su funcionamiento.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos librerías para cálculos matemáticos, generación de datos y visualización.
# - Estas librerías son esenciales para trabajar con datos y aplicar los algoritmos.
import numpy as np  # Para trabajar con arreglos y cálculos matemáticos
from sklearn.datasets import make_blobs  # Para generar datos de ejemplo
from sklearn.cluster import KMeans  # Para el algoritmo de k-Medias
from sklearn.neighbors import KNeighborsClassifier  # Para el algoritmo de k-NN
import matplotlib.pyplot as plt  # Para graficar los datos

# ------------------------------------------------------------------------------------
# PASO 2: IMPLEMENTACIÓN DEL ALGORITMO k-NN (k-Nearest Neighbors)
# ------------------------------------------------------------------------------------
# - Este algoritmo clasifica datos nuevos basándose en los k vecinos más cercanos.
# - Es útil para problemas de clasificación supervisada.
# - Aquí usamos un conjunto de datos generado con dos clases.

# Creamos un conjunto de datos de ejemplo
# - `n_samples=100`: Generamos 100 puntos de datos.
# - `centers=2`: Creamos 2 grupos o clases.
# - `random_state=42`: Aseguramos que los datos sean reproducibles.
datos, etiquetas = make_blobs(n_samples=100, centers=2, random_state=42)

# Dividimos los datos en entrenamiento y prueba
# - Los primeros 80 datos se usan para entrenar el modelo.
# - Los últimos 20 datos se usan para probar el modelo.
datos_entrenamiento = datos[:80]
etiquetas_entrenamiento = etiquetas[:80]
datos_prueba = datos[80:]
etiquetas_prueba = etiquetas[80:]

# Creamos el modelo de k-NN con k=3
# - `n_neighbors=3`: Consideramos los 3 vecinos más cercanos para clasificar.
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el modelo con los datos de entrenamiento
# - El modelo aprende las características de los datos de entrenamiento.
modelo_knn.fit(datos_entrenamiento, etiquetas_entrenamiento)

# Probamos el modelo con los datos de prueba
# - El modelo predice las etiquetas de los datos de prueba.
predicciones = modelo_knn.predict(datos_prueba)

# Mostramos los resultados
print("Predicciones de k-NN:", predicciones)
print("Etiquetas reales:", etiquetas_prueba)

# ------------------------------------------------------------------------------------
# PASO 3: IMPLEMENTACIÓN DEL ALGORITMO k-MEDIAS (k-Means)
# ------------------------------------------------------------------------------------
# - Este algoritmo agrupa datos en k grupos basándose en similitudes.
# - Es útil para problemas de agrupamiento no supervisado.

# Creamos un conjunto de datos de ejemplo con 3 grupos
# - `n_samples=150`: Generamos 150 puntos de datos.
# - `centers=3`: Creamos 3 grupos o clusters.
# - `random_state=42`: Aseguramos que los datos sean reproducibles.
datos_kmeans, _ = make_blobs(n_samples=150, centers=3, random_state=42)

# Creamos el modelo de k-Medias con k=3
# - `n_clusters=3`: Buscamos 3 grupos en los datos.
modelo_kmeans = KMeans(n_clusters=3, random_state=42)

# Entrenamos el modelo con los datos
# - El modelo encuentra los centros de los grupos.
modelo_kmeans.fit(datos_kmeans)

# Obtenemos las etiquetas de los grupos asignados por el modelo
# - Cada punto de datos se asigna a un grupo.
etiquetas_grupos = modelo_kmeans.labels_

# Mostramos los resultados
print("Etiquetas de los grupos asignados por k-Medias:", etiquetas_grupos)

# Graficamos los datos y los grupos
# - Mostramos los puntos de datos coloreados según su grupo.
plt.scatter(datos_kmeans[:, 0], datos_kmeans[:, 1], c=etiquetas_grupos, cmap='viridis')
plt.title("Resultados de k-Medias")
plt.show()

# ------------------------------------------------------------------------------------
# PASO 4: IMPLEMENTACIÓN DEL ALGORITMO DE CLUSTERING
# ------------------------------------------------------------------------------------
# - El clustering es una técnica general para agrupar datos similares.
# - Aquí reutilizamos los resultados de k-Medias como ejemplo de clustering.

# Mostramos los centros de los grupos encontrados
# - `cluster_centers_`: Coordenadas de los centros de los grupos.
centros = modelo_kmeans.cluster_centers_
print("Centros de los grupos encontrados:", centros)

# Graficamos los datos con los centros de los grupos
# - Mostramos los puntos de datos y los centros de los grupos.
plt.scatter(datos_kmeans[:, 0], datos_kmeans[:, 1], c=etiquetas_grupos, cmap='viridis')
plt.scatter(centros[:, 0], centros[:, 1], c='red', marker='x', s=200, label='Centros')
plt.title("Centros de los grupos (Clustering)")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. k-NN:
#    - Clasifica un punto nuevo basándose en la mayoría de las clases de sus k vecinos más cercanos.
#    - Ventaja: Simple y efectivo para datos pequeños.
#    - Limitación: Puede ser lento con grandes conjuntos de datos.
# 2. k-Medias:
#    - Agrupa datos en k grupos minimizando la distancia entre los puntos y el centro del grupo.
#    - Ventaja: Rápido y fácil de implementar.
#    - Limitación: Requiere especificar k y puede converger a mínimos locales.
# 3. Clustering:
#    - Técnica general para encontrar patrones en datos no etiquetados.
#    - Ventaja: Útil para explorar datos.
#    - Limitación: Depende del algoritmo usado (ej: k-Medias).

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que queremos clasificar un nuevo punto usando k-NN:
nuevo_punto = np.array([[0, 0]])  # Coordenadas del nuevo punto
prediccion_nuevo_punto = modelo_knn.predict(nuevo_punto)
print("El nuevo punto pertenece a la clase:", prediccion_nuevo_punto)