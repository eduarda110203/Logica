print('Olá, eu sou a sua assistente, pythrina. O que você quer fazer hoje?')

comando = input('Digite um comando: ')

match comando:
    case 'oi' | 'olá':
        print('Oi, como vai você?')
    case 'tchau' | 'sair' | 'exit': 
        print('Tchau, foi bom conversar com você!')
    case 'piada' | 'conte uma piada': 
        print('Sabe qual é o padroeiro das pessoas que trabalham com T.I? O São Login')
    case 'clima' | 'previsão do tempo': 
        print('Tá muuuuuito quente!! Deve ter passado de 40°C')
    case _:
        print('Desculpe, não entendi :/')             