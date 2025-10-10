dicionario={}
lista=[]
média = 0
mulheres = list()
while True:
    dicionario['nome'] = str(input('Nome:'))
    while True:
        sexo=str(input('sexo: [M/F] ')).upper().strip()
        if sexo == 'M' or sexo  == 'F':
            dicionario['sexo'] = sexo
            break
        else:
            sexo = str(input('Erro! Por Favor,digite apenas M ou F ')).upper().strip()
    dicionario['idade'] =int(input('Idade:'))
    lista.append(dicionario.copy())

    desejo=str(input('deseja continuar ? (S/N)')).upper().strip()
    if desejo == 'N':
        break

#para média
for c in lista:
    média = média+(c['idade'])
média=média/len(lista)

#para mulheres
for c in lista:
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])

print('=-'*30)
print(f'A) Ao todos temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {média} anos')
print(f'C) As mulheres registradas foram {mulheres}',end=' ')
