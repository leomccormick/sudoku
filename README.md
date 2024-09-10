# Sudoku Solver com Visualização em Python

Este projeto é um resolvedor de Sudoku desenvolvido em Python, com uma função adicional de visualização do progresso em tempo real. O algoritmo utiliza a técnica de força bruta para resolver quebra-cabeças de Sudoku de tamanhos variados, como 4x4, 9x9 e 16x16.

## Funcionalidades

- Resolução automática de Sudokus de diferentes tamanhos (4x4, 9x9, 16x16, etc.)
- Visualização do processo de resolução com números coloridos: números fixos em azul e tentativas em verde
- Geração automática de tabuleiros válidos para diferentes tamanhos
- Medição do tempo total de resolução do Sudoku

## Como usar

Para usar o resolvedor de Sudoku, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/sudoku-solver.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd sudoku-solver
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o resolvedor de Sudoku:
   ```bash
   python resolvedor_sudoku.py
   ```

Durante a execução, você poderá escolher o tamanho do tabuleiro (por exemplo, 9 para um Sudoku 9x9). O programa então gerará um tabuleiro aleatório e começará a resolver, mostrando o progresso diretamente no terminal.

## Personalização

- **Tempo de Delay**: Você pode ajustar o `tempo_delay` para alterar a velocidade de visualização no terminal.
- **Tamanhos de Tabuleiro**: O programa suporta Sudokus de tamanhos 4x4, 9x9, 16x16, entre outros.

## Estrutura do Projeto

- `resolvedor_sudoku.py`: Contém o código principal para resolver o Sudoku.
- `gerador_sudoku.py`: Funções responsáveis por gerar tabuleiros de Sudoku válidos.
- `README.md`: Este arquivo, explicando o projeto e como usá-lo.
