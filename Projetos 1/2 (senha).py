y="y"
continuar="y"
#1ºwhile
while True:
    print("="*30)
    print("CRIAÇÃO DE USUARIO")
    print("="*30)
    usuario=str(input("Indique o seu nome de usuario :"))
    print("-"*30)
    senha=str(input("Indique a sua nova senha : "))
    #2º while
    while True:
        print("="*30)
        print("LOGIN")
        print("="*30)
        usu=str(input("Indique o seu usuario: "))
        print("-"*30)
        passw=str(input("Inidique a sua senha: "))
        print("-"*30)
        if usu==usuario and passw==senha:
            print(f"Bem vindo ao nosso sistema {usuario}")
            # Não sei o que quebra
            break

        elif usu!=usuario and passw!=senha:
            print("O usuario e a senaha estão incorretas")
            #3º While
            while True:

                continuar = str(input("Quer continuar [y]/[n]: "))
                #quebra o 3º while
                if continuar == "y":

                    continuar=="y"
                    break

                elif continuar == "n":
                    continuar=="n"
                    break
        #Quebra o segundo while
        if continuar=="n":
            break
    #Quebra o 1º While
    if continuar=="n":
        break
    if continuar=="y":

        break

print("Adeus e volte sempre!")
