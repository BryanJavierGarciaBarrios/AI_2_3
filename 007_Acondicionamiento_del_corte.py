# instalar la biblioteca PuLP
pip install pulp

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Datos del problema
longitud_bobina = 100
demandas = [20, 15, 10]
longitudes_restantes = [longitud_bobina] * len(demandas)
n = len(demandas)

# Crear un problema de programación lineal entera
problem = LpProblem("Problema de Corte", LpMaximize)

# Crear variables
x = [LpVariable(f"x{i}", lowBound=0, upBound=demandas[i], cat="Integer") for i in range(n)]

# Función objetivo
problem += lpSum(x), "Máxima utilización de la bobina"

# Restricciones
for i in range(n):
    problem += x[i] <= demandas[i], f"Demanda máxima {i}"
    problem += lpSum(x[i] * demandas[i] for i in range(n)) <= longitud_bobina, "Máxima longitud de la bobina"

# Resolver el problema
problem.solve()

# Imprimir la solución
print("Estado:", problem.status)
print("Solución óptima:", LpMaximize if problem.status == 1 else "No encontrada")

if problem.status == 1:
    for i in range(n):
        print(f"Bobina {i + 1}: {int(x[i].varValue)} piezas")
