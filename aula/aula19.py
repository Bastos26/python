pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22 }
print('pessoas')
print(pessoas['nome'])
print(pessoas['idade'])
print(f'0 {pessoas["nome"]} tem {pessoas["idade"]} anos')
#as aspas duplos foram usando porque já estavam dentro de um
#elemento em que se utiliza as aspas simples
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
#o enumerate serve apenas para as tuplas e as listas
# para os dicionarios se utiliza o items que são os valores e os indices
#e fazemos este procedimento que retorna em ordem
del pessoas['sexo']
pessoas['nome'] = 'leandro'
pessoas['peso'] = 98.5

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

