pessoas=dict()
lista=list()
total=0
anos=0
mulheres=list()
while True:
    pessoas['nome']=str(input("NOME: "))
    while True:
        pessoas['sexo']=str(input('SEXO [m/f]: ')).upper()
        if pessoas['sexo'] == "M" or pessoas['sexo'] =="F":
            break
        else:
           print("Opção Iválida")
    if pessoas['sexo']=="F":
        mulheres.append([pessoas['nome']].copy())
    pessoas['idade']=int(input("IDADE:"))
    total+=1
    lista.append(pessoas.copy())
    while True:
        continuar=str(input("Quer continuar [s]/[n]: ")).upper().strip()
        if continuar=="S" or continuar=="N":
            break

    if continuar=="N":
        break
    else:
        continue

print("-="*35)

for i in lista:
    for k,v in i.items():
        if k =='idade':
            anos+=v


media=anos/total
print(f"O grupo tem  {total} pessoas.")
print(f"A média de idades é {media}.")
print(f"As mulheres são : {mulheres}")
print(f"As pessoas que estão com a idade a cima da media: ")
for i in lista:
    for k,v in i.items():
        if k =='idade':
            if v > media:
                print(i.items())


