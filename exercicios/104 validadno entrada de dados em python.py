def leiaInt(n):
    while True:
        try:
            n = int(n)
            break
        except ValueError:
            n = input('Erro,Tente novamente: ')
    return n


num = input('Digite um número: ')
leiaInt(num)
print(f'Você acabou de digitar o numero {num}')
"""resolução do guanabara
def LeiaInt(msg)
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido. \33[m')
        if ok:
            break
        return valor
        
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')"""