indice = []
def calcular_imc(p,a):
    imc = p/(a*a)
    print(f'Com o peso sendo {p} e a altura sendo {a} o indice de massa corporal é de {imc}')
    indice.append(imc)
def classificar_imc():
    if indice[0] < 18.5:
        print('Abaixo do peso')
    if 18.5 > indice[0] < 24.9:
        print('Peso normal')
    if 25 > indice[0] < 29.9:
        print('Sobrepeso')
    else:
        print('Obesidade')



peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
calcular_imc(peso,altura)
classificar_imc()

