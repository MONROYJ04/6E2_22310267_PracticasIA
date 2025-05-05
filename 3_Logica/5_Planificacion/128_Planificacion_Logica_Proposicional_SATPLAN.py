# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: SATPLAN PARA PLANIFICACIÓN LÓGICA PROPOSICIONAL
# ------------------------------------------------------------------------------------
# Este código implementa el algoritmo SATPLAN, que utiliza lógica proposicional y 
# técnicas de satisfacibilidad (SAT) para encontrar un plan que permita alcanzar 
# un objetivo desde un estado inicial. Es útil en problemas de planificación automática.

# ------------------------------------------------------------------------------------
# PASO 1: IMPORTAR LAS BIBLIOTECAS NECESARIAS
# ------------------------------------------------------------------------------------
# - Aquí se importa la biblioteca `pysat.solvers`, que contiene herramientas para 
#   resolver problemas SAT. En este caso, usamos el solucionador `Glucose3`.
# - Esta biblioteca es esencial para convertir el problema de planificación en un 
#   problema SAT y resolverlo.

from pysat.solvers import Glucose3  # Biblioteca para resolver problemas SAT

# ------------------------------------------------------------------------------------
# PASO 2: DEFINIR LA FUNCIÓN PRINCIPAL DEL ALGORITMO SATPLAN
# ------------------------------------------------------------------------------------
# - Esta función toma como entrada el estado inicial, las acciones disponibles, 
#   los objetivos y el horizonte (número máximo de pasos permitidos).
# - Devuelve un plan (lista de acciones) que permite alcanzar los objetivos o `None` 
#   si no hay solución.

def satplan(estado_inicial, acciones, objetivos, horizonte):
    """
    SATPLAN: Encuentra un plan para alcanzar los objetivos desde el estado inicial.
    
    Parámetros:
    - estado_inicial: Lista de proposiciones que representan el estado inicial.
    - acciones: Lista de acciones disponibles, cada una con precondiciones y efectos.
    - objetivos: Lista de proposiciones que representan el estado objetivo.
    - horizonte: Número máximo de pasos (profundidad) para encontrar el plan.
    
    Retorna:
    - Una lista de acciones que forman el plan, o None si no hay solución.
    """
    # --------------------------------------------------------------------------------
    # PASO 3: CREAR EL SOLUCIONADOR SAT
    # --------------------------------------------------------------------------------
    # - Se inicializa un solucionador SAT (`Glucose3`) para resolver el problema.
    # - Este solucionador se encargará de verificar si existe una combinación de 
    #   variables que satisfaga todas las restricciones del problema.
    solucionador = Glucose3()

    # --------------------------------------------------------------------------------
    # PASO 4: CODIFICAR EL PROBLEMA EN FORMATO SAT
    # --------------------------------------------------------------------------------
    # - Se crean variables proposicionales para representar los estados y acciones 
    #   en cada paso de tiempo.
    # - Cada variable tiene un identificador único asignado por un contador.
    variables = {}
    contador = 1  # Contador para asignar identificadores únicos a las variables

    # Codificar los estados en cada paso de tiempo
    for t in range(horizonte + 1):
        for estado in estado_inicial + objetivos:
            variables[(estado, t)] = contador
            contador += 1

    # Codificar las acciones en cada paso de tiempo
    for t in range(horizonte):
        for accion in acciones:
            variables[(accion['nombre'], t)] = contador
            contador += 1

    # --------------------------------------------------------------------------------
    # PASO 5: AGREGAR RESTRICCIONES AL SOLUCIONADOR SAT
    # --------------------------------------------------------------------------------
    # - Se definen las restricciones necesarias para que el solucionador pueda 
    #   encontrar un plan válido.

    # Restricción 1: El estado inicial debe cumplirse en t=0
    for estado in estado_inicial:
        solucionador.add_clause([variables[(estado, 0)]])

    # Restricción 2: Los objetivos deben cumplirse en algún t <= horizonte
    for objetivo in objetivos:
        solucionador.add_clause([variables[(objetivo, horizonte)]])

    # Restricción 3: Las precondiciones de las acciones deben cumplirse
    for t in range(horizonte):
        for accion in acciones:
            for precondicion in accion['precondiciones']:
                solucionador.add_clause([-variables[(accion['nombre'], t)], variables[(precondicion, t)]])

    # Restricción 4: Los efectos de las acciones deben cumplirse
    for t in range(horizonte):
        for accion in acciones:
            for efecto in accion['efectos']:
                solucionador.add_clause([-variables[(accion['nombre'], t)], variables[(efecto, t + 1)]])

    # --------------------------------------------------------------------------------
    # PASO 6: RESOLVER EL PROBLEMA SAT
    # --------------------------------------------------------------------------------
    # - Se utiliza el solucionador SAT para encontrar una solución al problema.
    # - Si se encuentra una solución, se extrae el plan del modelo generado.
    if solucionador.solve():
        modelo = solucionador.get_model()
        plan = []

        # Extraer el plan del modelo SAT
        for t in range(horizonte):
            for accion in acciones:
                if modelo[variables[(accion['nombre'], t)] - 1] > 0:
                    plan.append((accion['nombre'], t))

        return plan
    else:
        return None

# ------------------------------------------------------------------------------------
# PASO 7: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este ejemplo define un problema simple donde un robot debe mover una caja de 
#   una posición inicial "A" a una posición objetivo "B".
# - Se definen las acciones disponibles, el estado inicial, los objetivos y el 
#   horizonte máximo.

if __name__ == "__main__":
    # Definir el estado inicial
    estado_inicial = ["robot_en_A", "caja_en_A"]

    # Definir las acciones disponibles
    acciones = [
        {
            "nombre": "mover_A_a_B",
            "precondiciones": ["robot_en_A"],
            "efectos": ["robot_en_B", "-robot_en_A"]
        },
        {
            "nombre": "mover_B_a_A",
            "precondiciones": ["robot_en_B"],
            "efectos": ["robot_en_A", "-robot_en_B"]
        },
        {
            "nombre": "empujar_caja_A_a_B",
            "precondiciones": ["robot_en_A", "caja_en_A"],
            "efectos": ["caja_en_B", "-caja_en_A"]
        }
    ]

    # Definir los objetivos
    objetivos = ["caja_en_B"]

    # Definir el horizonte (profundidad máxima)
    horizonte = 2

    # Ejecutar el algoritmo SATPLAN
    plan = satplan(estado_inicial, acciones, objetivos, horizonte)

    # Mostrar el resultado
    if plan:
        print("Plan encontrado:")
        for accion, tiempo in plan:
            print(f"En el paso {tiempo}: {accion}")
    else:
        print("No se encontró un plan.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. SATPLAN convierte un problema de planificación en un problema SAT.
# 2. Las restricciones aseguran que las acciones sean válidas y conduzcan al objetivo.
# 3. El solucionador SAT encuentra una combinación de variables que satisface todas 
#    las restricciones, lo que equivale a un plan válido.
# 4. Ventajas: Es un enfoque general y puede resolver problemas complejos.
# 5. Limitaciones: Puede ser computacionalmente costoso para problemas grandes.