print("\033[1;31;40m olá mundo")
print('\033[0;30;41m olá mundo')
print('\033[4;34;42m olá mundo')
print('\033[7;31;41m olá mundo')
print('\033[0;32;40m olá mundo \033[m')
#print('\033[7;40m olá mundo')#pelo visto o style 7 altera as configurações seguintes
#print('\033[1;40m olá mundo')

a = 5
b = 10
print('podemos colocar as cores em conteúdos específicos , como eu vou fazer agr com \033[31m{}\033[m e o \033[32m{}\033[m'
      ' mas lembre de colocar o código de novo para limitar , se não fica  no restante do conteúdoa '.format(a , b)
      )
      #ou
print('numero {}{}{} e o numero {}{}{}'.format('\033[31m',a,'\033[m','\033[32m',b,'\033[m'))

