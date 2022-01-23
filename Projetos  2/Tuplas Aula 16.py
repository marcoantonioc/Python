# AS TUPLAS SÃO IMUTÁVEIS

lanche=("Banana","Coelho","Rabo","Mae")   # [] --> Para lista  /  {} --> Para dicionário
    #      0        1        2     3
print()
print('Mostra  o numero',lanche[2])
print()
print('Mostra a partir de um numero e vai ate ao outro num , ele não lê o ultimo num',lanche[1:3])
print()
print('Lê a partir do um e vai até ao final',lanche[1:])
print()
print('Lê  do final ate o numero indicado -1',lanche[:3])
print('Conta  a partir de traz para frente , assim o -1 passa a ser a mae e o 0 passa a ser o -4',lanche[-1]) #

print()
for posicao, comida in enumerate(lanche):
    print(f'{comida} , na posição {posicao}')
#for comida in range(0,len(lanche)):
#    print(f'{lanche[comida]} ,posição {comida} ')


print()
print(f'Organiza de forma alfabetica (mas tem que ter a primeira letra em mausculo) {sorted(lanche)}')
print()
a=(1,2,3,4,5)
b=(6,7,8,9,0,1)
c=a+b
print(f'Vai juntar (NÃO SOMAR) {c}')

print(f'Mostra em que posição está o 0 {c.index(0)}')
print(f'Mostra em que posição está o 1 a partir da "casa" 1{c.index(1,1)}')

del(c) # Elimina a tupla c toda



