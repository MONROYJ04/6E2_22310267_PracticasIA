# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO ID3 PARA LA CONSTRUCCIÓN DE ÁRBOLES DE DECISIÓN
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo ID3 para construir un árbol de decisión basado
# en la ganancia de información. El objetivo es clasificar datos categóricos de manera
# eficiente, dividiendo el conjunto de datos en función de los atributos más relevantes.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `pandas` para manejar los datos en formato de tablas (DataFrames).
# - Importamos `math` para realizar cálculos matemáticos como logaritmos.
import pandas as pd
import math

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PARA CALCULAR LA ENTROPÍA
# ------------------------------------------------------------------------------------
# - La entropía mide la incertidumbre o desorden en un conjunto de datos.
# - Es un concepto clave en teoría de la información y se calcula con la fórmula:
#   Entropía = -Σ(p_i * log2(p_i)), donde p_i es la probabilidad de cada clase.
# - Esta función toma como entrada un DataFrame y la columna objetivo (clase a predecir).
def calcular_entropia(datos, columna_objetivo):
    # Contamos la frecuencia de cada valor en la columna objetivo
    valores = datos[columna_objetivo].value_counts()
    entropia = 0

    # Calculamos la entropía usando la fórmula de Shannon
    for frecuencia in valores:
        probabilidad = frecuencia / len(datos)
        entropia -= probabilidad * math.log2(probabilidad)
    return entropia

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA FUNCIÓN PARA CALCULAR LA GANANCIA DE INFORMACIÓN
# ------------------------------------------------------------------------------------
# - La ganancia de información mide cuánto reduce la entropía al dividir los datos
#   según un atributo. Es la diferencia entre la entropía inicial y la entropía
#   condicional (después de dividir los datos).
# - Fórmula: Ganancia = Entropía_inicial - Entropía_condicional.
# - Esta función toma como entrada el DataFrame, la columna objetivo y el atributo.
def calcular_ganancia(datos, columna_objetivo, columna_atributo):
    # Calculamos la entropía inicial del conjunto de datos
    entropia_inicial = calcular_entropia(datos, columna_objetivo)
    valores = datos[columna_atributo].unique()
    entropia_condicional = 0

    # Calculamos la entropía condicional para cada valor del atributo
    for valor in valores:
        subconjunto = datos[datos[columna_atributo] == valor]
        probabilidad = len(subconjunto) / len(datos)
        entropia_condicional += probabilidad * calcular_entropia(subconjunto, columna_objetivo)

    # La ganancia de información es la diferencia entre la entropía inicial y la condicional
    ganancia = entropia_inicial - entropia_condicional
    return ganancia

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR LA FUNCIÓN PARA CONSTRUIR EL ÁRBOL DE DECISIÓN
# ------------------------------------------------------------------------------------
# - Esta función implementa el algoritmo ID3 recursivamente para construir el árbol.
# - En cada paso, selecciona el atributo con mayor ganancia de información y divide
#   los datos en subconjuntos según los valores de ese atributo.
# - Si todos los datos tienen la misma clase o no quedan atributos, se detiene.
def construir_arbol(datos, columna_objetivo, atributos):
    # Caso base 1: Si todos los ejemplos tienen la misma clase, devolvemos esa clase
    if len(datos[columna_objetivo].unique()) == 1:
        return datos[columna_objetivo].iloc[0]

    # Caso base 2: Si no quedan atributos para dividir, devolvemos la clase mayoritaria
    if len(atributos) == 0:
        return datos[columna_objetivo].mode()[0]

    # Elegimos el mejor atributo basado en la ganancia de información
    mejor_atributo = max(atributos, key=lambda atributo: calcular_ganancia(datos, columna_objetivo, atributo))
    arbol = {mejor_atributo: {}}

    # Dividimos los datos según los valores del mejor atributo
    for valor in datos[mejor_atributo].unique():
        subconjunto = datos[datos[mejor_atributo] == valor]
        nuevos_atributos = [atributo for atributo in atributos if atributo != mejor_atributo]
        arbol[mejor_atributo][valor] = construir_arbol(subconjunto, columna_objetivo, nuevos_atributos)

    return arbol

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Creamos un conjunto de datos de ejemplo con información sobre el clima y si se juega.
# - Construimos el árbol de decisión usando el algoritmo ID3.
# - Mostramos el árbol generado para entender cómo se toman las decisiones.
if __name__ == "__main__":
    # Creamos un conjunto de datos de ejemplo
    datos = pd.DataFrame({
        'Clima': ['Soleado', 'Soleado', 'Nublado', 'Lluvioso', 'Lluvioso', 'Lluvioso', 'Nublado', 'Soleado', 'Soleado', 'Lluvioso'],
        'Temperatura': ['Caliente', 'Caliente', 'Caliente', 'Templado', 'Frio', 'Frio', 'Frio', 'Templado', 'Frio', 'Templado'],
        'Humedad': ['Alta', 'Alta', 'Alta', 'Alta', 'Normal', 'Normal', 'Normal', 'Alta', 'Normal', 'Alta'],
        'Viento': ['Debil', 'Fuerte', 'Debil', 'Debil', 'Debil', 'Fuerte', 'Fuerte', 'Debil', 'Debil', 'Fuerte'],
        'Jugar': ['No', 'No', 'Si', 'Si', 'Si', 'No', 'Si', 'No', 'Si', 'Si']
    })

    # Definimos la columna objetivo y los atributos
    columna_objetivo = 'Jugar'
    atributos = ['Clima', 'Temperatura', 'Humedad', 'Viento']

    # Construimos el árbol de decisión
    arbol = construir_arbol(datos, columna_objetivo, atributos)

    # Mostramos el árbol resultante
    print("Árbol de decisión generado:")
    print(arbol)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo ID3 utiliza la ganancia de información para seleccionar el atributo
#    más relevante en cada paso, dividiendo los datos de manera recursiva.
# 2. Suposiciones clave:
#    - Los datos son categóricos.
#    - La columna objetivo tiene valores discretos.
# 3. Ventajas:
#    - Fácil de interpretar.
#    - Útil para problemas de clasificación.
#    Limitaciones:
#    - No maneja bien datos continuos sin preprocesamiento.
#    - Puede sobreajustarse si los datos tienen ruido.