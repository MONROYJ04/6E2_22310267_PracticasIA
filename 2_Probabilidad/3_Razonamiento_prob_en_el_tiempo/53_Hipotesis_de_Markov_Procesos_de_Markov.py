# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: PROCESOS DE MARKOV PARA SIMULACIÓN DE CLIMA
# ------------------------------------------------------------------------------------
# Este código implementa un modelo de Procesos de Markov para simular el clima diario.
# Un Proceso de Markov es un sistema que cambia de estado en función de probabilidades
# y cumple con la Hipótesis de Markov: el estado futuro depende únicamente del estado actual,
# no de los estados pasados.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos la librería `random` para realizar selecciones aleatorias basadas en probabilidades.
# - Esto es esencial para simular las transiciones entre estados.
import random

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LOS ESTADOS POSIBLES
# ------------------------------------------------------------------------------------
# - Creamos una lista llamada `estados` que contiene los posibles estados del sistema.
# - En este caso, los estados representan el clima: Soleado, Nublado y Lluvioso.
# - Esto es importante porque los Procesos de Markov trabajan con un conjunto finito de estados.
estados = ["Soleado", "Nublado", "Lluvioso"]

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR LA MATRIZ DE TRANSICIÓN
# ------------------------------------------------------------------------------------
# - La matriz de transición define las probabilidades de pasar de un estado actual a otro estado futuro.
# - Cada fila representa un estado actual, y cada columna representa un estado futuro.
# - Por ejemplo, si hoy está "Soleado", hay un 60% de probabilidad de que mañana también esté "Soleado".
matriz_transicion = [
    [0.6, 0.3, 0.1],  # Probabilidades desde el estado "Soleado"
    [0.2, 0.5, 0.3],  # Probabilidades desde el estado "Nublado"
    [0.1, 0.4, 0.5]   # Probabilidades desde el estado "Lluvioso"
]

# ------------------------------------------------------------------------------------
# PASO 4: FUNCIÓN PARA CALCULAR EL SIGUIENTE ESTADO
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada el estado actual del sistema.
# - Usa la matriz de transición para determinar probabilísticamente el siguiente estado.
# - Utiliza `random.choices` para seleccionar el siguiente estado basado en las probabilidades.
def siguiente_estado(estado_actual):
    """
    Calcula el siguiente estado del sistema basado en el estado actual
    y las probabilidades de la matriz de transición.
    """
    # Obtenemos el índice del estado actual
    indice_estado_actual = estados.index(estado_actual)
    
    # Obtenemos las probabilidades de transición desde el estado actual
    probabilidades = matriz_transicion[indice_estado_actual]
    
    # Elegimos el siguiente estado basado en las probabilidades
    siguiente = random.choices(estados, weights=probabilidades, k=1)[0]
    return siguiente

# ------------------------------------------------------------------------------------
# PASO 5: FUNCIÓN PARA SIMULAR UNA SECUENCIA DE ESTADOS
# ------------------------------------------------------------------------------------
# - Esta función genera una secuencia de estados simulando un Proceso de Markov.
# - Toma como entrada el estado inicial y el número de pasos a simular.
# - Devuelve una lista con la secuencia de estados generados.
def simular_proceso_markov(estado_inicial, pasos):
    """
    Simula una secuencia de estados de un Proceso de Markov.
    
    :param estado_inicial: El estado inicial del sistema.
    :param pasos: Número de pasos a simular.
    :return: Lista con la secuencia de estados.
    """
    # Inicializamos la secuencia con el estado inicial
    secuencia = [estado_inicial]
    
    # Iteramos para generar los estados siguientes
    estado_actual = estado_inicial
    for _ in range(pasos):
        estado_actual = siguiente_estado(estado_actual)
        secuencia.append(estado_actual)
    
    return secuencia

# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Simularemos el clima durante 10 días, comenzando con un día soleado.
# - Esto nos permitirá observar cómo evoluciona el clima según las probabilidades definidas.
estado_inicial = "Soleado"  # Estado inicial del sistema
dias_a_simular = 10         # Número de días a simular

# Ejecutamos la simulación
secuencia_clima = simular_proceso_markov(estado_inicial, dias_a_simular)

# Mostramos los resultados
print("Simulación del clima durante 10 días:")
for dia, estado in enumerate(secuencia_clima):
    print(f"Día {dia + 1}: {estado}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una matriz de transición para modelar las probabilidades de cambio entre estados.
# 2. La Hipótesis de Markov establece que el estado futuro depende únicamente del estado actual, no de los estados pasados.
# 3. Ventajas:
#    - Es simple y eficiente para modelar sistemas con transiciones probabilísticas.
#    - Útil en aplicaciones como predicción del clima, cadenas de suministro, y más.
# 4. Limitaciones:
#    - No considera dependencias más complejas (por ejemplo, estados pasados más lejanos).
#    - Requiere que las probabilidades de transición sean conocidas de antemano.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: SIMULACIÓN DEL CLIMA
# ------------------------------------------------------------------------------------
# - Comenzamos con un día soleado.
# - Usamos la matriz de transición para determinar probabilísticamente el clima de los días siguientes.
# - Cada día, el clima depende únicamente del clima del día anterior.
# Resultado esperado: Una secuencia de estados como ["Soleado", "Nublado", "Lluvioso", ...].