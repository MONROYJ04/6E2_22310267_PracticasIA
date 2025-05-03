# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: AGRUPAMIENTO NO SUPERVISADO CON K-MEANS
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo K-means para agrupar un conjunto de datos en 
# dos grupos (clusters). El objetivo es identificar patrones en los datos y asignar 
# cada punto a un grupo basado en su cercanía a los centroides.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos las bibliotecas que utilizaremos en el código.
# - `numpy` se usa para manejar arreglos y cálculos matemáticos.
# - `KMeans` de `sklearn.cluster` implementa el algoritmo K-means.
# - `matplotlib.pyplot` se usa para graficar los datos y los resultados.
import numpy as np  # Biblioteca para trabajar con arreglos y cálculos matemáticos
from sklearn.cluster import KMeans  # Implementación del algoritmo K-means
import matplotlib.pyplot as plt  # Biblioteca para graficar datos y resultados

# ------------------------------------------------------------------------------------
# PASO 2: GENERACIÓN DE DATOS DE EJEMPLO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos bidimensionales (x, y) para agrupar.
# - Los datos están organizados en dos grupos naturales para facilitar la visualización.
# - Esto simula un caso práctico donde los datos tienen patrones que queremos descubrir.
datos = np.array([
    [1, 2], [1, 4], [1, 0],  # Puntos cercanos entre sí (primer grupo)
    [10, 2], [10, 4], [10, 0]  # Otro grupo de puntos cercanos entre sí (segundo grupo)
])

# ------------------------------------------------------------------------------------
# PASO 3: DEFINICIÓN DEL NÚMERO DE GRUPOS
# ------------------------------------------------------------------------------------
# - Especificamos el número de grupos (clusters) que queremos encontrar.
# - En este caso, seleccionamos 2 grupos porque sabemos que los datos tienen dos patrones.
# - Este parámetro es clave para el funcionamiento del algoritmo.
numero_grupos = 2

# ------------------------------------------------------------------------------------
# PASO 4: CREACIÓN DEL MODELO K-MEANS
# ------------------------------------------------------------------------------------
# - Creamos una instancia del modelo K-means con el número de grupos definido.
# - `random_state=0` asegura que los resultados sean reproducibles.
# - El modelo buscará dividir los datos en los grupos especificados.
modelo_kmeans = KMeans(n_clusters=numero_grupos, random_state=0)

# ------------------------------------------------------------------------------------
# PASO 5: ENTRENAMIENTO DEL MODELO
# ------------------------------------------------------------------------------------
# - Entrenamos el modelo con los datos usando el método `fit`.
# - Durante este proceso, el modelo calcula los centroides y asigna cada punto a un grupo.
modelo_kmeans.fit(datos)

# ------------------------------------------------------------------------------------
# PASO 6: OBTENCIÓN DE RESULTADOS
# ------------------------------------------------------------------------------------
# - `labels_`: Etiquetas asignadas a cada punto, indicando a qué grupo pertenece.
# - `cluster_centers_`: Coordenadas de los centroides de los grupos.
etiquetas = modelo_kmeans.labels_
centroides = modelo_kmeans.cluster_centers_

# ------------------------------------------------------------------------------------
# PASO 7: MOSTRAR RESULTADOS EN CONSOLA
# ------------------------------------------------------------------------------------
# - Imprimimos las etiquetas y los centroides para entender cómo se agruparon los datos.
print("Etiquetas de los puntos:", etiquetas)  # Muestra a qué grupo pertenece cada punto
print("Centroides de los grupos:", centroides)  # Muestra las coordenadas de los centroides

# ------------------------------------------------------------------------------------
# PASO 8: VISUALIZACIÓN DE LOS RESULTADOS
# ------------------------------------------------------------------------------------
# - Graficamos los puntos de datos, coloreados según su grupo.
# - Dibujamos los centroides como una "x" roja para diferenciarlos de los puntos.
for i in range(numero_grupos):
    # Filtramos los puntos que pertenecen al grupo i
    puntos_grupo = datos[etiquetas == i]
    plt.scatter(puntos_grupo[:, 0], puntos_grupo[:, 1], label=f'Grupo {i + 1}')

# Dibujamos los centroides
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='x', s=100, label='Centroides')

# Agregamos etiquetas y leyenda al gráfico
plt.title("Agrupamiento No Supervisado con K-means")  # Título del gráfico
plt.xlabel("Coordenada X")  # Etiqueta del eje X
plt.ylabel("Coordenada Y")  # Etiqueta del eje Y
plt.legend()  # Muestra la leyenda para identificar los grupos y los centroides
plt.show()  # Muestra el gráfico en pantalla

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo K-means busca dividir los datos en `k` grupos minimizando la distancia
#    entre los puntos y sus centroides. Esto se logra iterativamente:
#    - Inicializa los centroides aleatoriamente.
#    - Asigna cada punto al centroide más cercano.
#    - Recalcula los centroides como el promedio de los puntos asignados.
# 2. Suposiciones clave:
#    - Los grupos son esféricos y tienen tamaños similares.
# 3. Ventajas:
#    - Fácil de implementar y rápido para conjuntos de datos pequeños.
#    - Útil para identificar patrones en datos no etiquetados.
# 4. Limitaciones:
#    - Sensible a la inicialización de los centroides.
#    - No funciona bien con grupos de formas complejas o tamaños desiguales.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: PREDICCIÓN DE UN NUEVO PUNTO
# ------------------------------------------------------------------------------------
# - Supongamos que queremos predecir a qué grupo pertenece un nuevo punto.
nuevo_punto = np.array([[5, 3]])  # Coordenadas del nuevo punto
prediccion = modelo_kmeans.predict(nuevo_punto)
print(f"El nuevo punto {nuevo_punto} pertenece al grupo {prediccion[0] + 1}.")