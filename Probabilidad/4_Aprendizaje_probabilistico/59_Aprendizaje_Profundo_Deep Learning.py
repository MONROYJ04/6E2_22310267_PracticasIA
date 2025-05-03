# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RED NEURONAL PARA CLASIFICACIÓN DE DÍGITOS ESCRITOS A MANO
# ------------------------------------------------------------------------------------
# Este código utiliza una red neuronal profunda para clasificar imágenes de dígitos escritos
# a mano del conjunto de datos MNIST. El objetivo es entrenar un modelo que pueda identificar
# correctamente el dígito representado en una imagen.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos TensorFlow para construir y entrenar la red neuronal.
# - Importamos matplotlib para visualizar las imágenes del conjunto de datos.
# - Importamos el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano.
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# PASO 2: CARGA DEL CONJUNTO DE DATOS MNIST
# ------------------------------------------------------------------------------------
# - Cargamos el conjunto de datos MNIST, que está dividido en datos de entrenamiento y prueba.
# - `datos_entrenamiento` y `etiquetas_entrenamiento` se usan para entrenar el modelo.
# - `datos_prueba` y `etiquetas_prueba` se usan para evaluar el modelo.
(datos_entrenamiento, etiquetas_entrenamiento), (datos_prueba, etiquetas_prueba) = mnist.load_data()

# ------------------------------------------------------------------------------------
# PASO 3: NORMALIZACIÓN DE LOS DATOS
# ------------------------------------------------------------------------------------
# - Dividimos los valores de los píxeles entre 255 para normalizarlos al rango [0, 1].
# - Esto ayuda al modelo a entrenar más rápido y con mayor estabilidad.
datos_entrenamiento = datos_entrenamiento / 255.0
datos_prueba = datos_prueba / 255.0

# ------------------------------------------------------------------------------------
# PASO 4: VISUALIZACIÓN DE UNA IMAGEN DE ENTRENAMIENTO
# ------------------------------------------------------------------------------------
# - Mostramos una imagen del conjunto de datos para entender qué estamos clasificando.
# - Usamos `plt.imshow` para visualizar la imagen en escala de grises.
plt.imshow(datos_entrenamiento[0], cmap='gray')
plt.title(f"Etiqueta: {etiquetas_entrenamiento[0]}")  # Mostramos la etiqueta correspondiente.
plt.show()

# ------------------------------------------------------------------------------------
# PASO 5: CREACIÓN DEL MODELO DE RED NEURONAL
# ------------------------------------------------------------------------------------
# - Creamos un modelo secuencial, que es una pila lineal de capas.
# - La primera capa aplana las imágenes de 28x28 píxeles a un vector de 784 valores.
# - La segunda capa es una capa oculta con 128 neuronas y función de activación ReLU.
# - La tercera capa es la capa de salida con 10 neuronas (una por cada dígito) y activación softmax.
modelo = Sequential([
    Flatten(input_shape=(28, 28)),  # Aplanamos las imágenes.
    Dense(128, activation='relu'),  # Capa oculta con activación ReLU.
    Dense(10, activation='softmax') # Capa de salida con activación softmax.
])

# ------------------------------------------------------------------------------------
# PASO 6: COMPILACIÓN DEL MODELO
# ------------------------------------------------------------------------------------
# - Configuramos el modelo para el entrenamiento.
# - Usamos la función de pérdida `sparse_categorical_crossentropy` para clasificación categórica.
# - El optimizador `adam` ajusta los pesos del modelo durante el entrenamiento.
# - La métrica `accuracy` mide qué tan preciso es el modelo.
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# ------------------------------------------------------------------------------------
# PASO 7: ENTRENAMIENTO DEL MODELO
# ------------------------------------------------------------------------------------
# - Entrenamos el modelo con los datos de entrenamiento.
# - `epochs=5` indica que el modelo verá todo el conjunto de datos 5 veces.
modelo.fit(datos_entrenamiento, etiquetas_entrenamiento, epochs=5)

# ------------------------------------------------------------------------------------
# PASO 8: EVALUACIÓN DEL MODELO
# ------------------------------------------------------------------------------------
# - Evaluamos el modelo con los datos de prueba para medir su rendimiento.
# - `modelo.evaluate` devuelve la pérdida y la precisión del modelo.
perdida, precision = modelo.evaluate(datos_prueba, etiquetas_prueba)
print(f"Precisión en datos de prueba: {precision * 100:.2f}%")

# ------------------------------------------------------------------------------------
# PASO 9: PREDICCIÓN CON UNA IMAGEN DE PRUEBA
# ------------------------------------------------------------------------------------
# - Seleccionamos una imagen del conjunto de prueba para hacer una predicción.
# - Mostramos la imagen y su etiqueta real.
indice = 0  # Cambia este valor para probar con diferentes imágenes.
imagen = datos_prueba[indice]
etiqueta_real = etiquetas_prueba[indice]

# Mostramos la imagen seleccionada.
plt.imshow(imagen, cmap='gray')
plt.title("Imagen de prueba")
plt.show()

# Redimensionamos la imagen para que sea compatible con el modelo.
imagen = imagen.reshape(1, 28, 28)

# Hacemos la predicción con el modelo.
prediccion = modelo.predict(imagen)
clase_predicha = prediccion.argmax()  # Obtenemos la clase con mayor probabilidad.

print(f"Etiqueta real: {etiqueta_real}")
print(f"Clase predicha por el modelo: {clase_predicha}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una red neuronal profunda para clasificar imágenes.
# 2. La red tiene una capa de entrada (aplanamiento), una capa oculta (128 neuronas, ReLU)
#    y una capa de salida (10 neuronas, softmax).
# 3. La función de activación ReLU introduce no linealidad, mientras que softmax convierte
#    las salidas en probabilidades.
# 4. El modelo se entrena ajustando los pesos para minimizar la pérdida.
# 5. Ventajas: fácil de implementar y preciso para tareas simples como MNIST.
# 6. Limitaciones: no es adecuado para datos complejos sin modificaciones adicionales.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Supongamos que queremos usar este modelo para reconocer dígitos escritos a mano en un formulario escaneado.
# Por ejemplo, un sistema bancario podría usar este modelo para leer automáticamente los números de cheques.

# Seleccionamos una nueva imagen del conjunto de prueba.
indice_nuevo = 15  # Cambia este valor para probar con diferentes imágenes.
imagen_nueva = datos_prueba[indice_nuevo]
etiqueta_real_nueva = etiquetas_prueba[indice_nuevo]

# Mostramos la nueva imagen seleccionada.
plt.imshow(imagen_nueva, cmap='gray')
plt.title("Nueva imagen de prueba")
plt.show()

# Redimensionamos la imagen para que sea compatible con el modelo.
imagen_nueva = imagen_nueva.reshape(1, 28, 28)

# Hacemos la predicción con el modelo.
prediccion_nueva = modelo.predict(imagen_nueva)
clase_predicha_nueva = prediccion_nueva.argmax()  # Obtenemos la clase con mayor probabilidad.

# Mostramos los resultados.
print(f"Etiqueta real de la nueva imagen: {etiqueta_real_nueva}")
print(f"Clase predicha por el modelo: {clase_predicha_nueva}")

# ------------------------------------------------------------------------------------
# RESULTADO ESPERADO
# ------------------------------------------------------------------------------------
# El modelo debería predecir correctamente el dígito representado en la imagen.
# Por ejemplo, si la imagen contiene un "5", el modelo debería predecir la clase "5".
# Esto demuestra cómo el modelo puede ser usado en aplicaciones prácticas como el reconocimiento
# automático de caracteres escritos a mano.