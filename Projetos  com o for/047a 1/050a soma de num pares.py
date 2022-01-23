total=0
for i in range(1,7):
    num=int(input('Indique o {}º numero :'.format(i)))
    if num % 2 ==0 :
        total+=num
print(total)