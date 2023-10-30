pip install python-constraint

from constraint import Problem

# Crear una instancia de un problema CSP
problem = Problem()

# Definir variables y sus dominios
variables = ["x", "y", "z"]
problem.addVariable(variables[0], [1, 2, 3])
problem.addVariable(variables[1], [1, 2, 3])
problem.addVariable(variables[2], [1, 2, 3])

# Definir restricciones
def custom_constraint(x, y, z):
    return x + y + z == 6

problem.addConstraint(custom_constraint, variables)

# Encontrar una solución
solutions = problem.getSolutions()

if not solutions:
    print("No se encontraron soluciones.")
else:
    print("Solución encontrada:", solutions[0])
