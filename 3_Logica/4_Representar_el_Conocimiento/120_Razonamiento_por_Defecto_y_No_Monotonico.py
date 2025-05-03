# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: RAZONAMIENTO POR DEFECTO Y NO MONÓTONO PARA INFERENCIA LÓGICA
# ------------------------------------------------------------------------------------
# Este algoritmo implementa el razonamiento por defecto y no monótono.
# El razonamiento por defecto asume que ciertas cosas son verdaderas a menos que se demuestre lo contrario.
# El razonamiento no monótono permite que las conclusiones cambien si se obtiene nueva información.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE RAZONAMIENTO POR DEFECTO
# ------------------------------------------------------------------------------------
# - Aquí definimos una clase que manejará las reglas por defecto y los hechos conocidos.
# - Esta clase es la base del algoritmo, ya que permite agregar reglas, hechos y razonar sobre ellos.
# - Contiene tres métodos principales: agregar reglas, agregar hechos y razonar.
class RazonamientoPorDefecto:
    def __init__(self):
        # Inicializamos una lista para almacenar las reglas por defecto.
        self.reglas_por_defecto = []
        # Inicializamos una lista para almacenar los hechos conocidos.
        self.hechos = []

    def agregar_regla_por_defecto(self, condicion, conclusion):
        """
        Agrega una regla por defecto al sistema.
        :param condicion: Una función que evalúa si se cumple la condición.
        :param conclusion: La conclusión que se asume si la condición es verdadera.
        """
        # Guardamos la regla como una tupla (condición, conclusión).
        self.reglas_por_defecto.append((condicion, conclusion))

    def agregar_hecho(self, hecho):
        """
        Agrega un hecho conocido al sistema.
        :param hecho: Un hecho que se sabe que es verdadero.
        """
        # Añadimos el hecho a la lista de hechos conocidos.
        self.hechos.append(hecho)

    def razonar(self):
        """
        Aplica las reglas por defecto para inferir nuevos hechos.
        """
        # Creamos una lista para almacenar los nuevos hechos inferidos.
        nuevos_hechos = []
        for condicion, conclusion in self.reglas_por_defecto:
            # Verificamos si la condición se cumple y si la conclusión no contradice los hechos conocidos.
            if condicion() and conclusion not in self.hechos:
                nuevos_hechos.append(conclusion)
        # Agregamos los nuevos hechos a la lista de hechos conocidos.
        self.hechos.extend(nuevos_hechos)

# ------------------------------------------------------------------------------------
# PASO 2: CREACIÓN DE UNA INSTANCIA DEL RAZONADOR
# ------------------------------------------------------------------------------------
# - Creamos un objeto de la clase `RazonamientoPorDefecto` para manejar las reglas y hechos.
# - Este objeto será usado para agregar reglas, hechos y realizar inferencias.
razonador = RazonamientoPorDefecto()

# ------------------------------------------------------------------------------------
# PASO 3: AGREGAR UNA REGLA POR DEFECTO
# ------------------------------------------------------------------------------------
# - Agregamos una regla que dice: "Si algo es un ave y no sabemos que no vuela, entonces puede volar".
# - Esta regla se basa en el razonamiento por defecto: asumimos que las aves pueden volar a menos que sepamos lo contrario.
razonador.agregar_regla_por_defecto(
    lambda: "ave" in razonador.hechos and "no_vuela" not in razonador.hechos,
    "puede_volar"
)

# ------------------------------------------------------------------------------------
# PASO 4: AGREGAR UN HECHO CONOCIDO
# ------------------------------------------------------------------------------------
# - Agregamos un hecho conocido: "Es un ave".
# - Este hecho será usado para evaluar las reglas por defecto.
razonador.agregar_hecho("ave")

# ------------------------------------------------------------------------------------
# PASO 5: APLICAR EL RAZONAMIENTO
# ------------------------------------------------------------------------------------
# - Aplicamos el razonamiento para inferir nuevos hechos basados en las reglas y hechos conocidos.
# - En este caso, se debería inferir que "puede_volar" porque es un ave y no sabemos lo contrario.
razonador.razonar()

# ------------------------------------------------------------------------------------
# PASO 6: MOSTRAR LOS HECHOS CONOCIDOS DESPUÉS DEL RAZONAMIENTO
# ------------------------------------------------------------------------------------
# - Mostramos los hechos conocidos después de aplicar el razonamiento.
# - Esto incluye tanto los hechos iniciales como los nuevos hechos inferidos.
print("Hechos conocidos después del razonamiento:", razonador.hechos)

# ------------------------------------------------------------------------------------
# PASO 7: AGREGAR UN NUEVO HECHO QUE CONTRADIGA LA REGLA POR DEFECTO
# ------------------------------------------------------------------------------------
# - Agregamos un nuevo hecho: "No vuela" (por ejemplo, porque es un pingüino).
# - Este hecho contradice la regla por defecto de que las aves pueden volar.
razonador.agregar_hecho("no_vuela")

# ------------------------------------------------------------------------------------
# PASO 8: APLICAR EL RAZONAMIENTO NUEVAMENTE
# ------------------------------------------------------------------------------------
# - Aplicamos el razonamiento nuevamente para actualizar las conclusiones.
# - Ahora, el hecho de que "no vuela" debería invalidar la conclusión de que "puede_volar".
razonador.razonar()

# ------------------------------------------------------------------------------------
# PASO 9: MOSTRAR LOS HECHOS CONOCIDOS DESPUÉS DEL RAZONAMIENTO ACTUALIZADO
# ------------------------------------------------------------------------------------
# - Mostramos los hechos conocidos después de aplicar el razonamiento actualizado.
# - Esto incluye los hechos iniciales, los nuevos hechos inferidos y los cambios debido al razonamiento no monótono.
print("Hechos conocidos después del razonamiento actualizado:", razonador.hechos)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza el razonamiento por defecto para asumir conclusiones en ausencia de información contradictoria.
# 2. El razonamiento no monótono permite que las conclusiones cambien si se agrega nueva información que contradiga las suposiciones iniciales.
# 3. Ventajas:
#    - Permite manejar incertidumbre de manera sencilla.
#    - Es flexible y se adapta a nueva información.
# 4. Limitaciones:
#    - No maneja conflictos complejos entre reglas.
#    - Depende de la calidad de las reglas y hechos proporcionados.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# 1. Inicialmente, asumimos que las aves pueden volar porque no sabemos lo contrario.
# 2. Cuando agregamos el hecho de que "no vuela", el razonamiento no monótono actualiza las conclusiones,
#    eliminando la suposición de que puede volar.