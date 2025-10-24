import time
import random

def maior(m):
    print('-='*50)
    print('Analisando os valores passados....')
    for c in m:
        time.sleep(0.5)
        print(c,end=' ')
    print(f'Foram informados {len(m)} valores ao todo',end='')
    print()
    print(f'O maior numero é {max(m)}')
    print()

#programa principal
grupos = {
'n6': random.choices(range(1,10),k=6),
'n3' : random.choices(range(1,10), k=3),
'n2' : random.choices(range(1,10), k=2),
'n1' : [random.choice(range(1,10))]
                                        }
maior(grupos['n6'])
maior(grupos['n3'])
maior(grupos['n2'])
maior(grupos['n1'])

"""
resolução do guanabara
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...)
    for valor in num:
        print(f'{valor} ',end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo'.)
    print(f'O maior valor informado foi {maior}.')
    
#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()"""

#falta aqui resolver a questão da identificação do maior numero de cada grupo e resolver o problama que acontece quando chega
#no valor 1 , quanto somente tem um elemento
#já resolvi a questão de gerar os numeros, do timing, e da leitura de quantos elementos tem
#22/10 O programa estava tendo um erro quando analisava o que era apenas um único numero, o for não conseguia pq n era ITERÁVEL