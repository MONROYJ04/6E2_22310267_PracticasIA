# Importamos las bibliotecas necesarias
import numpy as np

# Definimos la funcion de Iteracion de Politicas
def iteracion_de_politicas(recompensas, matriz_transicion, gamma, iteraciones_max):
    """
    Algoritmo de Iteracion de Politicas para resolver problemas de decision en procesos de decision de Markov (MDP).
    
    Parametros:
    - recompensas: Vector que contiene las recompensas inmediatas para cada estado.
    - matriz_transicion: Matriz que define las probabilidades de transicion entre estados para cada accion.
    - gamma: Factor de descuento que determina la importancia de las recompensas futuras (0 <= gamma <= 1).
    - iteraciones_max: Numero maximo de iteraciones para evitar bucles infinitos.

    Retorna:
    - politica_optima: Politica que maximiza la recompensa esperada.
    - valores: Valores optimos para cada estado.
    """
    # Inicializamos la politica de manera aleatoria (una accion por estado)
    num_estados, num_acciones = matriz_transicion.shape[:2]
    politica = np.zeros(num_estados, dtype=int)  # Politica inicial (accion 0 para todos los estados)
    
    # Inicializamos los valores de los estados en cero
    valores = np.zeros(num_estados)

    # Iteramos hasta que la politica sea estable
    for _ in range(iteraciones_max):
        # Paso 1: Evaluacion de la politica
        while True:
            nuevos_valores = np.zeros(num_estados)
            for estado in range(num_estados):
                accion = politica[estado]
                nuevos_valores[estado] = sum(
                    matriz_transicion[estado, accion, siguiente_estado] *
                    (recompensas[siguiente_estado] + gamma * valores[siguiente_estado])
                    for siguiente_estado in range(num_estados)
                )
            # Verificamos si los valores han convergido
            if np.allclose(valores, nuevos_valores, atol=1e-6):
                break
            valores = nuevos_valores

        # Paso 2: Mejoramiento de la politica
        politica_estable = True
        for estado in range(num_estados):
            # Calculamos el valor esperado para cada accion
            valores_acciones = np.zeros(num_acciones)
            for accion in range(num_acciones):
                valores_acciones[accion] = sum(
                    matriz_transicion[estado, accion, siguiente_estado] *
                    (recompensas[siguiente_estado] + gamma * valores[siguiente_estado])
                    for siguiente_estado in range(num_estados)
                )
            # Elegimos la mejor accion
            mejor_accion = np.argmax(valores_acciones)
            if mejor_accion != politica[estado]:
                politica_estable = False
            politica[estado] = mejor_accion

        # Si la politica es estable, terminamos
        if politica_estable:
            break

    return politica, valores


# Ejemplo practico
if __name__ == "__main__":
    # Definimos un problema simple con 3 estados y 2 acciones
    # Estados: 0, 1, 2
    # Acciones: 0 (izquierda), 1 (derecha)
    recompensas = np.array([0, 0, 1])  # Recompensa de llegar al estado 2
    matriz_transicion = np.array([
        # Estado 0
        [[1.0, 0.0, 0.0],  # Accion 0: quedarse en el estado 0
         [0.0, 1.0, 0.0]], # Accion 1: moverse al estado 1
        # Estado 1
        [[1.0, 0.0, 0.0],  # Accion 0: regresar al estado 0
         [0.0, 0.0, 1.0]], # Accion 1: moverse al estado 2
        # Estado 2
        [[0.0, 0.0, 1.0],  # Accion 0: quedarse en el estado 2
         [0.0, 0.0, 1.0]]  # Accion 1: quedarse en el estado 2
    ])
    gamma = 0.9  # Factor de descuento
    iteraciones_max = 1000  # Maximo de iteraciones

    # Ejecutamos el algoritmo
    politica_optima, valores_optimos = iteracion_de_politicas(recompensas, matriz_transicion, gamma, iteraciones_max)

    # Mostramos los resultados
    print("Politica optima:", politica_optima)
    print("Valores optimos:", valores_optimos)