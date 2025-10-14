lista=[]
totlist=[]
while True:
    lista.append(str(input('nome:')))
    lista.append(float(input('nota1 :')))
    lista.append(float(input('nota2 :')))
    totlist.append(lista[:])
    lista.clear()
    desejo=str(input('deseja continuar? (S/N)')).upper().strip()
    if desejo == 'N':
        break
for c in totlist:
    print(c, c[0] , (c[1]+c[2])/2)

while True:
    notas=int(input('deseja ver a notas de aqual aluno? (digite 999 para anular)'))
    if notas == 999:
        break
    elif notas > 0 and notas < len(totlist):
        print(totlist[notas])
    else:
        print('erro,tente novamente')
"""resolução do guanbara
ficha = list()
while True:
    nome = str(input('Nome:')
    nota1 = float(input('Nota1:')
    nota2 = float(input('Nota2:')
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') 
print('-'*26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
        opc = int(input('Mostrar notas de qual aluno ? (999 interrompe): ')
        if opc == 999:
            print('Finalizando...')
            break
        if opc <= len(ficha) -1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTESEMPRE >>>')        
"""
#O enumerate() é uma função embutida que permite iterar sobre uma lista
# (ou outro iterável) retornando o índice e o valor de cada item ao mesmo tempo.