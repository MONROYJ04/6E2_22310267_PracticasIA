from collections import deque

def ac3(grafo, dominios):
    """
    Algoritmo AC-3 para la propagación de restricciones.
    Este algoritmo asegura que los dominios de las variables sean consistentes
    con las restricciones binarias del grafo.

    :param grafo: Diccionario que representa el grafo como lista de adyacencia.
                  Ejemplo: {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
    :param dominios: Diccionario que contiene los posibles valores (dominios)
                     de cada variable. Ejemplo: {'A': ['Rojo', 'Verde'], ...}
    :return: Diccionario con los dominios consistentes o False si no hay solución.
    """
    # Cola para almacenar las restricciones (pares de nodos conectados)
    cola = deque()

    # Inicializamos la cola con todas las aristas del grafo
    for nodo in grafo:
        for vecino in grafo[nodo]:
            cola.append((nodo, vecino))

    # Procesamos las restricciones en la cola
    while cola:
        (xi, xj) = cola.popleft()  # Extraemos un par de nodos (xi, xj)
        if revisar(dominios, xi, xj):  # Revisamos si el dominio de xi debe reducirse
            if not dominios[xi]:  # Si el dominio de xi queda vacío, no hay solución
                return False
            # Agregamos a la cola las restricciones relacionadas con xi
            for xk in grafo[xi]:
                if xk != xj:  # Evitamos agregar de nuevo la restricción (xi, xj)
                    cola.append((xk, xi))
    return dominios

def revisar(dominios, xi, xj):
    """
    Revisa si el dominio de xi necesita ser reducido debido a las restricciones
    con xj. En este caso, la restricción es que xi y xj no pueden tener el mismo valor.

    :param dominios: Diccionario con los dominios de las variables.
    :param xi: Variable actual que estamos revisando.
    :param xj: Variable vecina que impone restricciones sobre xi.
    :return: True si el dominio de xi fue modificado, False en caso contrario.
    """
    modificado = False
    for valor in dominios[xi].copy():  # Iteramos sobre una copia del dominio de xi
        # Si no hay ningún valor en el dominio de xj que sea diferente al valor actual de xi
        if all(valor == v for v in dominios[xj]):
            dominios[xi].remove(valor)  # Eliminamos el valor de xi
            modificado = True
    return modificado

# Ejemplo práctico: Coloreado de mapas
# Grafo que representa las conexiones entre regiones de un mapa
grafo = {
    'WA': ['NT', 'SA'],       # WA está conectado con NT y SA
    'NT': ['WA', 'SA', 'Q'],  # NT está conectado con WA, SA y Q
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],  # SA está conectado con varios
    'Q': ['NT', 'SA', 'NSW'], # Q está conectado con NT, SA y NSW
    'NSW': ['Q', 'SA', 'V'],  # NSW está conectado con Q, SA y V
    'V': ['SA', 'NSW']        # V está conectado con SA y NSW
}

# Dominios iniciales: Cada región puede ser de color Rojo, Verde o Azul
dominios = {
    'WA': ['Rojo', 'Verde', 'Azul'],
    'NT': ['Rojo', 'Verde', 'Azul'],
    'SA': ['Rojo', 'Verde', 'Azul'],
    'Q': ['Rojo', 'Verde', 'Azul'],
    'NSW': ['Rojo', 'Verde', 'Azul'],
    'V': ['Rojo', 'Verde', 'Azul']
}

# Aplicamos el algoritmo AC-3
resultado = ac3(grafo, dominios)

# Mostramos los dominios resultantes después de aplicar AC-3
if resultado:
    print("Dominios después de aplicar AC-3:")
    for region, colores in resultado.items():
        print(f"{region}: {colores}")
else:
    print("No hay solución posible para el problema.")