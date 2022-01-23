num=0

while True:
    num = int(input("Inidque um numero : "))
    if num <0 :
        break

    for i in range(1,11):
        print(f"{num}X{i}={num*i}")

print("Acabou")
