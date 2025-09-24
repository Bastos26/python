lanche = ('hamburguer','suco','pizza','pudim')
print(lanche)
print(lanche[1])  # TUPLAS SÃO IMUTÁVEIS EX:LANCHE[]='REFRIGERANTE' <- ISSO TÁ ERRADO
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])#lembre que o python sempre vai ignorar o ultimo elemento
print(lanche[-2:])
print(lanche[:2])
for comida in lanche:
    print(f'eu vou comer {comida}') # ambas funcionam da mesma maneira
print('tava com uma fome de 50 mendingos')
print(len(lanche))
for cont in range(0,len(lanche)):
    print(cont) #aqui vai mostrar os numeros
    print(lanche[cont])# mas aqui vai mostrar o valor é como se estivesse colocando os numeros cada um e fazendo os indices

for cont in range(0,len(lanche)):
    print(f'eu voou comer {comida} na posição {cont}')

for pos,comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')

print(sorted(lanche))#organiza os valores tipo em ordem alfabética

a = (2,5,4)
b = (5,8,1,2)
c = a+b
print(c) # o sinal de mais tem um sentido um pouco diferente , ele vai juntar os valores ou concatenar
print(c.count(5)) # aqui essa propriedade count vai dizer quantas vezes o 5 aparece
print(c.index(8)) # aqui estamos pedindo para identificar em que posição o exemplo está
print(c.index(5,1)) # como tem dois cincos , estou pedindo para verificar a partir da posição 1
#se chama deslocamento

pessoa =('yuri',28,'M',96 ) # no python se pode declarar varios tipos de variaveis em uma variavel composta
del(pessoa)#aqui eu estou meio que cancelando essa variavel, por mais que estja escrito , ela não vai aparecer
# você pode apagar ela toda mas não um determinado elemento

#obs:a função index ajuda a encontrar um elemento especifico em uma tupla , lembrese que deva usar aspas('') para dizer a função qual valor procura
