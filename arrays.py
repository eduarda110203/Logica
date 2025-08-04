# Arrays são estruturas de dados que permite guardar varios dados dentro de um aúnic a variável #
notas = [9, 9.5, 10, 9.8]

print(notas)

media = 0 
#loop in python#
for nota in notas:
    media += nota

media /= 4 

print(f'A média é {media}')
 