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