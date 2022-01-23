from random import randint
pontos=0
computador=0
cp=""

total=0


while True:
    jogador=str(input("Indique se é Pare[P] ou Impar[I] e 0 para sair : ")).upper()

    if jogador=="0":
        break

    while True:
        jogada=int(input("Indique um numero entre 1 e 10 : "))
        if jogada >=1 and jogada<=10:
            break

    pc = randint(1, 10)
    total=jogada+pc

    print(f"O computador jogou {pc}")
    print(f"A soma total da {total}")

    if jogador=="P":
        cp="I"
        if jogador=="P":
            if total % 2 == 0:
                pontos+=1
        if cp=="I":
            if total % 2 == 1:
                computador+=1
    elif jogador == "I":
        cp="P"
        if jogador=="I":
                if total % 2 == 1:
                    pontos+=1
        if cp=="P":
            if total% 2 ==0:
                computador+=1


    print(f"Pontos Jogador {pontos}")
    print(f"Pontos pc {computador}")
print(f"Acabou no total o jogador ficou com {pontos} e o computador com {computador}")


