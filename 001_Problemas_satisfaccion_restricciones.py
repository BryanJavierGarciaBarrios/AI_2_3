# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install python-constraint

from constraint import Problem

# Crear una instancia de un problema CSP
problem = Problem()

# Definir variables y sus dominios
problem.addVariable("A", [1, 2, 3])
problem.addVariable("B", [2, 3, 4])
problem.addVariable("C", [1, 2, 3])

# Definir restricciones
def custom_constraint(a, b, c):
    return a + b == c

problem.addConstraint(custom_constraint, ("A", "B", "C"))

# Encontrar una solución
solutions = problem.getSolutions()

# Mostrar las soluciones encontradas
for solution in solutions:
    print(solution)
