lista=list()
maior=0
menor=0
for v in range(0,5):
    lista.append(int(input(f"Indique o valor {v} : ")))

    if v == 0:
        maior=lista[v]
        menor=lista[v]

    else:
        if lista[v] >maior:
            maior=lista[v]
        if lista[v] < menor :
            menor=lista[v]
print(f"O maior numero foi {maior} na posição",end=" ")
for i , c in enumerate(lista):
    if c == maior:

        print(f"{i}...")
print(f"O menor numero foi {menor} na posicao",end=" ")
for i, c in enumerate(lista):
    if c == menor:

        print(f"{i}...",end=" ")



