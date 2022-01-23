nome=str(input('Indique o seu nome completo :')).strip()

n=nome.split()
n1=nome.rsplit()

print('O primeiro nome e {} e o ultimo e {}'.format(n[0],n1[-1]))