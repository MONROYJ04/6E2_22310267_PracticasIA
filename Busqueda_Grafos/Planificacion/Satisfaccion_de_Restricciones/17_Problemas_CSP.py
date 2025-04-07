# Clase que representa un Problema de Satisfacción de Restricciones (CSP)
class CSP:
    def __init__(self, variables, dominios, restricciones):
        """
        Inicializa el problema CSP.

        :param variables: Lista de variables del problema. Ejemplo: ['X', 'Y']
        :param dominios: Diccionario que asocia cada variable con sus valores posibles. Ejemplo: {'X': [1, 2, 3], 'Y': [2, 4]}
        :param restricciones: Función que define las restricciones entre variables. Debe retornar True si se cumple, False si no.
        """
        self.variables = variables  # Lista de variables
        self.dominios = dominios    # Dominios de cada variable
        self.restricciones = restricciones  # Restricciones entre variables

    def es_consistente(self, variable, valor, asignacion):
        """
        Verifica si un valor asignado a una variable es consistente con las restricciones.

        :param variable: La variable a verificar.
        :param valor: El valor que se quiere asignar a la variable.
        :param asignacion: Asignación actual de valores a variables.
        :return: True si es consistente, False si no.
        """
        # Recorre todas las variables ya asignadas
        for otra_variable in asignacion:
            # Si la restricción entre la variable actual y otra no se cumple, retorna False
            if not self.restricciones(variable, valor, otra_variable, asignacion[otra_variable]):
                return False
        return True

    def busqueda_retroceso(self, asignacion={}):
        """
        Realiza una búsqueda con retroceso (backtracking) para encontrar una solución al problema CSP.

        :param asignacion: Asignación actual de valores a variables.
        :return: Una asignación completa que satisface todas las restricciones, o None si no hay solución.
        """
        # Si todas las variables están asignadas, retorna la asignación
        if len(asignacion) == len(self.variables):
            return asignacion

        # Selecciona una variable no asignada
        no_asignadas = [v for v in self.variables if v not in asignacion]
        primera = no_asignadas[0]

        # Intenta asignar un valor del dominio de la variable seleccionada
        for valor in self.dominios[primera]:
            if self.es_consistente(primera, valor, asignacion):
                # Si es consistente, realiza la asignación
                asignacion[primera] = valor
                # Llama recursivamente al algoritmo con la nueva asignación
                resultado = self.busqueda_retroceso(asignacion)
                if resultado is not None:
                    return resultado
                # Si no se encuentra solución, elimina la asignación (backtracking)
                del asignacion[primera]

        # Si no se encuentra solución, retorna None
        return None


# Ejemplo práctico: Problema de coloreo de mapas
# Variables: Regiones de un mapa
variables = ['A', 'B', 'C', 'D']

# Dominios: Colores disponibles para cada región
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul']
}

# Restricciones: Dos regiones adyacentes no pueden tener el mismo color
def restricciones(var1, val1, var2, val2):
    """
    Define las restricciones del problema. En este caso, dos regiones adyacentes no pueden tener el mismo color.

    :param var1: Primera variable.
    :param val1: Valor asignado a la primera variable.
    :param var2: Segunda variable.
    :param val2: Valor asignado a la segunda variable.
    :return: True si la restricción se cumple, False si no.
    """
    # Si las variables son diferentes, verifica que los valores también lo sean
    if var1 != var2:
        return val1 != val2
    return True

# Crear el problema CSP
problema_csp = CSP(variables, dominios, restricciones)

# Resolver el problema usando búsqueda con retroceso
solucion = problema_csp.busqueda_retroceso()

# Imprimir la solución encontrada
print("Solucion encontrada:", solucion)