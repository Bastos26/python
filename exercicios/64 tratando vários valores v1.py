n=int(input('digite um numero[999 para parar]:'))
inicio=n
resposta=0
contador=1
while n!= 999:
    n=int(input('digite um numer0[999 para parar]:'))
    resposta=resposta+n
    contador=contador+1
contagem=contador-1
soma = resposta - 999+inicio
print('você digitou {} vezes e a soma dos numeros é {}'.format(contagem,soma))


'''numeros = []  # Lista vazia para armazenar os números

while True:
    n = int(input("Digite um número (999 para parar): ")) #aqui ele fala sobre listas 
    if n == 999:                                          #a cada valor que se vai atribuindo em cada repetição, vai se introduzindo no laço
        break
    numeros.append(n)  # Adiciona o número à lista

soma = sum(numeros)
print(f"A soma dos números é {soma}")
🧠 Funções Built-in (embutidas)
Elas fazem parte da biblioteca padrão do Python e estão sempre disponíveis, sem precisar importar nada
'''
