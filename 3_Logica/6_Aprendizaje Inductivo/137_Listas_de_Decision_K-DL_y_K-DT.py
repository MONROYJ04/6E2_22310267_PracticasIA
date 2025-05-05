# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: LISTAS DE DECISIÓN (K-DL) Y ÁRBOLES DE DECISIÓN (K-DT)
# ------------------------------------------------------------------------------------
# Este código implementa un algoritmo para generar Listas de Decisión (K-DL) a partir
# de un Árbol de Decisión (K-DT). Las Listas de Decisión son secuencias de reglas que
# permiten clasificar datos de manera interpretable.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - `numpy`: Para manejar datos numéricos y matrices.
# - `sklearn.tree.DecisionTreeClassifier`: Para crear y entrenar árboles de decisión.
# - `sklearn.model_selection.train_test_split`: Para dividir los datos en entrenamiento y prueba.
# - `sklearn.metrics.accuracy_score`: Para evaluar la precisión del modelo.
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA CREAR UNA LISTA DE DECISIÓN (K-DL)
# ------------------------------------------------------------------------------------
# - Esta función genera una Lista de Decisión (K-DL) a partir de un Árbol de Decisión.
# - La Lista de Decisión es una secuencia de reglas que clasifica los datos.
# - Parámetros:
#   - `X`: Matriz de características (datos de entrada).
#   - `y`: Vector de etiquetas (clases).
#   - `max_nivel`: Profundidad máxima del árbol de decisión.
# - Retorna:
#   - `lista_reglas`: Lista de reglas generadas por el árbol de decisión.
def crear_lista_decision(X, y, max_nivel):
    """
    Esta función crea una Lista de Decisión (K-DL) utilizando un árbol de decisión.
    """
    # Creamos un clasificador de árbol de decisión con una profundidad máxima
    arbol = DecisionTreeClassifier(max_depth=max_nivel)
    arbol.fit(X, y)  # Entrenamos el árbol con los datos

    # Extraemos las reglas del árbol
    lista_reglas = extraer_reglas(arbol, X.columns)
    return lista_reglas

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN PARA EXTRAER REGLAS DEL ÁRBOL DE DECISIÓN
# ------------------------------------------------------------------------------------
# - Esta función convierte un Árbol de Decisión en una lista de reglas legibles.
# - Parámetros:
#   - `arbol`: Modelo de árbol de decisión entrenado.
#   - `nombres_columnas`: Nombres de las columnas de los datos.
# - Retorna:
#   - `reglas`: Lista de reglas en formato legible.
def extraer_reglas(arbol, nombres_columnas):
    """
    Extrae las reglas de un árbol de decisión.
    """
    reglas = []
    # Obtenemos las reglas del árbol
    n_nodos = arbol.tree_.node_count
    for nodo in range(n_nodos):
        if arbol.tree_.children_left[nodo] == -1:  # Nodo hoja
            regla = f"Si {nombres_columnas[arbol.tree_.feature[nodo]]} <= {arbol.tree_.threshold[nodo]} entonces {arbol.classes_[np.argmax(arbol.tree_.value[nodo])]}"
            reglas.append(regla)
    return reglas

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos ficticio con características como altura y peso.
# - Clasificamos si una persona es apta (1) o no apta (0) según las reglas generadas.
if __name__ == "__main__":
    # Creamos un conjunto de datos de ejemplo
    # X: Características (altura, peso)
    # y: Clases (0: No apto, 1: Apto)
    datos = np.array([
        [1.70, 70, 1],  # Persona 1
        [1.60, 60, 0],  # Persona 2
        [1.80, 80, 1],  # Persona 3
        [1.50, 50, 0],  # Persona 4
    ])
    X = datos[:, :-1]  # Características
    y = datos[:, -1]   # Clases

    # Dividimos los datos en entrenamiento y prueba
    # - `test_size=0.25`: El 25% de los datos se usa para prueba.
    # - `random_state=42`: Asegura que la división sea reproducible.
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.25, random_state=42)

    # Creamos una Lista de Decisión con profundidad máxima de 2
    lista_decision = crear_lista_decision(X_entrenamiento, y_entrenamiento, max_nivel=2)

    # Mostramos las reglas generadas
    print("Reglas generadas por la Lista de Decisión:")
    for regla in lista_decision:
        print(regla)

    # Evaluamos el modelo en los datos de prueba
    modelo = DecisionTreeClassifier(max_depth=2)
    modelo.fit(X_entrenamiento, y_entrenamiento)
    y_pred = modelo.predict(X_prueba)
    print("\nExactitud del modelo:", accuracy_score(y_prueba, y_pred))

    # --------------------------------------------------------------------------------
    # EJEMPLO ADICIONAL: PREDICCIÓN DE UNA NUEVA PERSONA
    # --------------------------------------------------------------------------------
    # - Creamos un nuevo dato (persona) con altura y peso.
    # - Usamos el modelo para predecir si es apto o no apto.
    nueva_persona = np.array([[1.65, 65]])  # Altura: 1.65m, Peso: 65kg
    prediccion = modelo.predict(nueva_persona)
    print("\nPredicción para nueva persona (1: Apto, 0: No apto):", prediccion[0])

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Árbol de Decisión (K-DT)**:
#    - Divide los datos en nodos basados en condiciones (reglas) para clasificar.
#    - Cada nodo representa una decisión basada en una característica.
# 2. **Lista de Decisión (K-DL)**:
#    - Convierte las decisiones del árbol en una lista de reglas legibles.
#    - Ejemplo: "Si altura <= 1.65 entonces No apto".
# 3. **Ventajas**:
#    - Fácil de interpretar.
#    - Útil para explicar decisiones a personas no técnicas.
# 4. **Limitaciones**:
#    - Menos eficiente para datos complejos.
#    - Puede sobreajustarse si la profundidad del árbol es muy alta.