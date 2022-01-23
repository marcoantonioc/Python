jogos=int(input("Quantos jogos voce quer : "))
from random import randint
from time import sleep
lista=[]
total=0
print(f"============== SORTEANDO {jogos} JOGOS ============= ")
while True:
    if total == jogos:
        break
    total += 1
    for v in range(0,6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    sleep(1)
    lista.sort()
    print(f"Jogo {total}:{lista}")
    lista.clear()
