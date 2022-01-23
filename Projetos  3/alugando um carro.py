dias=float(input('Quandos dias reservou o carro :'))

km=float(input('Quantos km andou com o carro : '))

total=dias*60+km*0.15

print('Sabendo que reservou durante {} dias \n E que andou {} KM \n Vai ter que pagar {:.3f}'.format(dias, km, total))