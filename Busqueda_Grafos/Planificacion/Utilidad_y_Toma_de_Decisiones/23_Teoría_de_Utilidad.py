# Este programa implementa un algoritmo basado en la Teoría de la Utilidad.
# La Teoría de la Utilidad se utiliza para tomar decisiones racionales
# en situaciones donde hay incertidumbre. Este algoritmo incluye una función
# de utilidad que asigna un valor numérico a cada posible resultado.

# Definimos la función de utilidad
def funcion_utilidad(resultado):
    """
    Esta función asigna un valor de utilidad a un resultado dado.
    La utilidad es una medida de cuán deseable es un resultado.

    Parametros:
    resultado (str): El resultado para el cual se calculará la utilidad.

    Retorna:
    float: El valor de utilidad asociado al resultado.
    """
    # Diccionario que asigna valores de utilidad a diferentes resultados
    utilidades = {
        "exito": 1.0,  # El éxito tiene la máxima utilidad
        "fracaso": 0.0,  # El fracaso tiene la mínima utilidad
        "riesgo_moderado": 0.5,  # Un riesgo moderado tiene una utilidad intermedia
    }
    # Retornamos la utilidad correspondiente al resultado
    return utilidades.get(resultado, 0.0)  # Si el resultado no está definido, retorna 0.0

# Ejemplo práctico: Evaluación de decisiones
def ejemplo_practico():
    """
    Este ejemplo práctico muestra cómo usar la función de utilidad
    para tomar una decisión racional basada en los posibles resultados.
    """
    # Definimos los posibles resultados de una decisión
    resultados = ["exito", "fracaso", "riesgo_moderado", "desconocido"]

    # Calculamos la utilidad de cada resultado
    print("Evaluando utilidades de los resultados:")
    for resultado in resultados:
        utilidad = funcion_utilidad(resultado)
        print(f"Resultado: {resultado}, Utilidad: {utilidad}")

    # Supongamos que queremos tomar una decisión basada en la utilidad
    # Seleccionamos el resultado con la mayor utilidad
    mejor_resultado = max(resultados, key=funcion_utilidad)
    print(f"\nEl mejor resultado basado en la utilidad es: {mejor_resultado}")

# Llamamos al ejemplo práctico para demostrar el algoritmo
if __name__ == "__main__":
    ejemplo_practico()