from datetime import date
data= date.today().year
datan=int(input('Em que ano voce nasceu :'))

idade=data-datan

print(idade)
if idade==18 :
    print('Esta na hora de servir !')
elif idade<18 :
    print('Voce ainda nao pode ainda ,mas falta {} anos'.format(18-idade))
elif idade>=19 :
    print('Ja deveria ter entrado a {} !'.format(idade-18))


