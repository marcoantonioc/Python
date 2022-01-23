
num=0
total=0
ok=0
num = int(input("Indique um numero : "))
while num != 999 :
    ok+=1
    total+=num
    num = int(input("Indique um numero : "))
print("No total voce digitou {} numeros e a soma de todos os numeros ficou :{} ".format(ok,total))