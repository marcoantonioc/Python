lista=[]
par=[]
impar=[]
while True:
    num=int(input("Indique um numero :"))
    lista.append(num)
    cont=str(input("Quer continuar [s]/[n]: ")).upper().strip()
    if cont=="N":
        break


for v in lista:
    if v % 2 == 0 :
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(f"A lista completa :{lista}")
print(f"A lista de numeros pares : {par}")
print(f"A lista de numeros impares : {impar}")