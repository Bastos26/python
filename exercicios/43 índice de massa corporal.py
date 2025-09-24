print('programa para calcular IMC(índice de massa corpórea)')
peso = int(input('digite seu peso:(kg)'))
altura = float(input('digite sua altura:(m)'))
imc = peso / ( altura**2)
if imc < 18.5 :
    print('O seu imc é de {:.2f} e você está ABAIXO DO PESO'.format(imc))
elif imc > 18.5 and imc < 25 :# ou elif 18.5<= imc < 25: tambem é aceitável
    print('O seu imc é de {:.2f} e você está com o PESO IDEAL'.format(imc))
elif imc > 25 and imc < 30 :
    print('o seu imc é de {:.2f} e você está SOBREPESO'.format(imc))
elif imc > 30 and imc < 40 :
    print('o seu imc é de {:.2f} e você está com OBESIDADE'.format(imc))
else:
    print('o seu imc é de {:.2f} e você está com OBESIDADE MÓRBIDA'.format(imc))
