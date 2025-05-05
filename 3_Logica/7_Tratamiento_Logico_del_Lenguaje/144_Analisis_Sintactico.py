# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ALGORITMO DE ANÁLISIS SINTÁCTICO PARA EXPRESIONES MATEMÁTICAS
# ------------------------------------------------------------------------------------
# Este programa implementa un algoritmo de análisis sintáctico básico que evalúa 
# expresiones matemáticas simples, como "3 + 5 * (2 - 8)". El objetivo es enseñar 
# cómo funciona un analizador sintáctico paso a paso, utilizando un enfoque 
# descendente recursivo.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE UNA CLASE PARA MANEJAR ERRORES DE SINTAXIS
# ------------------------------------------------------------------------------------
# - Esta clase personalizada se utiliza para manejar errores específicos de sintaxis.
# - Es importante porque permite identificar y reportar problemas en la expresión 
#   matemática ingresada por el usuario.
class ErrorSintactico(Exception):
    pass

# ------------------------------------------------------------------------------------
# PASO 2: DEFINICIÓN DE LA CLASE PRINCIPAL DEL ANALIZADOR SINTÁCTICO
# ------------------------------------------------------------------------------------
# - Esta clase contiene todos los métodos necesarios para analizar y evaluar 
#   expresiones matemáticas.
# - Se inicializa con la expresión a analizar y utiliza un puntero (`posicion`) para 
#   recorrerla carácter por carácter.
class AnalizadorSintactico:
    def __init__(self, expresion):
        # Inicializamos con la expresión a analizar
        self.expresion = expresion
        self.posicion = 0  # Posición actual en la cadena de texto
        self.caracter_actual = self.expresion[self.posicion]  # Caracter actual

    # --------------------------------------------------------------------------------
    # PASO 3: MÉTODO PARA AVANZAR AL SIGUIENTE CARÁCTER
    # --------------------------------------------------------------------------------
    # - Este método mueve el puntero al siguiente carácter de la expresión.
    # - Es esencial para procesar cada carácter de la expresión de forma secuencial.
    def avanzar(self):
        self.posicion += 1
        if self.posicion < len(self.expresion):
            self.caracter_actual = self.expresion[self.posicion]
        else:
            self.caracter_actual = None  # Fin de la expresión

    # --------------------------------------------------------------------------------
    # PASO 4: MÉTODO PARA IGNORAR ESPACIOS EN BLANCO
    # --------------------------------------------------------------------------------
    # - Este método salta cualquier espacio en blanco en la expresión.
    # - Es importante porque los espacios no afectan el resultado de la evaluación.
    def saltar_espacios(self):
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.avanzar()

    # --------------------------------------------------------------------------------
    # PASO 5: MÉTODO PARA ANALIZAR FACTORES (NÚMEROS O PARÉNTESIS)
    # --------------------------------------------------------------------------------
    # - Este método analiza números enteros o expresiones entre paréntesis.
    # - Es crucial porque los factores son los elementos básicos de una expresión.
    def factor(self):
        self.saltar_espacios()
        if self.caracter_actual is not None and self.caracter_actual.isdigit():
            numero = ''
            while self.caracter_actual is not None and self.caracter_actual.isdigit():
                numero += self.caracter_actual
                self.avanzar()
            return int(numero)  # Devuelve el número como entero
        elif self.caracter_actual == '(':
            self.avanzar()
            resultado = self.expr()  # Analiza la expresión dentro de los paréntesis
            if self.caracter_actual == ')':
                self.avanzar()
                return resultado
            else:
                raise ErrorSintactico("Se esperaba un ')'")  # Error si falta el paréntesis de cierre
        else:
            raise ErrorSintactico("Se esperaba un número o '('")

    # --------------------------------------------------------------------------------
    # PASO 6: MÉTODO PARA ANALIZAR TÉRMINOS (MULTIPLICACIÓN Y DIVISIÓN)
    # --------------------------------------------------------------------------------
    # - Este método analiza términos que involucran multiplicación (*) o división (/).
    # - Es importante porque estos operadores tienen mayor precedencia que suma/resta.
    def termino(self):
        resultado = self.factor()
        while self.caracter_actual in ('*', '/'):
            operador = self.caracter_actual
            self.avanzar()
            if operador == '*':
                resultado *= self.factor()
            elif operador == '/':
                resultado //= self.factor()  # División entera
        return resultado

    # --------------------------------------------------------------------------------
    # PASO 7: MÉTODO PARA ANALIZAR EXPRESIONES COMPLETAS (SUMA Y RESTA)
    # --------------------------------------------------------------------------------
    # - Este método analiza expresiones completas que incluyen suma (+) y resta (-).
    # - Es crucial porque estos operadores tienen menor precedencia que * y /.
    def expr(self):
        resultado = self.termino()
        while self.caracter_actual in ('+', '-'):
            operador = self.caracter_actual
            self.avanzar()
            if operador == '+':
                resultado += self.termino()
            elif operador == '-':
                resultado -= self.termino()
        return resultado

    # --------------------------------------------------------------------------------
    # PASO 8: MÉTODO PRINCIPAL PARA INICIAR EL ANÁLISIS
    # --------------------------------------------------------------------------------
    # - Este método inicia el análisis completo de la expresión.
    # - Verifica que no haya caracteres inesperados al final de la expresión.
    def analizar(self):
        resultado = self.expr()
        if self.caracter_actual is not None:
            raise ErrorSintactico("Caracter inesperado al final de la expresión")
        return resultado

# ------------------------------------------------------------------------------------
# PASO 9: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este bloque muestra cómo usar el analizador sintáctico con una expresión de ejemplo.
# - Permite al usuario ver el resultado del análisis o un mensaje de error si la 
#   expresión es inválida.
if __name__ == "__main__":
    # Expresión a analizar
    expresion = "3 + 5 * (2 - 8)"
    print(f"Analizando la expresión: {expresion}")
    
    # Crear una instancia del analizador y analizar la expresión
    analizador = AnalizadorSintactico(expresion)
    try:
        resultado = analizador.analizar()
        print(f"Resultado: {resultado}")
    except ErrorSintactico as e:
        print(f"Error de sintaxis: {e}")

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. El algoritmo utiliza un enfoque descendente recursivo para analizar expresiones.
# 2. Se basa en la precedencia de operadores: primero analiza paréntesis, luego 
#    multiplicación/división, y finalmente suma/resta.
# 3. Suposiciones clave:
#    - La expresión es una cadena válida con números enteros y operadores básicos.
#    - Los paréntesis están correctamente balanceados.
# 4. Ventajas:
#    - Fácil de entender y extender para otros operadores.
# 5. Limitaciones:
#    - No soporta números decimales ni operadores avanzados como potencias (^).