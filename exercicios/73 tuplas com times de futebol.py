time='corinthians','palmeiras','santos','grêmio','cruzeiro','flamengo','vasco da gama','chapecoense','atlético-MG','botafogo','athletico-PR','bahia','são paulo','fluminense','sport recife','ec vitória','coritiba','avaí','ponte preta','atlético-GO'
Chapecoense=time.index('chapecoense')+1
print('=-'*70)
print(f'Ao todo foram {len(time)} times que participaram')
print('=-'*70)
print(f'Os 5 primeiros colocados foram :{time[:6]}')
print('=-'*70)
print(f'Os 4 últimos foram :{time[16:]}')
print('=-'*70)
print(f'o time da Chapecoense ficou na posição numero {Chapecoense} na tabela')
print('=-'*70)
print(f'Os times em ordem alfabética são :{sorted(time)}')


""" resolução do guanabara:
times = ('corinthians','palmeiras','santos','grêmio','
        cruzeiro','flamengo','vasco da gama','chapecoense',
        'atlético-MG','botafogo','athletico-PR','bahia',
        'são paulo','fluminense','sport recife','ec vitória',
        'coritiba','avaí','ponte preta','atlético-GO')
print('-='*15)
print(f'lista de times {times}
print('-='*15)
print(f'o 5 primeiros times são {times[:5]}
print('-='*15)
print(f'os 4 ultimos são : {times[-4:]} -> quando coloca o traço(-) como se fosse um numero negativo, ele lê de trás para frente
print('-='*15)
print(f'times em ordem alfabética: {sorted(times)}) -> a tupla é imutável , o sorted não altera a tupla ele só nos mostra (retorna ) em uma ordem
print('-='*15)
print(f' o chapecoense está em {times.index('chapecoense')+1} posição:')




obs:for t in times : -> para cada time(t) em times, em outras palavras ele está se referindo a cada valor dentro da unidade composta
    print(t) -> ele vai retornar em forma de lista , um em cima do outro"""
