# Importamos la biblioteca necesaria para manejar datos en forma de tablas
import pandas as pd

# Funcion para realizar la eliminacion de variables en una red bayesiana
def eliminacion_de_variables(tabla, variable_a_eliminar):
    """
    Esta funcion realiza la eliminacion de una variable en una tabla de probabilidad conjunta.
    La eliminacion se realiza sumando las probabilidades sobre los valores de la variable a eliminar.

    Parametros:
    tabla (pd.DataFrame): Tabla de probabilidad conjunta.
    variable_a_eliminar (str): Nombre de la variable que se desea eliminar.

    Retorna:
    pd.DataFrame: Nueva tabla con la variable eliminada.
    """
    # Identificamos las columnas que no se van a eliminar
    columnas_a_conservar = [col for col in tabla.columns if col != variable_a_eliminar and col != 'Probabilidad']

    # Agrupamos por las columnas que se conservan y sumamos las probabilidades
    nueva_tabla = tabla.groupby(columnas_a_conservar)['Probabilidad'].sum().reset_index()

    # Retornamos la nueva tabla sin la variable eliminada
    return nueva_tabla

# Ejemplo practico: Eliminacion de variables en una tabla de probabilidad conjunta
if __name__ == "__main__":
    # Creamos una tabla de probabilidad conjunta como ejemplo
    # La tabla representa las probabilidades conjuntas de tres variables: A, B y C
    datos = {
        'A': ['si', 'si', 'si', 'si', 'no', 'no', 'no', 'no'],
        'B': ['si', 'si', 'no', 'no', 'si', 'si', 'no', 'no'],
        'C': ['si', 'no', 'si', 'no', 'si', 'no', 'si', 'no'],
        'Probabilidad': [0.1, 0.2, 0.1, 0.1, 0.15, 0.05, 0.1, 0.2]
    }

    # Convertimos los datos en un DataFrame de pandas
    tabla_probabilidad = pd.DataFrame(datos)

    # Mostramos la tabla original
    print("Tabla de probabilidad conjunta original:")
    print(tabla_probabilidad)

    # Eliminamos la variable 'C' de la tabla
    tabla_sin_c = eliminacion_de_variables(tabla_probabilidad, 'C')

    # Mostramos la tabla resultante
    print("\nTabla despues de eliminar la variable 'C':")
    print(tabla_sin_c)

    # Eliminamos la variable 'B' de la tabla resultante
    tabla_sin_b = eliminacion_de_variables(tabla_sin_c, 'B')

    # Mostramos la tabla final
    print("\nTabla despues de eliminar la variable 'B':")
    print(tabla_sin_b)