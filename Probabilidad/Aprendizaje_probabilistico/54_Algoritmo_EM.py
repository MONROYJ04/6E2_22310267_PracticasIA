import numpy as np

# Algoritmo de Expectation-Maximization (EM)
# Este algoritmo se utiliza para estimar los parámetros de un modelo estadístico
# cuando algunos datos están incompletos o son desconocidos.

# Paso 1: Inicializar los parámetros del modelo
# En este caso, asumimos que estamos trabajando con una mezcla de dos distribuciones gaussianas.
def inicializar_parametros():
    # Inicializamos las medias, varianzas y pesos de las dos gaussianas
    media1 = 0.0  # Media de la primera gaussiana
    media2 = 1.0  # Media de la segunda gaussiana
    varianza1 = 1.0  # Varianza de la primera gaussiana
    varianza2 = 1.0  # Varianza de la segunda gaussiana
    peso1 = 0.5  # Peso de la primera gaussiana
    peso2 = 0.5  # Peso de la segunda gaussiana
    return media1, media2, varianza1, varianza2, peso1, peso2

# Paso 2: Función de densidad de probabilidad de una gaussiana
def densidad_gaussiana(x, media, varianza):
    # Calcula la probabilidad de x dado una distribución gaussiana con media y varianza dadas
    return (1 / np.sqrt(2 * np.pi * varianza)) * np.exp(-0.5 * ((x - media) ** 2) / varianza)

# Paso 3: Paso de Expectación (E-step)
def paso_expectacion(datos, media1, media2, varianza1, varianza2, peso1, peso2):
    # Calcula las responsabilidades (probabilidades) de cada punto de datos para cada gaussiana
    responsabilidad1 = peso1 * densidad_gaussiana(datos, media1, varianza1)
    responsabilidad2 = peso2 * densidad_gaussiana(datos, media2, varianza2)
    suma_responsabilidades = responsabilidad1 + responsabilidad2
    gamma1 = responsabilidad1 / suma_responsabilidades  # Probabilidad de pertenecer a la primera gaussiana
    gamma2 = responsabilidad2 / suma_responsabilidades  # Probabilidad de pertenecer a la segunda gaussiana
    return gamma1, gamma2

# Paso 4: Paso de Maximización (M-step)
def paso_maximizacion(datos, gamma1, gamma2):
    # Actualiza los parámetros del modelo basándose en las responsabilidades calculadas
    peso1 = np.mean(gamma1)  # Nuevo peso de la primera gaussiana
    peso2 = np.mean(gamma2)  # Nuevo peso de la segunda gaussiana
    media1 = np.sum(gamma1 * datos) / np.sum(gamma1)  # Nueva media de la primera gaussiana
    media2 = np.sum(gamma2 * datos) / np.sum(gamma2)  # Nueva media de la segunda gaussiana
    varianza1 = np.sum(gamma1 * (datos - media1) ** 2) / np.sum(gamma1)  # Nueva varianza de la primera gaussiana
    varianza2 = np.sum(gamma2 * (datos - media2) ** 2) / np.sum(gamma2)  # Nueva varianza de la segunda gaussiana
    return media1, media2, varianza1, varianza2, peso1, peso2

# Paso 5: Algoritmo EM completo
def algoritmo_em(datos, iteraciones):
    # Inicializa los parámetros
    media1, media2, varianza1, varianza2, peso1, peso2 = inicializar_parametros()
    
    # Itera entre los pasos de Expectación y Maximización
    for i in range(iteraciones):
        # Paso de Expectación
        gamma1, gamma2 = paso_expectacion(datos, media1, media2, varianza1, varianza2, peso1, peso2)
        
        # Paso de Maximización
        media1, media2, varianza1, varianza2, peso1, peso2 = paso_maximizacion(datos, gamma1, gamma2)
        
        # Imprime los parámetros en cada iteración para observar la convergencia
        print(f"Iteracion {i + 1}:")
        print(f"Media1: {media1}, Media2: {media2}")
        print(f"Varianza1: {varianza1}, Varianza2: {varianza2}")
        print(f"Peso1: {peso1}, Peso2: {peso2}")
        print("-" * 30)
    
    return media1, media2, varianza1, varianza2, peso1, peso2

# Ejemplo práctico
if __name__ == "__main__":
    # Generamos datos simulados a partir de una mezcla de dos gaussianas
    np.random.seed(42)  # Fijamos la semilla para reproducibilidad
    datos_gaussiana1 = np.random.normal(0, 1, 100)  # 100 puntos con media 0 y varianza 1
    datos_gaussiana2 = np.random.normal(5, 1, 100)  # 100 puntos con media 5 y varianza 1
    datos = np.concatenate([datos_gaussiana1, datos_gaussiana2])  # Mezclamos los datos
    
    # Ejecutamos el algoritmo EM en los datos simulados
    iteraciones = 10  # Número de iteraciones del algoritmo
    algoritmo_em(datos, iteraciones)