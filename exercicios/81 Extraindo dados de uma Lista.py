lista=[]
cont=0
while True:
    n=int(input('digite um valor:'))
    lista.append(n)
    cont=cont+1
    desejo=str(input('deseja continuar ? (S/N)').upper().strip())
    if desejo == 'N' :
        break
if 5 in lista:
    print('o valor cinco foi adicionado na lista')
else:
    print('o valor 5 NÃO FOI  adicionado na lista...')
print(f'você inseriu {cont} numeros a lista')
print(f'a ordem crescente da lista é {sorted(lista)}')
print(f'a ordem decrescente é {lista.sort(reverse=True)}')