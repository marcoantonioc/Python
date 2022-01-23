contador=0
soma=0
while True:
    num=int(input("Indique um numero [999] para parar:"))
    if num == 999:
        break

    contador += 1
    soma += num

print(f"No final voce digitou {contador} e a soma entre eles é {soma}")

