import random

# Este algoritmo implementa el dilema de exploración vs. explotación.
# Exploración: Probar nuevas opciones para descubrir su valor.
# Explotación: Elegir la mejor opción conocida hasta ahora.

# Definimos una función que simula el dilema de exploración vs. explotación
def exploracion_vs_explotacion(prob_explorar, recompensas):
    """
    Simula el dilema de exploración vs. explotación.

    Args:
        prob_explorar (float): Probabilidad de explorar (valor entre 0 y 1).
        recompensas (list): Lista de recompensas asociadas a cada acción.

    Returns:
        int: Índice de la acción seleccionada.
    """
    # Generamos un número aleatorio entre 0 y 1
    numero_aleatorio = random.random()

    # Si el número aleatorio es menor que la probabilidad de explorar, exploramos
    if numero_aleatorio < prob_explorar:
        # Exploración: Elegimos una acción al azar
        accion_seleccionada = random.randint(0, len(recompensas) - 1)
        print("Explorando: Se eligió una acción al azar.")
    else:
        # Explotación: Elegimos la acción con la mayor recompensa conocida
        accion_seleccionada = recompensas.index(max(recompensas))
        print("Explotando: Se eligió la mejor acción conocida.")

    return accion_seleccionada

# Ejemplo práctico: Simulación de un problema de máquinas tragamonedas
if __name__ == "__main__":
    # Definimos las recompensas conocidas para 3 máquinas tragamonedas
    # (valores arbitrarios que representan la recompensa promedio de cada máquina)
    recompensas_maquinas = [1.5, 2.0, 1.0]

    # Probabilidad de explorar (por ejemplo, 30%)
    probabilidad_explorar = 0.3

    # Simulamos 10 decisiones
    for i in range(10):
        print(f"\nDecisión {i + 1}:")
        accion = exploracion_vs_explotacion(probabilidad_explorar, recompensas_maquinas)
        print(f"Acción seleccionada: Máquina {accion + 1}")