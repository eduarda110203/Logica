# f(x) = y 
# f(x,y,z) = 2x
# f(2) = 4
# f(5) = 10

def olaMundo():
    print('Olá, mundo!')

def olaPessoa(nome):
    print(f'Olá, {nome}!')

def dobro(n):
    return n * 2

def multiplicaDoisNumeros(a, b = 2): 
    """
    se b não tiver nada ele multiplica por 2"""
    return a * b

print(multiplicaDoisNumeros(3, 6))
print(multiplicaDoisNumeros(3))
"""Aqui é o seguinte, no default acima ele multiplica 3X6 = 18 e depois no valor 'b' ele multiplica pelo número 2 pois não informei nenhum número para multiplicar."""

x = 5 # Variável global
def soma():
    X = 10 # Variável local
    print(x)
    return x + 1
soma()
print(x)
