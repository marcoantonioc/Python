num=int(input('Indique o numero que quer a tabuada :'))

ate=int(input('Indique ate quanto quer a sua tabuada:'))

for i in range(1,ate +1):
    s=num*i
    print('{}X{}={}'.format(num,i,s))