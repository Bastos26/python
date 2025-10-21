import time
def contador(i, f, p):
    if i < f:
        print('~~'*15)
        for c in range(i, f+1, p):
            time.sleep(0.5)
            print(c, end=' ')
        print()
    if i > f:
        for c in range(i, f-1, -p):
            time.sleep(0.5)
            print(c,end=' ')
        print()
    print('~~' * 15)


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
"""resolução do guanabara
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} de {p}')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        
#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Início : '))
fim =int(input('Fim : '))
pas = int(input('Passo : '))
contador(ini, fim, pas)"""