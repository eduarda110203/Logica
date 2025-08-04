tabuleiro = [
    [' ', ' ', ''],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

jogador = 'X'

#função para exibir o tabuleiro
def exibeTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

#função para realizar a jogada
# retorna o jogador O se for ao contrário de X se não retorna X de novo.
    # Este comando faz com que números negativos ex: -1 não funcione
    # se o campo já estiver preenchido ele não deixa colocar naquele campo
    # Validando as jogadas e organizando a ordem dos jogadores.
def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != ' '
    ):
        print('jogada inválida!')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

#define o ganhador
def temGanhador():
   """ Verifica as linhas """
   if (
      tabuleiro [0][0] == tabuleiro [0][1] and
      tabuleiro [0][0] == tabuleiro [0][2]
   ):
    return True

# looping
while True: 
  print(f'Jogador da vez: {jogador}')
  try:
    linha = int(input('Digite a linha: '))  
    coluna = int(input('Digite a coluna: '))
    jogador = jogada(linha, coluna)

# Aqui ele retorna o erro de ValueError de outra forma, fazendo comq que a pessoa coloque números em vez de palavras.(ValueError é erro de valor, como se a pessoa escreveu "ifhwoiheo" em vez de os números corretos)(IndexError, quando a pessoa escreveu um número que não tem com por ex: 5)    
  except (ValueError, IndexError):
    print('Digite valores numéricos entre 0 e 2')
  if temGanhador():
     break
  exibeTabuleiro()
