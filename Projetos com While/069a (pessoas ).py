maior18=0
totalh=0
mulheres=0

while True:
    print("="*20)
    print("CADASTRO DE PESSOAS ")
    print("="*20)

    idade=int(input("Idade : "))
    if idade >= 18:
        maior18 += 1

    sexo=" "
    while sexo not in "MF":
        sexo=str(input("Sexo [M/F] : ")).upper().strip()[0]
    if sexo =="M":
        totalh+=1
    elif sexo=="F" and idade<20:
        mulheres+=1                   

    continuar=" "
    while continuar not in "SN":
        continuar=str(input("Quer continuar [S/N] : ")).upper().strip()[0]

    if continuar=="N":
        break


print(f"As pessoas com 18 anos ou mais são {maior18}")
print(f"O total de homens cadastrados foram {totalh}")
print(f"O total de mulheres com 20 ou + são {mulheres}")

