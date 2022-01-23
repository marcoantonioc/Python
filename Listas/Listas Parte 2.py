#pessoas=[]
#joao=["Joao",24]
#maria=["maria",19]
#duarte=["duarte",18]
#PARA METER A LISTA JOAO DENTRO DA LISTA PESSOAS

#pessoas.append(joao[:])
#pessoas.append(maria[:])
#pessoas.append(duarte[:])

#pessoas[["joao",24],["maria",19],["duarte",18]]
#           0     1      0     1      0      1
#             0     |       1    |      2
# SERVE PARA INDICAR QUAL CASA QUEREMOS
#print(pessoas[1][1])
#print(pessoas[2])

#for v in pessoas:
    #print(v[0])
pessoas=list()
dados=list()
for p in range(0,3):
    dados.append(str(input("Indique o seu nome :")))
    dados.append(int(input("Indique a sua idade: ")))
    pessoas.append(dados[:])
    dados.clear()
maior=menor=0
for v in pessoas:
    if v[1]>=18:
        maior+=1
        print(f"A pessoa {v[0]} é maior de idade")
    elif v[1]<18:
        menor+=1
        print(f"A pessoas {v[0]} é menor de idade")
print(f"No total tivemos {maior} pessoas maior de idade e {menor} pessoas menor de idade")
