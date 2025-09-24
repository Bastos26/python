contador=masculino=feminino=0
while True:
    idade = int(input('digite a idade da pessoa:'))
    sexo = str(input('digite o sexo da pessoa:(M/F')).strip().upper()
    if idade > 18 :
        contador=contador+1
    if sexo == 'M':
        masculino=masculino+1
    if sexo == 'F' and idade < 20 :
        feminino=feminino+1
    laço=str(input('deseja continuar?(S/N)')).strip().upper()
    if laço != 'S':
        break
print(f'existe {contador} pessoas maiores de 18 anos')
print(f'existe o total de {masculino} homens')
print(f'e existe {feminino} mulheres com menos de 20 anos')