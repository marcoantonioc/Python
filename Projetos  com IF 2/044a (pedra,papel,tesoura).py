from random import randint



nome=str(input('Indique o seu nome : '))

hu=int(input('[1]Pedra \n[2]Papel \n[3]Tesoura \nDigite a sua opcao :'))

pc=randint(1,3)


if hu == 1 and pc == 1 :
    print(' \033[1;30m EMPATE\033[m : O PC jogou \033[1;30m PEDRA \033[m e voce jogou \033[1;30m PEDRA \033[m!')
if hu == 2 and pc == 2 :
    print(' \033[1;30m EMPATE\033[m : O PC jogou \033[1;30m PAPEL \033[m e voce jogou \033[1;30m PAPEL \033[m!')
if hu == 3 and pc == 3 :
    print(' \033[1;30m EMPATE\033[m : O PC jogou \033[1;30m TESOURA \033[m e voce jogou \033[1;30m TESOURA \033[m!')

if hu == 1 and pc == 2 :
    print('O PC \033[1;30m GANHOU \033[m : O PC jogou \033[1;32mPapel\033[m e voce \033[1;31m Pedra \033[m')


if hu == 2 and pc == 1 :
    print('O', nome,  '\033[1;30m GANHOU \033[m: O PC jogou \033[1;31m Pedra \033[m e voce \033[1;32m Papel \033[m')


if hu == 1 and pc == 3 :
     print('O', nome ,'\033[1;30m GANHOU \033[m : O PC  jogou \033[1;31m Tesoura \033[m e voce \033[1;32mPedra\033[m !')

if hu == 3 and pc == 1 :
     print('O PC \033[1;30m GANHOU  \033[m: O PC jogou \033[1;32mPedra \033[m e voce \033[1;31m Tesoura \033[m!')


if hu == 2 and pc == 3 :
     print('O PC \033[1;30m GANHOU \033[m: O PC jogou \033[1;32mTesoura \033[m e voce \033[1;31mPapel \033[m !')


if hu == 3 and pc == 2 :
     print('O', nome ,'\033[1;30m GANHOU \033[m: O PC jogou \033[1;31m Papel \033[m e voce \033[1;32mTesoura \033[m !')





