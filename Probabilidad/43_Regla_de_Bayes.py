# Este programa implementa la Regla de Bayes, una fórmula matemática que permite calcular la probabilidad
# de que ocurra un evento A dado que ya ocurrió un evento B. 
# La fórmula es: P(A|B) = [P(B|A) * P(A)] / P(B)

# Definimos una función para calcular la probabilidad usando la Regla de Bayes
def regla_de_bayes(prob_a, prob_b_dado_a, prob_b):
    """
    Calcula la probabilidad de A dado B usando la Regla de Bayes.
    
    :param prob_a: Probabilidad de que ocurra el evento A (P(A))
    :param prob_b_dado_a: Probabilidad de que ocurra el evento B dado que ocurrió A (P(B|A))
    :param prob_b: Probabilidad de que ocurra el evento B (P(B))
    :return: Probabilidad de que ocurra el evento A dado que ocurrió B (P(A|B))
    """
    # Aplicamos la fórmula de la Regla de Bayes
    prob_a_dado_b = (prob_b_dado_a * prob_a) / prob_b
    return prob_a_dado_b

# Ejemplo práctico:
# Supongamos que estamos analizando una enfermedad rara:
# - La probabilidad de que una persona tenga la enfermedad (A) es del 1% (0.01).
# - Si una persona tiene la enfermedad, la probabilidad de que el test sea positivo (B|A) es del 99% (0.99).
# - La probabilidad de que el test sea positivo en general (B) es del 5% (0.05).

# Definimos las probabilidades conocidas
prob_enfermedad = 0.01  # P(A): Probabilidad de tener la enfermedad
prob_test_positivo_dado_enfermedad = 0.99  # P(B|A): Probabilidad de test positivo si tiene la enfermedad
prob_test_positivo = 0.05  # P(B): Probabilidad de test positivo en general

# Calculamos la probabilidad de tener la enfermedad dado que el test es positivo (P(A|B))
prob_enfermedad_dado_test_positivo = regla_de_bayes(
    prob_enfermedad,
    prob_test_positivo_dado_enfermedad,
    prob_test_positivo
)

# Mostramos el resultado con un mensaje explicativo
print("La probabilidad de tener la enfermedad dado que el test es positivo es:")
print(f"{prob_enfermedad_dado_test_positivo:.2%}")  # Mostramos el resultado en porcentaje