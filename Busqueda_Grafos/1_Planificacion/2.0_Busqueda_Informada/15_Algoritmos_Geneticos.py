import random

def algoritmo_genetico(poblacion, funcion_aptitud, conjunto_genes, generaciones=100):
    """
    Implementación de un algoritmo genético para optimizar soluciones.
    
    :param poblacion: Lista de individuos (soluciones iniciales).
    :param funcion_aptitud: Función que evalúa la calidad de un individuo.
    :param conjunto_genes: Genes posibles para mutación.
    :param generaciones: Número de iteraciones del algoritmo.
    :return: Mejor individuo encontrado.
    """
    for _ in range(generaciones):
        # Selección: Elegir dos padres mediante torneo
        padres = [seleccion_torneo(poblacion, funcion_aptitud) for _ in range(2)]
        
        # Cruza: Crear un hijo combinando los genes de los padres
        hijo = cruza(padres[0], padres[1])
        
        # Mutación: Alterar aleatoriamente los genes del hijo
        hijo = mutacion(hijo, conjunto_genes)
        
        # Reemplazo: Sustituir al peor individuo de la población con el nuevo hijo
        poblacion = sorted(poblacion, key=funcion_aptitud, reverse=True)[:-1] + [hijo]
    
    # Retornar el mejor individuo encontrado
    return max(poblacion, key=funcion_aptitud)

def seleccion_torneo(poblacion, funcion_aptitud, k=3):
    """
    Selecciona el mejor individuo de un grupo aleatorio de la población.
    
    :param poblacion: Lista de individuos.
    :param funcion_aptitud: Función que evalúa la calidad de un individuo.
    :param k: Tamaño del grupo aleatorio.
    :return: El mejor individuo del grupo.
    """
    seleccionados = random.sample(poblacion, k)
    return max(seleccionados, key=funcion_aptitud)

def cruza(padre1, padre2):
    """
    Combina los genes de dos padres para crear un hijo.
    
    :param padre1: Primer padre.
    :param padre2: Segundo padre.
    :return: Nuevo individuo (hijo).
    """
    # Elegir un punto de corte aleatorio
    punto_corte = random.randint(1, len(padre1) - 1)
    # Combinar genes de ambos padres
    return padre1[:punto_corte] + padre2[punto_corte:]

def mutacion(individuo, conjunto_genes, tasa_mutacion=0.1):
    """
    Modifica aleatoriamente los genes de un individuo con cierta probabilidad.
    
    :param individuo: Individuo a mutar.
    :param conjunto_genes: Genes posibles para la mutación.
    :param tasa_mutacion: Probabilidad de mutar cada gen.
    :return: Individuo mutado.
    """
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            # Cambiar el gen actual por uno aleatorio del conjunto de genes
            individuo[i] = random.choice(conjunto_genes)
    return individuo

# Ejemplo práctico: Optimizar una cadena binaria para maximizar la cantidad de '1's.
# Población inicial: Lista de cadenas binarias aleatorias
poblacion = [[random.randint(0, 1) for _ in range(10)] for _ in range(20)]

# Función de aptitud: Contar la cantidad de '1's en un individuo
funcion_aptitud = lambda individuo: sum(individuo)

# Conjunto de genes posibles: 0 y 1
conjunto_genes = [0, 1]

# Ejecutar el algoritmo genético
mejor_solucion = algoritmo_genetico(poblacion, funcion_aptitud, conjunto_genes)

# Imprimir la mejor solución encontrada y su aptitud
print(f"Mejor solución: {mejor_solucion}, Aptitud: {sum(mejor_solucion)}")