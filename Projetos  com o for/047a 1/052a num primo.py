num=int(input('Indique um numero : '))
total=0
for i in range(1,num+1):
     if num % i ==0:
         print('\033[33m', end=" ")
         total+=1
     else:
         print('\033[31m',end="")

     print(i ,end='')

if total ==2 :
    print('\033[mO numero e primo')
else:
    print('\033[mO numero neo e primo')