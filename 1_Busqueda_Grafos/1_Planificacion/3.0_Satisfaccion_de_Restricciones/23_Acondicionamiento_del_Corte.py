def acondicionamiento_corte(numeros, objetivo, subconjunto_actual=[], indice=0, suma_actual=0):
    """
    Encuentra subconjuntos de una lista de números que sumen un valor objetivo utilizando el acondicionamiento del corte.
    
    :param numeros: Lista de números enteros.
    :param objetivo: Valor objetivo que se desea alcanzar con la suma de un subconjunto.
    :param subconjunto_actual: Subconjunto que se está construyendo actualmente.
    :param indice: Índice actual en la lista de números.
    :param suma_actual: Suma parcial del subconjunto actual.
    :return: Imprime los subconjuntos válidos que cumplen con la condición.
    """
    # Si la suma actual es igual al objetivo, se encontró un subconjunto válido
    if suma_actual == objetivo:
        print(subconjunto_actual)  # Imprime el subconjunto encontrado
        return
    
    # Si se han recorrido todos los números o la suma actual supera el objetivo, se detiene la búsqueda en esta rama
    if indice >= len(numeros) or suma_actual > objetivo:
        return  # Corte: no hay solución en esta rama
    
    # Incluir el número actual en el subconjunto
    # Se llama recursivamente con el número actual incluido
    acondicionamiento_corte(
        numeros, 
        objetivo, 
        subconjunto_actual + [numeros[indice]],  # Agregar el número actual al subconjunto
        indice + 1,  # Avanzar al siguiente índice
        suma_actual + numeros[indice]  # Actualizar la suma parcial
    )
    
    # Excluir el número actual del subconjunto
    # Solo se explora esta rama si la suma de los números restantes es suficiente para alcanzar el objetivo
    if suma_actual + sum(numeros[indice + 1:]) >= objetivo:  # Corte: si la suma restante es suficiente
        acondicionamiento_corte(
            numeros, 
            objetivo, 
            subconjunto_actual,  # No se agrega el número actual
            indice + 1,  # Avanzar al siguiente índice
            suma_actual  # La suma parcial no cambia
        )

# Ejemplo práctico:
# Lista de números disponibles
numeros = [3, 1, 4, 2, 2]

# Valor objetivo que se desea alcanzar
objetivo = 5

# Llamada al algoritmo
print("Subconjuntos que suman al objetivo:")
acondicionamiento_corte(numeros, objetivo)