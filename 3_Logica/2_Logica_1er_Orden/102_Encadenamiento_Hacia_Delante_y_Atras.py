# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ENCADENAMIENTO HACIA ADELANTE Y HACIA ATRÁS PARA SISTEMAS EXPERTOS
# ------------------------------------------------------------------------------------
# Este código implementa dos algoritmos de inferencia lógica: encadenamiento hacia adelante 
# y encadenamiento hacia atrás. Estos algoritmos se utilizan en sistemas expertos para deducir 
# nuevos hechos o verificar si un objetivo es alcanzable a partir de un conjunto de reglas y hechos iniciales.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LAS REGLAS Y LOS HECHOS INICIALES
# ------------------------------------------------------------------------------------
# - Las reglas son representadas como una lista de diccionarios, donde cada regla tiene una condición 
#   (premisa) y una conclusión.
# - Los hechos iniciales son los datos conocidos al inicio del proceso.
# - Este paso es importante porque define la base de conocimiento del sistema experto.

# Definimos las reglas como una lista de diccionarios
reglas = [
    {"condicion": ["A"], "conclusion": "B"},  # Si A entonces B
    {"condicion": ["B"], "conclusion": "C"},  # Si B entonces C
    {"condicion": ["C", "D"], "conclusion": "E"},  # Si C y D entonces E
    {"condicion": ["E"], "conclusion": "F"}  # Si E entonces F
]

# Definimos los hechos iniciales
hechos_iniciales = ["A", "D"]  # Hechos conocidos al inicio

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN DE ENCADENAMIENTO HACIA ADELANTE
# ------------------------------------------------------------------------------------
# - Esta función deduce nuevos hechos a partir de las reglas y los hechos iniciales.
# - Verifica si las condiciones de una regla están presentes en los hechos conocidos.
# - Si se cumple, agrega la conclusión de la regla a los hechos.
# - Este proceso se repite hasta que no se puedan deducir más hechos.

def encadenamiento_hacia_adelante(reglas, hechos):
    """
    Realiza el encadenamiento hacia adelante.
    Agrega nuevos hechos a partir de las reglas y los hechos iniciales.
    """
    print("Encadenamiento hacia adelante:")
    nuevos_hechos = hechos[:]  # Copiamos los hechos iniciales
    while True:
        hecho_agregado = False  # Bandera para verificar si se agregó un nuevo hecho
        for regla in reglas:
            # Verificamos si todas las condiciones de la regla están en los hechos conocidos
            if all(condicion in nuevos_hechos for condicion in regla["condicion"]):
                if regla["conclusion"] not in nuevos_hechos:  # Evitamos duplicados
                    nuevos_hechos.append(regla["conclusion"])  # Agregamos la conclusión como nuevo hecho
                    print(f"Se agregó el hecho: {regla['conclusion']}")
                    hecho_agregado = True
        if not hecho_agregado:  # Si no se agregaron nuevos hechos, terminamos
            break
    return nuevos_hechos

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN DE ENCADENAMIENTO HACIA ATRÁS
# ------------------------------------------------------------------------------------
# - Esta función verifica si un objetivo puede ser alcanzado a partir de las reglas y los hechos iniciales.
# - Si el objetivo ya está en los hechos iniciales, se considera alcanzable.
# - Si no, busca una regla cuya conclusión sea el objetivo y verifica si las condiciones de esa regla 
#   pueden ser satisfechas recursivamente.

def encadenamiento_hacia_atras(reglas, hechos, objetivo):
    """
    Realiza el encadenamiento hacia atrás.
    Verifica si un objetivo puede ser alcanzado a partir de las reglas y los hechos iniciales.
    """
    print("\nEncadenamiento hacia atrás:")
    if objetivo in hechos:  # Si el objetivo ya está en los hechos iniciales
        print(f"El objetivo '{objetivo}' ya está en los hechos iniciales.")
        return True
    for regla in reglas:
        if regla["conclusion"] == objetivo:  # Buscamos una regla cuya conclusión sea el objetivo
            # Verificamos si todas las condiciones de la regla pueden ser satisfechas
            if all(encadenamiento_hacia_atras(reglas, hechos, condicion) for condicion in regla["condicion"]):
                print(f"El objetivo '{objetivo}' puede ser alcanzado.")
                return True
    print(f"El objetivo '{objetivo}' no puede ser alcanzado.")
    return False

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Hechos iniciales: A y D.
# - Reglas:
#   1. Si A entonces B.
#   2. Si B entonces C.
#   3. Si C y D entonces E.
#   4. Si E entonces F.
# - Realizamos el encadenamiento hacia adelante para deducir nuevos hechos.
# - Verificamos si el objetivo "F" es alcanzable con encadenamiento hacia atrás.

# Realizamos el encadenamiento hacia adelante
hechos_finales = encadenamiento_hacia_adelante(reglas, hechos_iniciales)
print("\nHechos finales después del encadenamiento hacia adelante:", hechos_finales)

# Verificamos si un objetivo puede ser alcanzado con encadenamiento hacia atrás
objetivo = "F"
es_alcanzable = encadenamiento_hacia_atras(reglas, hechos_iniciales, objetivo)
print(f"\n¿El objetivo '{objetivo}' es alcanzable? {'Sí' if es_alcanzable else 'No'}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. **Encadenamiento hacia adelante**:
#    - Parte de los hechos iniciales y aplica las reglas para deducir nuevos hechos.
#    - Es útil para descubrir todo lo que se puede deducir a partir de un conjunto de hechos.
# 2. **Encadenamiento hacia atrás**:
#    - Parte de un objetivo y verifica si puede ser alcanzado a partir de los hechos iniciales y las reglas.
#    - Es útil para responder preguntas específicas sobre si un hecho es alcanzable.
# 3. **Ventajas**:
#    - Encadenamiento hacia adelante: útil para exploración completa.
#    - Encadenamiento hacia atrás: eficiente para objetivos específicos.
# 4. **Limitaciones**:
#    - Ambos algoritmos dependen de la calidad y completitud de las reglas y hechos iniciales.