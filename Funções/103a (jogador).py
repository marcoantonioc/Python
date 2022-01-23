def ficha(jogador='<disconhecido>',golos=0):

    print(f"O jogador {jogador} fez {golos} golo(s) no campeonato.")

player=str(input("Indique o nome do jogador :"))
pontos=str(input(f"Indique quantos golos o jogador {player} fez :"))

if pontos.isnumeric():
    pontos=int(pontos)
else:
    pontos=0
if player.strip()=="":
    ficha(golos=pontos)
else:
    ficha(player,pontos)
