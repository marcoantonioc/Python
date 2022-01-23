km=float(input('Indique quantos KM vai andar  :'))

if  km<=200 :
    total=km*0.50
    print('Voce vai ter que pagar {}'.format(total))
elif km>200 :
    total1=km*0.45
    print('Ovce vai ter que pagar {}'.format(total1))