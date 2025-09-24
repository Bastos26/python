from datetime import date
nascimento = int(input('digite o ano de nascimento:'))
ano = date.today().year
idade = ano - nascimento
if idade <= 9 :
    print('quem nasceu em {} tem {} anos e sua categoria é MIRIM'.format(nascimento,idade))
elif idade <= 14 :
    print('quem nasceu em {} tem {} anos e sua categoria é INFANTIL'.format(nascimento,idade))
elif idade <= 19 :
    print('quem nasceu em {} tem {} anos e sua categoria é JÚNIOR'.format(nascimento,idade))
elif idade <=  25 :
    print('quem nasceu em {} tem {} anos e sua categpria é SÊNIOR'.format(nascimento,idade))
else:
    print('quem nasceu em {} tem {} anos e sua categoria é MASTER'.format(nascimento,idade))