# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SIMULACIÓN DE MOVIMIENTO EN UN PLANO 2D
# ------------------------------------------------------------------------------------
# Este algoritmo simula el movimiento de un objeto en un plano 2D utilizando un sistema
# de coordenadas cartesianas (x, y). El objeto puede moverse en cuatro direcciones 
# ('arriba', 'abajo', 'izquierda', 'derecha') según las instrucciones dadas por el usuario.

# ------------------------------------------------------------------------------------
# PASO 1: INICIALIZACIÓN DE VARIABLES
# ------------------------------------------------------------------------------------
# - Aquí se definen las coordenadas iniciales del objeto en el plano 2D.
# - Estas variables representan la posición actual del objeto en los ejes X e Y.
# - Inicialmente, el objeto comienza en el origen del plano (0, 0).

posicion_x = 0  # Coordenada X inicial del objeto
posicion_y = 0  # Coordenada Y inicial del objeto

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA FUNCIÓN PARA MOVER EL OBJETO
# ------------------------------------------------------------------------------------
# - Esta función permite mover el objeto en una dirección específica una cantidad de pasos.
# - Recibe dos parámetros:
#   1. `direccion` (str): Indica hacia dónde se moverá el objeto ('arriba', 'abajo', 'izquierda', 'derecha').
#   2. `pasos` (int): Especifica cuántos pasos se moverá el objeto en la dirección indicada.
# - La función actualiza las coordenadas globales `posicion_x` y `posicion_y` según la dirección.
# - Si la dirección no es válida, muestra un mensaje de error.

def mover_objeto(direccion, pasos):
    """
    Mueve el objeto en una dirección específica una cantidad de pasos.

    Parametros:
    direccion (str): La dirección en la que se moverá el objeto ('arriba', 'abajo', 'izquierda', 'derecha').
    pasos (int): La cantidad de pasos que el objeto se moverá.

    Retorna:
    tuple: La nueva posición del objeto como (x, y).
    """
    global posicion_x, posicion_y  # Usamos las variables globales para actualizar la posición

    # --------------------------------------------------------------------------------
    # PASO 2.1: ACTUALIZACIÓN DE COORDENADAS SEGÚN LA DIRECCIÓN
    # --------------------------------------------------------------------------------
    # - Dependiendo de la dirección, se actualizan las coordenadas X o Y.
    # - 'arriba': Incrementa la coordenada Y (movimiento hacia el eje positivo de Y).
    # - 'abajo': Decrementa la coordenada Y (movimiento hacia el eje negativo de Y).
    # - 'izquierda': Decrementa la coordenada X (movimiento hacia el eje negativo de X).
    # - 'derecha': Incrementa la coordenada X (movimiento hacia el eje positivo de X).
    # - Si la dirección no es válida, se muestra un mensaje de error.

    if direccion == 'arriba':
        posicion_y += pasos  # Incrementa la coordenada Y
    elif direccion == 'abajo':
        posicion_y -= pasos  # Decrementa la coordenada Y
    elif direccion == 'izquierda':
        posicion_x -= pasos  # Decrementa la coordenada X
    elif direccion == 'derecha':
        posicion_x += pasos  # Incrementa la coordenada X
    else:
        print("Direccion no valida. Usa 'arriba', 'abajo', 'izquierda' o 'derecha'.")

    # --------------------------------------------------------------------------------
    # PASO 2.2: RETORNO DE LA NUEVA POSICIÓN
    # --------------------------------------------------------------------------------
    # - La función retorna la nueva posición del objeto como una tupla (x, y).
    return posicion_x, posicion_y

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, un robot comienza en la posición inicial (0, 0) y sigue una serie
#   de instrucciones para moverse en el plano 2D.
# - Cada movimiento se realiza llamando a la función `mover_objeto` con la dirección
#   y el número de pasos deseados.
# - Después de cada movimiento, se imprime la nueva posición del objeto.

print("Posición inicial:", (posicion_x, posicion_y))  # Mostramos la posición inicial

# Movemos el objeto según las instrucciones
nueva_posicion = mover_objeto('arriba', 5)  # Mover 5 pasos hacia arriba
print("Después de moverse hacia arriba:", nueva_posicion)

nueva_posicion = mover_objeto('derecha', 3)  # Mover 3 pasos hacia la derecha
print("Después de moverse hacia la derecha:", nueva_posicion)

nueva_posicion = mover_objeto('abajo', 2)  # Mover 2 pasos hacia abajo
print("Después de moverse hacia abajo:", nueva_posicion)

nueva_posicion = mover_objeto('izquierda', 4)  # Mover 4 pasos hacia la izquierda
print("Después de moverse hacia la izquierda:", nueva_posicion)

# Resultado final
print("Posición final del objeto:", nueva_posicion)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza un sistema de coordenadas cartesianas para simular el movimiento
#    de un objeto en un plano 2D.
# 2. Las coordenadas iniciales del objeto son (0, 0), y se actualizan según las instrucciones
#    dadas por el usuario.
# 3. La función `mover_objeto` permite realizar movimientos en cuatro direcciones básicas:
#    - 'arriba': Incrementa la coordenada Y.
#    - 'abajo': Decrementa la coordenada Y.
#    - 'izquierda': Decrementa la coordenada X.
#    - 'derecha': Incrementa la coordenada X.
# 4. Ventajas:
#    - Es fácil de entender y modificar.
#    - Permite simular movimientos básicos en un plano 2D.
# 5. Limitaciones:
#    - No considera obstáculos ni límites en el plano.
#    - Solo admite movimientos en las cuatro direcciones cardinales.