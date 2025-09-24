print('vamos ver se o seu empréstimo vai ser permitido')
valor = float(input('digite o valor da casa:'))
salário = float(input('digite seu salário mensal:'))
ano = float(input('digite os anos em que pretende quitar a casa:'))
tempo=ano*12
prestação=valor/tempo
print('para pegar uma casa de {} em {} anos , é necessário pagar um empréstimo de {:.2f}'.format(valor,ano,prestação))
if prestação> salário*30/100:
    print('emprétismo negado')
else:
    print('empréstimo autorizado')
