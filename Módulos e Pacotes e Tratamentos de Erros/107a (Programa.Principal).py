from ex_107a import moeda
num=float(input("Digite o preço $: "))


print(f"A medate de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}")
print(f"O dobro de {num} é {moeda.moeda(moeda.dobro(num))}")
print(f"O aumneto de 10% de {num} é {moeda.moeda(moeda.aumento(num))}")
print(f"A diminuição de 10% {num} é {moeda.moeda(moeda.deminuindo(num))}")


