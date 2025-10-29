import datetime
def voto(resposta):
    ano = datetime.date.today().year
    idade = ano - resposta
    if idade > 16 and idade < 18:
        print('opcional')
    if idade > 18 and idade < 60:
        print('obrigatório')
    if idade < 16:
        print('não vota')
    print(idade)

voto(int(input('Digite o ano de nascimento: ')))

"""resolução do guanabara
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade or idade > 65:
        return f'Com {idade} anos: VOT OPCIONAL'
    else: 
        return f'Com {idade} anos:VOTO OBRIGATÓRIO'
        
        
print(voto(2000))"""
#lembrando que escopo local é quando esta dentro da função , por exemplo e global é quando está fora
#efetuando a importanção no escopo local ajuda a poupar espaço