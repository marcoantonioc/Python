def manual(comando):
    print(f"Acessando o manual do comando '{comando}' ")
    help(comando)




opcao=""
while True:

    opcao=str(input("Função ou Biblioteca > "))
    if opcao=="FIM":
        break
    else:
        manual(opcao)


