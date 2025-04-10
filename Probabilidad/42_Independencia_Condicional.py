# Este algoritmo explica el concepto de independencia condicional en probabilidad.
# La independencia condicional ocurre cuando dos eventos son independientes entre sí,
# dado que se conoce la ocurrencia de un tercer evento.

# Importamos la biblioteca necesaria para manejar datos y realizar cálculos
import pandas as pd

# Funcion para verificar la independencia condicional
def verificar_independencia_condicional(datos, evento_a, evento_b, condicion):
    """
    Verifica si dos eventos (evento_a y evento_b) son independientes condicionalmente
    dado un tercer evento (condicion).

    Parametros:
    - datos: DataFrame que contiene los datos de los eventos.
    - evento_a: Nombre de la columna que representa el primer evento.
    - evento_b: Nombre de la columna que representa el segundo evento.
    - condicion: Nombre de la columna que representa el evento condicional.

    Retorna:
    - True si los eventos son independientes condicionalmente, False en caso contrario.
    """
    # Calculamos la probabilidad conjunta de A y B dado la condicion
    prob_a_b_condicion = datos.groupby([condicion, evento_a, evento_b]).size() / datos.groupby([condicion]).size()

    # Calculamos la probabilidad de A dado la condicion
    prob_a_condicion = datos.groupby([condicion, evento_a]).size() / datos.groupby([condicion]).size()

    # Calculamos la probabilidad de B dado la condicion
    prob_b_condicion = datos.groupby([condicion, evento_b]).size() / datos.groupby([condicion]).size()

    # Verificamos si la probabilidad conjunta es igual al producto de las probabilidades individuales
    independencia = prob_a_b_condicion.reset_index(drop=True).equals(
        (prob_a_condicion * prob_b_condicion).reset_index(drop=True)
    )

    return independencia

# Ejemplo practico
# Creamos un conjunto de datos ficticio para ilustrar el concepto
datos = pd.DataFrame({
    'Evento_A': ['Si', 'Si', 'No', 'No', 'Si', 'No', 'Si', 'No'],
    'Evento_B': ['Si', 'No', 'Si', 'No', 'Si', 'No', 'No', 'Si'],
    'Condicion': ['Alta', 'Alta', 'Alta', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja']
})

# Explicacion del conjunto de datos:
# - Evento_A y Evento_B representan dos eventos que queremos analizar.
# - Condicion representa un evento condicional que afecta a los otros dos eventos.

# Llamamos a la funcion para verificar la independencia condicional
resultado = verificar_independencia_condicional(datos, 'Evento_A', 'Evento_B', 'Condicion')

# Mostramos el resultado
if resultado:
    print("Los eventos A y B son independientes condicionalmente dado la condicion.")
else:
    print("Los eventos A y B NO son independientes condicionalmente dado la condicion.")