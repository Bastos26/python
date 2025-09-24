'''import random
print('sou seu computador....')
print('acabei de pesar em um numero de 1 a 10')

n1=0
n2=random.randint(1,10)
contador=0
while n2!=n1: #pensa assim ,ele pergunta em cada loop se o n2 é diferente de n1 , a cada "sim" ele continua, entende ?
    n1=int(input('adivinha em que umero eu estou pensando'))
    contador=contador+1

    if n1<n2:
        print('mais...de novo')
    elif n1>n2:
        print('menos... de novo')
print('parabéns, você adivinhou depois de tentar {} vezes'.format(contador))'''
#código do professor

from random import randint
computador = randint(0,10)
print('sou o seu computador ... acabei de pensar em um número')
acertou = False
palpites = 0
while not acertou :
    jogador = int(input('qual é seu palpite?'))
    palpites += 1
    if jogador== computador:
        acertou = True
    else:
        if jogador < computador:
            print(' mais ....tente mais uma vez')
        elif jogador > computador:
            print('menos...tente mais uma vez')
        print('acertou com {} tentativas . Parabéns'.format(palpites))