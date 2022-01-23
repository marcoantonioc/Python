from random import randint

num=randint(1,10)
print(num)
resposta=int(input('Tente acertar o numero : '))
if resposta > num:

    print('O numero que o computador pensou e mais pequeno !')

elif resposta < num:
    print('O numero que o computador pensou e maior ! ')
resposta=0
total=0
while resposta != num:

        resposta=int(input('Voce falhou tente outra vez : '))
        total+=1

        if resposta > num :

            print('O numero que o computador pensou e mais pequeno !')

        elif resposta < num:
            print('O numero que o computador pensou e maior ! ')

print('Voce acertou o numero era {} \nDemorou {} tentativas ate acertar'.format(num,total))

# OU

acertou=False

while not acertou:
    resposta = int(input('Voce falhou tente outra vez : '))
    total += 1

    if resposta > num:

        print('O numero que o computador pensou e mais pequeno !')

    elif resposta < num:
        print('O numero que o computador pensou e maior ! ')

    elif resposta==num:
        acertou=True

print('Voce acertou o numero era {} \nDemorou {} tentativas ate acertar'.format(num, total))
