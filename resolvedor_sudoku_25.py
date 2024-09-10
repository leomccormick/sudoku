from colorama import Fore, Style, init
import time
from gerador_sudoku import generate_sudoku

# Função para imprimir o tabuleiro com cores e substituir 0 por '.'
def imprimir_sudoku(sudoku, original_sudoku):
    # Limpar o terminal (opcional para visualização mais limpa)
    print("\033[H\033[J", end="")
    
    tamanho = len(sudoku)
    sqrt_tamanho = int(tamanho**0.5)  # Calcula a raiz quadrada do tamanho para identificar sub-quadrantes

    for i in range(tamanho):
        for j in range(tamanho):
            if sudoku[i][j] == 0:
                print(".", end=" ")  # Substitui '0' por '.'
            elif original_sudoku[i][j] != 0:  # Se o número já estava no tabuleiro original
                print(Fore.BLUE + str(sudoku[i][j]) + Style.RESET_ALL, end=" ")
            else:
                print(Fore.GREEN + str(sudoku[i][j]) + Style.RESET_ALL, end=" ")
        print()  # Quebra de linha entre as linhas do sudoku
    print("\n")

# Função para resolver o Sudoku com força bruta
def resolver_sudoku(sudoku, original_sudoku, tempo_delay=0):
    vazio = encontrar_vazio(sudoku)
    tamanho = len(sudoku)
    if not vazio:
        return True  # Sudoku resolvido
    else:
        linha, coluna = vazio

    for num in range(1, tamanho + 1):  # Ajustado para lidar com tamanhos maiores
        if checar_valido(sudoku, num, linha, coluna):
            sudoku[linha][coluna] = num
            
            # Imprimir o estado atual do Sudoku
            imprimir_sudoku(sudoku, original_sudoku)
            time.sleep(tempo_delay)  # Delay para visualização

            if resolver_sudoku(sudoku, original_sudoku):
                return True

            sudoku[linha][coluna] = 0  # Resetar se o número não funcionar
            # Mostrar o reset
            imprimir_sudoku(sudoku, original_sudoku)
            time.sleep(tempo_delay)
    return False

# Função para encontrar espaços vazios (representados por 0)
def encontrar_vazio(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

# Função para checar se o número é válido na posição
def checar_valido(sudoku, num, linha, coluna):
    tamanho = len(sudoku)
    sqrt_tamanho = int(tamanho**0.5)  # Raiz quadrada do tamanho para encontrar o tamanho do sub-quadrante
    
    # Verificar linha e coluna
    if num in sudoku[linha]:
        return False
    if num in [sudoku[i][coluna] for i in range(tamanho)]:
        return False
    
    # Verificar sub-quadrante
    sub_quadrante_linha = linha // sqrt_tamanho * sqrt_tamanho
    sub_quadrante_coluna = coluna // sqrt_tamanho * sqrt_tamanho
    
    for i in range(sub_quadrante_linha, sub_quadrante_linha + sqrt_tamanho):
        for j in range(sub_quadrante_coluna, sub_quadrante_coluna + sqrt_tamanho):
            if sudoku[i][j] == num:
                return False
                
    return True

def print_time(tempo_fim, tempo_inicio) -> None:
    tempo_total = tempo_fim - tempo_inicio
    if tempo_total >= 60:
        print(f"Tempo decorrido: {tempo_total//60}min {tempo_total-tempo_total//60*60:.2f}s")
    elif tempo_total > 1:
        print(f"Tempo decorrido: {tempo_total:.2f} s")
    else:
        print(f"Tempo decorrido: {tempo_total:.4f} s")

# Exemplo de uso
while True:
    sudoku_para_resolver = [[6, 3, 0, 25, 15, 0, 0, 9, 1, 2, 7, 0, 0, 17, 0, 5, 0, 13, 0, 22, 11, 12, 14, 21, 0],
                            [12, 0, 0, 0, 14, 25, 7, 5, 0, 11, 0, 3, 0, 0, 2, 0, 8, 21, 4, 0, 24, 0, 13, 0, 0],
                            [0, 0, 0, 24, 16, 0, 0, 0, 0, 12, 0, 0, 25, 18, 0, 0, 2, 0, 0, 0, 15, 0, 0, 22, 0],
                            [2, 22, 0, 0, 18, 0, 0, 4, 0, 17, 9, 0, 14, 11, 15, 12, 6, 0, 0, 16, 0, 20, 19, 0, 0],
                            [20, 0, 1, 5, 0, 19, 0, 0, 0, 16, 24, 12, 10, 0, 13, 0, 0, 0, 0, 14, 17, 0, 2, 25, 4],
                            [0, 16, 18, 0, 0, 0, 19, 1, 7, 6, 0, 23, 12, 0, 0, 0, 0, 24, 0, 2, 0, 25, 9, 0, 0],
                            [0, 0, 0, 13, 1, 0, 0, 0, 0, 0, 21, 0, 24, 0, 22, 20, 5, 0, 0, 0, 0, 0, 15, 4, 12],
                            [0, 15, 0, 10, 0, 11, 5, 0, 25, 13, 0, 6, 0, 8, 9, 0, 0, 1, 0, 19, 21, 2, 0, 7, 14],
                            [0, 0, 14, 20, 0, 0, 0, 16, 0, 0, 10, 7, 0, 0, 25, 0, 9, 0, 13, 0, 8, 19, 6, 11, 17],
                            [25, 19, 7, 8, 0, 17, 12, 22, 0, 9, 11, 0, 13, 4, 0, 15, 0, 0, 0, 21, 18, 10, 23, 0, 5],
                            [0, 0, 0, 0, 0, 10, 6, 14, 0, 3, 0, 9, 0, 0, 23, 0, 0, 17, 0, 7, 2, 15, 0, 12, 0],
                            [1, 20, 0, 0, 25, 9, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 13, 0, 15, 5, 14, 0, 22, 17, 7],
                            [15, 13, 23, 14, 0, 0, 0, 19, 12, 0, 0, 1, 0, 24, 0, 0, 21, 9, 3, 8, 0, 0, 0, 16, 0],
                            [4, 0, 0, 7, 17, 0, 0, 0, 0, 0, 13, 14, 5, 0, 0, 6, 0, 16, 22, 11, 0, 0, 3, 8, 0],
                            [18, 8, 22, 9, 0, 0, 16, 11, 17, 0, 0, 25, 0, 7, 4, 0, 0, 0, 14, 20, 23, 0, 0, 0, 0],
                            [0, 0, 0, 2, 19, 24, 17, 21, 0, 4, 0, 0, 0, 0, 12, 0, 25, 3, 0, 0, 0, 0, 1, 18, 6],
                            [0, 0, 0, 12, 0, 20, 11, 13, 19, 22, 0, 0, 3, 23, 0, 0, 0, 15, 6, 0, 25, 0, 0, 14, 0],
                            [11, 14, 0, 0, 0, 12, 0, 0, 0, 0, 18, 0, 0, 25, 0, 2, 19, 0, 20, 23, 0, 0, 4, 15, 8],
                            [3, 0, 0, 15, 20, 0, 0, 25, 18, 5, 0, 13, 4, 0, 0, 14, 16, 0, 17, 0, 12, 7, 0, 0, 0],
                            [0, 0, 0, 0, 0, 15, 0, 0, 0, 8, 1, 0, 0, 0, 0, 0, 4, 0, 24, 0, 13, 0, 0, 20, 19],
                            [0, 9, 0, 0, 5, 22, 0, 6, 15, 0, 4, 10, 0, 13, 0, 11, 17, 8, 0, 0, 1, 0, 0, 23, 0],
                            [21, 0, 0, 3, 6, 0, 13, 0, 0, 0, 0, 0, 15, 9, 1, 0, 0, 14, 5, 0, 4, 0, 12, 0, 20],
                            [0, 11, 15, 1, 8, 16, 0, 0, 9, 14, 0, 5, 0, 12, 0, 0, 0, 0, 0, 10, 0, 17, 25, 19, 0],
                            [24, 2, 0, 0, 0, 7, 0, 0, 4, 0, 0, 0, 0, 0, 8, 13, 0, 25, 18, 0, 0, 0, 5, 3, 15],
                            [0, 18, 25, 0, 7, 8, 1, 17, 5, 0, 6, 11, 21, 0, 0, 0, 0, 12, 23, 0, 0, 0, 0, 0, 24]]

    # Clonar o tabuleiro original para comparação de cores
    original_sudoku = [linha[:] for linha in sudoku_para_resolver]

    inicio = time.time()  # Marca o tempo de início
    init(autoreset=True)
    resolver_sudoku(sudoku_para_resolver, original_sudoku)
    fim = time.time()  # Marca o tempo de fim
    print_time(fim, inicio)
    