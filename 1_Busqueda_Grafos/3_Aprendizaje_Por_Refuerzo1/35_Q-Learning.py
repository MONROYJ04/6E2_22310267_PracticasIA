import numpy as np

# Q-Learning es un algoritmo de aprendizaje por refuerzo que permite a un agente aprender
# a tomar decisiones en un entorno, maximizando una recompensa acumulada.

# Definimos los parametros del algoritmo
tasa_aprendizaje = 0.8  # Cuanto se actualiza el valor Q (entre 0 y 1)
factor_descuento = 0.95  # Cuanto se valora el futuro frente al presente (entre 0 y 1)
episodios = 1000  # Numero de episodios para entrenar al agente

# Definimos el entorno como una matriz de recompensas
# En este caso, es un grafo donde cada nodo tiene conexiones con otros nodos
# y las recompensas indican el beneficio de moverse entre nodos.
recompensas = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100]
])

# Inicializamos la tabla Q con ceros
# Esta tabla almacenara los valores Q para cada estado-accion
tabla_q = np.zeros_like(recompensas)

# Funcion para elegir una accion basada en el estado actual
# Usamos una estrategia de exploracion-explotacion
def elegir_accion(estado_actual):
    # Seleccionamos una accion aleatoria entre las posibles
    acciones_posibles = np.where(recompensas[estado_actual] >= 0)[0]
    return np.random.choice(acciones_posibles)

# Funcion para entrenar al agente usando Q-Learning
def entrenar_agente():
    for episodio in range(episodios):
        # Elegimos un estado inicial aleatorio
        estado_actual = np.random.randint(0, len(recompensas))
        
        # Continuamos hasta que el agente alcance un estado terminal
        while True:
            # Elegimos una accion
            accion = elegir_accion(estado_actual)
            
            # Obtenemos la recompensa inmediata y el siguiente estado
            recompensa = recompensas[estado_actual, accion]
            siguiente_estado = accion
            
            # Actualizamos el valor Q usando la formula de Q-Learning
            valor_q_actual = tabla_q[estado_actual, accion]
            maximo_q_siguiente = np.max(tabla_q[siguiente_estado])
            tabla_q[estado_actual, accion] = valor_q_actual + tasa_aprendizaje * (
                recompensa + factor_descuento * maximo_q_siguiente - valor_q_actual
            )
            
            # Si alcanzamos un estado terminal, terminamos el episodio
            if recompensa == 100:
                break
            
            # Actualizamos el estado actual
            estado_actual = siguiente_estado

# Funcion para encontrar el camino optimo desde un estado inicial
def encontrar_camino_optimo(estado_inicial):
    estado_actual = estado_inicial
    camino = [estado_actual]
    
    while True:
        # Elegimos la accion con el mayor valor Q
        accion = np.argmax(tabla_q[estado_actual])
        camino.append(accion)
        
        # Si alcanzamos el estado terminal, terminamos
        if recompensas[estado_actual, accion] == 100:
            break
        
        estado_actual = accion
    
    return camino

# Entrenamos al agente
entrenar_agente()

# Ejemplo practico: Encontrar el camino optimo desde el estado 0
estado_inicial = 0
camino_optimo = encontrar_camino_optimo(estado_inicial)

# Mostramos los resultados
print("Tabla Q entrenada:")
print(tabla_q)
print(f"Camino optimo desde el estado {estado_inicial}: {camino_optimo}")