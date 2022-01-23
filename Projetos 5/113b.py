while True:
    try:
        n1=int(input("Indique um numero inteiro: "))
    except ValueError:
        print("Erro!")
        continue
    else:
        break

while True:
    try:
        n2=float(input("Inndique um numero float:"))
    except ValueError:
        print("Erro!")
        continue
    else:
        break
print(f"O numero inteiro que escoleu foi {n1} e o float foi {n2}")