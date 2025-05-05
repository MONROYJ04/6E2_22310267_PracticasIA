# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: GRAMÁTICAS LIBRES DE CONTEXTO PARA VALIDAR CADENAS
# ------------------------------------------------------------------------------------
# Este programa implementa un ejemplo básico para entender las Gramáticas de la Jerarquía de Chomsky.
# En particular, se enfoca en las gramáticas libres de contexto (Tipo 2), que permiten generar cadenas
# válidas en un lenguaje específico. El objetivo es verificar si una cadena pertenece al lenguaje
# definido por la gramática: S -> aSb | ε.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------------
# - La función `verificar_cadena` evalúa si una cadena pertenece al lenguaje generado por la gramática.
# - Utiliza una pila para simular el proceso de derivación de la gramática.
# - La gramática utilizada es: S -> aSb | ε, donde:
#   - `S` es el símbolo inicial.
#   - `a` y `b` son terminales.
#   - `ε` representa la cadena vacía.

def verificar_cadena(cadena):
    """
    Esta función verifica si una cadena pertenece al lenguaje generado por la gramática:
    S -> aSb | ε
    Donde:
    - S es el símbolo inicial.
    - 'a' y 'b' son terminales.
    - ε representa la cadena vacía.
    """
    # ------------------------------------------------------------------------------------
    # PASO 2: INICIALIZACIÓN DE LA PILA Y EL ÍNDICE
    # ------------------------------------------------------------------------------------
    # - La pila se utiliza para simular el proceso de derivación de la gramática.
    # - Comienza con el símbolo inicial `S`.
    # - El índice `indice` se utiliza para recorrer la cadena de entrada.
    pila = ['S']  # Comenzamos con el símbolo inicial
    indice = 0  # Índice para recorrer la cadena

    # ------------------------------------------------------------------------------------
    # PASO 3: PROCESAMIENTO DE LA PILA
    # ------------------------------------------------------------------------------------
    # - Mientras haya elementos en la pila, se procesan uno por uno.
    # - Si el símbolo en la cima de la pila es un terminal (`a` o `b`), se compara con el
    #   carácter actual de la cadena.
    # - Si el símbolo es `S`, se aplican las reglas de producción de la gramática.
    while pila:
        # Obtenemos el símbolo en la cima de la pila
        simbolo = pila.pop()

        # ------------------------------------------------------------------------------------
        # PASO 4: VALIDACIÓN DE TERMINALES
        # ------------------------------------------------------------------------------------
        # - Si el símbolo es un terminal (`a` o `b`), se verifica si coincide con el carácter
        #   actual de la cadena.
        # - Si no coincide, la cadena no pertenece al lenguaje.
        if simbolo == 'a' or simbolo == 'b':
            if indice < len(cadena) and cadena[indice] == simbolo:
                indice += 1  # Avanzamos al siguiente carácter
            else:
                return False  # La cadena no pertenece al lenguaje

        # ------------------------------------------------------------------------------------
        # PASO 5: APLICACIÓN DE REGLAS DE PRODUCCIÓN
        # ------------------------------------------------------------------------------------
        # - Si el símbolo es `S`, se aplican las reglas de producción de la gramática.
        # - La regla `S -> aSb` se implementa añadiendo `b`, `S` y `a` a la pila en ese orden.
        elif simbolo == 'S':
            # Si aún hay caracteres por procesar, aplicamos la regla S -> aSb
            if indice < len(cadena):
                pila.append('b')  # Agregamos 'b' a la pila
                pila.append('S')  # Agregamos 'S' a la pila
                pila.append('a')  # Agregamos 'a' a la pila

        # ------------------------------------------------------------------------------------
        # PASO 6: VALIDACIÓN DE SÍMBOLOS DESCONOCIDOS
        # ------------------------------------------------------------------------------------
        # - Si se encuentra un símbolo desconocido, la cadena no pertenece al lenguaje.
        else:
            return False

    # ------------------------------------------------------------------------------------
    # PASO 7: VERIFICACIÓN FINAL
    # ------------------------------------------------------------------------------------
    # - Si se ha procesado toda la cadena y la pila está vacía, la cadena es válida.
    return indice == len(cadena)

# ------------------------------------------------------------------------------------
# PASO 8: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Se define una cadena de prueba para verificar si pertenece al lenguaje.
# - Se utiliza la función `verificar_cadena` para realizar la validación.
# - Se imprime el resultado indicando si la cadena pertenece o no al lenguaje.

if __name__ == "__main__":
    # Definimos una cadena de prueba
    cadena_prueba = "aabb"

    # Verificamos si la cadena pertenece al lenguaje
    resultado = verificar_cadena(cadena_prueba)

    # Mostramos el resultado
    if resultado:
        print(f"La cadena '{cadena_prueba}' pertenece al lenguaje generado por la gramática.")
    else:
        print(f"La cadena '{cadena_prueba}' NO pertenece al lenguaje generado por la gramática.")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. La gramática utilizada es `S -> aSb | ε`. Esto significa que:
#    - El símbolo inicial `S` puede reemplazarse por `aSb` o por la cadena vacía `ε`.
#    - El lenguaje generado contiene cadenas con el mismo número de `a` y `b`, donde todas las `a`
#      preceden a las `b`.
# 2. El algoritmo utiliza una pila para simular el proceso de derivación de la gramática.
# 3. Ventajas:
#    - Permite validar cadenas de manera eficiente para gramáticas libres de contexto.
# 4. Limitaciones:
#    - Solo funciona para gramáticas libres de contexto simples como la definida en este ejemplo.