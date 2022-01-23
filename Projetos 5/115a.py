while True:
    print('-'*30)
    print('        MENU PRINCIPAL')
    print('-'*30)
    print('1- Ver pessoas cadastradas')
    print('2- Cadastrar Nova pessoa ')
    print('3- Sair')

    try:
        opcao=int(input('Qual sua opção: '))

    except ValueError:
        print('Valor invalido ! Tente Novamente !')
    else:
        if opcao==1:
            print('ola')
        elif opcao==2:
            print('Gosto')
        elif opcao==3:
            break