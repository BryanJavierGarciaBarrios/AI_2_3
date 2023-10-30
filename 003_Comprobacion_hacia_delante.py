def is_safe(board, row, col, N):
    # Verifica si es seguro colocar una reina en la posición (row, col)
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Implementa el algoritmo de comprobación hacia adelante:

def forward_checking(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            if forward_checking(board, col + 1, N):
                return True

            board[i][col] = 0

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]

    if not forward_checking(board, 0, N):
        print("No se encontraron soluciones.")
        return

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    N = 4  # Tamaño del tablero (N x N)
    solve_n_queens(N)
