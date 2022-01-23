mediaidade=0
idademaior=0
total=0
for i in range(1,5):
    print('===={} PESSOA======'.format(i))
    nome=str(input('INdique o seu nome :'))
    idade=int(input('Indique a sua idade :'))
    sexo=str(input('INdique o seu sexo (m/f) :'))

    mediaidade+=idade

    if sexo=='m':
        if idade>idademaior:
            idademaior=idade
            nome1=nome

    elif sexo=='f':
        if idade<20:
            total+=1
print('A media de idade do grupo e de : {}'.format(mediaidade/i))
print('O homem mais velho e de {} e o nome dele e {:.3f} '.format(idademaior,nome1))
print('No total ha {} mulheres com a idade inferior a 20 ans '.format(total))








