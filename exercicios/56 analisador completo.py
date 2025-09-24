acumulador=0
velho=0
nomevelho=''
mulher=0
for p in range(1,5):
    print(p,'ª PESSOA')
    nome=str(input('nome:'))
    idade=int(input('idade:'))
    sexo=str(input('sexo[M/F]:')).strip().upper()

#NOME E IDADE DA PESSOA MAIS VELHA
    if p == 1 :
        velho=idade
        nomevelho=nome
    if idade>velho:
        velho=idade
        nomevelho=nome

#MULHERES MENORES DE 20 ANOS
    if sexo == 'F'and idade < 20:
        mulher+=1


#MEDIA
acumulador+=idade
media=acumulador/4


print('a media de anos é de ',media)
print('o mais velho tem {} anos e o seu nome é {}'.format(velho,nomevelho))
print('e existe {}  mulheres com menos de 20 anos '.format(mulher))
