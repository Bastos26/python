contador=1
n = int(input('digite um numero:'))
desejo = str(input('deseja continuar?(S/N)')).upper().strip()
maior=menor=soma=n
while desejo!= 'N':
    n = int(input('digite um numero:'))
    desejo = str(input('deseja continuar?(S/N)')).upper()
    soma = soma + n
    contador = contador + 1
    if n >= maior:
        maior=n
    elif n<= menor:
        menor=n
media = soma / contador
print('você digitou {} numeros, a media é {}, o maior é {} e o menor é {}'.format(contador,media,maior,menor))