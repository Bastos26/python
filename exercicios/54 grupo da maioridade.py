import datetime
ano=datetime.date.today().year
contador=0
contador2=0
for c in range(1,7+1):
    nascimento=int(input('em que ano a {}ª pessoa nasceu : '.format(c)))
    print(ano-nascimento) # é como se após a cada operação ele liberasse espaço para uma nova trinuição
    if ano - nascimento >= 18:
        contador= contador + 1 # ou contador += 1
    else:
        contador2 = contador2 + 1
if contador >=1 and contador2 >=1:
    print('o numero de pessoas que são maiores de idade é {}'.format(contador))
    print('e o numero de pessoas que são menores de idade é {}'.format(contador2))



