import random
import numpy as np

def print_sudoku(board):
    """Imprime o tabuleiro de Sudoku."""
    for row in board:
        print(" ".join(str(val) if val != 0 else '.' for val in row))

def is_safe(board, row, col, num):
    """Verifica se é seguro colocar o número no tabuleiro."""
    size = len(board)
    box_size = int(size ** 0.5)
    
    # Verificar linha e coluna
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(size)]:
        return False

    # Verificar sub-quadrante
    start_row = row - row % box_size
    start_col = col - col % box_size
    for r in range(start_row, start_row + box_size):
        for c in range(start_col, start_col + box_size):
            if board[r][c] == num:
                return False
                
    return True

def fill_board(board):
    """Preenche o tabuleiro de Sudoku usando backtracking."""
    size = len(board)
    
    def solve():
        for i in range(size):
            for j in range(size):
                if board[i][j] == 0:
                    nums = list(range(1, size + 1))
                    random.shuffle(nums)  # Embaralha os números para gerar uma solução aleatória
                    for num in nums:
                        if is_safe(board, i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    solve()

def remove_numbers(board, size):
    """Remove alguns números do tabuleiro para criar o desafio."""
    squares_to_remove = int(size ** 2 * 0.5)  # Aproximadamente metade das células
    while squares_to_remove > 0:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] != 0:
            board[row][col] = 0
            squares_to_remove -= 1

def generate_sudoku(size):
    """Gera um tabuleiro de Sudoku com o tamanho especificado."""
    if size == 1:
        return [[1]]  # Caso trivial 1x1

    board = np.zeros((size, size), dtype=int)
    
    # Preencher o tabuleiro com números válidos
    fill_board(board)
    
    # Remover alguns números para criar o desafio
    remove_numbers(board, size)
    
    return board.tolist()  # Retorna como lista de listas

if __name__ == "__main__":
    # Exemplo de uso
    size = int(input("Digite o tamanho do Sudoku (como 9 para 9x9): "))
    sudoku = generate_sudoku(size)

    print("Tabuleiro de Sudoku gerado:")
    print_sudoku(np.array(sudoku))  # Usando numpy para facilitar a visualização em matriz
    print("\nLista de Python do tabuleiro gerado:")
    for i, row in enumerate(sudoku):  # Exibe cada linha do tabuleiro separadamente
        if i == 0:
            print(f'[{row},')
            continue
        elif i == len(sudoku)-1:
            print(f'{row}]')
            continue
        print(f'{row},')
