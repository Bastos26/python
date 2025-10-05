pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22 }
print('pessoas')
print(pessoas['nome'])
print(pessoas['idade'])
print(f'0 {pessoas["nome"]} tem {pessoas["idade"]} anos')
#as aspas duplos foram usando porque já estavam dentro de um
#elemento em que se utiliza as aspas simples
print(pessoas.keys())# keys são referênte aos índices
print(pessoas.values())#values são referênte aos valores
print(pessoas.items())#items são referêntes aos items(indice e o valor)
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
pessoas['nome'] = 'leandro' #dicionarios são mutaveis igual listas
pessoas['peso'] = 98.5 # pode-se adicionar indices personalizados e seus valores quando necessário

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2) # lista com dicionarios
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado)#há um problema pq iria aparecer somente
                        #o último valor e não os outros valores
    brasil.append(estado[:])#o dicionário não se pode fazer fatiamento
                            #aqui já daria erro mesmo
    brasil.append(estado.copy())#este é um método interno do dicionário
                                #para fazermos a copia
    print(brasil)
    for e in brasil:#aqui é da camada da lista onde está o dicionário
        for k, v in e.items():#aqui é o equivalente ao enumerate
            print(f'O campo{k} tem o valor {v}.')
