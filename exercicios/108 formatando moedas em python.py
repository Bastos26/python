from modulos import mod108

valor = float(input('Digite o preço: R$'))
mod108.metade(valor)
mod108.dobro(valor)
mod108.porcentagem(valor)

"""resolução do guanabara
from ex108 import moeda
p = float('Digite o preço: R$')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')"""