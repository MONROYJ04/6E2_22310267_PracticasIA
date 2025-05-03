import numpy as np

# Definimos el entorno como una matriz de recompensas
# Cada celda representa la recompensa por moverse de un estado a otro
# -1 indica que no es posible moverse entre esos estados
recompensas = np.array([
    [-1, -1, -1, -1,  0, -1],
    [-1, -1, -1,  0, -1, 100],
    [-1, -1, -1,  0, -1, -1],
    [-1,  0,  0, -1,  0, -1],
    [ 0, -1, -1,  0, -1, 100],
    [-1,  0, -1, -1,  0, 100]
])

# Inicializamos la tabla Q con ceros
# Esta tabla almacenará los valores Q para cada estado y acción
tabla_q = np.zeros_like(recompensas)

# Definimos los parámetros del algoritmo
tasa_aprendizaje = 0.8  # Qué tan rápido aprende el agente
factor_descuento = 0.9  # Qué tanto valora el agente las recompensas futuras
episodios = 1000        # Número de iteraciones para entrenar al agente

# Función para elegir una acción aleatoria válida desde un estado dado
def elegir_accion(estado_actual):
    acciones_validas = np.where(recompensas[estado_actual] >= 0)[0]
    return np.random.choice(acciones_validas)

# Entrenamiento del agente
for episodio in range(episodios):
    # Elegimos un estado inicial aleatorio
    estado_actual = np.random.randint(0, recompensas.shape[0])
    
    # Mientras el estado actual no sea el objetivo
    while estado_actual != 5:  # El estado 5 es el objetivo
        # Elegimos una acción válida desde el estado actual
        accion = elegir_accion(estado_actual)
        
        # Calculamos el valor Q utilizando la fórmula de Q-Learning
        recompensa = recompensas[estado_actual, accion]
        valor_q_maximo = np.max(tabla_q[accion])  # Mejor valor Q del siguiente estado
        tabla_q[estado_actual, accion] += tasa_aprendizaje * (
            recompensa + factor_descuento * valor_q_maximo - tabla_q[estado_actual, accion]
        )
        
        # Actualizamos el estado actual
        estado_actual = accion

# Normalizamos la tabla Q para facilitar la interpretación
tabla_q_normalizada = tabla_q / np.max(tabla_q) * 100

# Mostramos la tabla Q resultante
print("Tabla Q (normalizada):")
print(tabla_q_normalizada)

# Ejemplo práctico: Encontrar el camino óptimo desde un estado inicial al objetivo
def encontrar_camino_optimo(estado_inicial):
    estado_actual = estado_inicial
    camino = [estado_actual]
    
    while estado_actual != 5:  # El estado 5 es el objetivo
        # Elegimos la acción con el mayor valor Q
        accion = np.argmax(tabla_q[estado_actual])
        camino.append(accion)
        estado_actual = accion
    
    return camino

# Probamos el camino óptimo desde el estado 0
estado_inicial = 0
camino_optimo = encontrar_camino_optimo(estado_inicial)
print(f"Camino óptimo desde el estado {estado_inicial}: {camino_optimo}")