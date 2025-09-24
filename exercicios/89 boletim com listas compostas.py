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