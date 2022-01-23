from datetime import date
atual=date.today().year

total=0
total1=0
for i in range(1,8):
    anonasc=int(input('Em que ano nasceu :'))

    idade=atual-anonasc

    if idade >=18 :
        total+=1
    else:
        total1+=1
print('As pessoas que sao maiores de idade sao {}'.format(total))

print('E as pessoas menores de idade sao {}'.format(total1))
