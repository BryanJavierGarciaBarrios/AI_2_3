import random

def initialize_board(n):
    board = [random.randint(0, n - 1) for _ in range(n)]
    return board

def calculate_conflicts(board):
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1

    return conflicts

def minimize_conflicts(board, max_steps):
    n = len(board)
    current_conflicts = calculate_conflicts(board)

    for _ in range(max_steps):
        if current_conflicts == 0:
            return board  # Solución encontrada

        # Encuentra una reina con conflictos y muévela a una posición que minimice los conflictos
        queen_with_conflicts = random.choice([i for i in range(n) if calculate_conflicts(board[:i] + board[i+1:]) > 0])
        min_conflicts = n

        for pos in range(n):
            board[queen_with_conflicts] = pos
            conflicts = calculate_conflicts(board)

            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_pos = pos

        board[queen_with_conflicts] = best_pos
        current_conflicts = min_conflicts

    return None  # No se encontró una solución en max_steps

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ['Q' if board[row] == col else '.' for col in range(n)]
        print(' '.join(line))

# Parámetros del problema
n_queens = 8
max_steps = 1000

# Inicializar el tablero
board = initialize_board(n_queens)

print("Tablero inicial:")
print_board(board)

solution = minimize_conflicts(board, max_steps)

if solution:
    print("\nSolución encontrada:")
    print_board(solution)
else:
    print("\nNo se encontró una solución en el número máximo de pasos.")
