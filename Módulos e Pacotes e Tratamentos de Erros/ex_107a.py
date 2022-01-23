def metade(n=0):
    return n/2

def dobro(n=0):
    return n*2

def aumento(n=0):
    dez=(n/100)
    total=n+dez
    return total

def deminuindo(n=0):
    dez=(n/100)
    total=n-dez
    return total

def moeda(moeda='$',n=0):
    return f"{moeda}{n:.2f}".replace(".",",")


