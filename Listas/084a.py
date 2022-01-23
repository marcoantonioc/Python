dados=list()
pessoas=list()
while True:
    dados.append(str(input("Indique qual o seu nome :")))
    dados.append(float(input("Indique qual o seu peso : ")))
    pessoas.append(dados[:])
    dados.clear()
    continuar=str(input("Quer continuar [s]/[n]: ")).upper().strip()

    if continuar=="N":
        break
maior=menor=0
for v in pessoas:
    if v[1] >maior:
        maior=v[1]
        menor=v[1]
    elif v[1]<menor:
        menor=v[1]

print(pessoas)
print(f"No total houve {len(pessoas)} pessoas.")
print(f"A pessoa mais pesada foi de {maior} KG. As pessoa com esse peso foram : ",end=" ")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}")

print(f"A pessoa mais leve foi de {menor} KG. As pessoas com esse peso foram ",end=" ")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}")
