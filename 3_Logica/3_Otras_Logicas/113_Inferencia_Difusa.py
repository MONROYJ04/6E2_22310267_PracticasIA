# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA DE INFERENCIA DIFUSA PARA CALCULAR PROPINA
# ------------------------------------------------------------------------------------
# Este código implementa un sistema de inferencia difusa que calcula el porcentaje 
# de propina sugerido en un restaurante, basado en la calidad del servicio y la calidad 
# de la comida. Utiliza la librería `skfuzzy` para definir las reglas y funciones de 
# membresía necesarias para la lógica difusa.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------------
# - Importamos las librerías necesarias para trabajar con lógica difusa.
# - `numpy` se utiliza para manejar los rangos de valores de las variables.
# - `skfuzzy` permite definir funciones de membresía y reglas difusas.
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE VARIABLES DE ENTRADA Y SALIDA
# ------------------------------------------------------------------------------------
# - Definimos las variables de entrada: `calidad_servicio` y `calidad_comida`.
#   Estas variables representan los factores que influirán en el cálculo de la propina.
# - Definimos la variable de salida: `propina`, que representa el porcentaje de propina.
# - Usamos `np.arange` para definir los rangos de valores posibles para cada variable.
calidad_servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_servicio')
calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# ------------------------------------------------------------------------------------
# PASO 3: DEFINICIÓN DE FUNCIONES DE MEMBRESÍA
# ------------------------------------------------------------------------------------
# - Las funciones de membresía definen cómo se clasifican los valores de las variables.
# - Para cada variable, definimos tres categorías: "mala", "regular" y "buena".
# - Usamos `fuzz.trimf` para crear funciones de membresía triangulares.
# - Estas funciones permiten asignar un grado de pertenencia a cada categoría.

# Funciones de membresía para la calidad del servicio
calidad_servicio['mala'] = fuzz.trimf(calidad_servicio.universe, [0, 0, 5])
calidad_servicio['regular'] = fuzz.trimf(calidad_servicio.universe, [0, 5, 10])
calidad_servicio['buena'] = fuzz.trimf(calidad_servicio.universe, [5, 10, 10])

# Funciones de membresía para la calidad de la comida
calidad_comida['mala'] = fuzz.trimf(calidad_comida.universe, [0, 0, 5])
calidad_comida['regular'] = fuzz.trimf(calidad_comida.universe, [0, 5, 10])
calidad_comida['buena'] = fuzz.trimf(calidad_comida.universe, [5, 10, 10])

# Funciones de membresía para la propina
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# ------------------------------------------------------------------------------------
# PASO 4: DEFINICIÓN DE REGLAS DIFUSAS
# ------------------------------------------------------------------------------------
# - Las reglas difusas describen cómo las entradas afectan la salida.
# - Usamos operadores lógicos como `|` (OR) y `&` (AND) para combinar condiciones.
# - Cada regla conecta las categorías de las entradas con una categoría de la salida.

# Si el servicio es malo o la comida es mala, entonces la propina es baja
regla1 = ctrl.Rule(calidad_servicio['mala'] | calidad_comida['mala'], propina['baja'])

# Si el servicio es regular o la comida es regular, entonces la propina es media
regla2 = ctrl.Rule(calidad_servicio['regular'] | calidad_comida['regular'], propina['media'])

# Si el servicio es bueno y la comida es buena, entonces la propina es alta
regla3 = ctrl.Rule(calidad_servicio['buena'] & calidad_comida['buena'], propina['alta'])

# ------------------------------------------------------------------------------------
# PASO 5: CREACIÓN DEL SISTEMA DE CONTROL DIFUSO
# ------------------------------------------------------------------------------------
# - Creamos un sistema de control difuso que combina las reglas definidas.
# - Este sistema se utiliza para realizar inferencias basadas en las entradas.
control_propina = ctrl.ControlSystem([regla1, regla2, regla3])
simulador_propina = ctrl.ControlSystemSimulation(control_propina)

# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Asignamos valores específicos a las variables de entrada.
# - En este caso, la calidad del servicio es 8 y la calidad de la comida es 6.
# - Calculamos la propina sugerida utilizando el sistema de inferencia difusa.
simulador_propina.input['calidad_servicio'] = 8
simulador_propina.input['calidad_comida'] = 6

# Calculamos la propina
simulador_propina.compute()

# Mostramos el resultado
print(f"Porcentaje de propina sugerido: {simulador_propina.output['propina']:.2f}%")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Lógica difusa**: Este algoritmo utiliza lógica difusa para modelar la incertidumbre
#    y subjetividad en la toma de decisiones (en este caso, calcular la propina).
# 2. **Funciones de membresía**: Las funciones triangulares asignan grados de pertenencia
#    a las categorías de las variables de entrada y salida.
# 3. **Inferencia difusa**: Las reglas difusas combinan las entradas para determinar la salida.
# 4. **Ventajas**: Este enfoque es flexible y puede manejar datos imprecisos.
# 5. **Limitaciones**: Requiere definir manualmente las funciones de membresía y reglas.