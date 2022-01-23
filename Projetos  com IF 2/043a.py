peso=float(input('Indique o seu peso em KG :'))

altura=float(input('Indique a sua altura em CM :'))

imc=peso/(altura**2)

if imc<18.5 :
    print('O seu IMC esta \033[1;30mABAIXO DO PESO !')
    print(imc)
elif  18.5>imc<=25 :
    print('O seu IMC esta \033[1;32m PESO IDEAL !')
    print(imc)
elif  25>=imc<=30 :
    print('O seu IMC esta \033[1;33m SOBREPESO !')
    print(imc)
elif  30>imc<=40 :
    print('O seu IMC esta \033[1;35m OBESIDADE !')
    print(imc)
elif  imc>40 :
    print('O seu IMC esta \033[1;31m OBESIDADE MORBIDA   !')
    print(imc)

