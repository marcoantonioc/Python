def leiaint(num):
    while True:
        try:
            n=int(input(num))
        except ValueError:
            print(f"Erro valor inválido!")
            continue
        else:
            return n


def leiafloat(num):
    while True:
        try:
            n=float(input(num))
        except ValueError:
            print("Erro digite um valor float :")
        else:
            return n


n1= leiaint("INdique um numero inteiro:")
n2 = leiafloat("Indique um numero do tipo float: ")
print(f"O valor digitado foi {n1} e {n2}")





