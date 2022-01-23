maiorpeso=0
menorpeso=1000
for i in range(1,5):
    peso=int(input('{}º pessoa indique o seu peso :'.format(i)))

    if peso>maiorpeso:
        maiorpeso=peso

    elif peso <maiorpeso and peso < menorpeso:
        menorpeso=peso

print('O maior peso e :{} \nO menor peso e : {}'.format(maiorpeso,menorpeso))
