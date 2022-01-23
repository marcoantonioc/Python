num=int(input('Digite um numero :'))

opcao=int(input('1-Binario\n2-octal\n3-hexadezimal\n4-Todos\nOPCAO:'))

if opcao==1 :
    print('O numero {} convertido para binario e {}'.format(num,bin(num)))
elif opcao==2:
    print('O numero {} convertido para Octal e {}'.format(num,oct(num)))
elif opcao ==3 :
    print('O numero {} convertido para hexadezimal e {}'.format(num, hex(num)))
elif opcao==4:
    print('O numero {} convertido para binario e {}'.format(num, bin(num)))
    print('O numero {} convertido para Octal e {}'.format(num, oct(num)))
    print('O numero {} convertido para hexadezimal e {}'.format(num, hex(num)))
else:
    print('Opcao invalida !')