import time
from colorama import Fore, Style, init
import numpy as np
from gerador_sudoku import generate_sudoku

# Função para imprimir o tabuleiro com cores e substituir 0 por '.'
def imprimir_sudoku(sudoku, original_sudoku):
    # Limpar o terminal (opcional para visualização mais limpa)
    print("\033[H\033[J", end="")
    
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                print(".", end=" ")  # Substitui '0' por '.'
            elif original_sudoku[i][j] != 0:  # Se o número já estava no tabuleiro original
                print("\033[94m" + str(sudoku[i][j]) + Style.RESET_ALL, end=" ")
            else:
                print(Fore.GREEN + str(sudoku[i][j]) + Style.RESET_ALL, end=" ")
        print()  # Quebra de linha entre as linhas do sudoku
    print("\n")

# Função para encontrar a célula com o menor número de opções (MRV - Minimum Remaining Values)
def encontrar_melhor_celula(sudoku):
    tamanho = len(sudoku)
    melhor_celula = None
    menor_opcoes = tamanho + 1  # Número impossível de ocorrer
    for i in range(tamanho):
        for j in range(tamanho):
            if sudoku[i][j] == 0:
                opcoes = [num for num in range(1, tamanho + 1) if checar_valido(sudoku, num, i, j)]
                if len(opcoes) < menor_opcoes:
                    menor_opcoes = len(opcoes)
                    melhor_celula = (i, j)
    return melhor_celula

# Função para resolver o Sudoku com backtracking otimizado
def resolver_sudoku(sudoku, original_sudoku, tempo_delay=0):
    vazio = encontrar_melhor_celula(sudoku)  # Usar MRV para escolher a melhor célula
    tamanho = len(sudoku)
    if not vazio:
        return True  # Sudoku resolvido
    else:
        linha, coluna = vazio

    for num in range(1, tamanho + 1):
        if checar_valido(sudoku, num, linha, coluna):
            sudoku[linha][coluna] = num
            
            # Imprimir o estado atual do Sudoku
            imprimir_sudoku(sudoku, original_sudoku)
            time.sleep(tempo_delay)  # Delay para visualização

            if resolver_sudoku(sudoku, original_sudoku, tempo_delay):
                return True

            sudoku[linha][coluna] = 0  # Resetar se o número não funcionar
            # Mostrar o reset
            imprimir_sudoku(sudoku, original_sudoku)
            time.sleep(tempo_delay)

    return False

# Função para checar se o número é válido na posição
def checar_valido(sudoku, num, linha, coluna):
    tamanho = len(sudoku)  # Obtemos o tamanho do tabuleiro
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

# Função para imprimir o tempo de execução
def print_time(fim, inicio):
    print(f"Tempo decorrido: {fim - inicio:.4f} segundos")


# Finalização do programa
while True:
    size = input("Digite o tamanho do Sudoku (como 9 para 9x9): ")
    if not size.isdigit():
        break
    if int(size) not in [1, 4, 9, 16, 25, 36]:
        print("Por favor, digite um tamanho válido (como 9 para 9x9 ou 16 para 16x16).")
        continue

    sudoku_para_resolver = generate_sudoku(int(size))
    # sudoku_para_resolver = [[6, 3, 0, 25, 15, 0, 0, 9, 1, 2, 7, 0, 0, 17, 0, 5, 0, 13, 0, 22, 11, 12, 14, 21, 0],
                            # [12, 0, 0, 0, 14, 25, 7, 5, 0, 11, 0, 3, 0, 0, 2, 0, 8, 21, 4, 0, 24, 0, 13, 0, 0],
                            # [0, 0, 0, 24, 16, 0, 0, 0, 0, 12, 0, 0, 25, 18, 0, 0, 2, 0, 0, 0, 15, 0, 0, 22, 0],
                            # [2, 22, 0, 0, 18, 0, 0, 4, 0, 17, 9, 0, 14, 11, 15, 12, 6, 0, 0, 16, 0, 20, 19, 0, 0],
                            # [20, 0, 1, 5, 0, 19, 0, 0, 0, 16, 24, 12, 10, 0, 13, 0, 0, 0, 0, 14, 17, 0, 2, 25, 4],
                            # [0, 16, 18, 0, 0, 0, 19, 1, 7, 6, 0, 23, 12, 0, 0, 0, 0, 24, 0, 2, 0, 25, 9, 0, 0],
                            # [0, 0, 0, 13, 1, 0, 0, 0, 0, 0, 21, 0, 24, 0, 22, 20, 5, 0, 0, 0, 0, 0, 15, 4, 12],
                            # [0, 15, 0, 10, 0, 11, 5, 0, 25, 13, 0, 6, 0, 8, 9, 0, 0, 1, 0, 19, 21, 2, 0, 7, 14],
                            # [0, 0, 14, 20, 0, 0, 0, 16, 0, 0, 10, 7, 0, 0, 25, 0, 9, 0, 13, 0, 8, 19, 6, 11, 17],
                            # [25, 19, 7, 8, 0, 17, 12, 22, 0, 9, 11, 0, 13, 4, 0, 15, 0, 0, 0, 21, 18, 10, 23, 0, 5],
                            # [0, 0, 0, 0, 0, 10, 6, 14, 0, 3, 0, 9, 0, 0, 23, 0, 0, 17, 0, 7, 2, 15, 0, 12, 0],
                            # [1, 20, 0, 0, 25, 9, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 13, 0, 15, 5, 14, 0, 22, 17, 7],
                            # [15, 13, 23, 14, 0, 0, 0, 19, 12, 0, 0, 1, 0, 24, 0, 0, 21, 9, 3, 8, 0, 0, 0, 16, 0],
                            # [4, 0, 0, 7, 17, 0, 0, 0, 0, 0, 13, 14, 5, 0, 0, 6, 0, 16, 22, 11, 0, 0, 3, 8, 0],
                            # [18, 8, 22, 9, 0, 0, 16, 11, 17, 0, 0, 25, 0, 7, 4, 0, 0, 0, 14, 20, 23, 0, 0, 0, 0],
                            # [0, 0, 0, 2, 19, 24, 17, 21, 0, 4, 0, 0, 0, 0, 12, 0, 25, 3, 0, 0, 0, 0, 1, 18, 6],
                            # [0, 0, 0, 12, 0, 20, 11, 13, 19, 22, 0, 0, 3, 23, 0, 0, 0, 15, 6, 0, 25, 0, 0, 14, 0],
                            # [11, 14, 0, 0, 0, 12, 0, 0, 0, 0, 18, 0, 0, 25, 0, 2, 19, 0, 20, 23, 0, 0, 4, 15, 8],
                            # [3, 0, 0, 15, 20, 0, 0, 25, 18, 5, 0, 13, 4, 0, 0, 14, 16, 0, 17, 0, 12, 7, 0, 0, 0],
                            # [0, 0, 0, 0, 0, 15, 0, 0, 0, 8, 1, 0, 0, 0, 0, 0, 4, 0, 24, 0, 13, 0, 0, 20, 19],
                            # [0, 9, 0, 0, 5, 22, 0, 6, 15, 0, 4, 10, 0, 13, 0, 11, 17, 8, 0, 0, 1, 0, 0, 23, 0],
                            # [21, 0, 0, 3, 6, 0, 13, 0, 0, 0, 0, 0, 15, 9, 1, 0, 0, 14, 5, 0, 4, 0, 12, 0, 20],
                            # [0, 11, 15, 1, 8, 16, 0, 0, 9, 14, 0, 5, 0, 12, 0, 0, 0, 0, 0, 10, 0, 17, 25, 19, 0],
                            # [24, 2, 0, 0, 0, 7, 0, 0, 4, 0, 0, 0, 0, 0, 8, 13, 0, 25, 18, 0, 0, 0, 5, 3, 15],
                            # [0, 18, 25, 0, 7, 8, 1, 17, 5, 0, 6, 11, 21, 0, 0, 0, 0, 12, 23, 0, 0, 0, 0, 0, 24]]

    # Clonar o tabuleiro original para comparação de cores
    original_sudoku = [linha[:] for linha in sudoku_para_resolver]

    inicio = time.time()  # Marca o tempo de início
    init(autoreset=True)
    resolver_sudoku(sudoku_para_resolver, original_sudoku)
    fim = time.time()  # Marca o tempo de fim
    print_time(fim, inicio)
