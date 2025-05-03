# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE BRESENHAM PARA DIBUJAR LÍNEAS
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo de Bresenham, que permite dibujar una línea entre
# dos puntos en un espacio discreto (como una cuadrícula de píxeles). Es eficiente porque
# utiliza operaciones enteras en lugar de operaciones de punto flotante.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Importamos `matplotlib.pyplot` para graficar los puntos calculados por el algoritmo.
# - Esta biblioteca nos permite visualizar la línea generada en un gráfico 2D.
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN DEL ALGORITMO DE BRESENHAM
# ------------------------------------------------------------------------------------
# - Esta función calcula los puntos que forman una línea entre dos coordenadas (x1, y1)
#   y (x2, y2) en una cuadrícula.
# - Utiliza diferencias incrementales para determinar los puntos de la línea.
# - Es eficiente porque evita cálculos con números decimales.
def dibujar_linea_bresenham(x1, y1, x2, y2):
    """
    Dibuja una línea entre dos puntos (x1, y1) y (x2, y2) utilizando el algoritmo de Bresenham.
    
    Parámetros:
    x1, y1: Coordenadas del punto inicial.
    x2, y2: Coordenadas del punto final.
    """
    # --------------------------------------------------------------------------------
    # PASO 2.1: INICIALIZAR VARIABLES
    # --------------------------------------------------------------------------------
    # - `puntos_x` y `puntos_y` almacenan las coordenadas de los puntos de la línea.
    # - `dx` y `dy` son las diferencias absolutas entre las coordenadas de los puntos.
    # - `sx` y `sy` determinan la dirección de incremento (positivo o negativo).
    puntos_x = []
    puntos_y = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # --------------------------------------------------------------------------------
    # PASO 2.2: CALCULAR EL ERROR INICIAL
    # --------------------------------------------------------------------------------
    # - `error` es la diferencia inicial entre las coordenadas x e y.
    # - Este valor se ajustará en cada iteración para determinar el próximo punto.
    error = dx - dy

    # --------------------------------------------------------------------------------
    # PASO 2.3: BUCLE PRINCIPAL PARA CALCULAR LOS PUNTOS
    # --------------------------------------------------------------------------------
    # - Este bucle se ejecuta hasta que se alcance el punto final (x2, y2).
    # - En cada iteración, se ajustan las coordenadas y el error según las reglas del
    #   algoritmo de Bresenham.
    while True:
        # Agregamos el punto actual a las listas
        puntos_x.append(x1)
        puntos_y.append(y1)

        # Si llegamos al punto final, terminamos el bucle
        if x1 == x2 and y1 == y2:
            break

        # Calculamos el doble del error
        e2 = 2 * error

        # Ajustamos el error y las coordenadas según sea necesario
        if e2 > -dy:
            error -= dy
            x1 += sx
        if e2 < dx:
            error += dx
            y1 += sy

    # --------------------------------------------------------------------------------
    # PASO 2.4: DEVOLVER LOS RESULTADOS
    # --------------------------------------------------------------------------------
    # - Retornamos las listas `puntos_x` y `puntos_y`, que contienen las coordenadas
    #   de los puntos que forman la línea.
    return puntos_x, puntos_y

# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - En este ejemplo, definimos dos puntos (2, 3) y (10, 7) y utilizamos el algoritmo
#   para calcular los puntos intermedios de la línea que los conecta.
# - Luego, graficamos la línea utilizando `matplotlib`.
if __name__ == "__main__":
    # Definimos los puntos inicial y final
    punto_inicial_x = 2
    punto_inicial_y = 3
    punto_final_x = 10
    punto_final_y = 7

    # Llamamos a la función para calcular los puntos de la línea
    puntos_x, puntos_y = dibujar_linea_bresenham(punto_inicial_x, punto_inicial_y, punto_final_x, punto_final_y)

    # Mostramos los puntos calculados
    print("Puntos de la línea:")
    for x, y in zip(puntos_x, puntos_y):
        print(f"({x}, {y})")

    # Graficamos la línea utilizando matplotlib
    plt.plot(puntos_x, puntos_y, marker="o", color="blue", label="Línea Bresenham")
    plt.title("Algoritmo de Bresenham - Ejemplo")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)
    plt.legend()
    plt.show()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo de Bresenham calcula los puntos de una línea en una cuadrícula discreta
#    utilizando diferencias incrementales. Esto lo hace eficiente y adecuado para gráficos
#    por computadora.
# 2. Suposiciones clave:
#    - La cuadrícula es discreta (como píxeles en una pantalla).
#    - Los puntos inicial y final están definidos.
# 3. Ventajas:
#    - Evita operaciones de punto flotante, lo que lo hace rápido.
#    - Es fácil de implementar y entender.
# 4. Limitaciones:
#    - Solo funciona para líneas rectas entre dos puntos.
#    - No considera curvas ni formas complejas.