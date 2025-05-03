# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SISTEMA DE LÓGICA DIFUSA PARA CALCULAR PROPINA
# ------------------------------------------------------------------------------------
# Este código implementa un sistema de lógica difusa que calcula la propina sugerida 
# en un restaurante basado en dos factores: la calidad de la comida y la calidad del servicio.
# Utiliza la biblioteca `skfuzzy` para definir las reglas y funciones de pertenencia.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `numpy` para manejar arreglos numéricos.
# - Importamos `skfuzzy` para trabajar con lógica difusa.
# - Importamos `control` de `skfuzzy` para crear sistemas de control difuso.

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR VARIABLES DE ENTRADA Y SALIDA
# ------------------------------------------------------------------------------------
# - Creamos las variables de entrada (calidad de la comida y calidad del servicio).
# - Creamos la variable de salida (propina).
# - Cada variable tiene un rango definido:
#   - `calidad_comida` y `calidad_servicio`: de 0 (malo) a 10 (excelente).
#   - `propina`: de 0 (baja) a 25 (alta).

calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
calidad_servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# ------------------------------------------------------------------------------------
# PASO 3: DEFINIR FUNCIONES DE PERTENENCIA
# ------------------------------------------------------------------------------------
# - Las funciones de pertenencia describen cómo los valores de entrada/salida 
#   se clasifican en categorías difusas (por ejemplo, "malo", "regular", "excelente").
# - Usamos funciones triangulares (`trimf`) para definir estas categorías.

# Para la calidad de la comida
calidad_comida['mala'] = fuzz.trimf(calidad_comida.universe, [0, 0, 5])
calidad_comida['regular'] = fuzz.trimf(calidad_comida.universe, [0, 5, 10])
calidad_comida['excelente'] = fuzz.trimf(calidad_comida.universe, [5, 10, 10])

# Para la calidad del servicio
calidad_servicio['malo'] = fuzz.trimf(calidad_servicio.universe, [0, 0, 5])
calidad_servicio['regular'] = fuzz.trimf(calidad_servicio.universe, [0, 5, 10])
calidad_servicio['excelente'] = fuzz.trimf(calidad_servicio.universe, [5, 10, 10])

# Para la propina
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# ------------------------------------------------------------------------------------
# PASO 4: DEFINIR REGLAS DIFUSAS
# ------------------------------------------------------------------------------------
# - Las reglas difusas relacionan las entradas con la salida.
# - Ejemplo: "Si la comida es mala o el servicio es malo, entonces la propina es baja".
# - Estas reglas son la base del sistema de lógica difusa.

regla1 = ctrl.Rule(calidad_comida['mala'] | calidad_servicio['malo'], propina['baja'])
regla2 = ctrl.Rule(calidad_comida['regular'] & calidad_servicio['regular'], propina['media'])
regla3 = ctrl.Rule(calidad_comida['excelente'] | calidad_servicio['excelente'], propina['alta'])

# ------------------------------------------------------------------------------------
# PASO 5: CREAR EL SISTEMA DE CONTROL DIFUSO
# ------------------------------------------------------------------------------------
# - Combinamos las reglas en un sistema de control.
# - Este sistema se utiliza para realizar cálculos basados en las entradas.

sistema_propina = ctrl.ControlSystem([regla1, regla2, regla3])
simulador_propina = ctrl.ControlSystemSimulation(sistema_propina)

# ------------------------------------------------------------------------------------
# PASO 6: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Asignamos valores específicos a las entradas:
#   - `calidad_comida` = 6 (calidad moderada).
#   - `calidad_servicio` = 9 (servicio excelente).
# - Calculamos la propina sugerida utilizando el sistema difuso.

simulador_propina.input['calidad_comida'] = 6
simulador_propina.input['calidad_servicio'] = 9

# Calculamos la propina
simulador_propina.compute()

# Mostramos el resultado
print(f"Propina sugerida: {simulador_propina.output['propina']:.2f}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Lógica difusa**: Este algoritmo utiliza lógica difusa para manejar incertidumbre 
#    y subjetividad en la evaluación de la calidad de la comida y el servicio.
# 2. **Funciones de pertenencia**: Las funciones triangulares clasifican los valores 
#    en categorías difusas (por ejemplo, "malo", "regular", "excelente").
# 3. **Reglas difusas**: Las reglas establecen relaciones entre las entradas y la salida.
# 4. **Ventajas**:
#    - Permite tomar decisiones en situaciones subjetivas.
#    - Es fácil de interpretar y ajustar.
# 5. **Limitaciones**:
#    - Depende de la calidad de las reglas definidas.
#    - No es adecuado para problemas con datos muy complejos o grandes volúmenes.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# Entrada:
# - Calidad de la comida: 6
# - Calidad del servicio: 9
# Salida:
# - Propina sugerida: 20.83