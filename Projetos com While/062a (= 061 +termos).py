#primeiro=int(input("Indique o primeiro termo : "))
#razao=int(input("Indique a razão : "))

#termo=primeiro
#contador=1
#totaltermos=10
#continuar=1

#while contador<=10:
#   print("{}".format(termo),end=" ")
#   termo+=razao
#   contador+=1
#print("Pausa\n")

#while continuar !=0:

#   contador=1
#   continuar=int(input("Indique o numero :"))
#   totaltermos+=continuar

#   while contador <= continuar:
#       print("{} ".format(termo), end="")
#       termo += razao
#       contador += 1
#       print("Pausa")
#print("Acabou")

#print("No final ouve {} termos".format(totaltermos))



primeiro=int(input("Indique o primeiro termo: "))
razao=int(input("Indique a razão do termo : "))
termo=primeiro
contador=1
total=0
mais=10
while mais!= 0:
    total+=mais
    while contador<=total:
        print("{} -> ".format(termo),end="")
        termo+=razao
        contador+=1
        print("PAUSA")
    mais=int(input("Mais numero : "))

print("FIm")

print("No final ouve {} termos ".format(total))

























