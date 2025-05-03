# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA DIFUSO PARA CALCULAR PROPINA EN UN RESTAURANTE
# ------------------------------------------------------------------------------------
# Este código utiliza lógica difusa para calcular la propina sugerida en un restaurante
# basado en dos factores: el nivel de servicio y la calidad de la comida. El sistema
# toma valores imprecisos y los convierte en una decisión clara (propina sugerida).

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `numpy` para manejar arreglos numéricos.
# - Importamos `skfuzzy` para implementar lógica difusa.
# - Importamos `control` de `skfuzzy` para definir y simular el sistema difuso.
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE VARIABLES DIFUSAS
# ------------------------------------------------------------------------------------
# - Definimos las variables de entrada (nivel de servicio y calidad de la comida) y
#   la variable de salida (propina).
# - Cada variable tiene un rango de valores (universo) y etiquetas lingüísticas
#   (por ejemplo, "malo", "regular", "excelente").

# Variable de entrada: nivel de servicio (rango de 0 a 10)
nivel_servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'nivel_servicio')

# Variable de entrada: calidad de la comida (rango de 0 a 10)
calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')

# Variable de salida: propina (rango de 0 a 25)
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# ------------------------------------------------------------------------------------
# PASO 3: DEFINICIÓN DE FUNCIONES DE MEMBRESÍA
# ------------------------------------------------------------------------------------
# - Las funciones de membresía representan cómo los valores numéricos se asignan a
#   etiquetas lingüísticas (por ejemplo, "malo", "regular", "excelente").
# - Usamos funciones triangulares (`trimf`) para definir estas etiquetas.

# Para el nivel de servicio
nivel_servicio['malo'] = fuzz.trimf(nivel_servicio.universe, [0, 0, 5])
nivel_servicio['regular'] = fuzz.trimf(nivel_servicio.universe, [0, 5, 10])
nivel_servicio['excelente'] = fuzz.trimf(nivel_servicio.universe, [5, 10, 10])

# Para la calidad de la comida
calidad_comida['mala'] = fuzz.trimf(calidad_comida.universe, [0, 0, 5])
calidad_comida['regular'] = fuzz.trimf(calidad_comida.universe, [0, 5, 10])
calidad_comida['excelente'] = fuzz.trimf(calidad_comida.universe, [5, 10, 10])

# Para la propina
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# ------------------------------------------------------------------------------------
# PASO 4: DEFINICIÓN DE REGLAS DIFUSAS
# ------------------------------------------------------------------------------------
# - Las reglas difusas relacionan las entradas con la salida usando lógica lingüística.
# - Por ejemplo: "Si el nivel de servicio es malo o la calidad de la comida es mala,
#   entonces la propina es baja".

# Si el nivel de servicio es malo o la calidad de la comida es mala, entonces la propina es baja
regla1 = ctrl.Rule(nivel_servicio['malo'] | calidad_comida['mala'], propina['baja'])

# Si el nivel de servicio es regular, entonces la propina es media
regla2 = ctrl.Rule(nivel_servicio['regular'], propina['media'])

# Si el nivel de servicio es excelente o la calidad de la comida es excelente, entonces la propina es alta
regla3 = ctrl.Rule(nivel_servicio['excelente'] | calidad_comida['excelente'], propina['alta'])

# ------------------------------------------------------------------------------------
# PASO 5: CREACIÓN DEL SISTEMA DIFUSO
# ------------------------------------------------------------------------------------
# - Creamos un sistema de control difuso que combina las reglas definidas.
# - Este sistema se utiliza para simular y calcular la salida (propina).

# Creamos el sistema de control difuso
sistema_propinas = ctrl.ControlSystem([regla1, regla2, regla3])

# Creamos un simulador para evaluar casos específicos
simulador = ctrl.ControlSystemSimulation(sistema_propinas)

# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Evaluamos un caso práctico donde el nivel de servicio es 8 y la calidad de la comida es 6.
# - El sistema calcula la propina sugerida basada en las reglas difusas.

# Asignamos valores a las variables de entrada
simulador.input['nivel_servicio'] = 8  # Nivel de servicio: 8 (bueno)
simulador.input['calidad_comida'] = 6  # Calidad de la comida: 6 (regular)

# Calculamos la propina sugerida
simulador.compute()

# Mostramos el resultado
print(f"Propina sugerida: {simulador.output['propina']}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza lógica difusa para manejar incertidumbre en las entradas.
# 2. Las funciones de membresía convierten valores numéricos en etiquetas lingüísticas.
# 3. Las reglas difusas combinan estas etiquetas para tomar decisiones.
# 4. El sistema calcula una salida precisa (propina) basada en entradas imprecisas.
# 5. Ventaja: permite tomar decisiones humanas en sistemas automatizados.
# 6. Limitación: requiere definir reglas y funciones de membresía manualmente.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Entrada:
# - Nivel de servicio: 8
# - Calidad de la comida: 6
# Salida:
# - Propina sugerida: (por ejemplo) 19.5