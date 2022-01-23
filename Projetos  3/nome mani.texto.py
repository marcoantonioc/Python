nome=str(input('Indique o seu nome :')).strip()

print('O seu nome em Maiusculo fica ',nome.upper())
print('O seu nome em minusculas fica ',nome.lower())

print(len(nome.replace(' ','')))

print('O seu primeiro nome tem {}'.format(nome.find(' ')))