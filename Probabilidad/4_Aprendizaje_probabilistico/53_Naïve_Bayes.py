# Importamos las bibliotecas necesarias
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.naive_bayes import GaussianNB  # Para usar el modelo de Naïve-Bayes Gaussiano
from sklearn.metrics import accuracy_score  # Para calcular la precisión del modelo

# Creamos un conjunto de datos de ejemplo
# Este conjunto de datos contiene información sobre si una persona compra o no un producto
# Basado en su edad y su ingreso mensual
import pandas as pd  # Biblioteca para manejar datos en formato de tablas (DataFrames)

# Creamos un DataFrame con los datos
datos = pd.DataFrame({
    'edad': [25, 30, 45, 35, 50, 23, 40, 60, 48, 33],  # Edad de las personas
    'ingreso_mensual': [2000, 2500, 4000, 3000, 5000, 1800, 3500, 6000, 4500, 2800],  # Ingreso mensual
    'compra': ['no', 'no', 'si', 'si', 'si', 'no', 'si', 'si', 'si', 'no']  # Si compran ('si') o no ('no')
})

# Dividimos los datos en características (X) y la variable objetivo (y)
# X contiene las columnas que usaremos para predecir (edad e ingreso mensual)
# y contiene la columna que queremos predecir (compra)
X = datos[['edad', 'ingreso_mensual']]  # Características
y = datos['compra']  # Variable objetivo

# Dividimos los datos en conjuntos de entrenamiento y prueba
# El conjunto de entrenamiento se usa para entrenar el modelo
# El conjunto de prueba se usa para evaluar el modelo
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos un modelo de Naïve-Bayes Gaussiano
# Este modelo asume que las características siguen una distribución normal (gaussiana)
modelo = GaussianNB()

# Entrenamos el modelo con los datos de entrenamiento
# Aquí el modelo aprende las probabilidades necesarias para hacer predicciones
modelo.fit(X_entrenamiento, y_entrenamiento)

# Realizamos predicciones con los datos de prueba
# El modelo usa lo que aprendió para predecir si las personas en el conjunto de prueba comprarán o no
predicciones = modelo.predict(X_prueba)

# Calculamos la precisión del modelo
# La precisión mide qué tan bien el modelo predijo los resultados correctos
precision = accuracy_score(y_prueba, predicciones)

# Mostramos los resultados
print("Predicciones:", predicciones)  # Muestra las predicciones del modelo
print("Precisión del modelo:", precision)  # Muestra la precisión del modelo

# Ejemplo práctico:
# Supongamos que queremos predecir si una persona de 28 años con un ingreso mensual de 2200 comprará el producto
nueva_persona = [[28, 2200]]  # Datos de la nueva persona
prediccion_nueva = modelo.predict(nueva_persona)  # El modelo hace la predicción
print("¿La persona comprará el producto?", prediccion_nueva[0])  # Muestra el resultado de la predicción

# Explicación del algoritmo:
# 1. El algoritmo de Naïve-Bayes asume que las características (edad, ingreso mensual) son independientes entre sí.
# 2. Calcula la probabilidad de que una instancia (persona) pertenezca a cada clase ('si' o 'no').
# 3. Asigna la clase con la mayor probabilidad a la instancia.
# 4. En este ejemplo, usamos el modelo Gaussiano, que es adecuado para datos continuos como la edad y el ingreso mensual.