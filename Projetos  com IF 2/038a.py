num1=int(input('Indique um numero :'))
num2=int(input('Digite um numero :'))

if num1>num2:
    print('O numero {} e maior que o numero {}'.format(num1,num2))
elif num2>num1 :
    print('O numero {} e maior que o numero {}'.format(num2, num1))
elif num1==num2 :
    print('Os numeros sao iguais !')