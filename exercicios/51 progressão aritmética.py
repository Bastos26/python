print(50*'=')
print('              10 TERMOS DE UMA PA')
print(50*'=')
pt=int(input('digite o primeiro termo:'))
razão=int(input('digite a razão:'))
décimo=(pt+(10-1)*razão)
for c in range(pt,décimo+razão,razão):
    print(c, '=>', end=' ')
print('acabou')
#ESSE FOI COMPLICADO