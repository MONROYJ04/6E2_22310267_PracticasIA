def cut_conditioning(numbers, target, current=[], index=0, total=0):
    """
    Encuentra subconjuntos que sumen 'target' usando acondicionamiento del corte.
    :param numbers: Lista de números.
    :param target: Suma objetivo.
    :param current: Subconjunto actual.
    :param index: Índice actual en la lista.
    :param total: Suma parcial actual.
    :return: Subconjuntos válidos.
    """
    if total == target:
        print(current)  # Solución encontrada
        return
    if index >= len(numbers) or total > target:
        return  # Corte: no hay solución en esta rama
    
    # Incluir el número actual
    cut_conditioning(numbers, target, current + [numbers[index]], index + 1, total + numbers[index])
    
    # Excluir el número actual (solo si es prometedor)
    if total + sum(numbers[index+1:]) >= target:  # Corte: si la suma restante es suficiente
        cut_conditioning(numbers, target, current, index + 1, total)

# Ejemplo de uso:
numbers = [3, 1, 4, 2, 2]
target = 5
cut_conditioning(numbers, target)