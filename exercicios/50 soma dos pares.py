acumulador = 0
contador = 0
for n in range(0,6):
    n1 = int(input('Digite o {} numero:'.format(n)))
    if n1 % 2==0:
        acumulador += n1
        contador = contador + 1
print('você informou {} numeros pares e a soma dos numeros pares é {}'.format(contador,acumulador))



