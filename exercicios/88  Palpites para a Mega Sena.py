import random
listatotal=[]
vezes=int(input('digite o numero de jogos que deseja sortear:'))
for c in range(0,vezes):
    n=sorted(random.sample(range(1 ,61),6))
    listatotal.append(n)
for p in listatotal:
    print(p)
"""resolução do guanabara
from random import radint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('      JOGA NA MEGAS SENA     ')
print('-'*30)
cont = 0
tot = 0
while True:
    num = radint(1,60)
        lista.append(num)
        cont+=1
    if cont >= 6:
        break
lista.sort()
jogos.append(lista[:])
lista.clear
tot +=1
print('-='*3, f'  SORTEADO {quant}  JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' *5 , '< BOA SORTE! >', '-='*5)"""
