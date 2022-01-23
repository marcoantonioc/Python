import random
n1 = str(input('Primeiro nome :'))
n2 = str(input('O segundo nome:'))
n3 = str(input('O terceiro nome:'))
n4 = str(input('O quarto nome :'))
lista = [n1,n2,n3,n4]
escolhido=random.choices(lista)
print('O aluno escolhido foi :{}'.format(escolhido))

