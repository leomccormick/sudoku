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
        print(f"Tempo decorrido: {tempo_total//60:.0f}min {tempo_total-tempo_total//60*60:.2f}s")
    elif tempo_total > 1:
        print(f"Tempo decorrido: {tempo_total:.2f} s")
    else:
        print(f"Tempo decorrido: {tempo_total:.4f} s")

while True:
    size = input("Digite o tamanho do Sudoku (como 9 para 9x9): ")
    if not size.isdigit():
        break
    if int(size) not in [1, 4, 9, 16, 25, 36]:
        print("Por favor, digite um tamanho válido (como 9 para 9x9 ou 16 para 16x16).")
        continue

    sudoku_para_resolver = generate_sudoku(int(size))

    # Clonar o tabuleiro original para comparação de cores
    original_sudoku = [linha[:] for linha in sudoku_para_resolver]

    inicio = time.time()  # Marca o tempo de início
    init(autoreset=True)
    resolver_sudoku(sudoku_para_resolver, original_sudoku)
    fim = time.time()  # Marca o tempo de fim
    print_time(fim, inicio)
    