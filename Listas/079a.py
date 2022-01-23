lista = []
while True:
    num=int(input("Digite um valor : "))

    if num not in lista:
        print("Valor adicionado!")
        lista.append(num)
    elif num in lista:
        print("Valor repetido ! Valor não Adicionado !")

    continuar=str(input("Quer continuar [s]/[n] : ")).upper()

    if continuar=="N":
        break
    elif continuar=="S":
        continue
    else:
        print("Tecla errada, tente novamente!")
        break

lista.sort()
print(f"A sua lista final foi {lista}")