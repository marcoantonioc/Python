numeros=[[],[]]
for v in range(1,8):
    num=(int(input(f"Indique o {v}º numero: ")))

    if num % 2 ==0:
        numeros[0].append(num)
    elif num % 2 ==1:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f"Os numeros pares são : {numeros[0]}")
print(f"Os numeros impares são : {numeros[1]}")