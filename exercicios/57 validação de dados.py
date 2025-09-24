sexo='M','F'
while sexo != 'M' and sexo != 'F':
    sexo=str(input('digite o seu sexo[M/F]')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos , porfavor digitar a informação correta!')
print('fim')


# do professor
'''
sexo=str(input('digite o seu sexo:')).strip().upper()[0]
 while sexo not in 'MmFf':
    sexo=str(input('dado invalido , tente novamente:')).strip.upper[0]
print('sexo {} registrado com sucesso'.format(sexo))'''