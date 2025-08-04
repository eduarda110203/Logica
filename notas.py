nota = int(input("Digite sua nota: "))

print('')

if nota >= 7:
        print('Aprovado! Parabéns')
elif nota < 5:
          print('Não passou :(..')
else:
          print('Recuperação!')


          #Explicação: no primeiro ele caso é se, a pessoa tiver uma nota maior ou igual a 7 ela está aprovada.
          #ELIF: É a palavra senão, resumida misturando o el e o if.
         # Senão.. se a nota for menor que 5 ela não passou..
         # Senão.. se a nota for 5 ele entra em recuperação.