valor=int(input("INdique um valor que quer sacar : "))


ced=50
totced=0

while True:
    if valor>=ced:
        valor-=ced
        totalnotas+=1
    else:
        print(f"O total de notas de {ced} foi {totced} ")
        if ced==50:
         nota=20

        elif valor==20:
            nota=10

        elif valor==10:
            nota=1
            totalnotas=0
        if nota ==0:
            break

