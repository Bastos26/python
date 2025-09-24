print('=-'*50)
print(' '*20,'BASTOS´STORE',' '*20)
print('=-'*50)
#dados iniciais
primeiro_produto=str(input('digite o nome do produto:'))
primeiro_preço=int(input('digite o preço:R$'))
repetir = str(input('deseja continuar?(S/N)')).strip().upper()
#atribuições
final=contador=valor=0
menor_preço=primeiro_preço # pelo visto duas variaveis podem ter o msm valor
menor_produto=primeiro_produto
inicio=menor_preço
#estrutura do laço de repetição
while True:
    produto=str(input('digite o nome do produto:'))
    preço=int(input('digite o preço:R$'))
    repetir=str(input('deseja continuar?(S/N)')).strip().upper()
#soma dos valores
    valor=valor+preço
    final=inicio+valor
#contador de quantos itens custam mais de mil reais
    if preço > 1000:
        contador=contador+1
#menor preço e qual produto é o mais barato
    if preço < menor_preço:
        menor_preço = preço
        menor_produto=produto
    if repetir !='S':
        break
print('=-'*20,'FIM DAS COMPRAS','=-'*20)
print(f'o total de compras foi de {final}R$')
print(f'temos {contador} produtos de valem mais de 1000 reais')
print(f'e o produto mais barato foi {menor_produto} que costou {menor_preço}R$')
#tive problema com a soma dos valores e de identificar o menor dos preços , estava dando certo