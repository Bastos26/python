palavras=('aprender',
          'programar',
          'linguagem',
          'python',
          'curso',
          'gratis',
          'estudar',
          'praticar',
          'trabalhar',
          'mercado',
          'programador',
          'futuro')
for letra in palavras:
    a=(letra.count('a'))
    e=(letra.count('e'))
    i=(letra.count('i'))
    o=(letra.count('o'))
    u=(letra.count('u'))
    if a or e or i or o or u >= 1 :
        print(f' na palavra {letra} as vogais que aparecem são : {'a'*a} {'e'*e} {'i'*i} {'o'*o} {'u'*u}')
    #elif a or e or i or o or u == 0 :

"""resolução do guanabara
palavras = ('aprender','programar','linguagem','python',   
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')
for p in palavras:                                          
    print(f'\na palavra {p} temos ',end='')   o conceito do for vai além do que se imagina
        for letra in p:                        ele tem uma questão/utilidade de ir destrinchando as coisas
            if letra.lower in 'aeiou' :        cada palavra é um conjunto de letras, logo , se é possivel dividir tambem
                print(letra,end='')             Quando se colocou 'aeiou' achei que daria problema porque estão juntas então
                                                parece mais uma palavra do que letras especificas mas acho que é porque está
                                                adentada em um contexto que se refere somentes em letras e não em um conjunto                
                                                maior que são as palavras, percebe ?
                """