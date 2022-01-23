from random import randint
def sorteio(lista):
    print("Os 5 valores da lista são :")
    for i in range(0, 5):
        lista.append(randint(1,10))
    print(lista)

def soma(lista):
    total=0
    print(" ",end="")
    for v in lista:
        if v % 2==0:
            total+=v

    print(f"Somando os valores pares de o resultado vai ser {total}")

numeros=list()

sorteio(numeros)
soma(numeros)
