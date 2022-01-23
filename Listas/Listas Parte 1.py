#PARA CRIAR UMA LISTA
#lanche = ["hamburguer","sumo","piza","gelado"]
#               0         1      2        3
#
# SERVE PARA CONTAR O NUMERO DE CASAS , CONTANDO COM O 0
# len(lanche)
#
# PARA TROCAR VALORES
#lanche[2]= "pastilha"

#==============================

#SERVE PARA ADICIONAR UM ITEM HÁ LISTA
#lanche.append("bolacha")

#=================================================================

# ADICIONA O ITEM HÁ LISTA NA POSIÇÃO 3
#lanche.insert(3,"cao-quente")

#================================================

#PARA ELIMINAR OS ITENS DA LISTA
#del lanche[3]
#    OU
#lanche.pop(3) O VALOR EM BRANCO ELIMINA A ULTIMA CASA
#    OU
#lanche.remove("piza")
#
# SE ESTIVEREM DOIS ITENS IGUAIS ELE VAI ELIMINAR O PRIMEIRO QUE APARECER
#=================================================================

# Exemplo:
#if "sumo" in lanche: # O "in" serve para isto
    #lanche.remove("sumo")

#=================================================================

# SERVE PARA CRIAR UMA LISTA AUTOMATICA
#valores=list(range(4,11))
#
# ORGANIZA POR ORDEM OS NUMEROS (Menor->Maior)
#valores.sort()
#     OU
#ORGANIZA POR ORDEM OS NUMEROS (Maior->Menor)
#valores.sort(reverse=True)
#========================================

#CICLO FOR
#
#for v in valores: A VARIAVEL "v" E PARA CADA ITEM DA LISTA
    #print(f"O valor é {v}")
#
# MOSTRA O VALOR DE CADA CASA
#for c , v in enumerate(valores):
    #print(f"A {c}º casa tem o valor {v}")
#
#PARA ADICIONAR VALORES DENTRO DA LISTA
#for i in range(0,5):
    #valores.append(int(input("Indique um numero:")))
#==============================================

# LISTAS IGUAIS E DIFERENTES
#a=[1,2,3,4,5]
#b=a
#b[2]=3 VAI MUDAR DAS DUAS LISTAS
#
# PARA COPIAR
#a=[1,2,3,4,5]
#b=a[:] PARA COPIAR A LISTA a
