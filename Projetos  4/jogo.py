import random

pc=random.randint(1,5)

jogador=int(input(('Indique um valor :')))

if jogador==pc :
    print('Voce acertou no numero')
else:
    print('Voce falhou')