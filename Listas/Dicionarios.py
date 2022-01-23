#dados={'nome':'Pedro',"idade":25}
#               idade|        idade  (Já não são numeros)
#print(dados['nome'])
#print(dados['idade'])
#
# ADICIONA UM DADO NO DICIONARIO
#dados['sexo']='M'
# ELIMINA UM DADO
#del dados['idade']
#print(dados)
#
filme={'titulo':'star wars','ano':1977,
'diretor':'George Lucas'
}
#
# MOSTRA OS DADOS
#print(filme.values())
# MOSTRA OS TOPICOS DOS DADOS
#print(filme.keys())
#  MOSTRA TUDO
#print(filme.items())
#
#for k,v in filme.items():
    #print(f'O {k} é {v}')
#
# SUBSTITUI O VALOR DO TITULO
#filme['titulo']='Marco'
#
# ADICIONA UM VALOR HÁ LISTA
#filme['tempo']=120
#
# DÁ PARA MISTURAR E METER DICIONÁRIOS DENTRO DE LISTAS
#locadora=[{'titulo':'star wars','ano':1977}]
#
#print(locadora[0]['titulo'])
#print(locadora[0]['ano'])
#
estado=dict()
brasil=list()

for c in range(0,3):
    estado['uf']=str(input("Unidade federativa:"))
    estado['sigla']=str(input('Sigla: '))
    brasil.append(estado.copy())#PARA COPIAR

for e in brasil:
    for k ,v in e.items():
        print(f"O campo {k} tem o valor {v}")



