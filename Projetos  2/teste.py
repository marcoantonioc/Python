primeiro=int(input("Inidique onde vai começar : "))
razao=int(input("Indique qual a razão :"))


termos=razao*10
while primeiro<termos:

    print(primeiro)
    primeiro += razao
    while termos!=0:
        termos=int(input("Indique quantos termos quer :"))

    print(primeiro)
