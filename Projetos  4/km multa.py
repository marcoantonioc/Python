velocidade=int(input('Indique a velocidade :'))

if velocidade>80 :
    total=(velocidade-80)*7
    print('Voce vai ter que pagar {}'.format(total))
else:
    print('Esta tudo bem !')
