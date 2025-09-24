maior=0
menor=0
for c in range(1,6):
   peso=float(input('digite o peso da {}ª pessoa:'.format(c)))
   if c ==1:  # obs:o 1 se refere a "primeira contagem desse laço de repetição
       maior=peso  #aqui ele atribuiu uma referência , um ponto de partida para compararmos as outras repetições
       menor=peso  # eu atribui duas variáveis com o mesmo valor , que é os dados numero 1 digitado e salvei
                  #pelo o que vi até agora , não consigo salvar todos os dados dentro dos laços de repetição,mas a primeira dá
   else:
    if peso>maior:
        maior=peso #então aqui ele faz a contagem , se o peso das demais linhas do laço da repetição(2,3,4,5 e etc)
    if peso < menor: #for maior do que o peso anterior que estabelecemos com a linha 1 ,ele SUBISTITUI pelo o valor do peso novo
        menor=peso #e se o peso for menor do que estabelecemos com o valor da linha 1 , ele SUBISTITUI pelo novo valor
                  #então com esses ultimos IFs eu não fui contando ,fiz com que reatribuice o valor da variavel caso fosse maior e menor com o valor do que já tinha atribuido
print('o maior peso é a pessoa com {}KG e o menor peso é da pessoa com {}KG'.format(maior,menor))
 # essa eu estava tendo dificuldade por que não sabia como fazer a contagem , não sabia como pegar o valor de cada linha para comparar
 #uma com a outra ou em como salvar cada valor digitado