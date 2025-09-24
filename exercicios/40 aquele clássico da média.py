n1 = float(input('digite sua primeira nota:'))
n2 = float(input('digite a sua segunda nota:'))
media = (n1 + n2) / 2
if media >= 5 and media < 7 :# atenção quando for usar o and ou or , tem q repetir sempre, igual eu repeti o "media"
    print('sua média é {} ,recuperação'.format(media))
elif media < 5 :
    print('sua média é {} ,reprovado'.format(media))
else:
    print('sua média é {} ,aprovado'.format(media))
