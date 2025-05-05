# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ESPACIO DE VERSIONES Y ALGORITMO AQ PARA APRENDIZAJE INDUCTIVO
# ------------------------------------------------------------------------------------
# Este programa implementa el Espacio de Versiones y el algoritmo AQ, utilizados en 
# aprendizaje inductivo para encontrar hipótesis consistentes con ejemplos positivos 
# y excluir ejemplos negativos. Es útil para clasificar datos basados en atributos.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE HIPÓTESIS
# ------------------------------------------------------------------------------------
# - Aquí definimos una clase llamada `Hipotesis` que representa una hipótesis.
# - Cada hipótesis contiene una lista de atributos que describen las características 
#   de los ejemplos (por ejemplo, color, tamaño, forma).
# - La función `es_consistente` verifica si una hipótesis es consistente con un ejemplo.
class Hipotesis:
    def __init__(self, atributos):
        # Inicializamos la hipótesis con una lista de atributos.
        # Los atributos pueden ser valores específicos, '?' (cualquier valor) o 'Ø' (vacío).
        self.atributos = atributos

    def es_consistente(self, ejemplo, es_positivo):
        # Verifica si la hipótesis es consistente con un ejemplo dado.
        # Un ejemplo es consistente si todos los atributos coinciden o son genéricos ('?').
        for i in range(len(self.atributos)):
            if self.atributos[i] != '?' and self.atributos[i] != ejemplo[i]:
                return False
        return es_positivo

# ------------------------------------------------------------------------------------
# PASO 2: INICIALIZACIÓN DEL ESPACIO DE VERSIONES
# ------------------------------------------------------------------------------------
# - Esta función crea el Espacio de Versiones inicial.
# - El Espacio de Versiones contiene dos conjuntos de hipótesis:
#   1. Hipótesis más general (todos los atributos son '?').
#   2. Hipótesis más específica (todos los atributos son 'Ø').
def inicializar_espacio_versiones(num_atributos):
    # Creamos la hipótesis más general y la más específica.
    hipotesis_general = Hipotesis(['?'] * num_atributos)
    hipotesis_especifica = Hipotesis(['Ø'] * num_atributos)
    return [hipotesis_general], [hipotesis_especifica]

# ------------------------------------------------------------------------------------
# PASO 3: ACTUALIZACIÓN DEL ESPACIO DE VERSIONES
# ------------------------------------------------------------------------------------
# - Esta función actualiza el Espacio de Versiones con base en un ejemplo.
# - Si el ejemplo es positivo, refinamos las hipótesis específicas para cubrirlo.
# - Si el ejemplo es negativo, refinamos las hipótesis generales para excluirlo.
def actualizar_espacio_versiones(espacio_general, espacio_especifico, ejemplo, es_positivo):
    if es_positivo:
        # Refinamos las hipótesis específicas para cubrir el ejemplo positivo.
        for hipotesis in espacio_especifico:
            for i in range(len(hipotesis.atributos)):
                if hipotesis.atributos[i] == 'Ø':
                    # Si el atributo es vacío ('Ø'), lo reemplazamos con el valor del ejemplo.
                    hipotesis.atributos[i] = ejemplo[i]
                elif hipotesis.atributos[i] != ejemplo[i]:
                    # Si el atributo no coincide, lo generalizamos a '?'.
                    hipotesis.atributos[i] = '?'
    else:
        # Refinamos las hipótesis generales para excluir el ejemplo negativo.
        for hipotesis in espacio_general:
            for i in range(len(hipotesis.atributos)):
                if hipotesis.atributos[i] == '?':
                    # Si el atributo es genérico ('?'), lo reemplazamos con el valor del ejemplo.
                    hipotesis.atributos[i] = ejemplo[i]

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO - CLASIFICACIÓN DE FRUTAS
# ------------------------------------------------------------------------------------
# - Atributos: [Color, Tamaño, Forma].
# - Ejemplo positivo: ['Rojo', 'Grande', 'Redonda'].
# - Ejemplo negativo: ['Verde', 'Pequeño', 'Ovalada'].

# Inicializamos el Espacio de Versiones con 3 atributos.
espacio_general, espacio_especifico = inicializar_espacio_versiones(3)

# Ejemplo positivo: Una fruta roja, grande y redonda.
ejemplo_positivo = ['Rojo', 'Grande', 'Redonda']
actualizar_espacio_versiones(espacio_general, espacio_especifico, ejemplo_positivo, True)

# Ejemplo negativo: Una fruta verde, pequeña y ovalada.
ejemplo_negativo = ['Verde', 'Pequeño', 'Ovalada']
actualizar_espacio_versiones(espacio_general, espacio_especifico, ejemplo_negativo, False)

# Mostramos el resultado final.
print("Hipótesis General:")
for hipotesis in espacio_general:
    print(hipotesis.atributos)

print("Hipótesis Específica:")
for hipotesis in espacio_especifico:
    print(hipotesis.atributos)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El Espacio de Versiones contiene todas las hipótesis posibles que son consistentes 
#    con los datos de entrenamiento.
# 2. El algoritmo AQ refina las hipótesis específicas para cubrir ejemplos positivos y 
#    las hipótesis generales para excluir ejemplos negativos.
# 3. Ventajas:
#    - Encuentra hipótesis consistentes con los datos.
#    - Es interpretable y fácil de entender.
# 4. Limitaciones:
#    - No maneja ruido en los datos.
#    - Puede ser computacionalmente costoso con muchos atributos o ejemplos.