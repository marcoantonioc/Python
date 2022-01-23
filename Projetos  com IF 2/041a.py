from datetime import date

data=date.today().year

datan=int(input('Quando voce nasceu :'))

anos=data-datan

if anos<=9 :
    print('Com {}  anos voce vai jogar na selecao \033[1;30m MIRIM'.format(anos))
elif  anos<=14 :
    print('Com {}  anos voce vai jogar na selecao \033[1;36m INFATIL '.format(anos))
elif  anos <=19 :
    print('Com {}  anos voce vai jogar na selecao \033[1;33m JUNIOR'.format(anos))
elif anos ==20 :
    print('Com {}  anos voce vai jogar na selecao \033[1;31m SENIOR'.format(anos))
elif anos >= 20 :
    print('Com {}  anos voce vai jogar na selecao \033[1;35m MASTER'.format(anos))