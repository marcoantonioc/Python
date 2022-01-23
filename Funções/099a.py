
def maior_(*num):
    maior=0
    print(f"Analisando os valores passados:")
    for i in num:
        if i > maior:
            maior=i
        print(f"{i} ",end="")

    print(f"Foram passados {len(num)} valores ao todo .")
    print(f"O maior valor informado foi {maior}")
    print("="*30)

maior_(1,3,2)
maior_(6)

