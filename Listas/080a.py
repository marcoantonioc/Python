lista=[]
maior=0
menor=0
for v in range(0,4):

    num=int(input(f"Estamos na posição {v} .Indique um valor: "))
    if num > maior:
        maior=num
        menor=num
    elif num<=menor:
        lista.insert(0,num)
        menor=num

    lista.append(num)
lista.pop()
print(lista)
print(maior,menor)