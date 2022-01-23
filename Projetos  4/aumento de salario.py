salario=int(input('Indique o seu salario :'))

if salario>1250:
    aumento=(salario/100)*10
    salarion=salario+aumento
    print('O seu salario novo e {}'.format(salarion))
elif salario<=1250:
    aumento=(salario/100)*15
    salarion = salario + aumento
    print('O seu novo salario e {}'.format(salarion))