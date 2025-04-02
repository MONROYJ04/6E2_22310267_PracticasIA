import random

def genetic_algorithm(population, fitness_func, gene_pool, generations=100):
    """
    :param population: Lista de individuos (soluciones iniciales).
    :param fitness_func: Función que evalúa la calidad de un individuo.
    :param gene_pool: Genes posibles para mutación.
    :param generations: Número de iteraciones.
    :return: Mejor individuo encontrado.
    """
    for _ in range(generations):
        # Selección (torneo)
        parents = [tournament_selection(population, fitness_func) for _ in range(2)]
        
        # Cruza (reproducción)
        offspring = crossover(parents[0], parents[1])
        
        # Mutación
        offspring = mutate(offspring, gene_pool)
        
        # Reemplazo (elitismo)
        population = sorted(population, key=fitness_func, reverse=True)[:-1] + [offspring]
    
    return max(population, key=fitness_func)

def tournament_selection(population, fitness_func, k=3):
    """Selecciona el mejor de k individuos aleatorios."""
    selected = random.sample(population, k)
    return max(selected, key=fitness_func)

def crossover(parent1, parent2):
    """Cruza dos padres para generar un hijo (punto de corte aleatorio)."""
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual, gene_pool, mutation_rate=0.1):
    """Muta un gen aleatorio con probabilidad mutation_rate."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(gene_pool)
    return individual

# Ejemplo: Optimizar una cadena binaria para que tenga más '1's.
population = [[random.randint(0, 1) for _ in range(10)] for _ in range(20)]
fitness_func = lambda ind: sum(ind)  # Función de aptitud: contar '1's
gene_pool = [0, 1]

best_solution = genetic_algorithm(population, fitness_func, gene_pool)
print(f"Mejor solución: {best_solution}, Fitness: {sum(best_solution)}")