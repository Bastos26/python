contador=1
primeiro=int(input('digite o primeiro termo:'))
razão = int(input('digite a razão:'))
termo=primeiro
while contador <= 10:
    contador =contador+1
    print('{} ->'.format(termo),end=' ')
    termo=termo+razão
print('fim')
#esse foi complicado.... primeiro que não precisou da formula,não entendi muito como se resolvia e seu funcionamento
#a não necessidade da formula é que só precisamos mesmo de que houvesse a questão de se acumular laço por laço , para se somar
#por isso do termo=termo+razão