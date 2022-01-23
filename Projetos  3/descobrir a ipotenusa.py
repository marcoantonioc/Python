from math import sqrt
resposta=str(input('O seu triagulo e reto ? (sim ou nao) :'))

if resposta == 'nao':
    print('Nao da para fazer o teorema de pitagoras !')
elif resposta =='sim':
    cat1=float(input('Indique o valor do primeiro cateto :'))
    cat2=float(input('Indique o segundo cateto :'))

    hipo = (cat1**2 + cat2**2)

    total=sqrt(hipo)

    print(cat1,' +',cat2,'=',hipo )

    print("A raiz de ", hipo, ' da {:.3f}'.format(total))

