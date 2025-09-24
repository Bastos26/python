frase = str(input('digite uma frase:'))
palavra=frase.split()
junto=''.join(palavra)
invertida=junto[::-1]#maneira para inverter a order dos caracteres em uma string
if frase==invertida:
    print('a frase {}  é um Políndromo'.format(invertida))
else:
    print('a frase {} não é um Políndromo'.format(invertida))