# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: NAÏVE BAYES GAUSSIANO PARA CLASIFICACIÓN BINARIA
# ------------------------------------------------------------------------------------
# Este código implementa un modelo de Naïve Bayes Gaussiano para predecir si una persona
# comprará un producto basado en su edad e ingreso mensual. Utiliza un conjunto de datos
# de ejemplo, entrena el modelo y evalúa su precisión.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos las bibliotecas necesarias para manejar datos, dividirlos en conjuntos
#   de entrenamiento y prueba, construir el modelo y evaluar su desempeño.
# - Estas bibliotecas son fundamentales para realizar tareas de preprocesamiento,
#   modelado y evaluación.
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.naive_bayes import GaussianNB  # Para usar el modelo de Naïve-Bayes Gaussiano
from sklearn.metrics import accuracy_score  # Para calcular la precisión del modelo
import pandas as pd  # Biblioteca para manejar datos en formato de tablas (DataFrames)

# ------------------------------------------------------------------------------------
# PASO 2: CREAR EL CONJUNTO DE DATOS
# ------------------------------------------------------------------------------------
# - Creamos un DataFrame con datos ficticios que representan la edad, el ingreso mensual
#   y si una persona compra o no un producto.
# - Este conjunto de datos será usado para entrenar y evaluar el modelo.
datos = pd.DataFrame({
    'edad': [25, 30, 45, 35, 50, 23, 40, 60, 48, 33],  # Edad de las personas
    'ingreso_mensual': [2000, 2500, 4000, 3000, 5000, 1800, 3500, 6000, 4500, 2800],  # Ingreso mensual
    'compra': ['no', 'no', 'si', 'si', 'si', 'no', 'si', 'si', 'si', 'no']  # Si compran ('si') o no ('no')
})

# ------------------------------------------------------------------------------------
# PASO 3: DIVIDIR LOS DATOS EN CARACTERÍSTICAS Y VARIABLE OBJETIVO
# ------------------------------------------------------------------------------------
# - `X` contiene las características (edad e ingreso mensual) que usaremos para predecir.
# - `y` contiene la variable objetivo (compra), que indica si una persona compra o no.
# - Esto es importante porque separa las entradas (X) de las salidas (y) para el modelo.
X = datos[['edad', 'ingreso_mensual']]  # Características
y = datos['compra']  # Variable objetivo

# ------------------------------------------------------------------------------------
# PASO 4: DIVIDIR LOS DATOS EN ENTRENAMIENTO Y PRUEBA
# ------------------------------------------------------------------------------------
# - Dividimos los datos en dos conjuntos:
#   - Conjunto de entrenamiento: usado para entrenar el modelo.
#   - Conjunto de prueba: usado para evaluar el modelo.
# - `test_size=0.3` significa que el 30% de los datos se usarán para prueba.
# - `random_state=42` asegura que la división sea reproducible.
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

# ------------------------------------------------------------------------------------
# PASO 5: CREAR EL MODELO DE NAÏVE BAYES GAUSSIANO
# ------------------------------------------------------------------------------------
# - Usamos el modelo de Naïve Bayes Gaussiano, que asume que las características siguen
#   una distribución normal (gaussiana).
# - Este modelo es adecuado para datos continuos como la edad y el ingreso mensual.
modelo = GaussianNB()

# ------------------------------------------------------------------------------------
# PASO 6: ENTRENAR EL MODELO
# ------------------------------------------------------------------------------------
# - Entrenamos el modelo con los datos de entrenamiento (`X_entrenamiento` y `y_entrenamiento`).
# - Durante este paso, el modelo aprende las probabilidades necesarias para hacer predicciones.
modelo.fit(X_entrenamiento, y_entrenamiento)

# ------------------------------------------------------------------------------------
# PASO 7: REALIZAR PREDICCIONES
# ------------------------------------------------------------------------------------
# - Usamos el modelo entrenado para predecir si las personas en el conjunto de prueba
#   comprarán o no el producto.
predicciones = modelo.predict(X_prueba)

# ------------------------------------------------------------------------------------
# PASO 8: EVALUAR EL MODELO
# ------------------------------------------------------------------------------------
# - Calculamos la precisión del modelo usando `accuracy_score`.
# - La precisión mide el porcentaje de predicciones correctas realizadas por el modelo.
precision = accuracy_score(y_prueba, predicciones)

# ------------------------------------------------------------------------------------
# PASO 9: MOSTRAR RESULTADOS
# ------------------------------------------------------------------------------------
# - Mostramos las predicciones realizadas por el modelo y su precisión.
print("Predicciones:", predicciones)  # Muestra las predicciones del modelo
print("Precisión del modelo:", precision)  # Muestra la precisión del modelo

# ------------------------------------------------------------------------------------
# PASO 10: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Supongamos que queremos predecir si una persona de 28 años con un ingreso mensual
#   de 2200 comprará el producto.
# - Creamos un nuevo conjunto de datos con esta información y usamos el modelo para predecir.
nueva_persona = [[28, 2200]]  # Datos de la nueva persona
prediccion_nueva = modelo.predict(nueva_persona)  # El modelo hace la predicción
print("¿La persona comprará el producto?", prediccion_nueva[0])  # Muestra el resultado de la predicción

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo de Naïve Bayes asume que las características (edad, ingreso mensual)
#    son independientes entre sí, lo cual simplifica los cálculos.
# 2. Calcula la probabilidad de que una instancia pertenezca a cada clase ('si' o 'no')
#    usando la fórmula de probabilidad condicional de Bayes:
#    P(clase | características) = (P(características | clase) * P(clase)) / P(características)
# 3. En este caso, usamos el modelo Gaussiano, que calcula P(características | clase)
#    asumiendo una distribución normal.
# 4. Ventajas:
#    - Rápido y eficiente para datos pequeños.
#    - Fácil de interpretar.
# 5. Limitaciones:
#    - La suposición de independencia puede no ser realista en algunos casos.
#    - Sensible a datos no gaussianos.