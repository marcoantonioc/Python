lado1=float(input('INdique o 1 lado :'))

lado2=float(input('Indique o 2 lado :'))

lado3=float(input('INdique o 3 lado :'))

if lado1 <lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado3:
  if lado1==lado2 and lado1 ==lado3 :
      print('O triangulo e Equilatero !')
  elif lado1==lado2 and lado3 !=lado1 :
      print('O triangulo e isosceles !')
  elif lado1!=lado2 and lado3 !=lado1 :
      print('O triangulo e Escaleno')
else:
    print('Nao da para fazer um traingulo')
