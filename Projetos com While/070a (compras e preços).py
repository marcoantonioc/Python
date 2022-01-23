total=0
miltotal=0
nomebarato=""
while True:
    nome=str(input("Qual o nome do protudo : "))
    preço=float(input("Qual foi o preço do produto : "))
    total+=preço

    if preço>1000:
        miltotal+=1

    maisbarato = preço
    if preço<maisbarato:
        maisbarato=preço
        nome==nome

    continuar=" "
    while continuar not in "SN":
        continuar=str(input("Quer continuar [S/N] :")).strip().upper()[0]
    if continuar=="N":
        break

print(f"O total casto foi {total:.3f}")
print(f"Temos {miltotal} produto que custa mais de 1000$")
print(f"O produto mais barato foi o {nome} que custou {maisbarato}$")
