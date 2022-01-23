produto=("Maça" ,0.34,"Livro",1.5,"Borracha",0.30,"Computador",1000)

print("="*30)
print("LISTAGEM DE PREÇOS")
print("="*30)

for pos in range(len(produto)):
    if pos % 2 ==0:
        print(f"{produto[pos]:.<30}",end=" ")
    else:
        print(f" {pos:>7.2f}")