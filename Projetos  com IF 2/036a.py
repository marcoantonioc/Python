casa=int(input('INdique o valor da casa : '))

salario=int(input('Indique o seu salario : '))

anos=int(input('Quanto tempo vai demorar para pagar :'))

#meses=anos*12

prestacao=casa/(anos*12)

por_cento=(salario/100)*30

if prestacao>por_cento :
    print('Nao vai dar nao,a prestacao sera de {:.3f} e 30% do seu salrio e {}'.format(prestacao,por_cento))
else:
    print('Para pagar a casa de {} em {} a prestacao sera de {:.3f} \n VAI FUNCIONAR '.format(casa,anos,prestacao))