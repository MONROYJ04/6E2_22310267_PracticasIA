def salto_atras_dirigido_por_conflictos(csp, asignacion={}):
    """
    Algoritmo de Salto Atrás Dirigido por Conflictos (CBJ) para resolver problemas de satisfacción de restricciones (CSP).
    :param csp: Diccionario que contiene:
        - variables: Lista de variables.
        - dominios: Diccionario de dominios {variable: [valores]}.
        - restricciones: Función que retorna True si se cumplen las restricciones.
    :param asignacion: Asignación actual {variable: valor}.
    :return: Asignación solución o None si no hay solución.
    """
    # Si todas las variables están asignadas, se encontró una solución
    if len(asignacion) == len(csp["variables"]):
        return asignacion

    # Seleccionar la siguiente variable sin asignar usando la heurística MRV
    variable = seleccionar_variable_sin_asignar(csp, asignacion)

    # Probar cada valor del dominio de la variable en orden LCV
    for valor in ordenar_valores_dominio(csp, variable, asignacion):
        # Verificar si el valor es consistente con las restricciones
        if es_consistente(csp, variable, valor, asignacion):
            # Asignar temporalmente el valor a la variable
            asignacion[variable] = valor

            # Llamada recursiva para intentar resolver con la nueva asignación
            resultado = salto_atras_dirigido_por_conflictos(csp, asignacion)
            if resultado is not None:
                return resultado  # Solución encontrada

            # Si no se encontró solución, deshacer la asignación
            del asignacion[variable]
        else:
            # Encontrar la variable en conflicto
            variable_conflicto = encontrar_conflicto(csp, variable, valor, asignacion)
            if variable_conflicto != variable:
                return None  # Saltar al nivel del conflicto
    return None  # No se encontró solución

# Funciones auxiliares:
def seleccionar_variable_sin_asignar(csp, asignacion):
    """Selecciona la próxima variable sin asignar usando la heurística MRV (Menor Restricción de Valores)."""
    sin_asignar = [v for v in csp["variables"] if v not in asignacion]
    return min(sin_asignar, key=lambda v: len(csp["dominios"][v]))

def ordenar_valores_dominio(csp, variable, asignacion):
    """Ordena los valores del dominio de la variable usando la heurística LCV (Menor Conflicto)."""
    return sorted(csp["dominios"][variable], key=lambda val: contar_conflictos(csp, variable, val, asignacion))

def es_consistente(csp, variable, valor, asignacion):
    """Verifica si asignar 'valor' a 'variable' es consistente con las restricciones."""
    asignacion[variable] = valor  # Asignación temporal
    consistente = csp["restricciones"](asignacion)
    del asignacion[variable]  # Deshacer asignación temporal
    return consistente

def encontrar_conflicto(csp, variable, valor, asignacion):
    """
    Encuentra la variable más reciente en el conflicto.
    :return: Variable en conflicto o 'variable' si no hay conflicto previo.
    """
    asignacion[variable] = valor  # Asignación temporal
    for v in reversed(list(asignacion.keys())):  # De más reciente a más antigua
        if v == variable:
            continue
        asignacion_temporal = asignacion.copy()
        del asignacion_temporal[variable]
        if not csp["restricciones"](asignacion_temporal):
            del asignacion[variable]
            return v
    del asignacion[variable]
    return variable

def contar_conflictos(csp, variable, valor, asignacion):
    """Cuenta los conflictos potenciales para la heurística LCV."""
    asignacion[variable] = valor
    conflictos = 0
    for vecino in obtener_vecinos(csp, variable):
        if vecino not in asignacion:
            for valor_vecino in csp["dominios"][vecino]:
                asignacion[vecino] = valor_vecino
                if not csp["restricciones"](asignacion):
                    conflictos += 1
                del asignacion[vecino]
    del asignacion[variable]
    return conflictos

def obtener_vecinos(csp, variable):
    """Retorna las variables relacionadas por restricciones (simulado)."""
    return [v for v in csp["variables"] if v != variable]

# Ejemplo práctico:
# Problema de coloreo de mapas: asignar colores a regiones adyacentes sin que compartan el mismo color
csp = {
    "variables": ["WA", "NT", "SA", "Q", "NSW", "V"],
    "dominios": {
        "WA": ["Rojo", "Verde", "Azul"],
        "NT": ["Rojo", "Verde", "Azul"],
        "SA": ["Rojo", "Verde", "Azul"],
        "Q": ["Rojo", "Verde", "Azul"],
        "NSW": ["Rojo", "Verde", "Azul"],
        "V": ["Rojo", "Verde", "Azul"]
    },
    "restricciones": lambda asignacion: all(
        asignacion.get(u) != asignacion.get(v)
        for u in asignacion
        for v in asignacion
        if v in obtener_vecinos(csp, u)
    )
}

# Resolver el CSP usando el algoritmo de Salto Atrás Dirigido por Conflictos
solucion = salto_atras_dirigido_por_conflictos(csp)
print("Solución encontrada:", solucion)