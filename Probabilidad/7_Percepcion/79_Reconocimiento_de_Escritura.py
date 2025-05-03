# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RED NEURONAL CONVOLUCIONAL PARA RECONOCIMIENTO DE DÍGITOS ESCRITOS A MANO
# ------------------------------------------------------------------------------------
# Este código implementa una red neuronal convolucional (CNN) para reconocer dígitos escritos a mano
# utilizando el conjunto de datos MNIST. El modelo se entrena para clasificar imágenes de dígitos
# (del 0 al 9) y luego se evalúa su precisión. Finalmente, se realiza una predicción práctica.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos TensorFlow para construir y entrenar la red neuronal.
# - Usamos Matplotlib para visualizar las imágenes.
# - Numpy se utiliza para operaciones matemáticas y manipulación de datos.
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: CARGAR Y PREPROCESAR LOS DATOS
# ------------------------------------------------------------------------------------
# - Cargamos el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano.
# - Dividimos los datos en dos conjuntos: entrenamiento y prueba.
# - Normalizamos los valores de los píxeles para que estén entre 0 y 1, lo que mejora el rendimiento del modelo.
(datos_entrenamiento, etiquetas_entrenamiento), (datos_prueba, etiquetas_prueba) = datasets.mnist.load_data()

# Normalizamos los datos dividiendo entre 255 (valor máximo de un píxel en escala de grises).
datos_entrenamiento = datos_entrenamiento / 255.0
datos_prueba = datos_prueba / 255.0

# Agregamos una dimensión extra para que los datos sean compatibles con la red neuronal.
# Esto convierte las imágenes de 28x28 en un formato de 28x28x1 (1 canal para escala de grises).
datos_entrenamiento = datos_entrenamiento.reshape((datos_entrenamiento.shape[0], 28, 28, 1))
datos_prueba = datos_prueba.reshape((datos_prueba.shape[0], 28, 28, 1))

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR EL MODELO DE LA RED NEURONAL
# ------------------------------------------------------------------------------------
# - Creamos una red neuronal convolucional (CNN) utilizando la API secuencial de Keras.
# - Incluimos capas convolucionales, de pooling, de aplanamiento y densas.
# - La última capa tiene 10 neuronas (una para cada dígito) con activación softmax para clasificación.
modelo = models.Sequential([
    # Primera capa convolucional:
    # - Conv2D aplica filtros de 3x3 para extraer características de las imágenes.
    # - ReLU es una función de activación que introduce no linealidad.
    # - MaxPooling2D reduce la dimensionalidad seleccionando los valores máximos en regiones de 2x2.
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Segunda capa convolucional:
    # - Similar a la primera, pero con 64 filtros para capturar características más complejas.
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Capa de aplanamiento:
    # - Convierte las características 2D en un vector 1D para conectarlas a las capas densas.
    layers.Flatten(),
    
    # Capa densa:
    # - Contiene 64 neuronas con activación ReLU para aprender patrones complejos.
    layers.Dense(64, activation='relu'),
    
    # Capa de salida:
    # - Contiene 10 neuronas (una para cada dígito del 0 al 9).
    # - La activación softmax convierte las salidas en probabilidades.
    layers.Dense(10, activation='softmax')
])

# ------------------------------------------------------------------------------------
# PASO 4: COMPILAR EL MODELO
# ------------------------------------------------------------------------------------
# - Especificamos el optimizador, la función de pérdida y la métrica de evaluación.
# - Adam es un optimizador eficiente para redes neuronales.
# - Sparse Categorical Crossentropy se utiliza para problemas de clasificación multiclase.
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# ------------------------------------------------------------------------------------
# PASO 5: ENTRENAR EL MODELO
# ------------------------------------------------------------------------------------
# - Entrenamos el modelo con los datos de entrenamiento durante 5 épocas.
# - Cada época representa un ciclo completo sobre los datos de entrenamiento.
modelo.fit(datos_entrenamiento, etiquetas_entrenamiento, epochs=5)

# ------------------------------------------------------------------------------------
# PASO 6: EVALUAR EL MODELO
# ------------------------------------------------------------------------------------
# - Evaluamos el modelo con los datos de prueba para medir su precisión.
# - La precisión indica el porcentaje de predicciones correctas.
perdida, precision = modelo.evaluate(datos_prueba, etiquetas_prueba)
print(f"Precisión del modelo: {precision * 100:.2f}%")

# ------------------------------------------------------------------------------------
# PASO 7: REALIZAR UNA PREDICCIÓN PRÁCTICA
# ------------------------------------------------------------------------------------
# - Seleccionamos una imagen de prueba para predecir el dígito que contiene.
# - Mostramos la imagen junto con el dígito predicho.
indice = 0  # Cambia este valor para probar con otras imágenes
imagen_prueba = datos_prueba[indice].reshape(1, 28, 28, 1)

# Realizamos la predicción utilizando el modelo entrenado.
prediccion = modelo.predict(imagen_prueba)
digito_predicho = np.argmax(prediccion)

# Mostramos la imagen y el resultado de la predicción.
plt.imshow(datos_prueba[indice].reshape(28, 28), cmap='gray')
plt.title(f"Dígito predicho: {digito_predicho}")
plt.show()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza una red neuronal convolucional (CNN) para extraer características
#    de las imágenes y clasificarlas en una de las 10 categorías (dígitos del 0 al 9).
# 2. Suposiciones clave:
#    - Las imágenes están normalizadas (valores entre 0 y 1).
#    - Los datos de entrenamiento y prueba están correctamente etiquetados.
# 3. Ventajas:
#    - Las CNN son muy efectivas para tareas de visión por computadora.
#    - El modelo es rápido y preciso para conjuntos de datos como MNIST.
# 4. Limitaciones:
#    - El modelo puede no generalizar bien a imágenes fuera del conjunto MNIST.
#    - Requiere un conjunto de datos grande y bien etiquetado para entrenarse correctamente.