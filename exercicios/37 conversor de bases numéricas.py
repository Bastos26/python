numero = int(input('digite um número inteiro:'))
print('escolha uma das bases para conversão:')
escolha = int(input('[1] para BINÁRIO \n[2] para OCTAL \n[3]para HEXADECIMAL'))
binário = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
if escolha == 1 :
    print(binário[2:])
elif escolha == 2 :
    print(octal[2:])   # os resultados vem com duas letras e numeros representando que são decimal e tals
elif escolha == 3 :    # coom esse [2:] a gente está dizendo que queremos o que vier a seguir dos dois primeiro quadrantes
    print(hexadecimal[2:])# matéria sobre manipulação de texto
