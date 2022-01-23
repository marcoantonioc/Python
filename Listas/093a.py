jogador=dict()
lista=[]
ok=list()
total=0
while True:
    jogador['nome']=str(input("Indique o nome do jogador: ")).upper()

    partidas=int(input(f"Quantas partidas o jogador {jogador['nome']} fez:"))

    for v in range(0,partidas):
        golos=(int(input(f"Quantos golos {jogador['nome']} fez na {v+1}º :")))
        total+=golos
        ok.append(golos)



    jogador['golos']=ok[:]
    jogador['total'] = total
    total = 0
    ok.clear()

    lista.append(jogador.copy())

    continuar = str(input("Quer continuar [s]/[n]:")).upper().strip()

    if continuar == "N":
        break



print("-="*35)
print(f"Cod Nome   golos  total")
for k, i in enumerate(lista):

    for c,v in i.items():
        print(f"{k}_{v}",end="")
    print()

print("-="*35)

while True:
    pessoa=int(input("Mostrar dados de qual jogador (999 para sair):"))
    if pessoa==999:
        break
    print("-"*35)
    print(f"LEVANTAMNETO DO JOGADOR {lista[pessoa]['nome']}")
    for p,i in enumerate(lista[pessoa]['golos']):
       print(f"No {p+1}º fez {i} golos.")

