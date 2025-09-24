lista=[]
while True:
    n=int(input('digite um numero:'))
    if n in lista:
        print('valor duplicato, não vou adicionar...')
    else:
        lista.append(n)
        print('valor adicionado com sucesso')
    desejo=input(('deseja continuar? (S/N)')).upper().strip()
    if desejo == "N":
        break
print(lista)
print(sorted(lista))
"""
resolução do guanabara
numeros=list()
while True:
    n=int(input('digite um valor:))
    if n not in numeros:
        numeros.append(n)
        print('valo adicionado com sucesso...')
    else:
        print('valor duplicado!não irei adicionar ')
    r=str(input('quer continuar? [S/N]')
    if r in 'Nn':
        break
print('=-'*30)
numeros.sort()
print(f'você digitou os valores {numeros}')"""