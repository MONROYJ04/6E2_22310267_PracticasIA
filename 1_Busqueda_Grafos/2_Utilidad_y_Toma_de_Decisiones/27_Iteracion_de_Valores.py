# Algoritmo de Iteracion de Valores
# Este algoritmo se utiliza para resolver problemas de decision en los que un agente debe maximizar su recompensa
# a lo largo del tiempo. Se basa en actualizar iterativamente los valores de los estados hasta que converjan.

# Definimos las variables principales
# estados: Lista de todos los estados posibles en el entorno
# acciones: Lista de todas las acciones posibles que el agente puede tomar
# transiciones: Diccionario que define la probabilidad de moverse de un estado a otro dado una accion
# recompensas: Diccionario que define la recompensa inmediata por estar en un estado o realizar una accion
# gamma: Factor de descuento que determina la importancia de las recompensas futuras
# epsilon: Umbral para determinar la convergencia del algoritmo

# Importamos la libreria math para trabajar con valores maximos
import math

def iteracion_de_valores(estados, acciones, transiciones, recompensas, gamma, epsilon):
    """
    Funcion que implementa el algoritmo de Iteracion de Valores.

    Parametros:
    estados (list): Lista de estados posibles.
    acciones (list): Lista de acciones posibles.
    transiciones (dict): Probabilidades de transicion entre estados.
    recompensas (dict): Recompensas inmediatas para cada estado o accion.
    gamma (float): Factor de descuento para recompensas futuras.
    epsilon (float): Umbral para determinar la convergencia.

    Retorna:
    valores (dict): Valores optimos para cada estado.
    politica (dict): Politica optima para cada estado.
    """
    # Inicializamos los valores de todos los estados en 0
    valores = {estado: 0 for estado in estados}
    politica = {estado: None for estado in estados}

    while True:
        # Copiamos los valores actuales para compararlos despues
        nuevos_valores = valores.copy()
        delta = 0  # Variable para medir el cambio maximo entre iteraciones

        # Iteramos sobre cada estado
        for estado in estados:
            max_valor = -math.inf  # Inicializamos el valor maximo como negativo infinito
            mejor_accion = None  # Inicializamos la mejor accion como None

            # Iteramos sobre cada accion posible
            for accion in acciones:
                # Calculamos el valor esperado para esta accion
                valor_accion = sum(
                    transiciones[(estado, accion, siguiente_estado)] * 
                    (recompensas[(estado, accion, siguiente_estado)] + gamma * valores[siguiente_estado])
                    for siguiente_estado in estados
                )

                # Actualizamos el valor maximo y la mejor accion si es necesario
                if valor_accion > max_valor:
                    max_valor = valor_accion
                    mejor_accion = accion

            # Actualizamos el valor del estado con el valor maximo encontrado
            nuevos_valores[estado] = max_valor
            politica[estado] = mejor_accion

            # Calculamos el cambio maximo (delta) entre los valores antiguos y nuevos
            delta = max(delta, abs(valores[estado] - nuevos_valores[estado]))

        # Actualizamos los valores para la siguiente iteracion
        valores = nuevos_valores

        # Si el cambio maximo es menor que el umbral, terminamos
        if delta < epsilon:
            break

    return valores, politica

# Ejemplo practico
# Supongamos un entorno simple con 3 estados y 2 acciones
estados = ["A", "B", "C"]
acciones = ["ir_a", "quedarse"]
transiciones = {
    ("A", "ir_a", "B"): 1.0,
    ("A", "quedarse", "A"): 1.0,
    ("B", "ir_a", "C"): 1.0,
    ("B", "quedarse", "B"): 1.0,
    ("C", "ir_a", "C"): 1.0,
    ("C", "quedarse", "C"): 1.0,
}
recompensas = {
    ("A", "ir_a", "B"): 10,
    ("A", "quedarse", "A"): 0,
    ("B", "ir_a", "C"): 50,
    ("B", "quedarse", "B"): 0,
    ("C", "ir_a", "C"): 0,
    ("C", "quedarse", "C"): 0,
}
gamma = 0.9  # Factor de descuento
epsilon = 0.01  # Umbral de convergencia

# Llamamos a la funcion para calcular los valores y la politica optima
valores_optimos, politica_optima = iteracion_de_valores(estados, acciones, transiciones, recompensas, gamma, epsilon)

# Mostramos los resultados
print("Valores optimos:", valores_optimos)
print("Politica optima:", politica_optima)