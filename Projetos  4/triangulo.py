lado1=float(input('Indique um medida :'))
lado2=float(input('Indique outra medida :'))
lado3=float(input('Indique o ultimo lado :'))

if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    print('E traingulo')
else:
    print('Nao e triangulo ')
#OU

if lado1>lado2 and lado1 >lado3 :
    if lado1<(lado2+lado3):
        print('E triangulo')
    else:
        print('Nao e triangulo ')
elif lado2>lado1 and lado2 >lado3 :
    if lado2<(lado1+lado3):
        print('E triangulo')
    else:
        print('Nao e triangulo ')
elif lado3>lado1 and lado3 >lado2 :
    if lado3<(lado2+lado1):
        print('E triangulo')
    else:
        print('Nao e triangulo ')