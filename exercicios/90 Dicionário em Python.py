dicionario={}
dicionario['nome'] = str(input('Nome:'))
dicionario['média'] = float(input('Média:'))

if dicionario['média'] > 0 and dicionario['média'] <= 5 :
    dicionario['situação'] = 'reprovado'
if dicionario['média'] > 5 and dicionario['média'] <= 7 :
    dicionario['situação'] = 'recuperação'
if dicionario['média'] > 7 and dicionario['média'] <= 10 :
    dicionario['situação'] = 'aprovado'
else:
    print('erro!!')

print('='*30)
for k,v in dicionario.items():
    print(f'-> {k} é igual á {v}')

"""resolução do guanabra
aluno = dict()
aluno['nome] = str(input('nome:'))
aluno['media'] = float(input('média do aluno{aluno["nome"]}:'))
if aluno['media'] >=7:
    aluno['situação']= ' aprovado'
elif 5 <= aluno['media']"< 7:
    aluno['situação'] = ' recuperação'
else:
    aluno['situação'] = 'reprovado'
print('-='*30)
for k,v in aluno.items():
    print(f'  {k} é igual a {v}')"""


    #nunca esquecer das aspas duplas quando estiver usando aspas simpes