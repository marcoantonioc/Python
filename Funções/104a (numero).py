def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print(f"ERRO!")
        if ok:
            break
    return valor


n = leiaint("Indique um numero :")
print(f"Voce digitou o numero {n}")

