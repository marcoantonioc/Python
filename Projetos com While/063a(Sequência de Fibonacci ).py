#print("-"*30)
#print("Sequência de Fibonacci ")
#print("-"*30)
#num=int(input("Indique o numero que quer : "))
#t1=0
#t2=1

#print("{} -> {}".format(t1, t2), end=" ")
#contador=3
#while contador<=num:
    #A ordem das coisas
   # t3=t1+t2
   # print("-> {}".format(t3),end=" ")
   # t1=t2
  #  t2=t3
  #  contador+=1
#print("FIM")

num=int(input("Indique um numero : "))
t1=0
t2=1
contador=3
print("{} -> {} ->".format(t1,t2),end=" ")
while contador<=num:
    t3 = t1 + t2
    print("{} ->".format(t3),end=" ")
    contador+=1
    t1=t2
    t2=t3
print("Acabou")




























