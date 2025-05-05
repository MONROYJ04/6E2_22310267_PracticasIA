# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ÁRBOL DE DECISIÓN PARA GENERAR EXPLICACIONES BASADAS EN DATOS
# ------------------------------------------------------------------------------------
# Este código utiliza un modelo de árbol de decisión para identificar patrones en un 
# conjunto de datos y generar explicaciones basadas en las características más relevantes.
# El objetivo es predecir una variable objetivo y entender qué factores influyen más 
# en dicha predicción.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `pandas` para manejar datos tabulares.
# - Importamos `DecisionTreeClassifier` de `sklearn` para construir el modelo.
# - Importamos `train_test_split` para dividir los datos en entrenamiento y prueba.
# - Importamos `accuracy_score` para evaluar la precisión del modelo.
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - Esta función entrena un modelo de árbol de decisión para predecir una columna objetivo.
# - Genera explicaciones basadas en las características más relevantes del modelo.
# - Recibe como parámetros:
#   - `datos`: Un DataFrame con los datos de entrada.
#   - `columna_objetivo`: El nombre de la columna que se desea predecir.
def generar_explicaciones(datos, columna_objetivo):
    """
    Esta función entrena un modelo de árbol de decisión para predecir una columna objetivo
    y genera explicaciones basadas en las características más relevantes.

    :param datos: DataFrame con los datos de entrada.
    :param columna_objetivo: Nombre de la columna que se desea predecir.
    :return: Modelo entrenado y las características más importantes.
    """
    # --------------------------------------------------------------------------------
    # PASO 3: SEPARAR LAS CARACTERÍSTICAS Y LA COLUMNA OBJETIVO
    # --------------------------------------------------------------------------------
    # - `X` contiene todas las columnas excepto la columna objetivo.
    # - `y` contiene únicamente la columna objetivo.
    # - Esto es necesario porque el modelo necesita saber qué predecir (`y`) y con qué 
    #   características (`X`) hacerlo.
    X = datos.drop(columns=[columna_objetivo])
    y = datos[columna_objetivo]

    # --------------------------------------------------------------------------------
    # PASO 4: DIVIDIR LOS DATOS EN ENTRENAMIENTO Y PRUEBA
    # --------------------------------------------------------------------------------
    # - Dividimos los datos en dos conjuntos:
    #   - Entrenamiento (70% de los datos): Para entrenar el modelo.
    #   - Prueba (30% de los datos): Para evaluar el modelo.
    # - `random_state=42` asegura que los resultados sean reproducibles.
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

    # --------------------------------------------------------------------------------
    # PASO 5: CREAR Y ENTRENAR EL MODELO
    # --------------------------------------------------------------------------------
    # - Usamos un árbol de decisión (`DecisionTreeClassifier`) como modelo.
    # - Entrenamos el modelo con los datos de entrenamiento (`fit`).
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_entrenamiento, y_entrenamiento)

    # --------------------------------------------------------------------------------
    # PASO 6: EVALUAR EL MODELO
    # --------------------------------------------------------------------------------
    # - Realizamos predicciones con los datos de prueba (`predict`).
    # - Calculamos la precisión del modelo comparando las predicciones con los valores reales.
    predicciones = modelo.predict(X_prueba)
    precision = accuracy_score(y_prueba, predicciones)
    print(f"Precisión del modelo: {precision:.2f}")

    # --------------------------------------------------------------------------------
    # PASO 7: IDENTIFICAR LAS CARACTERÍSTICAS MÁS IMPORTANTES
    # --------------------------------------------------------------------------------
    # - `feature_importances_` devuelve la importancia de cada característica.
    # - Ordenamos las características por su importancia de mayor a menor.
    importancia_caracteristicas = modelo.feature_importances_
    caracteristicas = X.columns
    explicaciones = sorted(zip(caracteristicas, importancia_caracteristicas), key=lambda x: x[1], reverse=True)

    # Mostramos las características más relevantes.
    print("Características más relevantes:")
    for caracteristica, importancia in explicaciones:
        print(f"{caracteristica}: {importancia:.2f}")

    # Devolvemos el modelo entrenado y las explicaciones.
    return modelo, explicaciones

# ------------------------------------------------------------------------------------
# PASO 8: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos ficticio con columnas como `edad`, `ingresos` y `compra`.
# - Llamamos a la función `generar_explicaciones` para entrenar el modelo y generar 
#   explicaciones basadas en los datos.
if __name__ == "__main__":
    # Crear un conjunto de datos de ejemplo
    datos_ejemplo = pd.DataFrame({
        "edad": [25, 30, 35, 40, 45],
        "ingresos": [20000, 30000, 40000, 50000, 60000],
        "compra": [0, 0, 1, 1, 1]  # 0 = No compra, 1 = Compra
    })

    # Llamar a la función para generar explicaciones
    modelo, explicaciones = generar_explicaciones(datos_ejemplo, "compra")

    # Explicación final
    print("\nEl modelo ha identificado las características más relevantes para predecir si una persona compra.")

    # --------------------------------------------------------------------------------
    # PASO 9: PREDICCIÓN DE UN NUEVO CASO
    # --------------------------------------------------------------------------------
    # - Creamos un nuevo caso con valores específicos para `edad` e `ingresos`.
    # - Usamos el modelo entrenado para predecir si esta persona compraría o no.
    nueva_persona = pd.DataFrame({
        "edad": [28],
        "ingresos": [25000]
    })
    prediccion = modelo.predict(nueva_persona)
    print(f"\nPredicción para la nueva persona: {'Compra' if prediccion[0] == 1 else 'No compra'}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El árbol de decisión divide los datos en nodos basándose en las características 
#    que mejor separan las clases (en este caso, `compra` o `no compra`).
# 2. Suposiciones clave:
#    - Las características son relevantes para la predicción.
#    - Los datos no tienen valores faltantes.
# 3. Ventajas:
#    - Fácil de interpretar (muestra qué características son importantes).
#    - Funciona bien con datos categóricos y numéricos.
# 4. Limitaciones:
#    - Puede sobreajustarse si no se controla la profundidad del árbol.