nota1=float(input('Indique a 1 nota :'))

nota2=float(input('INdique a segunda nota :'))

media=(nota1+nota2)/2



if media<4.9:
    print('Com a media de {} voce esta \033[1;31m REPROVADO '.format(media))
elif 5.0> media <=6.9 :
    print('Com a media de {} voce esta \033[1;33mRECUPERACAO '.format(media))
elif media>=7.0 :
    print('Com a media de {} voce esta \033[1;32mAPROVADO '.format(media))