# Este algoritmo calcula la probabilidad condicionada y realiza la normalización de probabilidades.
# La probabilidad condicionada se utiliza para determinar la probabilidad de un evento dado que otro evento ya ocurrió.
# La normalización asegura que las probabilidades sumen 1, lo cual es un requisito en la teoría de probabilidades.

# Definimos una funcion para calcular la probabilidad condicionada
def probabilidad_condicionada(prob_evento_a, prob_evento_b_dado_a):
    """
    Calcula la probabilidad condicionada P(B|A).
    
    :param prob_evento_a: Probabilidad de que ocurra el evento A (P(A)).
    :param prob_evento_b_dado_a: Probabilidad de que ocurra el evento B dado que ocurrió A (P(B|A)).
    :return: Probabilidad conjunta de A y B (P(A y B)).
    """
    # Multiplicamos la probabilidad de A por la probabilidad de B dado A
    return prob_evento_a * prob_evento_b_dado_a

# Definimos una funcion para normalizar un conjunto de probabilidades
def normalizar_probabilidades(probabilidades):
    """
    Normaliza un conjunto de probabilidades para que sumen 1.
    
    :param probabilidades: Lista de probabilidades.
    :return: Lista de probabilidades normalizadas.
    """
    # Calculamos la suma total de las probabilidades
    suma_total = sum(probabilidades)
    # Dividimos cada probabilidad entre la suma total para normalizar
    return [p / suma_total for p in probabilidades]

# Ejemplo practico:
# Supongamos que tenemos dos eventos:
# Evento A: Una persona estudia para un examen.
# Evento B: La persona aprueba el examen.
# Queremos calcular la probabilidad de que la persona apruebe el examen dado que estudió.

# Probabilidad de que la persona estudie (P(A))
prob_estudiar = 0.6

# Probabilidad de que la persona apruebe dado que estudió (P(B|A))
prob_aprobar_dado_estudiar = 0.8

# Calculamos la probabilidad conjunta de que la persona estudie y apruebe (P(A y B))
prob_conjunta = probabilidad_condicionada(prob_estudiar, prob_aprobar_dado_estudiar)

# Ahora supongamos que tenemos un conjunto de probabilidades sin normalizar:
# Probabilidad de aprobar sin estudiar: 0.1
# Probabilidad de aprobar estudiando: 0.48 (calculada previamente como P(A y B))
# Probabilidad de no aprobar: 0.42
probabilidades_sin_normalizar = [0.1, prob_conjunta, 0.42]

# Normalizamos estas probabilidades
probabilidades_normalizadas = normalizar_probabilidades(probabilidades_sin_normalizar)

# Mostramos los resultados
print("Probabilidad conjunta (P(A y B)): ", prob_conjunta)
print("Probabilidades sin normalizar: ", probabilidades_sin_normalizar)
print("Probabilidades normalizadas: ", probabilidades_normalizadas)

# Explicacion del resultado:
# - La probabilidad conjunta (P(A y B)) nos dice qué tan probable es que la persona estudie y apruebe.
# - Las probabilidades normalizadas aseguran que la suma de todas las probabilidades sea igual a 1.