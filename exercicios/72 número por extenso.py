valor =int(input('digite um valor de 0 a 20'))
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dose', 'trese','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True :
    if valor > 20 :
        print('numero não compatível.')
        valor = int(input('digite um valor de 0 a 20'))
    if valor <= 20:
        break
print(f' você digitou o numero {n[valor]}')
""" versão do guanabara:
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dose', 'trese','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while true :    
    núm=int(input(digite um numero de um a vinte:')
    if 0 <= núm <=20 :
        break
    print('tente novamente.',end=' ')
print('você digitou o numero {cont[núm]}"""
