from traceback import print_tb

n1 = int(input('digite um numero:'))
n2 = int(input('digite o segundo numero:'))
if n1 < n2 :
    print('o segundo número é o maior')
elif n2 < n1 :
    print('o primeiro número é o maior')
elif n2 == n1 :
    print( 'ambos os números são iguais')