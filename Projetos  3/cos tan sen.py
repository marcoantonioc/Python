import math
angulo=float(input('Indique um angulo:'))

seno= math.sin(math.radians(angulo))

cosseno=math.cos(math.radians(angulo))

tan=math.tan(math.radians(angulo))

print('O seno de angulo e {:.3f}'.format(seno))

print('O cosseno de angulo e {:.3f}'.format(cosseno) )

print('A tangente do angulo e {:.3f}'.format(tan) )