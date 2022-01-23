import uteis # (mas não é recomendado )ou from uteis import fatorial , dobro
n=int(input("Indique um numero :"))
fat= uteis.fatorial(n)

print(f"O numero que escolheu foi {n} e o seu fatorial é {fat}")
print(f"O numero que escolheu foi {n} e o seu dobro foi {uteis.dobro(n)}")
