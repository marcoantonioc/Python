termo=int(input('Indique o primeiro termo :'))

razao=int(input('Indique de em quanto em quanto vai andar :'))

for i in range(termo,10*razao,razao):
    print(i, end='->')
print("Acabou")