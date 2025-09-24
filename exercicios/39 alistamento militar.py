'''ano = int(input('digite o ano em que nasceu:'))
idade = 2025 - ano
if idade > 18 :
    print('você tem {} anos , deveria ter se alistado em {} anos atrás'.format(idade,idade-18))
elif idade < 18 :
    print('você tem {} anos , ainda falta {} para se alistar'.format(idade,18-idade))
elif idade == 18 :
    print('você tem {} anos , está na hora de se alistar'.format(idade))
#ver o exercicio 38 para ver o video que ele sugere sobre esses módulos aritméticos
#acima está a maneira q eu fiz , vou colocar a baixo a maneira q o professor fez.'''
from datetime import date
data = date.today().year
ano = int(input('digite o ano de nascimento:'))
idade = data - ano
if idade > 18 :
    print('quem nasceu em {} tem {} em {} ,deveria ter se alistado em {} '.format(ano,idade,data,data-18))
elif idade < 18 :
    print('quem nasceu em {} tem {} em {} , ainda falta {} anos para se alistar'.format(ano,idade,data,18-idade))
else:
    print('quem nasceu em {} tem {} , está na hora de se alistar'.format(ano,idade))