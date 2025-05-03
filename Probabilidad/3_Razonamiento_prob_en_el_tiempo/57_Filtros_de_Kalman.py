# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: FILTRO DE KALMAN PARA SEGUIMIENTO DE POSICIÓN EN 1D
# ------------------------------------------------------------------------------------
# Este código implementa un Filtro de Kalman para estimar la posición y velocidad de un objeto
# que se mueve en línea recta, utilizando mediciones ruidosas. El objetivo es combinar las 
# predicciones del modelo con las mediciones observadas para obtener estimaciones más precisas.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Aquí se importa `numpy`, una biblioteca para realizar cálculos matemáticos y operaciones
#   con matrices, que son esenciales para implementar el Filtro de Kalman.
import numpy as np

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA CLASE FILTRO DE KALMAN
# ------------------------------------------------------------------------------------
# - Esta clase encapsula toda la lógica del Filtro de Kalman.
# - Contiene métodos para predecir el estado futuro y actualizarlo con nuevas mediciones.
# - Los parámetros iniciales son esenciales para configurar el modelo.

class FiltroKalman:
    def __init__(self, estado_inicial, incertidumbre_inicial, matriz_transicion, matriz_observacion, ruido_proceso, ruido_medicion):
        """
        Inicializa el filtro de Kalman con los parámetros necesarios.
        
        estado_inicial: Vector que representa el estado inicial del sistema.
        incertidumbre_inicial: Matriz de covarianza inicial que representa la incertidumbre del estado inicial.
        matriz_transicion: Matriz que describe cómo el estado cambia de un paso al siguiente.
        matriz_observacion: Matriz que relaciona el estado con las mediciones observadas.
        ruido_proceso: Matriz que representa la incertidumbre en el modelo del proceso.
        ruido_medicion: Matriz que representa la incertidumbre en las mediciones.
        """
        # Guardamos los parámetros iniciales como atributos de la clase
        self.estado = estado_inicial
        self.incertidumbre = incertidumbre_inicial
        self.matriz_transicion = matriz_transicion
        self.matriz_observacion = matriz_observacion
        self.ruido_proceso = ruido_proceso
        self.ruido_medicion = ruido_medicion

    # ------------------------------------------------------------------------------------
    # PASO 3: MÉTODO PARA LA PREDICCIÓN
    # ------------------------------------------------------------------------------------
    # - Este método predice el estado futuro del sistema basándose en el modelo.
    # - También actualiza la incertidumbre asociada al estado predicho.
    def predecir(self):
        """
        Predice el siguiente estado del sistema y actualiza la incertidumbre.
        """
        # Predicción del estado siguiente usando la matriz de transición
        self.estado = np.dot(self.matriz_transicion, self.estado)
        # Actualización de la incertidumbre considerando el ruido del proceso
        self.incertidumbre = np.dot(np.dot(self.matriz_transicion, self.incertidumbre), self.matriz_transicion.T) + self.ruido_proceso

    # ------------------------------------------------------------------------------------
    # PASO 4: MÉTODO PARA LA ACTUALIZACIÓN
    # ------------------------------------------------------------------------------------
    # - Este método ajusta el estado predicho utilizando una nueva medición.
    # - Calcula la ganancia de Kalman, que determina cuánto confiar en la medición.
    def actualizar(self, medicion):
        """
        Actualiza el estado del sistema con una nueva medición.
        
        medicion: Vector que representa la medición observada.
        """
        # Cálculo de la matriz de covarianza de la medición
        S = np.dot(np.dot(self.matriz_observacion, self.incertidumbre), self.matriz_observacion.T) + self.ruido_medicion
        # Cálculo de la ganancia de Kalman
        K = np.dot(np.dot(self.incertidumbre, self.matriz_observacion.T), np.linalg.inv(S))
        
        # Actualización del estado con la medición
        self.estado = self.estado + np.dot(K, (medicion - np.dot(self.matriz_observacion, self.estado)))
        
        # Actualización de la incertidumbre
        I = np.eye(self.incertidumbre.shape[0])  # Matriz identidad
        self.incertidumbre = np.dot((I - np.dot(K, self.matriz_observacion)), self.incertidumbre)

# ------------------------------------------------------------------------------------
# PASO 5: CONFIGURAR EL EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, rastreamos la posición de un objeto que se mueve en línea recta.
# - Las mediciones de posición tienen ruido, pero el filtro de Kalman ayuda a estimar
#   la posición y velocidad reales del objeto.

# Estado inicial: posición = 0, velocidad = 1
estado_inicial = np.array([0, 1])  # [posición, velocidad]

# Incertidumbre inicial: asumimos que no estamos seguros del estado inicial
incertidumbre_inicial = np.array([[1, 0], [0, 1]])

# Matriz de transición: describe cómo el estado cambia de un paso al siguiente
# Aquí asumimos que la posición cambia según la velocidad.
matriz_transicion = np.array([[1, 1], [0, 1]])

# Matriz de observación: indica qué parte del estado podemos observar directamente
# En este caso, solo observamos la posición.
matriz_observacion = np.array([[1, 0]])

# Ruido del proceso: incertidumbre en el modelo del movimiento
ruido_proceso = np.array([[1, 0], [0, 1]])

# Ruido de medición: incertidumbre en las mediciones
ruido_medicion = np.array([[1]])

# Creamos el filtro de Kalman con los parámetros definidos
filtro = FiltroKalman(estado_inicial, incertidumbre_inicial, matriz_transicion, matriz_observacion, ruido_proceso, ruido_medicion)

# ------------------------------------------------------------------------------------
# PASO 6: SIMULAR MEDICIONES Y APLICAR EL FILTRO
# ------------------------------------------------------------------------------------
# - Simulamos una serie de mediciones ruidosas de la posición del objeto.
# - Aplicamos el filtro de Kalman para estimar la posición y velocidad reales.

# Mediciones simuladas de la posición del objeto
mediciones = [1, 2, 3, 4, 5, 6]

# Aplicamos el filtro de Kalman a cada medición
for medicion in mediciones:
    filtro.predecir()  # Predicción del siguiente estado
    filtro.actualizar(np.array([medicion]))  # Actualización con la medición
    print(f"Estado estimado: {filtro.estado}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El Filtro de Kalman combina predicciones del modelo con mediciones observadas para
#    obtener estimaciones más precisas del estado del sistema.
# 2. Suposiciones clave:
#    - El sistema es lineal y puede representarse con matrices.
#    - El ruido en el proceso y las mediciones es gaussiano.
# 3. Ventajas:
#    - Reduce el impacto del ruido en las mediciones.
#    - Proporciona estimaciones óptimas bajo las suposiciones mencionadas.
# 4. Limitaciones:
#    - No funciona bien si el sistema no es lineal o si el ruido no es gaussiano.