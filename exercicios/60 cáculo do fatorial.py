'''n=0
fatorial=int(input('escreva o numero em que deseja saber o fatorial:'))
n2=1
while n < fatorial:
    n=n+1             #obs:o fator nulo de soma é 0 e o fator nulo de multiplicação é 1
for c in range(n,0,-1):#por isso que o n2 tem q ser com 1 e o n é com 0
    n2=n2*c
    print('Calculando {}!={}x={}'.format(fatorial,c,n2),end=' ')
#do professor n1
from math import factorial
n=int(input('digite o numero em que deseja se saber o fatorial:'))
f = factorial(n)
print(f)'''
# do professor n2
n=int(input('digite o numero em que deseja se saber o fatorial:'))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c),end='')
    print( ' x 'if c > 1 else ' = ',end='')
    f = f*c
    c -=1  # a maneira da aula para fazer a contagem regressiva
print(f)