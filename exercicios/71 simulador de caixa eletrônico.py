#minha resposta
'''print('='*50)
print('BASTOS´BANK'.center(20))
print('='*50)

n50=n20=n10=n1=0
valor=int(input('digite o valor com o qual se deseja sacar:'))
n50=valor//50
restante=valor%50
while True:
    if restante >=1:
        n20=restante//20
        restante=restante%20
    if restante >=1:
        n10=restante//10
        restante=restante%10
    if restante >=1:
        n1=restante//1
        restante=restante%1
    else:
        break
print('='*30)
print(f'o total de cedulas de 50 é de {n50}')
print(f'o total de cedulas de 20 é de {n20}')
print(f'o totoal de cedulas de 10 é de {n10}')
print(f'o total de cedulas de 1 é de {n1}')
print('='*30)
print('VOLTE SEMPRE')'''
#a arquitetura da resposta do professor
valor=int(input(':'))
total=valor
cedula=50
total_cedula=0
while True:
    if total>=cedula:
        total=total-cedula   #ou total-=cedula  #aqui ele monta o laço para se acontecer , ir subtraindo o maximom possivel com cada nota
        total_cedula=total_cedula+1
    else:
        print(f'o total de {total_cedula} cedulas é de {cedula} reais')
        if cedula == 50:
            cedula = 20      # mas ai a pergunta que ficava era de como ele faria para alterar cada valor para se diminuir com o total
        elif cedula == 20:   #e a maneira tá aqui
            cedula = 10      #ele vai subtraindo o maximo possivel no laço e quando ver que não da mais , ele troca aqui
        elif cedula == 10 :  # é como se fosse um complemento para que o laço funcione até chegar em 0
            cedula = 1       # se o total é maior que a cedula,ele diminui e vai fazendo até o total for menor que o valor da nota
        total_cedula=0       # o que eu não entendi aqui na altura é que como ele vai fazendo primeiro com 50 e , depois que não tivesse como , iria pular pro 20?
        if total == 0:       # porque pra mim a cedula iria passar a ser 1 direto,ele iria ver que cedula é 50 , então passaria pra 20 e etc
            break            # mas , se eu entendi bem , o laço vai travando em cada valor , ele não deixar ir direto
        # e é por isso que está adentada dentro do laço
        #ele fala que a cedula tem 4 valores , mas não de uma vez, vai se alterando um por vez

