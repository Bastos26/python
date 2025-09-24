n = soma = cont =0
while True:
    n = int(input('digite um numero:'))
    if n == 999:
# estava colocando o soma e o cont aqui e ele estava contando com o 999 e está errado
        break
    cont = cont + 1
    soma=soma+n # aqui ele está considerando 999 somente como um flag e não como valor e desconsiderando a vez em que 999 foi digitado
print(f'você digitou {cont} numeros e a soma dos numeros digitador é {soma}')