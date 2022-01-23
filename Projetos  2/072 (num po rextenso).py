num=('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze', 'Douze','Treze','Catorze','Quinze',
     'Dezaseis','Dezasete','Dezoito','Dezanove','Vinte')

escolha = int(input('Indique um numero de 0 entre 20 : '))
while True:

    if escolha < 0 or escolha > 20:
        escolha = int(input("Tente novamnete . Digite um numero entre 0 e 20: "))

    if escolha>=0 and escolha<=20:
        break

print(f"O número que escolheu foi {num[escolha]}")