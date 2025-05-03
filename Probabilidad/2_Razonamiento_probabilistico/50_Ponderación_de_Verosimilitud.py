# Este archivo implementa un algoritmo de Ponderación de Verosimilitud.
# La Ponderación de Verosimilitud se utiliza para medir qué tan probable es un evento
# en comparación con su opuesto, dado un conjunto de datos.

# Importamos la biblioteca math para realizar cálculos matemáticos como logaritmos.
import math

# Definimos una función para calcular la ponderación de verosimilitud.
def ponderacion_verosimilitud(prob_evento, prob_no_evento):
    """
    Calcula la ponderación de verosimilitud.

    :param prob_evento: Probabilidad de que ocurra el evento dado un conjunto de datos.
    :param prob_no_evento: Probabilidad de que no ocurra el evento dado un conjunto de datos.
    :return: Ponderación de verosimilitud.
    """
    # Validamos que las probabilidades estén en el rango correcto (entre 0 y 1).
    # Esto asegura que los valores ingresados sean válidos en términos probabilísticos.
    if not (0 < prob_evento <= 1) or not (0 < prob_no_evento <= 1):
        raise ValueError("Las probabilidades deben estar entre 0 y 1.")

    # Calculamos la ponderación de verosimilitud.
    # Esto se hace dividiendo la probabilidad del evento entre la probabilidad del no evento
    # y luego aplicando el logaritmo natural para obtener una medida más interpretable.
    verosimilitud = math.log(prob_evento / prob_no_evento)
    
    # Retornamos el resultado de la ponderación de verosimilitud.
    return verosimilitud

# Ejemplo práctico:
# Supongamos que estamos analizando un diagnóstico médico.
# Probabilidad de que un paciente tenga una enfermedad dado un síntoma específico.
prob_enfermedad = 0.8  # 80%
# Probabilidad de que un paciente no tenga la enfermedad dado el mismo síntoma.
prob_no_enfermedad = 0.2  # 20%

# Calculamos la ponderación de verosimilitud para este caso.
# Esto nos permitirá determinar qué tan probable es que el paciente tenga la enfermedad
# en comparación con que no la tenga.
resultado = ponderacion_verosimilitud(prob_enfermedad, prob_no_enfermedad)

# Mostramos el resultado con una explicación.
print("Ejemplo práctico:")
print(f"Probabilidad de enfermedad: {prob_enfermedad}")
print(f"Probabilidad de no enfermedad: {prob_no_enfermedad}")
print(f"Ponderación de verosimilitud: {resultado:.2f}")

# Explicación del resultado:
# Si el resultado es positivo, indica que el evento (tener la enfermedad) es más probable.
# Si el resultado es negativo, indica que el evento (no tener la enfermedad) es más probable.
# Si el resultado es cercano a 0, indica que ambos eventos son igualmente probables.