# Importamos las bibliotecas necesarias
import numpy as np  # Biblioteca para trabajar con arreglos y cálculos matemáticos
from sklearn.cluster import KMeans  # Implementación del algoritmo K-means
import matplotlib.pyplot as plt  # Biblioteca para graficar datos y resultados

# Generamos un conjunto de datos de ejemplo
# Creamos un arreglo con puntos en un espacio bidimensional (x, y)
# Estos puntos representan los datos que queremos agrupar
datos = np.array([
    [1, 2], [1, 4], [1, 0],  # Puntos cercanos entre sí
    [10, 2], [10, 4], [10, 0]  # Otro grupo de puntos cercanos entre sí
])

# Definimos el número de grupos (clusters) que queremos encontrar
# En este caso, queremos dividir los datos en 2 grupos
numero_grupos = 2

# Creamos el modelo K-means
# El modelo intentará agrupar los datos en el número de grupos especificado
modelo_kmeans = KMeans(n_clusters=numero_grupos, random_state=0)

# Entrenamos el modelo con los datos
# Esto significa que el modelo buscará patrones en los datos para agruparlos
modelo_kmeans.fit(datos)

# Obtenemos las etiquetas asignadas a cada punto
# Cada etiqueta indica a qué grupo pertenece un punto
etiquetas = modelo_kmeans.labels_

# Obtenemos las coordenadas de los centroides de los grupos
# Los centroides son los puntos centrales de cada grupo
centroides = modelo_kmeans.cluster_centers_

# Mostramos los resultados en la consola
print("Etiquetas de los puntos:", etiquetas)  # Muestra a qué grupo pertenece cada punto
print("Centroides de los grupos:", centroides)  # Muestra las coordenadas de los centroides

# Graficamos los datos y los resultados
# Dibujamos los puntos de datos, coloreados según su grupo
for i in range(numero_grupos):
    # Filtramos los puntos que pertenecen al grupo i
    puntos_grupo = datos[etiquetas == i]
    plt.scatter(puntos_grupo[:, 0], puntos_grupo[:, 1], label=f'Grupo {i + 1}')

# Dibujamos los centroides
# Los centroides se dibujan como una "x" roja para diferenciarlos de los puntos
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='x', s=100, label='Centroides')

# Agregamos etiquetas y leyenda al gráfico
plt.title("Agrupamiento No Supervisado con K-means")  # Título del gráfico
plt.xlabel("Coordenada X")  # Etiqueta del eje X
plt.ylabel("Coordenada Y")  # Etiqueta del eje Y
plt.legend()  # Muestra la leyenda para identificar los grupos y los centroides
plt.show()  # Muestra el gráfico en pantalla

# Explicación general:
# Este código utiliza el algoritmo K-means para agrupar puntos en un espacio bidimensional.
# Los puntos se dividen en dos grupos basándose en su cercanía. Los centroides son los
# puntos centrales de cada grupo, y el gráfico muestra los resultados de forma visual.