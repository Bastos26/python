print('{:=^40}'.format('Basto´s Store'))
valor = float(input('digite o valor das compras : R$'))
print('selecioe a forma de pagamento:')
escolha = int(input('[1] a vista(dinheiro/cheque)\n[2] a vista com cartão\n[3] 2 vezes no cartão\n[4] 3 vezes ou mais no cartão'))
if escolha == 1 :
    print('Com essa opção , se consegue {}R$ de desconto.O valor final é {}R$'.format(valor*10/100,valor-(valor*10/100)))
elif escolha == 2 :
    print('Com esta opção , se consegue {}R$ de desconto.O valor final é {}R$'.format(valor*5/100,valor-valor*5/100))
elif escolha ==  3 :
    print('Com essa opção ,se consegue0R$ de desconto e o valor permanece o mesmo')
elif escolha ==4:
    print('Com essa opção , se tem um acrescimo de {}R$ e o valor final fica em {}R$'.format(valor*20/100,valor+valor*20/100))
else:
    print('Opção inválida.Tente novamete , teu merda .Sabe que só tem 4 opções e escolheu uma q n existe pq ?')

#print('''exemplo das três aspas
#exemplo das três aspas     # com três aspas vc pode pular linhas , n precisaria fazer com aquele \n q fiz lá em cima
#exemplo das três aspas''') #n sei se funciona com atribuição de valores em variaveis mas em print funciona