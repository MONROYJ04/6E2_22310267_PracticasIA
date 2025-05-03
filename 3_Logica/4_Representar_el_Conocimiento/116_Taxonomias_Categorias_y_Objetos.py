# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: TAXONOMÍAS UTILIZANDO CATEGORÍAS Y OBJETOS
# ------------------------------------------------------------------------------------
# Este código implementa una taxonomía jerárquica utilizando categorías y objetos.
# Una taxonomía es una forma de organizar información en niveles, como un árbol.
# Por ejemplo, podemos organizar animales en categorías como "Mamíferos" y "Aves",
# y dentro de estas, subcategorías como "Perros" y "Gatos".

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LA CLASE `Categoria`
# ------------------------------------------------------------------------------------
# - Esta clase representa una categoría dentro de la taxonomía.
# - Cada categoría tiene un nombre, una lista de subcategorías y una lista de objetos.
# - Es la base para construir la estructura jerárquica.
class Categoria:
    def __init__(self, nombre):
        # El nombre de la categoría (por ejemplo, "Mamiferos").
        self.nombre = nombre
        # Lista para almacenar subcategorías (por ejemplo, "Perros", "Gatos").
        self.subcategorias = []
        # Lista para almacenar objetos que pertenecen a esta categoría (por ejemplo, "Labrador").
        self.objetos = []

    # ------------------------------------------------------------------------------------
    # PASO 2: MÉTODO PARA AGREGAR SUBCATEGORÍAS
    # ------------------------------------------------------------------------------------
    # - Este método permite añadir subcategorías a una categoría existente.
    # - Es importante para construir la jerarquía de la taxonomía.
    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    # ------------------------------------------------------------------------------------
    # PASO 3: MÉTODO PARA AGREGAR OBJETOS
    # ------------------------------------------------------------------------------------
    # - Este método permite añadir objetos a una categoría específica.
    # - Los objetos representan elementos concretos dentro de una categoría.
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    # ------------------------------------------------------------------------------------
    # PASO 4: MÉTODO PARA MOSTRAR LA TAXONOMÍA
    # ------------------------------------------------------------------------------------
    # - Este método imprime la estructura jerárquica de la taxonomía.
    # - Utiliza recursión para mostrar subcategorías y objetos en cada nivel.
    # - El parámetro `nivel` controla la sangría para representar la jerarquía.
    def mostrar_taxonomia(self, nivel=0):
        # Imprime el nombre de la categoría con sangría según el nivel.
        print("  " * nivel + f"Categoria: {self.nombre}")
        # Muestra los objetos de esta categoría.
        for objeto in self.objetos:
            print("  " * (nivel + 1) + f"Objeto: {objeto}")
        # Llama recursivamente a este método para mostrar las subcategorías.
        for subcategoria in self.subcategorias:
            subcategoria.mostrar_taxonomia(nivel + 1)

# ------------------------------------------------------------------------------------
# PASO 5: EJEMPLO PRÁCTICO - CREACIÓN DE UNA TAXONOMÍA DE ANIMALES
# ------------------------------------------------------------------------------------
# - Este bloque crea una taxonomía de animales con categorías y subcategorías.
# - Se añaden objetos específicos a las categorías para ilustrar el uso del algoritmo.
if __name__ == "__main__":
    # Creamos la categoría principal "Animales".
    animales = Categoria("Animales")

    # Creamos subcategorías para "Mamiferos" y "Aves".
    mamiferos = Categoria("Mamiferos")
    aves = Categoria("Aves")

    # Agregamos las subcategorías a la categoría principal.
    animales.agregar_subcategoria(mamiferos)
    animales.agregar_subcategoria(aves)

    # Creamos subcategorías para "Perros" y "Gatos" dentro de "Mamiferos".
    perros = Categoria("Perros")
    gatos = Categoria("Gatos")
    mamiferos.agregar_subcategoria(perros)
    mamiferos.agregar_subcategoria(gatos)

    # Agregamos objetos a las subcategorías.
    perros.agregar_objeto("Labrador")
    perros.agregar_objeto("Bulldog")
    gatos.agregar_objeto("Siames")
    gatos.agregar_objeto("Persa")
    aves.agregar_objeto("Aguila")
    aves.agregar_objeto("Loro")

    # Mostramos la taxonomía completa.
    print("Taxonomía de Animales:")
    animales.mostrar_taxonomia()

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Este algoritmo utiliza una estructura de árbol para organizar información jerárquica.
# 2. Cada nodo del árbol es una categoría, que puede tener subcategorías (hijos) y objetos.
# 3. La recursión se utiliza para recorrer y mostrar la estructura completa del árbol.
# 4. Ventajas:
#    - Permite organizar información compleja de manera clara y estructurada.
#    - Es fácil de extender añadiendo nuevas categorías u objetos.
# 5. Limitaciones:
#    - No es eficiente para búsquedas en estructuras muy grandes (sin optimización adicional).
#    - No incluye validaciones para evitar duplicados.

# ------------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: TAXONOMÍA DE ANIMALES
# ------------------------------------------------------------------------------------
# Entrada:
# - Categoría principal: "Animales".
# - Subcategorías: "Mamiferos", "Aves".
# - Subcategorías de "Mamiferos": "Perros", "Gatos".
# - Objetos: "Labrador", "Bulldog", "Siames", "Persa", "Aguila", "Loro".
#
# Salida esperada:
# Taxonomía de Animales:
# Categoria: Animales
#   Categoria: Mamiferos
#     Categoria: Perros
#       Objeto: Labrador
#       Objeto: Bulldog
#     Categoria: Gatos
#       Objeto: Siames
#       Objeto: Persa
#   Categoria: Aves
#     Objeto: Aguila
#     Objeto: Loro