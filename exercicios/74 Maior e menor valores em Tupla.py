import random
tupla=(random.sample(range(1, 9),5))
print(f'os valores sorteados foram {tupla}')
for c in tupla:
    maior = menor = tupla[0]
    if menor > c:
       menor = c
    if c > maior:
       maior = c
print(f'o maior numero da tupla é {maior}')
print(f'o menor valor da tupla é {menor}')

"""resolução do guanabara
from random import radint
numeros = (radint(1, 10),(radint(1, 10),(radint(1, 10),
            (radint(1, 10),(radint(1, 10),
print('os valores sorteador foram: ',end='')
for n in numeros:
    print(f'{n} ',end='')
print(f'\no maior valor sorteado foi {max(numeros)}')
print(f'o menor valor sorteado foi {min(numeros)}'))"""
#max e min são métodos das tuplas , deixa tudo mais facil e não precisa fazer o que se faz normalmente de definir valores e ir comparando