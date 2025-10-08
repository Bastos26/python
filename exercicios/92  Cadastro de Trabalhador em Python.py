import datetime
registro={}
ano_atual=(datetime.date.today().year)
while True:
    registro['nome'] = str(input('Nome:'))
    registro['idade'] = int(input('Ano de Nascimento:'))
    registro['idade'] = ano_atual - registro['idade']
    registro['ctps'] = int(input('Carteira de Trabalho(0 caso não tenha):'))
    if registro['ctps'] <= 0 :
        break
    else:
        registro['contratação'] = int(input('Ano da Contratação:'))
        registro['salario'] = float(input('Salário:'))
        registro['aposentadoria']= 70 - registro['idade']
        break
for k,v in registro.items():
    print(f' - {k} tem o valor {v}')
"""resolução do guanabara
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho( 0 não tem ): '))
if dados['ctps'] != 0 :
    dados['contratação'] = int(input('Ano de Contratação :'))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now()year)
print('-='*30)
for k,v in dados.items():
    print(f'  -{k} tem o valor {v}')"""
