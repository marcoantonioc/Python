pares=maior=0
tudo =[[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f"Indique um numero para a casa [{l},{c}]:"))
        if num % 2==0:
            pares+=num
        tudo[l].append(num)

#print(f"[{tudo[0][0]}]  [{tudo[0][1]}] [{tudo[0][2]}]")
#print(f"[{tudo[1][0]}]  [{tudo[1][1]}] [{tudo[1][2]}]")
#print(f"[{tudo[2][0]}]  [{tudo[2][1]}] [{tudo[2][2]}]")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{tudo[l][c]:^3}]",end=" ")
    print()

total=tudo[0][2]+tudo[1][2]+tudo[2][2]

print(f"A soma de todos os numeros pares deu : {pares}")
print(f"A soma dos numeros da terceira coluna deu : {total}")

for v in range(0,3):
        if tudo[1][v]> maior:
            maior= tudo[1][v]
print(f"O maior numero da segunda linha é : {maior}")