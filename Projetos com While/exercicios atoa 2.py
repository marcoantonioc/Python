#maior = 0
#menor = 0
#for i in range(1,6):
    #num=int(input("Indique um numero : "))

    #if num >maior:
        #maior=num
# menor=num
#elif num<menor:
# menor=num
#print("O maior numero é {} e o menor é {} !".format(maior,menor))
#nome=str(input("Indique o seu nome : "))
#from random import randint
#maior=0
#menor=0
#total=0
#for i in range(1,8):
#   num=randint(0,10)
#   print(num)
#   total+=num
#   if num >maior:
#       maior=num
#       menor=num
 #   elif num <menor:
#      menor=num
#pime=maior+menor
#media=(total-pime)/5
#print("A media do atleta {} foi {} não contando com a maior nota {} e nei com a menor {}".format(nome,media,maior,menor))

print("Bem vindo há loja do MARCO ! ")
total=0
fim=0
while fim ==0 :
    print("Para sair digite 0")
    produto=float(input("INdique o valor da mercadoria : "))
    total+=produto
    if produto==0:
        fim=1
print("Deve pagar {}".format(total))

opcao=int(input("[1]Cartão de cretido\n[2]Com notas\n[3]Tenho o dinheiro certo\nIndique como vai pagar :"))

if opcao==1:
    print("Operação concluida com sucesso ! Volte sempre")
elif opcao==2:
    nota=int(input("Indique com que nota vai pagar : "))
    troco=nota-total
    print("Operação concluida ! O seu troco é {:.3f}".format(troco))
elif opcao==3:
    print("Operação concluida com sucesso ! Volte sempre !")
