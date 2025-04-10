# Este algoritmo calcula la probabilidad a priori, que es la probabilidad inicial
# de que ocurra un evento antes de observar cualquier evidencia adicional.

# Definimos una funcion para calcular la probabilidad a priori
def calcular_probabilidad_a_priori(casos_favorables, casos_totales):
    """
    Calcula la probabilidad a priori de un evento.

    Parametros:
    casos_favorables (int): Numero de casos en los que ocurre el evento deseado.
    casos_totales (int): Numero total de casos posibles.

    Retorna:
    float: Probabilidad a priori del evento.
    """
    # Validamos que los casos totales no sean cero para evitar division por cero
    if casos_totales == 0:
        raise ValueError("El numero de casos totales no puede ser cero.")
    
    # Calculamos la probabilidad dividiendo los casos favorables entre los casos totales
    probabilidad = casos_favorables / casos_totales
    
    # Retornamos el resultado
    return probabilidad

# Ejemplo practico:
# Supongamos que estamos lanzando un dado justo de 6 caras.
# Queremos calcular la probabilidad de que salga un numero impar (1, 3 o 5).

# Definimos los casos favorables (numeros impares en un dado de 6 caras)
casos_favorables = 3  # Los numeros impares son: 1, 3, 5

# Definimos los casos totales (total de caras del dado)
casos_totales = 6  # El dado tiene 6 caras en total

# Calculamos la probabilidad a priori
probabilidad_impar = calcular_probabilidad_a_priori(casos_favorables, casos_totales)

# Mostramos el resultado
print("La probabilidad a priori de obtener un numero impar al lanzar un dado es:", probabilidad_impar)

# Explicacion del resultado:
# En este caso, la probabilidad a priori es 3/6 = 0.5 o 50%.
# Esto significa que, antes de lanzar el dado, hay un 50% de probabilidad de que salga un numero impar.