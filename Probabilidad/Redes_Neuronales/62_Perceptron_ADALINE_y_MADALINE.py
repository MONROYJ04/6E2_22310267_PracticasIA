# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: PERCEPTRÓN, ADALINE Y MADALINE PARA CLASIFICACIÓN BINARIA
# ------------------------------------------------------------------------------------
# Este código implementa tres algoritmos de aprendizaje supervisado: Perceptrón, ADALINE y MADALINE.
# Su objetivo es ajustar pesos para clasificar datos de entrada en dos categorías (1 o -1).

# ------------------------------------------------------------------------------------
# PASO 1: IMPLEMENTACIÓN DEL PERCEPTRÓN
# ------------------------------------------------------------------------------------
# - El Perceptrón es un modelo de clasificación lineal que ajusta los pesos en función del error.
# - Es importante porque es uno de los algoritmos más básicos en redes neuronales.
# - Parámetros clave:
#   - `tasa_aprendizaje`: Controla la magnitud del ajuste de los pesos.
#   - `epocas`: Número de iteraciones sobre los datos de entrenamiento.

def perceptron(entrenamiento, etiquetas, tasa_aprendizaje, epocas):
    """
    Algoritmo de Perceptrón para clasificación binaria.
    entrenamiento: Matriz de datos de entrada.
    etiquetas: Vector de etiquetas (1 o -1).
    tasa_aprendizaje: Velocidad de ajuste de los pesos.
    epocas: Número de iteraciones.
    """
    # Inicializamos los pesos con ceros
    pesos = np.zeros(entrenamiento.shape[1])
    sesgo = 0  # Sesgo inicializado en 0

    for _ in range(epocas):
        for i in range(len(entrenamiento)):
            # Calculamos la salida del modelo
            salida = np.dot(entrenamiento[i], pesos) + sesgo
            # Actualizamos los pesos si hay error
            if etiquetas[i] * salida <= 0:
                pesos += tasa_aprendizaje * etiquetas[i] * entrenamiento[i]
                sesgo += tasa_aprendizaje * etiquetas[i]
    return pesos, sesgo

# ------------------------------------------------------------------------------------
# PASO 2: IMPLEMENTACIÓN DE ADALINE
# ------------------------------------------------------------------------------------
# - ADALINE (Adaptive Linear Neuron) ajusta los pesos minimizando el error cuadrático.
# - Es importante porque utiliza una función de activación lineal, lo que permite un aprendizaje más estable.
# - Parámetros clave:
#   - `tasa_aprendizaje`: Controla la velocidad de ajuste.
#   - `epocas`: Número de iteraciones para ajustar los pesos.

def adaline(entrenamiento, etiquetas, tasa_aprendizaje, epocas):
    """
    Algoritmo ADALINE (Adaptative Linear Neuron).
    entrenamiento: Matriz de datos de entrada.
    etiquetas: Vector de etiquetas (1 o -1).
    tasa_aprendizaje: Velocidad de ajuste de los pesos.
    epocas: Número de iteraciones.
    """
    pesos = np.zeros(entrenamiento.shape[1])
    sesgo = 0

    for _ in range(epocas):
        for i in range(len(entrenamiento)):
            # Calculamos la salida del modelo
            salida = np.dot(entrenamiento[i], pesos) + sesgo
            # Calculamos el error
            error = etiquetas[i] - salida
            # Ajustamos los pesos y el sesgo
            pesos += tasa_aprendizaje * error * entrenamiento[i]
            sesgo += tasa_aprendizaje * error
    return pesos, sesgo

# ------------------------------------------------------------------------------------
# PASO 3: IMPLEMENTACIÓN DE MADALINE
# ------------------------------------------------------------------------------------
# - MADALINE (Multiple ADALINE) utiliza múltiples unidades ADALINE para resolver problemas más complejos.
# - Es importante porque puede manejar problemas no linealmente separables como XOR.
# - Parámetros clave:
#   - `tasa_aprendizaje`: Controla la magnitud del ajuste.
#   - `epocas`: Número de iteraciones para ajustar los pesos.

def madaline(entrenamiento, etiquetas, tasa_aprendizaje, epocas):
    """
    Algoritmo MADALINE (Multiple ADALINE).
    entrenamiento: Matriz de datos de entrada.
    etiquetas: Vector de etiquetas (1 o -1).
    tasa_aprendizaje: Velocidad de ajuste de los pesos.
    epocas: Número de iteraciones.
    """
    # Inicializamos los pesos para dos ADALINE
    pesos1 = np.zeros(entrenamiento.shape[1])
    pesos2 = np.zeros(entrenamiento.shape[1])
    sesgo1 = 0
    sesgo2 = 0

    for _ in range(epocas):
        for i in range(len(entrenamiento)):
            # Calculamos las salidas de las dos ADALINE
            salida1 = np.dot(entrenamiento[i], pesos1) + sesgo1
            salida2 = np.dot(entrenamiento[i], pesos2) + sesgo2
            # Seleccionamos la salida más cercana a la etiqueta
            if abs(etiquetas[i] - salida1) < abs(etiquetas[i] - salida2):
                error = etiquetas[i] - salida1
                pesos1 += tasa_aprendizaje * error * entrenamiento[i]
                sesgo1 += tasa_aprendizaje * error
            else:
                error = etiquetas[i] - salida2
                pesos2 += tasa_aprendizaje * error * entrenamiento[i]
                sesgo2 += tasa_aprendizaje * error
    return (pesos1, sesgo1), (pesos2, sesgo2)

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este ejemplo utiliza el problema XOR, un caso clásico en redes neuronales.
# - Muestra cómo los algoritmos ajustan los pesos para clasificar los datos.

if __name__ == "__main__":
    # Datos de entrada (XOR)
    entrenamiento = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    etiquetas = np.array([-1, 1, 1, -1])  # Etiquetas para XOR

    # Perceptrón
    print("Perceptrón:")
    pesos, sesgo = perceptron(entrenamiento, etiquetas, tasa_aprendizaje=0.1, epocas=10)
    print(f"Pesos: {pesos}, Sesgo: {sesgo}")

    # ADALINE
    print("\nADALINE:")
    pesos, sesgo = adaline(entrenamiento, etiquetas, tasa_aprendizaje=0.1, epocas=10)
    print(f"Pesos: {pesos}, Sesgo: {sesgo}")

    # MADALINE
    print("\nMADALINE:")
    (pesos1, sesgo1), (pesos2, sesgo2) = madaline(entrenamiento, etiquetas, tasa_aprendizaje=0.1, epocas=10)
    print(f"Pesos1: {pesos1}, Sesgo1: {sesgo1}")
    print(f"Pesos2: {pesos2}, Sesgo2: {sesgo2}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Perceptrón: Ajusta los pesos en función del error de clasificación. Es simple pero no puede resolver problemas no linealmente separables.
# 2. ADALINE: Minimiza el error cuadrático, lo que lo hace más estable que el Perceptrón.
# 3. MADALINE: Usa múltiples unidades ADALINE para manejar problemas más complejos como XOR.
# Ventajas:
# - Perceptrón: Rápido y simple.
# - ADALINE: Mejor estabilidad.
# - MADALINE: Capacidad para problemas no lineales.
# Limitaciones:
# - Perceptrón y ADALINE no resuelven problemas no lineales.
# - MADALINE es más complejo y requiere más recursos.