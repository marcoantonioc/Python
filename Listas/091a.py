from random import randint
from operator import itemgetter
jogo={'jogadores1':randint(1,6),'jogador2':randint(1,6)
      ,'jogador3':randint(1,6),'jogador4':randint(1,6)}
for jo,num in jogo.items():
    print(f"O {jo} tirou {num} no dado!")

ranked=[]
#organiza do menor->maior|Troca o sentido|pega no valor 1 da lista gerada|
ranked=sorted(jogo.items(), reverse=True, key=itemgetter(1) )# ORGANIZA OS DADOS QUE ESTÃO NO KEY QUE SÃO OS NUMEROS(É 1 PORQUE O RANKED É UM LISTA
# OS OS NUM ESTÃO NA POSIÇÃO 1) DO MAIOR PARA O MENOR

print('='*30)
for j , n in enumerate(ranked):
    print(f"O {j+1}º lugar: {n[0]} tirou {n[1]}",end="")
    print()
