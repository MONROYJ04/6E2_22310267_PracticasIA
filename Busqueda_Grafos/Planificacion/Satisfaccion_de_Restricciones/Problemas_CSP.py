class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # Ej: ['X', 'Y']
        self.domains = domains      # Ej: {'X': [1, 2, 3], 'Y': [2, 4]}
        self.constraints = constraints  # Funciones que retornan True/False