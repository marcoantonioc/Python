num1=int(input('INdique um numero :'))
num2=int(input('Indique um segundo numero :'))



opcao=0
while not opcao==5:
    print(
        '=================================================================================================================')
    opcao=int(input('[1]Somar\n[2]Multiplicar\n[3]Saber qual e o maior\n[4]Trocar os numeros\n[5]Sair do programa\nEscolha uma opcao :'))
    if opcao==1:
        print('{}+{}={}'.format(num1,num2,num1+num2))
    elif opcao==2:
        print('{}X{}={}'.format(num1, num2, num1 * num2))
    elif opcao==3:
        if num1>num2:
            print('O numero {} e maior que um nuemro {}'.format(num1,num2))
        elif num2 < num1:
            print('O numero {} e maior que um nuemro {}'.format(num2,num1))
        elif num1==num2:
            print('Os numeros sao iguais !')
    elif opcao==4:
        num1 = int(input('INdique um numero :'))
        num2 = int(input('Indique um segundo numero :'))
    elif opcao==5 :
        opcao=False
print('Adeus')

