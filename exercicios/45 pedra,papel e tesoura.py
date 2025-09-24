import random
import time
print('game JO KEN PO!')
escolha=int(input('''As opções são:
[1] pedra
[2] papel
[3] tesoura
faça a sua escolha para começarmos : '''))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
a = ('pedra')
b = ('papel')
c = ('tesoura')
lista = [a,b,c]
computador = random.choice(lista)
if escolha == 1 :
 print('Você escolheu pedra e computador escolheu {}'.format(computador))
 if computador == a and computador != b and computador != c :
  print('EMPATE!!')
 elif computador != a and computador == b and computador != c :
  print('VENCE O COMPUTADOR !!')
 elif computador != a and computador != b and computador == c :
  print('VENCE O JOGADOR !! parabens !!')

elif escolha == 2 :
 print('Você escolheu papel e computador escolheu {}'.format(computador))
 if computador != a and computador == b and computador != c :
  print('EMPATE!!')
 elif computador != a and computador != b and computador == c :
  print('VENCE O COMPUTADOR !!')
 elif computador == a and computador != b and computador != c :
  print('VENCE O JOGADOR !! parabens !!')



else:
 print('Você esoclheu tesoura e o computador escolheu {}'.format(computador))
 if computador != a and computador != b and computador == c :
  print('EMPATE!!')
 elif computador != a and computador == b and computador != c :
  print('VENCE O COMPUTADOR !!')
 elif computador == a and computador != b and computador != c :
  print('VENCE O JOGADOR !! parabens !!')
