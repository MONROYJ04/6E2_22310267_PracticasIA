# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: EVENTOS Y OBJETOS MENTALES: CREENCIAS
# ------------------------------------------------------------------------------------
# Este algoritmo modela el concepto de "Eventos y Objetos Mentales: Creencias".
# Las creencias son representaciones mentales que una persona tiene sobre un evento o situación.
# Este modelo permite asociar un nivel de certeza a las creencias y una probabilidad a los eventos.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINIR LA CLASE "CREENCIA"
# ------------------------------------------------------------------------------------
# - Esta clase representa una creencia que un sujeto tiene sobre una proposición.
# - Incluye atributos como el sujeto (quién cree), la proposición (qué se cree) y el nivel de certeza.
# - Es importante porque modela cómo las personas perciben eventos con diferentes niveles de confianza.

class Creencia:
    def __init__(self, sujeto, proposicion, certeza):
        """
        Inicializa una creencia.

        :param sujeto: La persona o entidad que tiene la creencia.
        :param proposicion: La idea o afirmación que se cree.
        :param certeza: El nivel de certeza de la creencia (0 a 1).
        """
        self.sujeto = sujeto  # Nombre del sujeto que tiene la creencia
        self.proposicion = proposicion  # La proposición que se cree
        self.certeza = certeza  # Nivel de certeza de la creencia (0 = duda total, 1 = certeza total)

    def __str__(self):
        """
        Representación en texto de la creencia.
        """
        return f"{self.sujeto} cree que '{self.proposicion}' con un nivel de certeza de {self.certeza * 100}%."


# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA CLASE "EVENTO"
# ------------------------------------------------------------------------------------
# - Esta clase representa un evento con una descripción y una probabilidad de ocurrencia.
# - Es importante porque permite modelar situaciones del mundo real con incertidumbre.
# - Atributos clave:
#   - `descripcion`: Describe el evento (ejemplo: "Lloverá mañana").
#   - `probabilidad`: Probabilidad de que ocurra el evento (valor entre 0 y 1).

class Evento:
    def __init__(self, descripcion, probabilidad):
        """
        Inicializa un evento.

        :param descripcion: Descripción del evento.
        :param probabilidad: Probabilidad de que el evento ocurra (0 a 1).
        """
        self.descripcion = descripcion  # Descripción del evento
        self.probabilidad = probabilidad  # Probabilidad de ocurrencia del evento

    def __str__(self):
        """
        Representación en texto del evento.
        """
        return f"Evento: '{self.descripcion}' con una probabilidad de {self.probabilidad * 100}%."


# ------------------------------------------------------------------------------------
# PASO 3: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar las clases `Evento` y `Creencia` juntas.
# - Se crea un evento con una probabilidad específica y una creencia asociada a ese evento.
# - Es importante porque ilustra cómo modelar eventos y creencias en un contexto real.

if __name__ == "__main__":
    # Crear un evento
    # - Aquí se modela un evento llamado "Lloverá mañana" con una probabilidad del 70%.
    evento_lluvia = Evento("Lloverá mañana", 0.7)

    # Crear una creencia sobre el evento
    # - Juan cree con un 80% de certeza que el evento "Lloverá mañana" ocurrirá.
    creencia_juan = Creencia("Juan", "Lloverá mañana", 0.8)

    # Mostrar el evento y la creencia
    # - Se imprimen los detalles del evento y la creencia para que el usuario los visualice.
    print(evento_lluvia)
    print(creencia_juan)

    # Explicación adicional
    # - Si la probabilidad del evento es alta (por ejemplo, 70%), es razonable que alguien tenga una creencia fuerte (80%).
    # - Sin embargo, si la probabilidad del evento fuera baja, la creencia podría ser menos fuerte.

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo modela cómo las personas perciben eventos con diferentes niveles de certeza.
# 2. Suposiciones clave:
#    - La probabilidad de un evento es un valor entre 0 y 1.
#    - El nivel de certeza de una creencia también es un valor entre 0 y 1.
# 3. Ventajas:
#    - Permite modelar incertidumbre de manera sencilla.
#    - Es flexible y puede extenderse a otros contextos (por ejemplo, predicciones).
# 4. Limitaciones:
#    - No considera factores externos que puedan influir en la certeza o probabilidad.
#    - No modela cambios dinámicos en las creencias o eventos.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO ADICIONAL
# ------------------------------------------------------------------------------------
# - Supongamos que queremos modelar otro evento y creencia:
#   - Evento: "Habrá tráfico mañana" con una probabilidad del 50%.
#   - Creencia: "Ana cree con un 60% de certeza que habrá tráfico mañana".

# Crear un nuevo evento
evento_trafico = Evento("Habrá tráfico mañana", 0.5)

# Crear una nueva creencia
creencia_ana = Creencia("Ana", "Habrá tráfico mañana", 0.6)

# Mostrar el nuevo evento y la nueva creencia
print(evento_trafico)
print(creencia_ana)

# ------------------------------------------------------------------------------------
# SALIDA ESPERADA
# ------------------------------------------------------------------------------------
# Evento: 'Lloverá mañana' con una probabilidad de 70.0%.
# Juan cree que 'Lloverá mañana' con un nivel de certeza de 80.0%.
# Evento: 'Habrá tráfico mañana' con una probabilidad de 50.0%.
# Ana cree que 'Habrá tráfico mañana' con un nivel de certeza de 60.0%.