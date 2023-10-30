pip install python-constraint
from constraint import Problem

def graph_coloring(graph, colors):
    problem = Problem()

    # Agregar variables al problema (una variable por nodo)
    for node in graph.keys():
        problem.addVariable(node, colors)

    # Agregar restricciones: ningún par de nodos adyacentes debe tener el mismo color
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            problem.addConstraint(lambda color1, color2: color1 != color2, (node, neighbor))

    # Encontrar una solución que satisface todas las restricciones
    solution = problem.getSolution()

    if solution:
        return solution
    else:
        return "No se encontró una asignación válida de colores."

# Ejemplo de un grafo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Colores disponibles
colors = ['Rojo', 'Verde', 'Azul']

result = graph_coloring(graph, colors)

if isinstance(result, dict):
    print("Asignación de colores válida:")
    for node, color in result.items():
        print(f"Nodo {node}: {color}")
else:
    print(result)
