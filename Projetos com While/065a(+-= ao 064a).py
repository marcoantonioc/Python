num=int(input("Indique um numero : "))

continuar=str(input("Deseija continuar [s] ou [n] : "))

media=num
total=1
maior=num
menor=num

while continuar == "s" :
    num=int(input("Indique um numero : "))
    media+=num
    if num>maior:
        maior=num
    elif num<menor:
        menor=num
    continuar = str(input("Deseija continuar [s] ou [n] : "))
    total+=1
print("A media de todos os {} numeros da {}".format(total,media/total))

print("E o maior numero é {} e o menor é {}".format(maior,menor))