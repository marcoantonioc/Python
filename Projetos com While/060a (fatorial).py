num=int(input('INdique um numero : '))
ok=1
for i in range(num,0,-1):
    ok*=i
    print("{}".format(i),end=" ")
    print("x" if i>1 else "=",end=" ")

print(ok)






