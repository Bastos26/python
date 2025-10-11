dicionario={}
lista=[]
media = 0
acima = []
while True:
    dicionario['nome'] = str(input('Nome:'))
    while True:
        sexo=str(input('sexo: [M/F] ')).upper().strip()
        if sexo == 'M' or sexo  == 'F':
            dicionario['sexo'] = sexo
            break
        else:
            sexo = str(input('Erro! Por Favor,digite apenas M ou F ')).upper().strip()
            break
    dicionario['idade'] =int(input('Idade:'))
    lista.append(dicionario.copy())

    desejo=str(input('deseja continuar ? (S/N)')).upper().strip()
    if desejo == 'N':
        break

#para média
for c in lista:
    media = media+(c['idade'])
media=media/len(lista)

print('=-'*30)
print(f'A) Ao todos temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {media} anos')

#para mulheres
print(f'C) As mulheres registradas foram ',end='')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'])

#para idades acima da média
print('D) Lista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] > media:
        print(f'Nome = {c["nome"]} ; Sexo = {c["sexo"]} ; Idade = {c["idade"]}; ')

"""resolução do guanabara
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [S/N'] ')).upper()[0]
        if pessoa['sexo'] in 'MF'
            break
        print('ERRO! Por Favor, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper[0]
        if resp in 'SN':
            break
         print('ERRO! Responda apenas com S ou N.')
        if resp == 'N':
            break
print'-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ' end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
    for p in galera:
    if p['idade] >= média:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')"""