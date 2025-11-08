def ajuda(assunto):
    help(assunto)


#programa principal
while True:
    ajuda = str(input('SISTEMA DE AJUDA PyHelp: '))
    help(ajuda)
    if ajuda == '0':
        break

"""resolução do guanabara
from time import sleep
c = ('\033[m'          # 0 - sem cores
     '\033[0;30;41n',  # 1 - vermelho
     '\033[0;30;42n',  # 2 - verde
     '\033[0;30;43n',  # 3 - amarelo
     '\033[o;30;44n',  # 4 - azul
     '\033[0;30;45n',  # 5 - roxo
     '\033[7;30n'      # 6 - branco
    ):
    
def ajuda(com):
    título(f' Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)
    
def título(msg,cor=0):
    tan = len(msg) + 4
    print(c[cor], end='')
    print('~' * tan)
    print(f' {msg}')
    print('~' * tan)
    print(c[0], end='')
    sleep(1)
    
#programa principal
comando = ''
while True:
    título ( 'Sistema de ajuda PyHelp', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)"""

# é possível você utilizar um comando junto a outro