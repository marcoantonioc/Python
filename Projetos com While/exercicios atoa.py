#num=int(input("Indique um numero : "))

#while num < 0 or num > 10 :
    #num=int(input("Indique um numero : "))

#print("Acabou !")
#print("CRIE UM USUARIO E UMA SENHA PARA VOCE !")
#usuario1=""
#senha1=""
#usuario=str(input("INdique um usuario : "))


#senha=str(input("INdique uma senha : "))

#print("LOGIN")
#usuario1 = str(input("INdique o seu usuario : "))
#senha1 = str(input("INdique a sua senha : "))

#while usuario1!=usuario and senha1!=senha:
  #  print("LOGIN ERRADO TENTE OUTRA VEZ !")
  #  usuario1 = str(input("INdique o seu usuario : "))
#  senha1 = str(input("INdique a sua senha : "))
#print("Conseguiu entrar !\nBem vindo {}".format(usuario))
ano=0
ok=0
OK=0

a=int(input("Indique o valor do numero de habitantes : "))
A=float(input("Indique em % qual é a taxa de crescimento : "))
crescimentoA=(a/100)*A

b=int(input("Indique o valor do numero de habitantes : "))
B=float(input("Indique em % qual é a taxa de crescimento : "))
crescimentoB=(b/100)*B
if a > b :
    while a + ok >= b + OK:
        ok + crescimentoA
        OK += crescimentoB
        ano += 1
    print("Acabou , demorou {:.3f} ".format(ano))
elif b > a :

    while b + OK >= a + ok:
        ok += crescimentoA
        OK + crescimentoB
        ano += 1
    print("Acabou , demorou {:.3f} ".format(ano))

else:
    print("Insira um valor maior que o outro")
    b = int(input("Indique o valor do numero de habitantes : "))
    a = int(input("Indique o valor do numero de habitantes : "))






