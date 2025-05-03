# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: BASE DE CONOCIMIENTO PARA LÓGICA PROPOSICIONAL
# ------------------------------------------------------------------------------------
# Este código implementa una Base de Conocimiento que permite almacenar hechos y reglas
# para deducir nueva información utilizando lógica proposicional. Es útil para sistemas
# de inferencia y razonamiento automático.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE BASE DE CONOCIMIENTO
# ------------------------------------------------------------------------------------
# - Aquí se define la estructura principal que almacena los hechos y reglas.
# - Los hechos son datos conocidos, y las reglas son implicaciones que relacionan hechos.
# - Esto es importante porque permite razonar sobre los datos almacenados.
class BaseDeConocimiento:
    def __init__(self):
        # Lista para almacenar los hechos conocidos
        self.hechos = set()  # Usamos un conjunto para evitar duplicados.
        # Lista para almacenar las reglas (como implicaciones)
        self.reglas = []  # Cada regla es una tupla (condición, conclusión).

    # --------------------------------------------------------------------------------
    # PASO 2: MÉTODO PARA AGREGAR HECHOS
    # --------------------------------------------------------------------------------
    # - Este método permite agregar hechos conocidos a la Base de Conocimiento.
    # - Los hechos son cadenas de texto que representan información verdadera.
    # - Es importante porque los hechos son la base para deducir nueva información.
    def agregar_hecho(self, hecho):
        """
        Agrega un hecho a la Base de Conocimiento.
        :param hecho: Hecho que se desea agregar (cadena de texto).
        """
        self.hechos.add(hecho)  # Agregamos el hecho al conjunto de hechos.

    # --------------------------------------------------------------------------------
    # PASO 3: MÉTODO PARA AGREGAR REGLAS
    # --------------------------------------------------------------------------------
    # - Este método permite agregar reglas a la Base de Conocimiento.
    # - Una regla tiene una condición (lista de hechos) y una conclusión (hecho deducido).
    # - Es importante porque las reglas permiten deducir nueva información.
    def agregar_regla(self, condicion, conclusion):
        """
        Agrega una regla a la Base de Conocimiento.
        :param condicion: Condición de la regla (lista de hechos que deben cumplirse).
        :param conclusion: Conclusión de la regla (hecho que se deduce si se cumple la condición).
        """
        self.reglas.append((condicion, conclusion))  # Agregamos la regla como una tupla.

    # --------------------------------------------------------------------------------
    # PASO 4: MÉTODO PARA VERIFICAR SI UN HECHO ES VERDADERO
    # --------------------------------------------------------------------------------
    # - Este método verifica si un hecho es verdadero basándose en los hechos y reglas.
    # - Si el hecho está en los hechos conocidos, es verdadero.
    # - Si no, intenta deducirlo utilizando las reglas.
    # - Es importante porque permite razonar sobre los datos almacenados.
    def es_verdadero(self, hecho):
        """
        Verifica si un hecho es verdadero basándose en los hechos y reglas de la Base de Conocimiento.
        :param hecho: Hecho que se desea verificar.
        :return: True si el hecho es verdadero, False en caso contrario.
        """
        # Si el hecho ya está en los hechos conocidos, es verdadero
        if hecho in self.hechos:
            return True

        # Verificar si alguna regla puede deducir el hecho
        for condicion, conclusion in self.reglas:
            # Si la conclusión de la regla es el hecho que buscamos
            if conclusion == hecho:
                # Verificar si todos los hechos en la condición son verdaderos
                if all(self.es_verdadero(h) for h in condicion):
                    return True

        # Si no se puede deducir el hecho, es falso
        return False


# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO DE USO DE LA BASE DE CONOCIMIENTO
# ------------------------------------------------------------------------------------
# - En este ejemplo, se crean hechos y reglas para deducir si hace frío y si se necesita un abrigo.
# - Se verifica si ciertos hechos son verdaderos utilizando el método `es_verdadero`.
if __name__ == "__main__":
    # Crear una instancia de la Base de Conocimiento
    base = BaseDeConocimiento()

    # Agregar hechos conocidos
    base.agregar_hecho("es_de_noche")  # Sabemos que es de noche.
    base.agregar_hecho("esta_nublado")  # Sabemos que está nublado.

    # Agregar reglas
    # Si es de noche y está nublado, entonces hace frío
    base.agregar_regla(["es_de_noche", "esta_nublado"], "hace_frio")
    # Si hace frío, entonces se necesita un abrigo
    base.agregar_regla(["hace_frio"], "necesita_abrigo")

    # Verificar hechos
    print("¿Hace frío?", base.es_verdadero("hace_frio"))  # Debería imprimir: True
    print("¿Se necesita un abrigo?", base.es_verdadero("necesita_abrigo"))  # Debería imprimir: True
    print("¿Es de día?", base.es_verdadero("es_de_dia"))  # Debería imprimir: False

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza lógica proposicional para razonar sobre hechos y reglas.
# 2. Los hechos son datos conocidos, y las reglas son implicaciones que relacionan hechos.
# 3. El método `es_verdadero` utiliza un enfoque recursivo para verificar si un hecho es verdadero.
# 4. Ventajas:
#    - Permite deducir nueva información a partir de hechos y reglas.
#    - Es flexible y fácil de extender con nuevos hechos y reglas.
# 5. Limitaciones:
#    - Puede ser ineficiente si hay muchas reglas y hechos debido a la recursión.
#    - No maneja incertidumbre ni contradicciones entre reglas.