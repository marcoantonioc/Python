lista=[]
total=0
while True:
    num=int(input("Indique um numero :"))
    lista.append(num)
    total += 1
    cont=str(input("Quer continuar [s]/[n]: ")).upper()


    if cont=="N" :
        break
if 5 in lista:
    print("Existe um numero 5!")

else:
    print("O numero 5 não está na lista !")
lista.sort(reverse=True)
print(f" O conteudo da lista é : {lista}")
print(f"E no total houve {len(lista)} numeros adicionados na lista!")