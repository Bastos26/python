import random
import time

def sorteio(num):
    num = random.choices(range(0, 9),k=5)
    print('Sorteando 5 valores da lista:')
    for c in num:
        print(c,end=' ')
        time.sleep(0.3)
    print('Pronto!!')
    lista.append(num)
def SomaPar(num):
    total = 0
    for c in num:
        for valor in c :
            if valor % 2 ==0:
                total = total + valor
    print(f'Somando os valores pares de {num} ,temos {total}')

#programa principal
lista=[]
sorteio(lista)
SomaPar(lista)
"""resolução do guanabara
 from random import randint
 from time import sleep
 
 def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end'',flush=True)
        sleep(0.3)
    print('Pronto!')
    
defsomaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+= valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
    
números = list()
sorteia(números)
somaPar(números()"""



