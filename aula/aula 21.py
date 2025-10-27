help(print)
print(print.__doc__)
#manieras de chamar o interactive help e ter acesso as DOCSTRINGS deles
def exemplo():
    """exemplo de docstring que estou criando"""
exemplo()

#exemplo de parâmetros opcionais
def somar(a=0,b=0,c=0):
    s = a+b+c
    print(s)
#o que estou dizenod aqui é que , caso o usuário coloque menos parâmetros do que se tem aqui nos reais,
#a funçºao vai considerar que o valor não posto vai ser 0
#pode ser :somar(1,5),somar(a=4,b=4),pode ser fora de ordem tbm e etc

#exemplo de escopo de variáveis(global e local)
def teste():
    x= 8 # escopo local , só existe dentro da função
    print(f'Na função teste , n vale {n}')
    print(f'Na função teste , x vale {x}')

#programa principal
n = 2 # escopo local , funciona dentro e fora da função
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')
#outro exemplo do qu epode acontecer
def função():
    #global n1 -> com esta palavra reservada , estou dizendo para que n leve mais em consideração aquele escolo global do n1 q esta valendo 2 e transformw o local que vale 4 em global
    n1 = 4
    print(f'n1 dentro vale {n1}')
n1 = 2      #aqui vemos os conceitos de prioridade nos escopos locais e globais,sempre estar atento
print(f'n1 fora vale {n1}')

#retornando valores(return)
def somar (a=0, b=0, c=0):
    s = a + b + c
    return s #o return ele disponibiliza o valor a sair da função , podendo , por exemplo, ser atribuido em alguma variável

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f' Os resultados foram {r1}, {r2}, {r3}')

#exemplos!!!!!!!!!!
def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f = f * c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os fatoraias são {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('é par!')
else:
    print('não é par !')