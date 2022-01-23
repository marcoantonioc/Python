num0=int(input("Indique um numero : "))
num1=int(input("Indique um numero : "))
num2=int(input("Indique um numero : "))
num3=int(input("Indique um numero : "))

tupla=(num0,num1,num2,num3)



print(f"O numero 9 aparece {tupla.count(9)} vezes !")
if 3 in tupla:
    print(f"O numero tres aparece pela primeira vez na  {tupla.index(3)+1}º posição")
else:
    print("Voce não digitou nenhum tres ")

print(f"Os valores pares foram : ")

for p in tupla:
    if p % 2 ==0 :
        print(p , end=" ")