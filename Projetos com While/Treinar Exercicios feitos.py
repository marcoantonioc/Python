primeiro=int(input("Indique em que no quer começar :"))

razao=int(input("Qual a razao : "))

termos=primeiro
total=10

while termos!=10:
    print(termos*razao,end=" ")
    termos+=1
    termos=int(input("Quer continuar 0 :"))