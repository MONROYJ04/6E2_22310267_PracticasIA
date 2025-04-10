# Este programa calcula la distribución de probabilidad de un conjunto de datos.
# La distribución de probabilidad muestra la probabilidad de que ocurra cada valor en un conjunto de datos.

# Importamos la biblioteca necesaria para manejar datos y cálculos matemáticos
import numpy as np

# Función para calcular la distribución de probabilidad
def calcular_distribucion_probabilidad(datos):
    """
    Calcula la distribución de probabilidad de un conjunto de datos.

    Parametros:
    datos (list): Lista de valores numéricos.

    Retorna:
    dict: Un diccionario donde las claves son los valores únicos de los datos
          y los valores son las probabilidades asociadas.
    """
    # Convertimos los datos a un arreglo de numpy para facilitar los cálculos
    datos_array = np.array(datos)
    
    # Obtenemos los valores únicos y sus frecuencias
    valores_unicos, frecuencias = np.unique(datos_array, return_counts=True)
    
    # Calculamos la probabilidad dividiendo las frecuencias entre el total de datos
    probabilidades = frecuencias / len(datos_array)
    
    # Creamos un diccionario para almacenar los valores únicos y sus probabilidades
    distribucion = dict(zip(valores_unicos, probabilidades))
    
    return distribucion

# Ejemplo práctico
if __name__ == "__main__":
    # Conjunto de datos de ejemplo
    # Supongamos que estos datos representan las calificaciones de un grupo de estudiantes
    datos_ejemplo = [8, 9, 10, 8, 7, 9, 8, 10, 7, 8]
    
    # Llamamos a la función para calcular la distribución de probabilidad
    distribucion = calcular_distribucion_probabilidad(datos_ejemplo)
    
    # Mostramos los resultados
    print("Distribución de Probabilidad:")
    for valor, probabilidad in distribucion.items():
        print(f"Valor: {valor}, Probabilidad: {probabilidad:.2f}")